import unittest


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.result = []

    def find_euler_path(self, start_vertex):
        self.result = []
        self._dfs(start_vertex)
        return self.result

    def _dfs(self, current_vertex):
        while self.graph[current_vertex]:
            neighbor = self.graph[current_vertex].pop()
            self.graph[neighbor].remove(current_vertex)
            self._dfs(neighbor)
        self.result.append(current_vertex)


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sort = Graph(graph)

    def test_EulerPath(self):
        self.assertEqual(self.sort.find_euler_path(start_vertex),
                         ['F', 'A', 'B', 'C', 'A', 'E', 'B', 'D', 'C', 'E', 'D', 'F'])


graph = {
    'A': ['B', 'C', 'E', 'F'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['A', 'B', 'C', 'D'],
    'F': ['A', 'D']
}

start_vertex = 'F'
