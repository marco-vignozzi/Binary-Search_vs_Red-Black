class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BTree:
    def __init__(self):
        self.root = None

    def get_name(self):
        return "binary tree"

    def clear(self):
        self.set_root(None)

    def set_root(self, key):
        if key:
            self.root = Node(key)
        else:
            self.root = None

    def insert(self, key):
        if not self.root:
            self.set_root(key)
        else:
            self.insert_node(self.root, key)

    def insert_node(self, current_node, key):
        if key <= current_node.key:
            if current_node.left:
                return self.insert_node(current_node.left, key)
            else:
                current_node.left = Node(key)
        else:
            if current_node.right:
                return self.insert_node(current_node.right, key)
            else:
                current_node.right = Node(key)

    def find(self, key):
        return self.find_node(self.root, key)

    def find_node(self, current_node, key):
        if current_node is None:
            return False
        elif current_node.key == key:
            return True
        elif key < current_node.key:
            return self.find_node(current_node.left, key)
        else:
            return self.find_node(current_node.right, key)

    def inorder(self):
        def _inorder(v):
            if v is None:
                return
            if v.left:
                _inorder(v.left)
            print(v.key)
            if v.right:
                _inorder(v.right)
        _inorder(self.root)


def main():
    tree = BTree()
    for x in range(30, 10, -1):
        tree.insert(x)
    print(tree.find(15))
    print(tree.find(4))
    tree.inorder()


if __name__ == "__main__":
    main()
