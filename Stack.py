# Student : Jignesh Chaudhary, Student id : 197320 #
# Assignment-1 (a)

class Stack:
    '''This class Implement raw array Stack ADT which include operations for create empty stack,
    isEmpty, isFull, push, and pop methods'''
    def __init__(self):
        self.items = []

    def isEmpty(self): # To chech stack is empty or not
        return self.items == []

    def isFull(self, x): # To chech stack is full or not
        if (len(self.items)) == x:
            print (".... Stck is full....!")
        else:
            print ("Stack has {} Items".format((len(self.items))))

    def push(self, item): # Method to add items in stack
            self.items.append(item)

    def pop(self): # method to pop items
        return self.items.pop()

    def size(self): # to display size of array
        return len(self.items)
