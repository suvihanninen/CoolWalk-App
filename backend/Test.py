import PreprocessData as preprocessData

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

#TODO implement various functionality from network_kris.ipynb which is related to testing


"""
Utility class responsible for providing various test functions 
"""
class Test():

    def __init__(self):
        self.__preprocessed_nodes = preprocessData.PreprocessData().get_preprocessed_data()[0]
        self.__preprocessed_edges = preprocessData.PreprocessData().get_preprocessed_data()[1]

    """ ##############################################   TEST HELPER FUNCTION IMPLEMENTATION SECTION STARTS   ############################################## """
    """
    Returns nodes dataframe of helper node rows only. Returns the nodes dataframe consisting only of rows where value of osm_id column == 0
    """
    def get_helper_nodes_rows(self, nodes_datafram: pd.DataFrame) -> pd.DataFrame:
        helper_nodes = nodes_datafram.loc[nodes_datafram['osm_id'] == 0]
        return helper_nodes

    """
    Returns edges dataframe of helper node rows only. Returns the edges dataframe consisting only of rows where value of helper column == True
    """
    def get_helper_edges_rows(self, edges_datafram: pd.DataFrame) -> pd.DataFrame:
        helper_edges = edges_datafram.loc[edges_datafram['helper'] == True]
        return helper_edges

    """ ##############################################   TEST HELPER FUNCTION IMPLEMENTATION SECTION ENDS   ############################################## """

    """ ##############################################   TEST SECTION STARTS   ############################################## """

    def discard_helpernodes_test(self) -> pd.DataFrame:
        test_dataframe = self.__preprocessed_nodes
        test_result = Test().get_helper_nodes_rows(test_dataframe)
        assert test_result.empty, "Some or all helper nodes not removed from data"

    def discard_helperedges_test(self) -> pd.DataFrame:
        test_dataframe = self.__preprocessed_edges
        test_result = Test().get_helper_edges_rows(test_dataframe)
        assert test_result.empty, "Some or all helper edges not removed from data"

    """ ##############################################   TEST SECTION ENDS   ############################################## """


TestInstane = Test()

TestInstane.discard_helpernodes_test()

TestInstane.discard_helperedges_test()


