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

    #TODO add functionality for filling NA´s in the dataframes
    #TODO rearrange the order such that it matches the order in the notebook. That is, such that the pandas dataframes are not converted into geo dataframes untill in the very end of the pre-preprocessing


    """
    Creating new column in the edges which represents the fraction of shadow on each edge. Is to be used as a weight/contraint when computing walking route.
    TODO should be done AFTER shadowed_part_length and full_length have been filled

    """
    @staticmethod
    def set_shadow_fraction_column_in_edges() -> pd.DataFrame:
        __edgesPd = readData.ReadData().get_edges_as_pd()

        shadow_fraction_colum = (__edgesPd['shadowed_length']/__edgesPd['full_length'])

        # mutating
        __edgesPd['shadow_fraction'] = shadow_fraction_colum

        return __edgesPd

    """
    Dont execute
    
    TODO If shadow is None it is 0. However, our current cost-function is not compatible with this, since it is a division, and will thus result in division by 0 errors.
    TEMPORARY SOLUTION: Dont execute this cell. Let the shortest_path_algorithm cost-function fill out the None shadow values with 1. 

    Find and replace all None-valued 'shadowed_part_length' instances in edges with 0
    """
    @staticmethod
    def fill_none_value_shadows_in_edges() -> pd.DataFrame:
        __edgesPd_with_shadow_fraction_column = PreprocessData().set_shadow_fraction_column_in_edges()
        __shadow_column_filled = __edgesPd_with_shadow_fraction_column['shadowed_part_length'].fillna(0)
        __edgesPd_with_shadow_filled = PreprocessData().set_shadow_fraction_column_in_edges()
        
        # mutating
        __edgesPd_with_shadow_filled['full_length'] = __shadow_column_filled

        return __edgesPd_with_shadow_filled



    """
    Find and replace all None-valued 'full_length' instances in edges with the average full_length value
    """
    @staticmethod
    def fill_none_value_lengths_in_edges() -> pd.DataFrame:
        __edgesPd_with_shadow_fraction = PreprocessData().fill_none_value_shadows_in_edges()
        __length_mean = __edgesPd_with_shadow_fraction['full_length'].mean()
        __length_column_filled = __edgesPd_with_shadow_fraction['full_length'].fillna(__length_mean)
        __edgesPd_with_length_filled = PreprocessData().fill_none_value_shadows_in_edges()
        
        # mutating
        __edgesPd_with_length_filled['full_length'] = __length_column_filled

        return __edgesPd_with_length_filled


    """
    Find and discard helper nodes from __nodesPd
        Only rows with helper=Nan should remain
    """
    @staticmethod
    def discard_helpernodes() -> pd.DataFrame:
        __nodesPd = readData.ReadData().get_nodes_as_pd()

        __nodesPd_no_helpers = __nodesPd.drop(__nodesPd[__nodesPd.osm_id == 0].index)

        return __nodesPd_no_helpers


    """
    Find and discard helper edges from __edgesPd
        Only rows with helper=NaN should remain
    """
    @staticmethod
    def discard_helperedges() -> pd.DataFrame:
        __edgesPd_with_length_filled = PreprocessData.fill_none_value_lengths_in_edges()
        __edgesPd_no_helpers = __edgesPd_with_length_filled.drop(__edgesPd_with_length_filled[__edgesPd_with_length_filled.osm_id == 0].index)

        return __edgesPd_no_helpers

    """
    Setting osmid as index for nodes

    ATTENTION! the osmnx code will create the x_lookup and y_lookup dictionaries based on the index of the nodes data frame. That is, the keys of these dictionaries will consist
    of the values of the index column, and the values will be the lon(x_lookup) and lat(y_lookup) values respectively   
    """
    @staticmethod
    def set_nodes_index() -> pd.DataFrame:
        __nodesPd_no_helpers = PreprocessData.discard_helpernodes()

        __nodesPd_with_index = __nodesPd_no_helpers.set_index('vertex_id') 
        #__nodesPd_with_index = __nodesPd_no_helpers.set_index('osm_id') 


        return __nodesPd_with_index

    """
    Setting src_id, dst_id and osm_id of edge geodf's as the multiindex(u, v, key) of each node
    """
    @staticmethod
    def set_edges_index() -> pd.DataFrame:
        __edgesPd_no_helpers = PreprocessData.discard_helperedges()

        __edgePd_with_index = __edgesPd_no_helpers.set_index(['src_id','dst_id','osm_id'])

        return __edgePd_with_index

    """
    Generate a GeoPandas geometry column from 'geopoint' column in nodes, which will be used to replace the 'geopoint' in nodes in a later step
    """
    @staticmethod
    def generate_nodesgeom_column() -> any:
        df = readData.ReadData().get_nodes_as_pd()
        nodes_geom_column = gpd.GeoSeries.from_wkt(df['geopoint'])

        return nodes_geom_column
    
    """
    Generate a GeoPandas geometry column from 'edgegeom' column in edges, which will be used to replace the 'edgegeom' in edges in a later step
    """
    @staticmethod
    def generate_edgesgeom_column() -> any:
        df = readData.ReadData().get_edges_as_pd()
        edges_geom_column = gpd.GeoSeries.from_wkt(df['edgegeom'])

        return edges_geom_column

    """
    Transforming relevant columns of DataFrames into GeoSeries to be used as geometry column of GeoDataFrames
    """
    @staticmethod
    def set_geometry_column_nodes() -> pd.DataFrame:
        __nodesPd_with_index = PreprocessData().set_nodes_index()
        
        #mutating
        __nodesPd_with_index['geopoint'] = PreprocessData.generate_nodesgeom_column()

        return __nodesPd_with_index 

    """
    Transforming relevant columns of DataFrames into GeoSeries to be used as geometry column of GeoDataFrames
    """
    @staticmethod
    def set_geometry_column_edges() -> pd.DataFrame:

        __edgePd_with_index = PreprocessData.set_edges_index()
        
        #mutating
        __edgePd_with_index['edgegeom'] = PreprocessData.generate_edgesgeom_column()

        return __edgePd_with_index 



    """
    Defining Pandas GeoDataFrames from Pandas Dataframes 
    """
    @staticmethod
    def pd_to_gpd(which_pd) -> gpd.GeoDataFrame:
        
        if which_pd == 'nodes':
            __nodesPd_with_geom_column = PreprocessData.set_geometry_column_nodes()
            __nodesGdp = gpd.GeoDataFrame(__nodesPd_with_geom_column, geometry='geopoint', crs="EPSG:27700")
            return __nodesGdp
        if which_pd == 'edges':
            __edgesPd_with_geom_column = PreprocessData.set_geometry_column_edges()
            __edgesGdp = gpd.GeoDataFrame(__edgesPd_with_geom_column, geometry='edgegeom', crs="EPSG:27700")
            return __edgesGdp



    """
    renaming and rearranging columns of nodes to accomodate specifations of osmnx MultiDiGraphs function
    """
    @staticmethod
    def rename_nodes_columns() -> gpd.GeoDataFrame:
        __nodesGdp = PreprocessData.pd_to_gpd('nodes')
        
        __nodesGdp_named_columns = __nodesGdp.rename(columns = {'lat':'x', 'lon':'y'})


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
        __preprocessed_edges = PreprocessData.pd_to_gpd('edges')

        return __preprocessed_nodes, __preprocessed_edges 

    
    @staticmethod
    def make_graph() -> any:
        __preprocessed_nodes = PreprocessData.rename_nodes_columns()
        __preprocessed_edges = PreprocessData.pd_to_gpd('edges')

        G = ox.utils_graph.graph_from_gdfs(__preprocessed_nodes, __preprocessed_edges, graph_attrs=None)

        return G 

instance = PreprocessData()

#x = readData.ReadData().get_nodes_as_pd()['geopoint']
y = instance.make_graph()

#x,z = instance.get_preprocessed_data()

#print(z)

#test = instance.generate_nodesgeom_column()
#print(test) #Getting error 'Point has no len() ?

