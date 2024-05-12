import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    priority_queue = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_huffman_codes(root, current_code, codes):
    if root:
        if root.char is not None:
            codes[root.char] = current_code
        build_huffman_codes(root.left, current_code + '0', codes)
        build_huffman_codes(root.right, current_code + '1', codes)

def huffman_encode(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1

    root = build_huffman_tree(freq_dict)
    codes = {}
    build_huffman_codes(root, '', codes)

    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

# Example Usage
text = "apple"
encoded_text, codes = huffman_encode(text)
print("Encoded Text:", encoded_text)
print("Huffman Codes:", codes)
