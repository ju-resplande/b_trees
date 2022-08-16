# TODO:
# - Testar mais
# - Nome da ordem

# https://www.geeksforgeeks.org/insert-operation-in-b-tree/


class Btree:
    def __init__(self, order: int):
        self.root = BtreeNode(order)

    def insert(self, element: int):
        self.root.insert(element)

        while self.root.parent:  # Houve promoção
            self.root = self.root.parent

    def __repr__(self) -> str:
        return f"Btree(order={self.order})"

    def __str__(self) -> str:
        return str(self.root)


class BtreeNode:
    def __init__(self, order: int):
        self.order: int = order
        self.children = []
        self.parent = None
        self.keys = []

    def __repr__(self) -> str:
        return f"BtreeNode(order={self.order}, keys={self.keys})"

    def __str__(self) -> str:
        nodes = str(self.keys) + "\n"

        for child in self.children:
            nodes += str(child)

        return nodes

    def insert(self, element: int, promotion_children: list = []):
        insert_idx = 0

        for key in self.keys:
            if element < key:
                break
            insert_idx += 1

        if self.children and not promotion_children:
            self.children[insert_idx].insert(element)
        else:
            self.keys = self.keys[:insert_idx] + [element] + self.keys[insert_idx:]

            if promotion_children:
                self.children = (
                    self.children[:insert_idx]
                    + promotion_children
                    + self.children[insert_idx:]
                )

            if len(self.keys) == self.order - 1:
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
            self.parent = right_tree.parent = BtreeNode(self.order)
            self.parent.keys = [middle_key]
            self.parent.children = [self, right_tree]
        else:
            self.parent.insert(middle_key, [self, right_tree])
