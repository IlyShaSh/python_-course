from collections import defaultdict
import unittest


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
        self.visited = set()
        self.stack = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs_first_pass(self, vertex):
        self.visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in self.visited:
                self._dfs_first_pass(neighbor)
        self.stack.append(vertex)

    def _dfs_second_pass(self, vertex, component):
        self.visited.add(vertex)
        component.append(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in self.visited:
                self._dfs_second_pass(neighbor, component)

    def Kosaraju_algorithm(self):
        for vertex in self.vertices:
            if vertex not in self.visited:
                self._dfs_first_pass(vertex)
        self.visited.clear()
        strongly_connected_components = []
        while self.stack:
            current_vertex = self.stack.pop()
            if current_vertex not in self.visited:
                current_component = []
                self._dfs_second_pass(current_vertex, current_component)
                strongly_connected_components.append(current_component)

        return strongly_connected_components


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sort = Graph(vertices)

    def test_Kosaraju(self):
        self.assertEqual(self.sort.Kosaraju_algorithm(), [['K'], ['P'], ['F'], ['E'], ['D'], ['C'], ['B'], ['A']])


graph = {
    'A': ['B'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['C'],
    'E': ['D', 'P'],
    'F': ['C', 'E', 'P'],
    'P': ['C', 'D', 'F'],
    'K': ['D', 'F']
}

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'P', 'K']

