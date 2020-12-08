#author : Jignesh Chaudhary (Student id: 197320)
#Test.py include test code for GraphADT

from GraphADT import Vertex
from GraphADT import Graph

g = Graph() # create Graph


def main(graph):
    #Using for loop to add vertex in graph
    for i in range(ord('0'), ord('9')):
        graph.add_vertex(Vertex(chr(i)))
    #Usnign add_edge(src, dst) method to add edges
    graph.add_edge('0', '1')
    graph.add_edge('1', '2')
    graph.add_edge('2', '3')
    graph.add_edge('3', '4')
    graph.add_edge('4', '5')
    graph.add_edge('5', '6')
    graph.add_edge('6', '7')
    graph.add_edge('7', '8')
    graph.add_edge('8', '0')
    graph.add_edge('1', '6')
    graph.add_edge('3', '8')
    # calling dfs triversal
    graph.dfs(Vertex('0'))
    # remove edges using rem_edge(srt, dst) method
    graph.rem_edge('8', '3')
    # calling dfs triversal after remove edge form graph src vertex 8 to dst vertex 3
    graph.dfs(Vertex('0'))

main(g)
