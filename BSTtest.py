from Bst import Tree

bst = Tree()

testdata = [10,15,5,4,14,16,6]

for x in testdata:
    bst.insert(x)

def original(): # to print original tree
    print("Original Tree")
    return bst.printbylevels()

def mirror(): # to print mirror tree
    bst.mirror()
    print("Mirror Tree")
    return bst.printbylevels()




original()
mirror()
# Original Tree
# 10
# 5 15
# 4 6 14 16

# Mirror Tree
# 10
# 15 5
# 16 14 6 4