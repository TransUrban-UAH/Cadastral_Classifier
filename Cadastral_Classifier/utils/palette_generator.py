# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:31:08 2021

@author: by Nikolai Shurupov (Universidad de Alcalá de Henares)

@purpose: palette generator for the classification result map visualization, used 
          in the cadastral classifier QGIS plugin"""

#------------------------------------------------------------------------------

from qgis.core import QgsSymbol, QgsSimpleFillSymbolLayer, QgsRendererCategory
import random

###############################################################################
#------------------------------------------------------------------------------

def random_color():
    ''' function aimed to create a random hexadecimal coded color, returns a str
    with hexadecimal color code
    '''
    # gives a rangom value from 0 to 255
    r = lambda: random.randint(0,255)
    
    # generate a random hexadecimal color code
    color = '#{:02x}{:02x}{:02x}'.format(r(), r(), r())
    
    return color

#------------------------------------------------------------------------------

def palette_generator (layer, use_list, d_palettes, d_labels):
    ''' Generates a QGIS palette based on the given classes, labels and colors
    to define.

    :param layer: shp opened as a QGIS layer
    :type QGIS layer

    :param use_list: list with the uses to add colors
    :type list: str

    :param d_palettes: dictionary with the values of use-hexadecimal code
    :type dictionary: str
    
    :param d_labels: dictionary with the values of use-label to display
    :type dictionary: str
    
    :output list of categories with the QGIS categories to display on map
    :type list: QGIS Category
    '''
    
    # list to store each class charasteristics
    categories = []
    
    # iterate over all the classes of the classification
    for uso in use_list:
        
        # create a QGIS symbol variable
        symbol = QgsSymbol.defaultSymbol(layer.geometryType())

        # create a tuple to save the style to add to the class
        layer_style = {}
        layer_style['outline'] = '#000000'
        layer_style['color'] = d_palettes[uso]
        
        # define the symbol layer with the style
        symbol_layer = QgsSimpleFillSymbolLayer.create(layer_style)
    
        # replace default symbol layer with the configured one
        if symbol_layer is not None:
            symbol.changeSymbolLayer(0, symbol_layer)
    
        # create renderer object
        category = QgsRendererCategory(uso, symbol, d_labels[uso])
        
        # entry for the list of category items
        categories.append(category)
    
    return categories