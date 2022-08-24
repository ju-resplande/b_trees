"""
https://www.ime.usp.br/~pf/estruturas-de-dados/aulas/B-trees.html
"""


class Btree:
    def __init__(self, order: int):
        self.root = BtreeNode(order)
        self.height = -1

    def insert(self, element: int):
        if self.height == -1:
            self.height = 0

        self.root.insert(element)

        while self.root.parent:  # Houve promoção
            self.root = self.root.parent
            self.height += 1

    def search(self, element: int):
        return self.root.search(element)

    def __repr__(self) -> str:
        return f"Btree(order={self.order})"

    def __str__(self) -> str:
        line = [self.root]

        out = ""
        while line:
            item = line.pop(0)
            out += str(item) + "\n"

            for child in item.children:
                line.append(child)

        return out


class BtreeNode:
    def __init__(self, order: int):
        self.order: int = order
        self.children = []
        self.parent = None
        self.keys = []

    def __repr__(self) -> str:
        return f"BtreeNode(order={self.order}, keys={self.keys})"

    def __str__(self) -> str:
        return str(self.keys)

    def search(self, element: int):
        idx = 0

        for key in self.keys:
            if element == key:
                return key
            elif element < key:
                break
            idx += 1

        if self.children:
            return self.children[idx].search(element)
        else:
            return -1

    def insert(self, element: int):
        insert_idx = 0

        for key in self.keys:
            if element < key:
                break
            insert_idx += 1

        if self.children:
            self.children[insert_idx].insert(element)
        else:
            self.keys = self.keys[:insert_idx] + [element] + self.keys[insert_idx:]

            if len(self.keys) == self.order:
                self.promote()

    def promote(self):
        middle_idx = int(len(self.keys) / 2)
        middle_key = self.keys[middle_idx]

        right_tree = BtreeNode(self.order)
        right_tree.keys = self.keys[middle_idx + 1 :]
        right_tree.children = self.children[middle_idx + 1 :]

        self.keys = self.keys[:middle_idx]
        self.children = self.children[: middle_idx + 1]

        if not self.parent:
            self.parent = BtreeNode(self.order)
            self.parent.children = [self]

        right_tree.parent = self.parent

        insert_idx = self.parent.children.index(self)
        self.parent.keys = (
            self.parent.keys[:insert_idx] + [middle_key] + self.parent.keys[insert_idx:]
        )
        self.parent.children = (
            self.parent.children[: insert_idx + 1]
            + [right_tree]
            + self.parent.children[insert_idx + 1 :]
        )
