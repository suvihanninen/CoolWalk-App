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


"""
    Utility class responsible for reading data from CSV file (TODO: make it read from PostGis data base) and return it as pandas dataframes

"""
class ReadData():
    __dfNodes = pd.read_csv("/mnt/c/users/kriso/documents/itu/5th_semester/research_project/CoolWalk/data/CoolWalksDataStorge/nodes.csv")
    __dfEdges = pd.read_csv("/mnt/c/users/kriso/documents/itu/5th_semester/research_project/CoolWalk/data/CoolWalksDataStorge/edges.csv")

    """considered as utility functions and therefore implemented with the @staticmethod decorator"""
    @staticmethod
    def get_nodes_as_pd() -> pd.DataFrame:
        return ReadData.__dfNodes

    @staticmethod
    def get_edges_as_pd() -> pd.DataFrame:
        return ReadData.__dfEdges
