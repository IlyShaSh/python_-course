from collections import defaultdict
import unittest


class Graph:
    def fleury(self, start_vertex):
        visited_edges = defaultdict(list)
        eulerian_path = []
        current_vertex = start_vertex
        while graph[current_vertex]:
            for neighbor in graph[current_vertex]:
                if len(graph[current_vertex]) != 0 or len(graph[neighbor]) != 0:
                    edge = (current_vertex, neighbor)
                    graph[current_vertex].remove(neighbor)
                    graph[neighbor].remove(current_vertex)
                    visited_edges[current_vertex].append(neighbor)
                    visited_edges[neighbor].append(current_vertex)
                    eulerian_path.append(edge)
                    current_vertex = neighbor
                    break
        return eulerian_path


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sort = Graph()

    def test_fleury(self):
        self.assertEqual(self.sort.fleury(start_vertex), [('F', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'A'),
                                                          ('A', 'E'), ('E', 'B'), ('B', 'D'), ('D', 'C'),
                                                          ('C', 'E'), ('E', 'D'), ('D', 'F')])


graph = {
    'A': ['B', 'C', 'E', 'F'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['A', 'B', 'C', 'D'],
    'F': ['A', 'D']
}

start_vertex = 'F'
