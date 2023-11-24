import heapq
import unittest


class Graph():
    def prim(self, graph):
        visited = set()
        dist = []
        start = list(graph.keys())[0]
        visited.add(start)
        edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]
        heapq.heapify(edges)
        while edges:
            weight, current, next = heapq.heappop(edges)
            if next not in visited:
                visited.add(next)
                dist.append((current, next, weight))
                for neighbor, weight in graph[next]:
                    if neighbor not in visited:
                        heapq.heappush(edges, (weight, next, neighbor))
        return dist


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sort = Graph()

    def test_prim(self):
        self.assertEqual(self.sort.prim(graph),
                         [('1', '3', 1), ('1', '2', 2), ('2', '4', 1), ('4', '7', 1), ('2', '5', 3), ('3', '6', 3)])


graph = {
    '1': [('2', 2), ('3', 1), ('4', 3), ('6', 6)],
    '2': [('1', 2), ('4', 1), ('5', 3)],
    '3': [('1', 1), ('4', 2), ('6', 3)],
    '4': [('1', 3), ('2', 1), ('3', 2), ('7', 1)],
    '5': [('2', 3), ('7', 4)],
    '6': [('1', 6), ('3', 3), ('7', 7)],
    '7': [('4', 1), ('5', 4), ('6', 7)],
}
