# import ReadData class
import BuildNetwork as buildNetwork

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
Class responsible for implmenting functionality for finding the optimal walking path, which is optimized on the amount of shadow on the route
"""
class OptimalPathService:
    graph : ox.MultiDiGraph = buildNetwork.BuildNetwork().build_multidigraph()
    whatever = str = 'whatever'


    @staticmethod
    def generate_optimal_path(sourcec, target, cls) -> list:
        cls.whatever

    @classmethod
    def generate_optimal_path(sourcec, target, cls) -> list:
        cls.whatever



    @staticmethod
    def generate_shortest_path(sourcec, target) -> list:

    
instance = OptimalPathService()

    a = instance.graph()

    #getattr(<instance_name>,<attribute_name>)