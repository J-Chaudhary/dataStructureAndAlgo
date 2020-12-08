# Author : Jignesh Chaudhary (Student id: 197320)
# this programme will generage list with 10 randum numbers to create raw data
# which is unsorted and random numbers in unsorted series and return raw data list
# with sorted data list

# this part of code will generate raw data to test our quick sort function
import random

testdata = [] #empty list

for i in range (10):# loop to populate list with 10 random elements
    i = random.randint(1,100)
    testdata.append(i)

print ("Raw array :", testdata) # print random generated list



def partition(list): # method to devide list
    length = len(list)
    lower=[]
    higher=[]
    pivot = list[length-1]
    for i in range(length-1): # loop to compare each element with pivot
        item = list[i]
        if item < pivot:
            lower += [item]
        else: higher += [item]
    return lower, pivot, higher


def quicksort(list):#Quick sort devided lists and concatenate them
    if len(list)<=1: #base case
        return list
    else: # recursive case
        (lower, pivot, higher) = partition(list)
        sort_lower = quicksort(lower)
        sort_higher = quicksort(higher)
    return sort_lower + [pivot] + sort_higher

print ("Sorted List:", quicksort(testdata))

