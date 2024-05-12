RED = True
BLACK = False

class Node:
    def __init__(self, key, color=RED):
        self.key = key
        self.left = None
        self.right = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def insert_node(root, key):
            if not root:
                return Node(key)

            if key < root.key:
                root.left = insert_node(root.left, key)
            else:
                root.right = insert_node(root.right, key)

            if is_red(root.right) and not is_red(root.left):
                root = rotate_left(root)
            if is_red(root.left) and is_red(root.left.left):
                root = rotate_right(root)
            if is_red(root.left) and is_red(root.right):
                flip_colors(root)

            return root

        self.root = insert_node(self.root, key)
        self.root.color = BLACK

    def search(self, key):
        def search_node(root, key):
            if not root or root.key == key:
                return root

            if key < root.key:
                return search_node(root.left, key)
            else:
                return search_node(root.right, key)

        return search_node(self.root, key)

    def print_tree(self, node, level=0):
        if node:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.key))
            if node.color == RED:
                print(' ' * 4 * (level + 1) + '(Red)')
            else:
                print(' ' * 4 * (level + 1) + '(Black)')
            self.print_tree(node.left, level + 1)

def is_red(node):
    if not node:
        return False
    return node.color == RED

def rotate_left(node):
    x = node.right
    node.right = x.left
    x.left = node
    x.color = node.color
    node.color = RED
    return x

def rotate_right(node):
    x = node.left
    node.left = x.right
    x.right = node
    x.color = node.color
    node.color = RED
    return x

def flip_colors(node):
    node.color = RED
    node.left.color = BLACK
    node.right.color = BLACK

# Example Usage
rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(5)
rb_tree.insert(15)
rb_tree.insert(3)
rb_tree.insert(7)

print(rb_tree.search(5).key)  # Вывод: 5

print("Red-Black Tree:")
rb_tree.print_tree(rb_tree.root)
