# Assignment 6
# Author: Jignesh Chaudhary, Student Id: 197320
# c) CompareSearch: Implement Interpolation Search algorithm from textbook (Algorithm 8.1) and the Binary Search algorithm from textbook
# (Algorithm 1.5). Try different problem instances against both algorithms to analyze best-case, average-case, and worstcase. Compare the
# performances of both of the algorithms based on your results and how they compare to each other.


def interpolationSearch(input, x):
    n = len(input)
    low = 0
    high = int(n - 1)
    i = 0
    if input[low] <= x <= input[high]:
        while low <= high and i == 0:
            denominator = input[high] - input[low]
            if denominator == 0:
                mid = low
            else:
                mid = low + (x - input[low]) * (high - low) / denominator
                if input[int(mid)] == x:
                    i = int(mid)
                elif x < input[int(mid)]:
                    high = int(mid) - 1
                else:
                    low = int(mid) + 1
    return int(mid)


def binarySearch(input, x):
    low = 0
    high = len(input) - 1
    while low <= high:
        mid = (low + high) / 2
        if input[int(mid)] == x:
            return int(mid)
        if input[int(mid)] > x:
            high = int(mid) - 1
        else:
            low = int(mid) + 1
    return mid


if __name__ == '__main__':
    input1 = (7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
    x1 = 11
    input2 = (21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
    x2 = 27
    print("InterpolationSearch usinginput1: ", interpolationSearch(input1, x1))
    print("BinarySearch using input1:", binarySearch(input1, x1))
    print("InterpolationSearch usinginput2:", interpolationSearch(input2, x2))
    print("BinarySearch using input2:", binarySearch(input2, x2))
