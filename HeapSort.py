# Assignment 6
# Author: Jignesh Chaudhary, Student Id: 197320
# a) Heapsort: Implement the heapsort algorithm from your textbook (Algorithm 7.5) but modify it so it ends after finding z largest keys
# in non-increasing order. You can hardcode the keys to be integer type. Implement test program to provide unsorted integer list, z
# value, and outputs the z sorted number of elements. Then analyze the algorithm and provide the analysis using big O notation.

class heap:
    '''This class take array as a input and find z number of largest key in non-increasing order
    class has method call siftdown, makeheap, removekey and display'''
    def __init__(self, array, z):
        '''Constructur which create unsorted array from input and take int z to find z number of largest key in array '''
        self.array = []
        self.z = z
        for i in array:
            self.array.append(i)

    def siftdown(self, array, i, size): # this method used by makeheap method to arrange array data in proper manner
        array = self.array
        leftchild = 2*i+1
        rightchild = 2*i+2
        parent = i
        if leftchild <= size-1 and array[leftchild] > array[i]:
            parent = leftchild
        if rightchild <= size-1 and array[rightchild] > array[parent]:
            parent = rightchild
        if parent != i:
            largchild = array[i]
            array[i] = array[parent]
            array[parent] = largchild
            self.siftdown(array, parent, size)

    def makeheap(self):
        size = len(self.array)
        J = (size//2)-1
        while J>=0:
            self.siftdown(self.array, J, size)
            J -= 1

    def removekey(self): # this function will run heapsort algorithm for z number of large key
        end = len(self.array)-1
        for i in range(self.z):# modify algorithm
            root = self.array[0]
            self.array[0] = self.array[end]
            self.array[end] = root
            self.siftdown(self.array, 0, end)
            end -= 1

    def display(self): # to display array
        result=[]
        for i in range(1,len(self.array)-1):
            result.append(self.array[i])
        print(self.array)

if __name__ == '__main__':
    z = 4
    list = [7,8,5,9,3,2,6,4,1,10]
    test = heap(list, z)
    test.display()
    test.makeheap()
    test.removekey()
    test.display()

