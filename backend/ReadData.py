# import modules
import pandas as pd



"""
    Utility class responsible for reading data from CSV file (TODO: make it read from PostGis data base) and return it as pandas dataframes

"""
class ReadData():
    __dfNodes = pd.read_csv("../data/CoolWalksDataStorge/nottingham/nottingham_nodes.csv")
    __dfEdges = pd.read_csv("../data/CoolWalksDataStorge/nottingham/nottingham_edges.csv")

    """considered as utility functions and therefore implemented with the @staticmethod decorator"""
    @staticmethod
    def get_nodes_as_pd() -> pd.DataFrame:
        return ReadData.__dfNodes

    @staticmethod
    def get_edges_as_pd() -> pd.DataFrame:
        return ReadData.__dfEdges


instance = ReadData()

instance.get_edges_as_pd
    