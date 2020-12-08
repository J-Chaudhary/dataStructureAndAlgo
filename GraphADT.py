class Vertex:
    '''This class will create Vertex of Graph, include methods
    add neighbours(v) and rem_neighbor(v)'''

    def __init__(self, n):  # To initiate instance Graph Vertex
        self.name = n
        self.neighbors = list()
        self.color = 'black'

    def add_neighbor(self, v):  # To add neighbour in graph
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

    def rem_neighbor(self, v):  # To remove neighbor in graph
        if v in self.neighbors:
            self.neighbors.remove(v)


class Graph:
    '''This Graph Class will implement Graph using adjacency list include
    methods add vertex, add edge and dfs triversal that print Vertax label using
    adjacency list '''
    vertices = {}  # create directory

    def add_vertex(self, vertex):  # To add vertex
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, src, dst):  # To add Edges
        if src in self.vertices and dst in self.vertices:
            for key, value in self.vertices.items():
                if key == src:
                    value.add_neighbor(dst)
                if key == dst:
                    value.add_neighbor(src)
            return True
        else:
            return False

    def rem_edge(self, src, dst):  # To remove Edges
        if src in self.vertices and dst in self.vertices:
            self.vertices[src].rem_neighbor(dst)
            self.vertices[dst].rem_neighbor(src)
            print("Edges removed from {} to {}".format(src, dst))
            return True
        else:
            return False

    def dfs(self, vertex):  # dfs Triversal
        vertex.color = 'blue'
        for v in vertex.neighbors:
            if self.vertices[v].color == 'black':
                self.dfs(self.vertices[v])
        vertex.color = 'blue'
        if vertex.color == 'blue':
            for key in sorted(list(self.vertices.keys())):
                print(key + str(self.vertices[key].neighbors))
