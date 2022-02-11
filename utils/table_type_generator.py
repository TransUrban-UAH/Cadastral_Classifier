# -*- coding: utf-8 -*-
"""
Created on Tue Nov 2 11:56:33 2021

@author: by Nikolai Shurupov (Universidad de Alcalá de Henares)

@purpose: using the cadastral structures, extrad information from .CAT and 
          generate differente tables with differente information, used in the
          cadastral classifier QGIS plugin"""

#------------------------------------------------------------------------------#

# global imports
import gzip
from os import chdir, makedirs
from time import time
from csv import writer
from os.path import basename, isfile

# local imports
from .cadastral_structure import catstruct

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
###############################################################################

def table_type_generator(file_path, list_of_interest, output_csv):
    ''' Performs a decompression and reading of the CAT file, then generates the
    table-type that user selected. Uses a structured dictionary with extraction
    parameters.

    :param file_path: path of the CAT file
    :type text: str

    :param list_of_interest: list of the types of tables to generate (13, 14, etc)
    :type list: int

    :param output_csv: path of the folder that will contain all the generated
                       tables (in .csv format)
    :type numeric: str
    
    :output folder path with all the generated tables
    :type text: str
    '''
    
    # save time before starting the processing
    t_start = time()
    
    # create the directory if it does not exist
    try: 
        makedirs(output_csv)
        
    except:
        pass
    
    # set the output as current directory
    chdir(output_csv)
    
    # get the name of the input file 
    file_name = basename(file_path)


    # decompress the CAT file if the used gives as input the raw downloaded file
    if file_name[-3:] == ".gz":
        
        # generate a nave without the .gz extension
        unziped_name = file_name[:-7] + ".cat"
        
        # creates the directory path for the file
        wd_each_table = output_csv + "\\" + unziped_name[:-4] + "_CAT"
        
        # create the directory
        try:
            makedirs(wd_each_table)
        except:
            pass
        
        # set the directory 
        chdir(wd_each_table)
        
        # if the unzipped name (file) doesn't already exist, decompress it
        if isfile(unziped_name) == False:
            
            try:
                gunzip(file_path, unziped_name)
                
            except:
                pass
    
    # if the user already gives the decompressed .CAT file, just create the
    # directory to store the files

    elif file_name[-4:] == ".cat":
        
        unziped_name = file_name[:-4]
        
        wd_each_table = output_csv + "\\" + unziped_name + "_CAT"
        
        try:
            makedirs(wd_each_table)
        except:
            pass
        
        chdir(wd_each_table)
        
        unziped_name = file_path

    # create a dictionary to store each possible table type
    wf = {}   
    
    #--------------------------------------------------------------------------
    
    # for every type that is possible to extraxt data from CAT file
    for type_ in catstruct:
        
        # if it is selected by the user
        if type_ in list_of_interest:
            
            # generate a name
            output_file_name = wd_each_table + '/Tipo_' + str(type_) + '.csv'        
            
            # create a file 
            wf[type_] = open(output_file_name, 'w')
            
            # create a list to store the column names to use for the tables
            cols = []
            
            # store the col names in the list 
            for item in catstruct[type_]:
                cols.append(item[4])
            
            # write the column names in the files
            writer(wf[type_]).writerow(cols)
                 
    try:
        # open the input file
        rf = open(unziped_name)
                
        #----------------------------------------------------------------------
        
        # read line by line the CAT file and add the information to each table
        # type that user selected, using the cadastral structure info
        for line in rf.readlines():
            row = []
            type_ = int(line[0:2]) # table type
            
            if type_ in list_of_interest:
                output_file_name = wd_each_table + '/Tipo_' + str(type_) + '.csv'
                
                # for each column(field) get the value using positions declared
                # in the catstruct dictionaries
                for fields in catstruct[type_]:
                    valor = line[fields[0]-1 : fields[0]-1 + fields[1]].strip()
                    row.append(valor)
                
                # write the values
                writer(wf[type_]).writerow(row)
        
    except:
        
        # open the file using specific encoding 
        rf = open(unziped_name, encoding = "ISO-8859-1")
                
        #----------------------------------------------------------------------
        
        # read line by line the CAT file and add the information to each table
        # type that user selected, using the cadastral structure info
        for line in rf.readlines():
            row = []
            tipo = int(line[0:2])
            
            if tipo in list_of_interest:
                output_file_name = wd_each_table + '/Tipo_' + str(tipo) + '.csv'
                
                # for each column(field) get the value using positions declared
                # in the catstruct dictionaries
                for fields in catstruct[tipo]:
                    valor = line[fields[0]-1 : fields[0]-1 + fields[1]].strip()
                    row.append(valor)
                
                writer(wf[tipo]).writerow(row)
                
    # close all the files
    for f in wf:
        wf[f].close()
        
    rf.close()
    
    #--------------------------------------------------------------------------
    
    # save time after running all the processing
    t_finish = time()
    
    # calculate the time needed to perform the processing
    t_process = (t_finish - t_start)
    
    print("Process time: " + str(round(t_process, 2)) + "seconds.")
  
    return wd_each_table