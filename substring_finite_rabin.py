import unittest


class StringSearchAlgorithms:
    @staticmethod
    def rabin_karp(text, pattern):
        n = len(text)
        m = len(pattern)
        if m == 0:
            return -1
        if n < m:
            return -1
        d = 256
        q = 101
        h = pow(d, m - 1) % q
        p = 0
        t = 0
        result = []
        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q
        for i in range(n - m + 1):
            if p == t:
                if pattern == text[i:i + m]:
                    result.append(i)
            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                if t < 0:
                    t = t + q
        if result:
            return result
        return -1

    @staticmethod
    def finite_automaton(text, pattern):
        m = len(pattern)
        if m == 0:
            return -1
        char_set = set(text)
        transition = {}
        for state in range(m + 1):
            for char in char_set:
                k = min(m, state + 1)
                while not (pattern[:state] + char).endswith(pattern[:k]):
                    k -= 1
                transition[state, char] = k
        state = 0
        result = []
        for i, char in enumerate(text):
            state = transition.get((state, char), 0)
            if state == m:
                result.append(i - m + 1)

        if result:
            return result
        return -1


class TestStringSearchAlgorithms(unittest.TestCase):

    def test_rabin_karp(self):
        text = "nalana"
        pattern = "na"
        self.assertEqual(StringSearchAlgorithms.rabin_karp(text, pattern), [0, 4])

        text_2 = "rioroirioroi"
        pattern_2 = "roi"
        self.assertEqual(StringSearchAlgorithms.rabin_karp(text_2, pattern_2), [3, 9])

        pattern_3 = "abc"
        self.assertEqual(StringSearchAlgorithms.rabin_karp(text, pattern_3), -1)

    def test_finite_automaton(self):
        text = "roiriorioroi"
        pattern = "roi"
        self.assertEqual(StringSearchAlgorithms.finite_automaton(text, pattern), [0, 9])

        text2 = "xaxaxa"
        pattern2 = "xa"
        self.assertEqual(StringSearchAlgorithms.finite_automaton(text2, pattern2), [0, 2, 4])

        pattern3 = "abc"
        self.assertEqual(StringSearchAlgorithms.finite_automaton(text, pattern3), -1)


if __name__ == '__main__':
    unittest.main()
