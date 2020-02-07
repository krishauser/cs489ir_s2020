"""A simple graph data structure.  For better performance, use NetworkX."""

from six import iteritems

class AdjListGraph:
    """A very simple adjacency list graph structure.  For higher performance use
    in Python, you will probably want to learn a library like networkx, which will
    have graph search algorithms built in.
    
    The API here is a simplified version of networkx.DiGraph and is somewhat
    compatible.
    """
    def __init__(self,vertices,edges):
        self.vertices = vertices
        self.edges = dict((v,[]) for v in vertices)
        for (v,w) in edges:
            self.edges[v].append(w)
            
    def neighbors(self,v):
        return self.edges[v]
        
    def nodes(self):
        return self.vertices
    
    def add_node(self,v):
        assert v not in self.edges
        self.vertices.append(v)
        self.edges[v] = []
    
    def add_edge(self,v,w):
        assert v in self.edges
        assert w in self.edges
        self.edges[v].append(w)
    
    def subgraph(self,node_subset):
        """Extracts the subgraph corresponding to a set of nodes"""
        nodeset = set(node_subset)
        vertices = list(node_subset)
        edges = []
        for (v,w) in self.edges_iter():
            if v in nodeset and w in nodeset:
                edges.append((v,w))
        return AdjListGraph(vertices,edges)
    
    def edges_iter(self):
        """Returns an iterator over edges (v,w)"""
        for k,v in iteritems(self.edges):
            for w in v:
                yield (k,w)
        return
    
    def assert_valid(self):
        """Asserts that the graph is constructed properly"""
        assert len(self.edges) == len(self.vertices),"Edge list and vertices do not have the same length"
        for v in self.vertices:
            try:
                hash(v)
            except Exception:
                assert False,"Vertex "+str(v)+" is not hashable"
            assert v in self.edges,"Vertex "+str(v)+" has no edge list"
        for k,v in self.edges.items():
            for w in v:
                try:
                    hash(w)
                except Exception:
                    assert False,"Invalid neighbor of "+str(k)+": "+str(w)
                assert w in self.edges,"Invalid neighbor of "+str(k)+": "+str(w)
