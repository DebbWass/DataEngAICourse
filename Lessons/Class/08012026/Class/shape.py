"""This is the shape class it contains the
 number of edges and  nodes"""
 
from abc import ABC , abstractmethod

class Shape(ABC):
    def __init__(self, edges, nodes):
        super().__init__()
        self.edges = edges
        self.nodes = nodes
    
    @abstractmethod
    def CalcParimeter(self):
        pass
    
    @abstractmethod
    def CalcArea(self):
        pass
    
    @abstractmethod
    def set_edge_length(self,edge_lenght):
        pass
    
    def get_edges(self):
        return self.edges
 
    def get_nodes(self):
        return self.nodes