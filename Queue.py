# Student : Jignesh Chaudhary,  Student id : 197320
# Assignment - 1 (b)

class Node:
    '''Node for storing data in to queue'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    '''Queue structure implement using link list'''
    def __init__(self): # create empty list
        self.front = None
        self.rear = None

    def isEmpty(self):# to check queue is empty or not and return result
        if self.front == None:
            return True
        return False

    def EnQueue(self, data):# Method to add data to the queue
        new_node = Node(data)
        if self.front == None and self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node


    def DeQueue(self):# Method to remove data from front of the queue

        if self.isEmpty():
            return

        temp = self.front.data
        if (self.front == self.rear):
            self.rear = None
            self.front = None
        else:
            self.front = self.front.next
        return temp

    def size(self): # methhod to check size of Queue
        current = self.front
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def display(self): # Method to display Queue elements
        list = []
        current_node = self.front
        while current_node != None:
            list.append(current_node.data)
            current_node = current_node.next
        print(list)

