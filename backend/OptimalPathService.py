# import ReadData class
import BuildNetwork as buildNetwork
import CostfunctionGenerator as costfunctionGenerator
import GraphUtility as graphUtility



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
from geojson import Feature, LineString, FeatureCollection


"""
Class responsible for implmenting functionality for finding the optimal walking path, which is optimized on the amount of shadow on the route
"""
class OptimalPathService():
    __directed_multi_graph = buildNetwork.BuildNetwork().build_multidigraph()


    """HELPER METHODS SECTION STARTS"""
    def provide_cost_function(self, which_function:str) -> function:
        costfunctionGenerator = costfunctionGenerator()
        if which_function == "1":
            return costfunctionGenerator().cost_function1 # no () since we want to return the function
        if which_function == "2":
            return costfunctionGenerator().cost_function2 # no () since we want to return the function
        #TODO throw error if not match
        return None 

    """HELPER METHODS SECTION ENDS"""

    @staticmethod
    def test() -> any:
        __directed_multi_graph = buildNetwork.BuildNetwork().build_multidigraph()
        return __directed_multi_graph

    @classmethod
    def __get_graph(cls) -> nx.MultiDiGraph:
        return cls.__directed_multi_graph


    def compute_optimal_path(self, src:int, dst:int) -> FeatureCollection:
        G = OptimalPathService().__get_graph()
        graphUtility = graphUtility()
        cost_function = OptimalPathService().provide_cost_function("1")
        optimal_path = nx.shortest_path(G, src, dst, cost_function) 
        list_coords = graphUtility.path_to_list_of_coords(G, optimal_path)
        geojson_feature_response = graphUtility.path_coords_to_geojson(list_coords)
        return geojson_feature_response



        return G

    def get_optimal_path_as_geojson() -> FeatureCollection:
        return None



    @staticmethod
    def generate_optimal_path(sourcec, target, cls) -> list:
        cls.whatever

    @classmethod
    def generate_optimal_path(sourcec, target, cls) -> list:
        cls.whatever


    @staticmethod
    def generate_shortest_path(sourcec, target) -> list:
        return

instance = OptimalPathService()

graph = instance.compute_optimal_path(1,2)
#graph = instance.test2()