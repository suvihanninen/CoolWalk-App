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
    __MultiDiGraph = buildNetwork.BuildNetwork().build_multidigraph()

    