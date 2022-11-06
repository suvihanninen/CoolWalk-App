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


    """
    Creating new column in the edges which represents the fraction of shadow on each edge. Is to be used as a weight/contraint when computing walking route.
    """
    @staticmethod
    def set_shadow_fraction_column_in_edges() -> pd.DataFrame:
        __edgesPd = readData.ReadData().get_edges_as_pd()

        shadow_fraction_colum = (__edgesPd['shadowed_length'] / __edgesPd['full_length'])

        __edgesPd['shadow_fraction'] = shadow_fraction_colum

        return __edgesPd

    """
    Generate a GeoPandas geometry column from 'geopoint' column in nodes, which will be used to replace the 'geopoint' in nodes in a later step
    """
    @staticmethod
    def generate_nodesgeom_column() -> any:
        nodes_geom_column = gpd.GeoSeries.from_wkt(readData.ReadData().get_nodes_as_pd()['geopoint'])

        return nodes_geom_column
    
    """
    Generate a GeoPandas geometry column from 'edgegeom' column in edges, which will be used to replace the 'edgegeom' in edges in a later step
    """
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
        __edgesPd_with_shadow_fraction = PreprocessData.set_shadow_fraction_column_in_edges()
        
        #mutating
        __nodesPd['geopoint'] = PreprocessData.generate_nodesgeom_column()
        __edgesPd_with_shadow_fraction['edgegeom'] = PreprocessData.generate_edgesgeom_column()

        return __nodesPd, __edgesPd_with_shadow_fraction 

    """
    Defining Pandas GeoDataFrames from Pandas Dataframes 
    """
    @staticmethod
    def pd_to_gpd() -> Tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
        __nodesPd_with_geom_column, __edgesPd_with_geom_column = PreprocessData.set_geometry_column()

        __nodesGdp = gpd.GeoDataFrame(__nodesPd_with_geom_column, geometry='geopoint', crs="EPSG:27700")
        __edgesGdp = gpd.GeoDataFrame(__edgesPd_with_geom_column, geometry='edgegeom', crs="EPSG:27700")

        return __nodesGdp, __edgesGdp 

    """
    Find and discard helper nodes from __nodesGdp
    """
    @staticmethod
    def discard_helpernodes() -> gpd.GeoDataFrame:
        __nodesGdp, __edgesGdp = PreprocessData.pd_to_gpd()

        __nodesGdp_no_helpers = __nodesGdp.drop(__nodesGdp[__nodesGdp.osm_id == 0].index)

        return __nodesGdp_no_helpers

    """
    Find and discard helper edges from __edgesGdp
    """
    @staticmethod
    def discard_helperedges() -> gpd.GeoDataFrame:
        __nodesGdp, __edgesGdp = PreprocessData.pd_to_gpd()

        __edgesGdp_no_helpers = __edgesGdp.drop(__edgesGdp[__edgesGdp.osm_id == 0].index)

        return __edgesGdp_no_helpers

    """
    Setting osmid as index for nodes
    """
    @staticmethod
    def set_nodes_index() -> gpd.GeoDataFrame:
        __nodesGdp_no_helpers = PreprocessData.discard_helpernodes()

        __nodesGdp_with_index = __nodesGdp_no_helpers.set_index('osm_id') 

        return __nodesGdp_with_index

    """
    Setting src_id, dst_id and osm_id of edge geodf's as the multiindex(u, v, key) of each node
    """
    @staticmethod
    def set_edges_index() -> gpd.GeoDataFrame:
        __edgesGdp_no_helpers = PreprocessData.discard_helperedges()

        __edgesGdp_with_index = __edgesGdp_no_helpers.set_index(['src_id','dst_id','osm_id'])

        return __edgesGdp_with_index

    """
    renaming and rearranging columns of nodes to accomodate specifations of osmnx MultiDiGraphs function
    """
    @staticmethod
    def rename_nodes_columns() -> gpd.GeoDataFrame:
        __nodesGdp_with_index = PreprocessData.set_nodes_index()
        
        __nodesGdp_named_columns = __nodesGdp_with_index.rename(columns = {'lat':'x', 'lon':'y'})


        __nodesGdp_named_columns['x'] = __nodesGdp_named_columns["geopoint"].x #is inplace?
        __nodesGdp_named_columns['y'] = __nodesGdp_named_columns["geopoint"].y

        return __nodesGdp_named_columns

    """ PREPROCESSING PIPELINE ends """

    """
    Return preprocessed nodes and edges ready for Graph construction
    """
    @staticmethod
    def get_preprocessed_data() -> Tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
        
        __preprocessed_nodes = PreprocessData.rename_nodes_columns()
        __preprocessed_edges = PreprocessData.set_edges_index()

        return __preprocessed_nodes, __preprocessed_edges 


instance = PreprocessData()

x = readData.ReadData().get_nodes_as_pd()['geopoint']

y,z = instance.get_preprocessed_data()

print(y) #Getting error 'Point has no len() ?
