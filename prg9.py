class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def depth_limited_search(root, limit):
    def dls(node, depth):
        if node is None:
            return
        print(node.value, end=' ')
        if depth == limit:
            return
        for child in node.children:
            dls(child, depth + 1)
    dls(root, 0)

root = Node('B')
b = Node('C')
c = Node('D')
d = Node('F')
e = Node('A')
f = Node('E')

root.children = [b, c]
b.children = [d, e]
c.children = [f]

depth_limited_search(root, 2)