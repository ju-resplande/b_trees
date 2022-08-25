from b_tree.btree import Btree

btree = Btree(3)

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
    print(btree)

print("btree")
print(btree)

print(btree.search(39))
print(btree.search(42))

print(btree.height)