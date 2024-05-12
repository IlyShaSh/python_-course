class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie_tree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_end = True

    def delete(self, word):
        def delete_helper(node, word, depth):
            if depth == len(word):
                if node.is_end:
                    node.is_end = False
                if not node.children:
                    return True
                return False
            i = word[depth]
            if i in node.children:
                if delete_helper(node.children[i], word, depth + 1):
                    del node.children[i]
                    return not node.children
            return False

        if not self.search(word):
            return False
        delete_helper(self.root, word, 0)
        return True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.is_end


trie = Trie_tree()
trie.insert("Moscow")
trie.insert("Kazan")
print(trie.search("Moscow"))  # Результат: True
print(trie.search("Kazan"))  # Результат: True

trie.delete("Moscow")
trie.delete("Kazan")
print(trie.search("Kazan"))  # Результат: False
print(trie.search("Moscow"))  # Результат: False
