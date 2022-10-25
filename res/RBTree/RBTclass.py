import math


class Node:
    def __init__(self, key):
        self.key = key
        self.color = ""
        self.p = None
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.root = None

    def get_name(self):
        return "red-black tree"

    def clear(self):
        self.set_root(None)

    def set_root(self, node):
        self.root = node
        if self.root:
            self.root.color = "BLACK"

    def insert(self, key):
        z = Node(key)
        if not self.root:
            self.set_root(z)
        else:
            self.insert_node(z)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.p = x
        y.p = x.p
        if not x.p:
            self.set_root(y)
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.p = x
        y.p = x.p
        if not x.p:
            self.set_root(y)
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y

    def insert_node(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if not y:
            self.set_root(z.key)
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.color = "RED"
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        while z.p and z.p.color == "RED":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y and y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = "BLACK"
                    z.p.p.color = "RED"
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y and y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = "BLACK"
                    z.p.p.color = "RED"
                    self.left_rotate(z.p.p)
        self.root.color = "BLACK"

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
    parent = Node(3)
    son = Node(4)
    son.p = parent
    parent.right = son
    if son.p.right is son:
        print("it will work!")
    pass


if __name__ == "__main__":
    main()
