# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:25:46 2023

@author: Niko
"""

#global imports
from os.path import basename

#------------------------------------------------------------------------------

def input_check (filename, component, typology, form):
    ''' Check if the filename has all specified elements: correct extension
    (.shp, .gz, .CAT...) and composition (urban/rustic). If it does return
    True, otherwise return false.

    :param filename: the whole path of the file
    :type text: str

    :param component: urban or rustic. Determine the elements to look for in the
                      name
    :type text: str

    :param typology: cat or shp. Determine the extension that it should have and
                     name characters
    :type text: str
    
    :param form: multi or unique. Needs to be specified to distinguish between
                 the different file formats
    :type text: str
    '''
        
    # get the name of the file
    name = basename(filename)
    
    # if it is a multiple municipalities file
    if form == "multi":
        
        # split to pure name and extension
        split_ext = name.split(".")
        
        # split the pure name on its different components
        split_comp = split_ext[0].split("_")
        
        # if needed to check if file is rustic
        if component.lower() == "rustic":
            cl_1 = 'ra'
            cu_1 = 'RA'
            cl_2 = 'r'
            cu_2 = 'R'
        
        # if needed to check if file is urban
        elif component.lower() == "urban":
            cl_1 = 'ua'
            cu_1 = 'UA'
            cl_2 = 'u'
            cu_2 = 'U'           
        
        # if needed to check if the file is the alphanumeric data (CAT)
        if typology.lower() == 'cat':
            tl = 'cat'
            tu = 'CAT'            
        
        # if needed to check if the file is the geometry data (shp)
        elif typology.lower() == "shp":
            tl = 'shp'
            tu = 'SHP'
        
        # check if any of the correspondent variables are contained in the 
        # name of the file. If all conditions are met return True, otherwise 
        # return False
        
        if (cl_1 in split_comp or cu_1 in split_comp or\
             cl_2 in split_comp or cu_2 in split_comp) and\
            (tl in split_comp or tu in split_comp):
                
            return True
        
        else:
            return False
    
    # if it is a single municipality file (its structure differs from the 
    # mutiple one)
    elif form == "unique":
        
        # split to pure name and extension
        split_ext = name.split(".")
        ext = split_ext[-1] # save the extension
        
        # split the pure name on its components
        split_comp = split_ext[0].split("_")
        
        # from the first component, taking only the string and not the code
        comp = split_comp[0][5:]
        
        # add the values that each option should include
        if component.lower() == "rustic":
            comp_list = ['ra', 'RA', 'rA', 'r', 'R']
            
        elif component.lower() == "urban":
            comp_list = ['ua', 'UA', 'uA', 'u', 'U']

        if typology.lower() == 'cat':
            ext_list = ['gz', 'GZ', 'cat', 'CAT']
                      
        elif typology.lower() == "shp":
            ext_list = ['shp', 'SHP', 'zip', 'ZIP']
        
        # add an exception for when the geometry parcel is the decompressed
        # Shapefile 
        shp_exceptions = ['parcel', 'parcela']
        
        # if all conditions are met return True, otherwise return False
        if ((ext in ext_list) and (comp in comp_list)):
            return True
        
        elif (typology.lower() == "shp") and (ext in ext_list) and \
            (split_comp[0].lower() in shp_exceptions):
            return True
        
        else:
            return False
        