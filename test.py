from b_tree.btree import Btree

btree = Btree(4)

for element in [3, 2, 1, 4]:
    btree.insert(element)
    print('Btree root')
    print(repr(btree.root))
    print('Btree')
    print(btree)
