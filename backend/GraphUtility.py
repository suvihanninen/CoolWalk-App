import networkx as nx
from geojson import Feature, LineString, FeatureCollection




"""
Class responsible for providing various functions for working with a NetworkX network
"""


class GraphUtility():
    #declare and/or instantiate class attributes
    __some_attr = None

    def __init__(self):
        #declare and/or instantiate instance attributes by the help of self
        return None


    @classmethod
    def some_classmethod(cls) -> any:
        #access class attributs by the help of cls.
        return None

    """ ##############################################   UTILUTY METHODS SECTION STARTS   ############################################## """

    """
    Function responsible for generation a list of coordinates of a given paths.
    Takes a path and the NetworkX Graph from which the path is computed as arguments
    Returns a list of lists
    """
    def path_to_list_of_coords(self, G:nx.MultiDiGraph, path:list) -> list:
        x_lookup = nx.get_node_attributes(G, "x")
        y_lookup = nx.get_node_attributes(G, "y")
        path_nodes_coords = []
        for node in path:
            node_coords = [x_lookup[node],y_lookup[node]]
            path_nodes_coords.append(node_coords)
        return path_nodes_coords  

    """
    Function responsible for generating a geojson FeatureCollection based on a list of coordinates
    Takes the list of coordinates as argument 
    """
    def path_coords_to_geojson(self, listCoord:list) -> FeatureCollection:
        coords = []
        for pt in listCoord:
             coords.append((pt[0], pt[1]))
        linestring = LineString(coords)
        feature = Feature(geometry=linestring)
        feature_collection = FeatureCollection([feature])
        return feature_collection

    #TODO: implement other graph utility functions from notebook, such as the various graph inspection functions.

    """ ##############################################   UTILUTY METHODS SECTION ENDS   ############################################## """
