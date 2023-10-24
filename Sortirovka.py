import unittest


class Sort:
    # Сортировка вставками:
    def insertion_sort(self, spisok):
        for i in range(1, len(spisok)):
            key = spisok[i]
            j = i - 1
            while j >= 0 and spisok[j] > key:
                spisok[j + 1] = spisok[j]
                j -= 1
            spisok[j + 1] = key
        return spisok

    # Сортировка выбором:
    def selection_sort(self, spisok):
        for i in range(len(spisok)):
            min_idx = i
            for j in range(i + 1, len(spisok)):
                if spisok[j] < spisok[min_idx]:
                    min_idx = j
            spisok[i], spisok[min_idx] = spisok[min_idx], spisok[i]
        return spisok

    # Сортировка пузырьком:
    def bubble_sort(self, spisok):
        for i in range(len(spisok) - 1):
            for j in range(len(spisok) - 1 - i):
                if spisok[j] > spisok[j + 1]:
                    spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
        return spisok


class TestSort(unittest.TestCase):
    def setUp(self):
        self.sort = Sort()

    def test_insertion(self):
        self.assertEqual(self.sort.insertion_sort([2, 19, 1, 4, 9, 3, 7]), [1, 2, 3, 4, 7, 9, 19])

    def test_selection(self):
        self.assertEqual(self.sort.selection_sort([21, 3, 11, 45, 6, 9, 10]), [3, 6, 9, 10, 11, 21, 45])

    def test_bubble(self):
        self.assertEqual(self.sort.bubble_sort([3, 8, 19, 44, -10, 1, 17]), [-10, 1, 3, 8, 17, 19, 44])


if __name__ == "__main__":
    unittest.main()
