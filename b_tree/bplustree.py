"""
https://www.ime.usp.br/~pf/estruturas-de-dados/aulas/B-trees.html
"""
import math

class BPlusTree:
    def __init__(self, order: int):
        self.root = BPlusTreeNode(order)
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
        return f"BPlusTree(order={self.order})"

    def __str__(self) -> str:
        level = [self.root]

        out = ""
        while level: 
            out += " ".join([str(i) for i in level]) + "\n"
            if not level[0].children:
                linked_list = []
                link = level[0]
                while link: 
                    linked_list.append(link)
                    link = link.next_node
                out += "##" + "->".join([str(i) for i in linked_list]) + "##" + "\n" 

            new_level = []
            for item in level:
                for child in item.children:
                    new_level.append(child)

            level = new_level
        return out


class BPlusTreeNode:
    def __init__(self, order: int):
        self.order: int = order
        self.children = []
        self.parent = None
        self.keys = []
        self.next_node = None

    def __repr__(self) -> str:
        return f"BPlusTreeNode(order={self.order}, keys={self.keys})"

    def __str__(self) -> str:
        return str(self.keys)

    def search(self, element: int):
        is_leaf = len(self.children) == 0
        idx = 0

        for key in self.keys:
            if element == key and is_leaf:
                return key
            elif element < key:
                break
            elif element == key:
                idx += 1
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
        is_leaf = len(self.children) == 0

        middle_idx = math.floor((len(self.keys) - 1) / 2)
        middle_key = self.keys[middle_idx]
        copy_idx = middle_idx if is_leaf else middle_idx + 1

        right_tree = BPlusTreeNode(self.order)
        right_tree.keys = self.keys[copy_idx :]
        right_tree.children = self.children[copy_idx :]
        #Update parents on the right tree
        for c in right_tree.children:
            c.parent = right_tree

        self.keys = self.keys[:middle_idx]
        self.children = self.children[: copy_idx]

        if is_leaf:
            right_tree.next_node = self.next_node
            self.next_node = right_tree
        else:
            self.next_node = None

        if not self.parent:
            self.parent = BPlusTreeNode(self.order)
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

        # Parentes são promovidos de forma recursiva
        if len(self.parent.keys) == self.order:
            self.parent.promote()
        