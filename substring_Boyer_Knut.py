import unittest


class StringSearchAlgorithms:
    @staticmethod
    def boyer_Moore(text, pattern):
        n = len(text)
        m = len(pattern)
        if m == 0:
            return -1
        last = {}
        for i in range(m):
            last[pattern[i]] = i
        i = m - 1
        k = m - 1
        while i < n:
            if text[i] == pattern[k]:
                if k == 0:
                    return i
                i -= 1
                k -= 1
            else:
                j = last.get(text[i], -1)
                i += m - min(k, j + 1)
                k = m - 1
        return -1

    @staticmethod
    def knut_Morris_Pratt(text, pattern):
        lps = StringSearchAlgorithms.compute_lps(pattern)
        i = 0
        j = 0
        indices = []

        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                indices.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return indices

    @staticmethod
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps


class TestStringSearchAlgorithms(unittest.TestCase):

    def test_Boyer_Moore(self):
        text = "rioroirioroi"
        template = "roi"
        self.assertEqual(StringSearchAlgorithms.boyer_Moore(text, template), 3)

    def test_Knut_Morris_Pratt(self):
        text = "ABABDABACDABABCABAB"
        template = "ABABCABAB"
        self.assertEqual(StringSearchAlgorithms.knut_Morris_Pratt(text, template), [10])


if __name__ == '__main__':
    unittest.main()
