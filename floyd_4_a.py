# __Author__: Student : Jignesh Chaudhary (id.197320)
# Assignemnt 4 (a) FloydAnalysis (Dynamic prog)

from math import inf

class floyd_algo:
    '''This class is for implement floyd algorithm to find all pair shortest path in weighted, directed graph. G=(V,E) '''
    def __init__(self, n, edges):
        '''This method tak input n = number or vertexes in a graph and array of edges '''
        self.dist = []
        self.nxt = []
        self.n = n

        for i in range(self.n):  self.dist.append([inf] * self.n)
        for i in range(self.n):  self.nxt.append([0] * self.n)
        for i in range(self.n):  self.dist[i][i] = 0
        for u, v, w in edges:
            self.dist[u - 1][v - 1] = w
            self.nxt[u - 1][v - 1] = v - 1

    def run(self):
        '''This method will run floyd algorithm on object created with floyd_algo class'''
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    sum_ik_kj = self.dist[i][k] + self.dist[k][j]
                    if self.dist[i][j] > sum_ik_kj:
                        self.dist[i][j] = sum_ik_kj
                        self.nxt[i][j] = self.nxt[i][k]

    def print_shortest_paths(self):
        '''Print method to print shortest path all pair of vertexes in graph '''
        # To print output
        print("pair     dist    path")
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    path = [i]
                    while path[-1] != j:
                        path.append(self.nxt[path[-1]][j])
                    print("%d ==> %d  %4d       %s"
                          % (i + 1, j + 1, self.dist[i][j],
                             ' ==> '.join(str(p + 1) for p in path)))

if __name__ == '__main__':
    v = 4
    test = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]
    graph = floyd_algo(v, test)
    graph.run()
    graph.print_shortest_paths()

    v = 5
    test = [[1,2,15],[1,5,2],[2,4,14],[2,3,7],[3,4,12],[4,1,21],[5,4,6],[5,2,9]]
    graph1 = floyd_algo(v, test)
    graph1.run()
    graph1.print_shortest_paths()