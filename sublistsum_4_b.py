# __Author__: Student : Jignesh Chaudhary (id.197320)
# Assignemnt 4 (b) SublistSum(dynamic programming)
from sys import maxsize

class sublistsum:
    ''' an algorithm to determine the largest sum of
        adjacent sub list of numbers (negatives are allowed)'''
    def __init__(self, array):
        self.array = array
        self.a = len(array)

    def run(self):
        ''' Run algorithm on array to get maximum sublist sum as a result'''
        size = self.a # To get length of list
        result = -maxsize - 1 # using python sys module to find largest negative integer
        max_sum = 0
        for i in range(size): #for loop using length of list
            max_sum += self.array[i] #define maximum sum = maximum sum + list[index]
            if (result < max_sum): # if result is less than maximum sum is true
                result = max_sum # result = maximum sum

            if max_sum < 0: # if maximum sum is negative then sum = 0
                max_sum = 0
        return result # will return reuslt

if __name__ == '__main__':

# Assignment 4 Problem (a) Floyd algorithm

    print("======Assignment 4(b) Sublist Sum(Dynamic prog)")
    a = [1, -3, 4, -2, -1, 6]
    array = sublistsum(a)
    print("Result: Maximum contiguous sum = ", array.run() )
