#
# My implementation of QuickSort using a randomized pivot
# Author: Emily Quinn Finney
#

import random
import statistics as stats


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

        split_list, partition = partition_list(any_list, 0, n)

        any_list[0:partition] = quicksort(any_list[0:partition])
        any_list[partition+1:n] = quicksort(any_list[partition+1:n])
            
        return any_list


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
    import doctest
    doctest.testmod()
