class Graph:
    def __init__(self):
        self.adj_list = {} #adjacency list to store graph vertices and edges

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = [] #add a vertex with empty edge list

    def add_edge(self, v1, v2, weight=1.0):
        if v1 not in self.adj_list:
            self.add_vertex(v1) #ensure vertex v1 exists
        if v2 not in self.adj_list:
            self.add_vertex(v2) #ensure vertex v2 exists
        self.adj_list[v1].append((v2, weight))  #add edge from v1 to v2
        self.adj_list[v2].append((v1, weight))  #add edge from v2 to v1 (undirected graph)

    def get_neighbors(self, v):
        return self.adj_list.get(v, []) #return neighbors and edge weights of vertex v

    def __str__(self):
        return str(self.adj_list) #string representation of adjacency list
    def clear_edges(self):
        for vertex in self.adj_list:
            self.adj_list[vertex] = [] #remove all edges from every vertex
    def vertices(self):
        return list(self.adj_list.keys()) #return list of all vertices
    def clear(self):
        self.adj_list={}