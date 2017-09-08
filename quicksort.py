#
# My implementation of QuickSort using a randomized pivot
# Author: Emily Quinn Finney
#

import random
import statistics as stats

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
    #>>> quicksort_first([3, 2, 1])
    #[1, 2, 3]
    #>>> quicksort_first([2, 3, 4])
    #[2, 3, 4]
    #>>> quicksort_first([3, 5, 2, 3, 9])
    #[2, 3, 3, 5, 9]
    #>>> quicksort_first([7, 8, 2, 9, 4, 8, 1, 2, 5])
    #[1, 2, 2, 4, 5, 7, 8, 8, 9]
    >>> quicksort_first([2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504])
    ([504, 609, 2148, 3153, 5469, 6324, 7017, 7628, 7742, 9058], 25)
    """

    n = len(any_list)

    if n <= 1:
        return any_list, 0

    else:

        split_list, partition = partition_list(any_list)
        comparisons = len(any_list) - 1

        if partition == n:
            before_partition, new_comparisons = quicksort_first(split_list[1:])
            after_partition = []
            comparisons += new_comparisons
        elif partition == 1:
            after_partition, new_comparisons = quicksort_first(split_list[1:])
            before_partition = []
            comparisons += new_comparisons
        else:
            before_partition, new_comparisons_before = quicksort_first(split_list[1:partition])
            after_partition, new_comparisons_after = quicksort_first(split_list[partition:])
            comparisons += new_comparisons_before + new_comparisons_after
            
        return (before_partition + [split_list[0]] + after_partition), comparisons


def quicksort_last(any_list):
    """
    Takes in any list and returns a sorted version.
    #>>> quicksort([3, 2, 1])
    #[1, 2, 3]
    #>>> quicksort([2, 3, 4])
    #[2, 3, 4]
    #>>> quicksort([3, 5, 2, 3, 9])
    #[2, 3, 3, 5, 9]
    #>>> quicksort([7, 8, 2, 9, 4, 8, 1, 2, 5])
    #[1, 2, 2, 4, 5, 7, 8, 8, 9]
    >>> quicksort_last([2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504])
    ([504, 609, 2148, 3153, 5469, 6324, 7017, 7628, 7742, 9058], 31)
    """

    n = len(any_list)

    if n <= 1:
        return any_list, 0

    else:
        
        any_list[0], any_list[len(any_list)-1] = any_list[len(any_list)-1], any_list[0]

        split_list, partition = partition_list(any_list)
        comparisons = len(any_list) - 1

        if partition == n:
            before_partition, new_comparisons = quicksort_last(split_list[1:])
            after_partition = []
            comparisons += new_comparisons
        elif partition == 1:
            after_partition, new_comparisons = quicksort_last(split_list[1:])
            before_partition = []
            comparisons += new_comparisons
        else:
            before_partition, new_comparisons_before = quicksort_last(split_list[1:partition])
            after_partition, new_comparisons_after = quicksort_last(split_list[partition:])
            comparisons += new_comparisons_before + new_comparisons_after
            
        return (before_partition + [split_list[0]] + after_partition), comparisons


def quicksort_median(any_list):
    """
    Takes in any list and returns a sorted version.
    #>>> quicksort([3, 2, 1])
    #[1, 2, 3]
    #>>> quicksort([2, 3, 4])
    #[2, 3, 4]
    #>>> quicksort([3, 5, 2, 3, 9])
    #[2, 3, 3, 5, 9]
    #>>> quicksort([7, 8, 2, 9, 4, 8, 1, 2, 5])
    #[1, 2, 2, 4, 5, 7, 8, 8, 9]
    >>> quicksort_median([2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504])
    ([504, 609, 2148, 3153, 5469, 6324, 7017, 7628, 7742, 9058], 21)
    """

    n = len(any_list)

    if n <= 1:
        return any_list, 0

    else:

        first, middle, last = any_list[0], any_list[int(len(any_list)/2) - 1], any_list[len(any_list)-1]
        median = stats.median([first, middle, last])
        if median == first:
            pass
        elif median == last:
            any_list[0], any_list[len(any_list)-1] = any_list[len(any_list)-1], any_list[0]
        else:
            any_list[0], any_list[int(len(any_list)/2)-1] = any_list[int(len(any_list)/2)-1], any_list[0]

        split_list, partition = partition_list(any_list)
        comparisons = n-1

        if partition == n:
            before_partition, new_comparisons = quicksort_median(split_list[1:])
            after_partition = []
            comparisons += new_comparisons
        elif partition == 1:
            after_partition, new_comparisons = quicksort_median(split_list[1:])
            before_partition = []
            comparisons += new_comparisons
        else:
            before_partition, new_comparisons_before = quicksort_median(split_list[1:partition])
            after_partition, new_comparisons_after = quicksort_median(split_list[partition:])
            comparisons += new_comparisons_before + new_comparisons_after
        
        return (before_partition + [split_list[0]] + after_partition), comparisons

def partition_list(any_list):
    """
    Partitions the list
    """

    n = len(any_list)
    pivot_value = any_list[0]
    partition = 1

    for j in range(1, n):
        if any_list[j] < pivot_value:
            any_list[partition], any_list[j] = any_list[j], any_list[partition]
            partition += 1
        else:
            pass
        j += 1

    return any_list, partition
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()

