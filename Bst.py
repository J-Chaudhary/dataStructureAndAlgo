# Author : Jignesh Chaudhary (Student id: 197320)
# this programme is part of assignment question b) and c) will create Node for Binary Search Tree and
# use base case of all functions of BST

import Node

class Tree(object): # create BST with node
    def __init__(self):
        self.root = None

    def insert(self, data): # Base case function to insert data in BST
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node.Node(data)
            return True

    def delete(self, data): # Base case function to delete data from BST
        if self.root is not None:
            return self.root.delete(data)
        else:
            return False

    def find(self, data): # Base case function to find data in BST
        if self.root:
            return self.root.find(data)
        else:
            return False

    def inorder(self): # Base case function to inorder triverse BST
        print()
        if self.root:
            print('Inorder: ')
            self.root.inorder()
        else:
            return False

# this function print BST each level in saprate line
    def printbylevels(self):
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        queue.append("newline")
        while len(queue) > 0:
            self.root = queue.pop(0)
            if self.root == "newline":
                print ()
                if len(queue) > 0:
                    queue.append("newline")
                continue
            else:
                print (self.root.data,end = " ")
            if self.root.left != None:
                queue.append(self.root.left)
            if self.root.right != None:
                queue.append(self.root.right)

# this function will mirror tree by interchanging subtrees
    def mirror(self):
        self.root.mirror()
        self.root.right.mirror()
        self.root.left.mirror()

