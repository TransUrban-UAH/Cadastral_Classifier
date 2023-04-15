# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 21:04:35 2023

@author: Niko
"""

#global imports
import requests
from qgis.PyQt.QtCore import QVariant
from qgis.core import (QgsCoordinateReferenceSystem,
                       QgsPointXY,
                       QgsPolygon,
                       QgsField,
                       QgsFeature,
                       QgsGeometry,
                       QgsProject,
                       QgsVectorLayer,
                       QgsCoordinateReferenceSystem,
                       QgsCoordinateTransform)
from shapely.geometry import Polygon

#------------------------------------------------------------------------------
###############################################################################

def get_green_zones(bbox):
    ''' bbox format example:
    minlat = 40.4508446
    maxlat = 40.5290077
    minlon = -3.4276476
    maxlon = -3.2746865
    
    bbox = (minlat, minlon, maxlat, maxlon)
    '''
    
    # different urls to make the parks request
    ENDPOINTS = ["https://overpass.kumi.systems/api/interpreter",
                 "https://overpass-api.de/api/interpreter",
                 "https://lz4.overpass-api.de/api/interpreter",
                 "https://overpass.torres.voyager.hr/api/interpreter",
                 "https://overpass-turbo.eu/"]
    
    # Build the Overpass query string
    overpass_query = f"""
    [out:json] [timeout:100];
    (
        node["leisure"="park"]{bbox};
        way["leisure"="park"]{bbox};
        relation["leisure"="park"]{bbox};
    );
    (._;>;);
    out body;
    """
    
    # define the layer variable
    layer = None
    
    # iterate over the endpoints list
    for endpoint in ENDPOINTS:
        
        # if the layer information has not been yet obtaine
        if not layer:
            
            # try to make the request
            try:
                
                # Send the query to the Overpass API
                response = requests.get(endpoint, params={'data': overpass_query})
                    
                # Check if the query was successful
                if response.status_code == 200:
                    # Parse the response as JSON get the elements
                    features = response.json()['elements']
                    
                    # if there is no elements means there is no data for 
                    # the stying zone
                    if len(features) == 0:
                        print("No park data found within the specified bounding box.")
                    
                    else:
    
                        # Create a new vector layer
                        crs = QgsCoordinateReferenceSystem('EPSG:4326')  # WGS84
                        layer_name = 'Urban_green_zones'
                        layer = QgsVectorLayer('Polygon', layer_name, 'memory')
                        layer.setCrs(crs)
                        
                        # add fields related to the area and ID of each geometry
                        layer.addExpressionField('$id', QgsField('ID', QVariant.Int))
                        layer.addExpressionField('$area', QgsField('AREA', QVariant.Double))
                        
                        layer.updateFields()
            
                        # create a dictionary to store the values
                        nodes_info = {}
                        
                        # iterate over each feature
                        for node in features:
                            
                            # if the feature is a node
                            if node['type'] == 'node':
                                
                                # store its information to the dictionary
                                nodes_info[node['id']] = {'lon': node['lon'],
                                                          'lat': node['lat']} 
                        # iterate again over the features
                        for way in features:
                            
                            # in this case, if it is a way
                            if way['type'] == 'way':
                                
                                # get all the nodes that are part of the way
                                way_nodes = way['nodes'] # AVOID SORTING!! breaks coords order!!
                                
                                # store in a list the coordinates of the nodes
                                # that are part of the way in the exact order
                                # they were defined
                                polygon_coords = []
                                for node in way_nodes:
                                    polygon_coords.append((nodes_info[node]['lon'], nodes_info[node]['lat'])) # create a list of node coordinates
                                
                                if len(polygon_coords) >= 3:  # Make sure the polygon has at least 3 vertices
                                    
                                    # create the polygon using the nodes coordinates
                                    geometry = Polygon(polygon_coords)
                                    
                                    # store the polygon characteristicis as a wkt
                                    polygon = QgsGeometry.fromWkt(geometry.wkt)
                                    
                                    # create a feature and set its geometry using the wkt
                                    f = QgsFeature()
                                    f.setGeometry(polygon)
                                    
                                    # define the properties of the feature
                                    feature_attrs = {
                                        'name': way.get('name', ''),
                                        'leisure': way.get('leisure', ''),
                                        'landuse': way.get('landuse', ''),
                                    }
                                    f.setAttributes(list(feature_attrs.values()))
                                    layer.dataProvider().addFeatures([f]) # add the feature to the layer
                else:
                    # if response was not 200, no data could be retrieved from 
                    # that endpoint
                    print("Endpoint:", endpoint, " is not responding, trying next one...")
            except:
                # if any other error occured treat as an endpoint issue
                print("Endpoint:", endpoint, " is not responding, trying next one...")
    # no layer info after all the endpoint tries return None
    if not layer:
        print("No green zones information could be obtained.")
        return None
    else:
        return layer
