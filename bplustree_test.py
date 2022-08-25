from b_tree.bplustree import BPlusTree

btree = BPlusTree(3)

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
    203,
    5,
    6,
    7,
    8
]


for element in elements:
    btree.insert(element)
    print(btree.height)
    print(btree)

print("b plus tree")
print(btree)

print(btree.search(39))
print(btree.search(43))

print(btree.height)