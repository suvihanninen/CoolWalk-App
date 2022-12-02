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
Consider implementng it with static methods instead
"""
class OptimalPathService():
    __directed_multi_graph = buildNetwork.BuildNetwork().build_multidigraph()

    def __init__(self):
        self.graphUtility = graphUtility.GraphUtility()
        self.costfunctionGenerator = costfunctionGenerator.CostfunctionGenerator()

    """ ##############################################   HELPER METHODS SECTION STARTS   ############################################## """

    def provide_cost_function(self, which_function:str) -> any: #should be python buildin type 'function', right?
        costfunctionGenerator = self.costfunctionGenerator
        if which_function == "1":
            return costfunctionGenerator.cost_function1 # no () since we want to return the function
        if which_function == "2":
            return costfunctionGenerator.cost_function2 # no () since we want to return the function
        #TODO throw error if not match
        return None 

    @classmethod
    def __get_graph(cls) -> nx.MultiDiGraph:
        return cls.__directed_multi_graph

    """ ##############################################   HELPER METHODS SECTION ENDS   ############################################## """

    """ ##############################################   SERVICE METHODS SECTION BEGINS   ############################################## """

    def compute_optimal_path(self, src:int, dst:int) -> FeatureCollection:
        G = OptimalPathService().__get_graph()
        graphUtility = self.graphUtility
        cost_function = OptimalPathService().provide_cost_function("2") 
        optimal_path = nx.shortest_path(G, int(src), int(dst), cost_function) #TODO define this getter method inside CostFunctionGenerator, and access via a constFunctionGenerator instance
        list_coords = graphUtility.path_to_list_of_coords(G, optimal_path)
        geojson_feature_response = graphUtility.path_coords_to_geojson(list_coords)
        print(len(optimal_path))
        return geojson_feature_response

    def compute_shortest_path() -> FeatureCollection:
        return None
        #TODO implement compute_shortest_path() function

    """ ##############################################   SERVICE METHODS SECTION ENDS   ############################################## """


instance = OptimalPathService()

graph = instance.compute_optimal_path(2,8924)
print(graph)
#graph = instance.test2()