# Student : Jignesh Chaudhary,  Student id : 197320
# Assignment - 1 (d)

import Queue
import Stack
def main():
    linklist = Queue.Queue()

    def add():
        data = input("enter data in to queue: ")
        linklist.EnQueue(data)

    def remore():
        linklist.DeQueue()

    def display():
        linklist.display()

    def len():
        linklist.size()

    def rev_display():
        temp = Stack.Stack()
        while not linklist.isEmpty():
            data = linklist.DeQueue()
            temp.push(data)
        tmpQ = Queue.Queue()
        while not temp.isEmpty():
            x = temp.pop()
            tmpQ.EnQueue(x)
        return tmpQ


    print("===========================================================")
    print("1 : Entry, 2: display original, 3: display reverse, 4: exit")
    print("===========================================================")
    print("")

    while True:
        com = input ("Enter command: ")
        if com == str(1):
            add()
        elif com == str(2):
            display()
        elif com == str(3):
            output = rev_display()
            print(output.display())
        elif com == str(4):
            print ("Thank You for Using Testing Queue ADT")
            break

main()
