# import ReadData class
import ReadData as readData

# import modules
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import wkt
from shapely.geometry import Point
import shapely
import osmnx as ox
import pandas as pd
import networkx as nx
from shapely.geometry import LineString
from tabulate import tabulate
from IPython.display import display
from typing import Dict, List, Tuple


"""
Utility class responsible for preprocessing the the data, recieved as panda dataframes 
"""
class PreprocessData:

    """ PREPROCESSING PIPELINE START """


    @staticmethod
    def generate_nodesgeom_column() -> any:
        nodes_geom_column = gpd.GeoSeries.from_wkt(readData.ReadData().get_nodes_as_pd()['geopoint'])

        return nodes_geom_column

    @staticmethod
    def generate_edgesgeom_column() -> any:
        edges_geom_column = gpd.GeoSeries.from_wkt(readData.ReadData().get_edges_as_pd()['edgegeom'])

        return edges_geom_column

    """
    Transforming relevant columns of DataFrames into GeoSeries to be used as geometry column of GeoDataFrames
    """
    @staticmethod
    def set_geometry_column() -> Tuple[pd.DataFrame, pd.DataFrame]:
        __nodesPd = readData.ReadData().get_nodes_as_pd()
        __edgesPd = readData.ReadData().get_edges_as_pd()
        
        #mutating
        __nodesPd['geopoint'] = PreprocessData.generate_nodesgeom_column()
        __edgesPd['edgegeom'] = PreprocessData.generate_edgesgeom_column()

        return __nodesPd, __edgesPd 

    """
    Defining Pandas GeoDataFrames from Pandas Dataframes 
    """
    @staticmethod
    def pd_to_gpd() -> Tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
        __nodesPd_with_geom_column, __edgesPd_with_geom_column = PreprocessData.set_geometry_column()

        #__nodesGdp = gpd.GeoDataFrame(__nodesPd_with_geom_column, geometry='geopoint', crs="EPSG:27700")
        #__edgesGdp = gpd.GeoDataFrame(__edgesPd_with_geom_column, geometry='edgegeom', crs="EPSG:27700")

        return __nodesPd_with_geom_column, __edgesPd_with_geom_column 

instance = PreprocessData()

x,y = instance.pd_to_gpd()

z = readData.ReadData().get_nodes_as_pd()

print(z)