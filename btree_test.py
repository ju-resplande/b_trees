from b_tree.btree import BTree

btree = BTree(3)

elements = [
    3,
    2,
    1,
    4,
    10,
    11,
    34,
    120,
    128,
    39,
    190,
    42,
    200,
    201,
    203
]

for element in elements:
    btree.insert(element)
    print(btree.height)
    print(btree)

print("btree")
print(btree)

print(btree.search(39))
print(btree.search(43))

print(btree.height)