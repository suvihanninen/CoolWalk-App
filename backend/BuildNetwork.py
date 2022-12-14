# import ReadData class
import PreprocessData as preprocessedData

# import modules
import osmnx as ox

"""
Utility class responsible for building graph/network based on the preprocessed data recieved from PreprocessData class 
"""

class BuildNetwork:

    """
    Constructing a directional multi graph class from the networkX library MultiDiGraph constructor
    """
    @staticmethod
    def build_multidigraph() -> any:
        __preprocessed_nodes, __preprocessed_edges = preprocessedData.PreprocessData().get_preprocessed_data()

        __directed_multi_graph = ox.utils_graph.graph_from_gdfs(__preprocessed_nodes, __preprocessed_edges, graph_attrs=None)

        return __directed_multi_graph


# TODO Suggestion from Maria add attribute values to the edges in the graph manually. fx. by G[<src>][<dst>][<attr_name>] = <value> (See networkX documention for the Graph.get_edge_data method). 
