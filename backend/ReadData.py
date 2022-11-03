#!/usr/bin/env python
# coding: utf-8


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


"""
    Class responsible for reading data from CSV file (TO-DO: make it read from PostGis data base) and return it as pandas dataframes

"""
class ReadData(object):
    """Creating class attrributes which can only be accessed via Class reference"""

    dfNodes = pd.read_csv("/mnt/c/users/kriso/documents/itu/5th_semester/research_project/CoolWalk/data/CoolWalksDataStorge/nodes.csv")
    dfEdges = pd.read_csv("/mnt/c/users/kriso/documents/itu/5th_semester/research_project/CoolWalk/data/CoolWalksDataStorge/edges.csv")
    """print(dfNodes)"""

    def __init__(self):
        self.nodes = pd.read_csv("/mnt/c/users/kriso/documents/itu/5th_semester/research_project/CoolWalk/data/CoolWalksDataStorge/nodes.csv")
        self.edges = pd.read_csv("/mnt/c/users/kriso/documents/itu/5th_semester/research_project/CoolWalk/data/CoolWalksDataStorge/edges.csv")

    def someFunction():
        return "hello"

