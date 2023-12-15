import operator
import unittest
import random
from collections import deque


class Sort:
    # Сортировка слиянием
    def merge_sort(self, spisok, compare=operator.lt):
        if len(spisok) < 2:
            return spisok[:]
        else:
            middle = int(len(spisok) / 2)
            left = self.merge_sort(spisok[:middle], compare)
            right = self.merge_sort(spisok[middle:], compare)
            return self.merge(left, right, compare)

    def merge(self, left, right, compare):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if compare(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    # Быстрая сортировка
    def quicksort(self, spisok):
        if len(spisok) <= 1:
            return spisok
        else:
            chislo = random.choice(spisok)
        less = [n for n in spisok if n < chislo]

        equal = [chislo] * spisok.count(chislo)
        more = [n for n in spisok if n > chislo]
        return self.quicksort(less) + equal + self.quicksort(more)

    # Пирамидальная сортировка
    def heapify(self, spisok, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2
        if left_child < heap_size and spisok[left_child] > spisok[largest]:
            largest = left_child
        if right_child < heap_size and spisok[right_child] > spisok[largest]:
            largest = right_child
        if largest != root_index:
            spisok[root_index], spisok[largest] = spisok[largest], spisok[root_index]
            self.heapify(spisok, heap_size, largest)

    def heap_sort(self, spisok):
        n = len(spisok)
        for i in range(n, -1, -1):
            self.heapify(spisok, n, i)
        for i in range(n - 1, 0, -1):
            spisok[i], spisok[0] = spisok[0], spisok[i]
            self.heapify(spisok, i, 0)
        return spisok

    def dfs(self, graph, start, visit=None):
        if visit is None:
            visit = set()
        visit.add(start)
        for next in graph[start] - visit:
            self.dfs(graph, next, visit)
        return visit

    def bfs(self, graph, start):
        visit = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visit:
                visit.add(vertex)
                print(vertex)
                queue.extend(graph[vertex] - visit)


class TestSort(unittest.TestCase):
    def setUp(self):
        self.sort = Sort()

    def test_merge(self):
        self.assertEqual(self.sort.merge_sort([2, 19, 1, 4, 9, 3, 7]), [1, 2, 3, 4, 7, 9, 19])

    def test_quicksort(self):
        self.assertEqual(self.sort.quicksort([3, 8, 19, 44, -10, 1, 17]), [-10, 1, 3, 8, 17, 19, 44])

    def test_heap_sort(self):
        self.assertEqual(self.sort.heap_sort([21, 3, 11, 45, 6, 9, 10]), [3, 6, 9, 10, 11, 21, 45])

    def test_dfs(self):
        self.assertEqual(self.sort.dfs(graph, '0'), {'2', '3', '0', '4', '1'})

    def test_bfs(self):
        self.assertEqual(self.sort.dfs(graph_2, 'A'), {'A', 'B', 'C', 'D', 'E', 'F'})


graph = {'0': set(['1', '2']), '1': set(['0', '3', '4']), '2': set(['0']), '3': set(['1']), '4': set(['2', '3'])}
graph_2 = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}
