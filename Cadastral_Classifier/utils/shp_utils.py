# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:29:25 2021

@author: by Nikolai Shurupov (Universidad de Alcalá de Henares)

@purpose: shapefile vector file format utilities to use for cadastral classifier
          QGIS plugin
"""

#------------------------------------------------------------------------------

#global imports
import gzip
from os.path import dirname, basename, join
from os import chdir, getcwd, makedirs
from glob import glob
from os import remove
from zipfile import ZipFile
import processing
from shutil import copyfile, rmtree

#------------------------------------------------------------------------------

def gunzip(source_filepath, dest_filepath, block_size = 64):
    ''' Dcompress the CAT file. Use small blocks to secure correct 
    decompression.

    :param source_filepath: the filepath of the file to decompress (.zip format)
    :type text: str

    :param dest_filepath: the result file filepath name 
    :type text: str

    :param block_size: size of the block to decode
    :type numeric: int
    '''
    
    # open the file with the gzip open method and generate a new file to store the data
    with gzip.open(source_filepath, 'rb') as s_file, open(dest_filepath, 'wb') as d_file:
        
        # read the file data using the blocks and save it to the created file
        while True:
            block = s_file.read(block_size)
            
            if not block:
                break
            
            else:
                d_file.write(block)

#------------------------------------------------------------------------------

def unzip_shp (zip_shp):
    ''' Decompress the shapefile, that is in .zip format. In case there is double 
    compression (presented in the spanish cadastral data o public use) first
    extract the lower level zip and then the files inside the a folder with 
    the same name (without extension)

    :param zip_shp: file path of the file
    :type text: str
    
    :output file path of the result
    :type text: str
    '''
    
    # creates a name with the deletion the extension from the name
    dest_filepath = zip_shp[:-4]
    
    with ZipFile(zip_shp, 'r') as zipObj: # open the file
        listOfiles = zipObj.namelist() # list with the files in it
        
        if "PARCELA.zip" in listOfiles: # check specific file of interest
            zipObj.extractall(dest_filepath) # exctract it to firt level
            
            chdir(dest_filepath) # set new directory   
            shp2 = "PARCELA.zip"
            
            with ZipFile(shp2, "r") as zipObj2: # list with files in the second file
                zipObj2.extractall(dest_filepath) # extract them outside the zip

            # delete unnecesary mid-progress files
            lista_zip = glob("*.zip")
            
            if len(lista_zip) > 0:
                for e in lista_zip:
                    remove(e)
        else:
            chdir(dest_filepath)
            zipObj.extractall(dest_filepath)
    
    # get the name of the shapefile
    shp_name = glob("*.shp")
    
    return dest_filepath + "/" + shp_name[0]

###############################################################################
#------------------------------------------------------------------------------..

def unzip_files (zip_shp, dest_filepath, zip_path, comp):
    ''' Decompress .zip format cadastral data, presented in the spanish cadastral
    data for public use. extract the lower level zip and then if the component
    is the parcel SHP perform a second decompression

    :param zip_shp: file path of the zip file
    :type text: str

    :param dest_filepath: path where the results will be saved
    :type text: str

    :param zip_path: the internal path of the zip with the file that needs to 
                     be decompress
    :type text: str

    :param comp: 'cat' for the alphanumeric data or 'parcelario' for the 
                 parcel geometries
    :type text: str
    
    :output path of the results 
    :type text: str
    '''
    
    # if the component is the parcels
    if comp == "parcelario":
        
        # create a temporal path to store mid files
        temp_path = join(dest_filepath, "temp")
        
        # create the final destination and temporal directories
        makedirs(dest_filepath, exist_ok = True)
        makedirs(temp_path, exist_ok = True)
        
        # open the zip object
        zip_object = ZipFile(zip_shp, 'r')
    
        # extract the internal file to a temporal path
        temp_result = zip_object.extract(zip_path, temp_path)
        
        # extact them again to the final destination path
        zip_object2 = ZipFile(temp_result, 'r')
        zip_object2.extractall(dest_filepath)
        
        chdir(dest_filepath)
        
        shp_name = glob("*.shp")
        
        del zip_object2
        
        try:
            rmtree(temp_path)
        except:
            print("Está trabajando en un directorio que no permite ser modificado.")
            
        return dest_filepath + "/" + shp_name[0]
        
    elif comp == "cat":
        
        # create the final destination and temporal directories
        makedirs(dest_filepath, exist_ok = True)
        
        # open the zip object
        zip_object = ZipFile(zip_shp, 'r')
    
        # extract the internal file to a temporal path
        CAT_result = zip_object.extract(zip_path, dest_filepath)
        
        return CAT_result

###############################################################################
#------------------------------------------------------------------------------

def merge_qgis(shp_1, shp_2, shp_result):
    ''' Use QGIS native method to merge two shapefiles

    :param shp_1: first shapefile filepath to merge
    :type text: str
    
    :param shp_2: second shapefile filepath to merge
    :type text: str
    
    :param shp_result: name(route) that the resulted shapefile will have
    :type text: str
    
    :output same route introduced as shp result filepath
    :type text: str
    '''

    shapefile_list = []
    shapefile_list.append(shp_1)
    shapefile_list.append(shp_2)

    parameters = {'LAYERS': shapefile_list,
                  'OUTPUT': shp_result}

    processing.run("qgis:mergevectorlayers", parameters)

    return shp_result

###############################################################################
#------------------------------------------------------------------------------

def shp_copy(shp_filepath, result_filepath):
    
    ''' Use QGIS native method to merge two shapefiles

    :param shp_filepath: filepath of the shapefile to be copied
    :type text: str
    
    :param result_filepath: name(route) that the copy shapefile will have
    :type text: str
    
    :output same route introduced as shp result filepath
    :type text: str
    '''
    
    # get current working directory
    cwd = getcwd()
    
    # get the name and the directory of the input shp
    wd_root_shp = dirname(shp_filepath)
    name_shp = basename(shp_filepath)
        
    # get the name and the directory of the wanted copied file
    wd_root_result = dirname(result_filepath)
    name_result = basename(result_filepath)

    # delete the extensions from the names
    if name_result[-4:].lower() == ".shp":
        name_result = name_result[0:-4]
        
    if name_shp[-4:].lower() == ".shp":
        name_shp = name_shp[0:-4]
    
    # set new directory
    chdir(wd_root_shp)

    # get all the files related to the input shapefile (alongside .shp, get all
    # others, dbf, prj, etc)
    file_list = glob(name_shp + ".*")
    
    # perform a copy of each file with the new route (name)
    for file in file_list:
        
        extension = file[-4:]
        file_path = wd_root_shp + "/" + file
        copied_file_path = wd_root_result + "/" + name_result + extension.lower()
        copyfile(file_path, copied_file_path)
  
    chdir(cwd) # set original working directory
    
    return result_filepath