#
# My implementation of QuickSort using a randomized pivot
# Author: Emily Quinn Finney
#

import random
import statistics as stats

#import sys; sys.setrecursionlimit(100000)


def read_integers(text):
    """
    Reads a file of integers.
    """
    intlist = []
    with open(text, 'r') as f:
        for line in f:
            integer = int(line.strip())
            intlist.append(integer)

    print(len(intlist))

    return intlist


def quicksort(any_list):
    """
    Takes in any list and returns a sorted version.
    >>> quicksort([3, 2, 1])
    [1, 2, 3]
    >>> quicksort([2, 3, 4])
    [2, 3, 4]
    >>> quicksort([3, 5, 2, 3, 9])
    [2, 3, 3, 5, 9]
    >>> quicksort([7, 8, 2, 9, 4, 8, 1, 2, 5])
    [1, 2, 2, 4, 5, 7, 8, 8, 9]
    """

    n = len(any_list)

    if n <= 1:
        return any_list

    else:

        pivot = random.choice(range(len(any_list)))
        pivot_value = any_list[pivot]
        any_list[0], any_list[pivot] = any_list[pivot], any_list[0]

        split_list, partition = partition_list(any_list)

        if partition == n:
            before_partition = quicksort(split_list[1:])
            after_partition = []
        elif partition == 1:
            after_partition = quicksort(split_list[1:])
            before_partition = []
        else:
            before_partition = quicksort(split_list[1:partition])
            after_partition = quicksort(split_list[partition:])
        
        return before_partition + [split_list[0]] + after_partition


def quicksort_first(any_list):
    """
    Takes in any list and returns a sorted version.
    """

    n = len(any_list)

    if n <= 1:
        return any_list, 0

    else:
        first = any_list[0]
        
        split_list, partition = partition_list(any_list, 0, n)
        comparisons = n-1

        any_list[0:partition], newcompb = quicksort_first(any_list[0:partition])
        any_list[partition+1:n], newcompa = quicksort_first(any_list[partition+1:n])
        comparisons += newcompb + newcompa            

        return any_list, comparisons


def quicksort_last(any_list):
    """
    Takes in any list and returns a sorted version.
    """

    n = len(any_list)

    if n <= 1:
        return any_list, 0

    else:
        any_list[n-1], any_list[0] = any_list[0], any_list[n-1]

        split_list, partition = partition_list(any_list, 0, n)
        comparisons = n-1

        any_list[0:partition], newcompb = quicksort_last(any_list[0:partition])
        any_list[partition+1:n], newcompa = quicksort_last(any_list[partition+1:n])
        comparisons += newcompb + newcompa
            
        return any_list, comparisons
    

def quicksort_median(any_list):
    """
    Takes in any list and returns a sorted version.
    """

    n = len(any_list)

    if n <= 1:
        return any_list, 0

    else:

        middle_index = find_middle(any_list)
        first, middle, last = any_list[0], any_list[middle_index], any_list[n-1]
        median = stats.median([first, middle, last])
        if median == first:
            pass
        elif median == last:
            any_list[n-1], any_list[0] = any_list[0], any_list[n-1]
        else:
            any_list[middle_index], any_list[0] = any_list[0], any_list[middle_index]

        split_list, partition = partition_list(any_list, 0, n)
        comparisons = n-1

        any_list[0:partition], newcompb = quicksort_median(any_list[0:partition])
        any_list[partition+1:n], newcompa = quicksort_median(any_list[partition+1:n])
        comparisons += newcompb + newcompa
            
        return any_list, comparisons


def find_middle(any_list):
    """
    Locates the middle value in a list.
    """
    n = len(any_list)
    if n % 2 == 0:
        middle = int(len(any_list)/2)-1
    else:
        middle = int(len(any_list)/2)

    return middle


def partition_list(any_list, left_index, right_index):
    """
    Partitions the list
    """

    pivot_value = any_list[left_index]
    i = left_index + 1

    for j in range(i, right_index):
        if any_list[j] < pivot_value:
            any_list[i], any_list[j] = any_list[j], any_list[i]
            i += 1
        else:
            pass

    any_list[left_index], any_list[i-1] = any_list[i-1], any_list[left_index]

    return any_list, i-1
        

if __name__ == '__main__':
    integers = read_integers('integers_2.txt')
    first = quicksort_first(integers)[1]
    integers = read_integers('integers_2.txt')
    last = quicksort_last(integers)[1]
    integers = read_integers('integers_2.txt')
    median = quicksort_median(integers)[1]
    print(first, last, median)

    
