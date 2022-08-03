# According to Knuth's definition, a B-tree of order m is a tree which satisfies the following properties:[7]

# 1. Every node has at most m children.
# 2. Every internal node has at least ⌈m/2⌉ children.
# 3. Every non-leaf node has at least two children.
# 4. All leaves appear on the same level and carry no information.
# 5. A non-leaf node with k children contains k−1 keys.

from typing import List


# TODO: deixar keys, children como dado interno
# TODO: checar busca
# TODO: split children
# TODO: printar árvore

# https://www.geeksforgeeks.org/insert-operation-in-b-tree/
class Btree:
    def __init__(self, order: int):
        self.order: int = order
        self.children = [None] * self.order
        self.parent = None
        self.keys = [None] * (self.order - 1)

    @staticmethod
    def search(btree, element: int):
        node = btree

        while True:
            for idx in range(len(node.keys)):
                if idx == len(node.keys) - 1:
                    idx += 1
                    break

                if node.keys[idx + 1] > element:
                    break
                elif node.keys[idx + 1] == element:
                    return node, idx

            if node.children[idx]:
                node = node.children[idx]
            else:
                break

    def insert(element: int):
        raise NotImplementedError

    def _split_children(self):
        raise NotImplementedError
