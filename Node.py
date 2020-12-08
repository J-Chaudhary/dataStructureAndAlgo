# Author : Jignesh Chaudhary (Student id: 197320)
# this programme is part of assignment question b) and c) will create Node for Binary Search Tree and
# use recusion for all functions of BST class functions

class Node(object): # Create node in BST
    def __init__(self, data, left = None, right=None):
        self.data = data
        self.left = left
        self.right = right

# this function use recursion to insert data in BST
    def insert(self, data):
        if self.data == data:
            return False
        # As BST cannot contain duplicate data

        # If Data less than the root data is placed to the left of the root
        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        # If Data greater than the root data is placed to the right of the root
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

# We are using in delete function to find minimum value in tree and change it to deleted node
    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current

# Function use recursion to delete data from bst
    def delete(self, data): # to deleting the node
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            # deleting node with one
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # deleting node with two children
            temp = self.minValueNode(self.right)
            self.data = temp.data
            self.right = self.right.delete(temp.data)

        return self

# This function use recursion to find data in bst and return result in True or False
    def find(self, data):
        if(data == self.data):
            print ("True")
        elif(data < self.data):
            if self.left:
                return self.left.find(data)
            else:
                print("False")
        else:
            if self.right:
                return self.right.find(data)
            else:
                print ("False")

#This function use recursion For Inorder traversal of the BST
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.data), end=' ')
            if self.right:
                self.right.inorder()

#This function use recursion to trun bst in to mirror
    def mirror(self):
        tmp = self.left
        self.left = self.right
        self.right = tmp