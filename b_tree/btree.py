# TODO:
# - Testar
#     - fazer prints
# - encapsular

# https://www.geeksforgeeks.org/insert-operation-in-b-tree/
class Btree:
    def __init__(self, order: int):
        self.order: int = order
        self.children = []
        self.parent = None
        self.keys = []

    def insert(self, element: int, children=None):
        insert_idx = 0
        for idx, key in enumerate(self.keys):
            if key > element:
                insert_idx = idx
                break

        if len(self.children) >= insert_idx + 1 and not children:
            self.children[insert_idx].insert(element)

        if len(self.keys) < self.order - 1:
            self.keys = self.keys[: insert_idx - 1] + element + self.keys[insert_idx:]

            if children:
                self.children = (
                    self.children[: insert_idx - 1]
                    + element
                    + self.children[insert_idx:]
                )

            if len(self.keys) == self.order - 1:
                self.promote()

    def promote(self):
        middle_idx = int((self.order - 1) / 2)
        middle_key = self.keys[middle_idx]

        right_tree = Btree(self.order)
        right_tree.order = self.keys[middle_idx + 1 :]
        right_tree.children = self.children[middle_idx + 1 :]

        self.keys = self.keys[:middle_idx]
        self.children = self.children[:middle_idx]

        if not self.parent:
            self.parent = right_tree.parent = Btree(self.order)
            self.parent.keys[0] = middle_key
            self.parent.children = [self, right_tree]
        else:
            self.parent.insert(middle_key, [self, right_tree])
