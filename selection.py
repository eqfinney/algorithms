#
# Partitions a list using the randomized selection algorithm
# Author: Emily Quinn Finney
#

import random

def pick_element(unordered_list, order_statistic):
    """
    Chooses an element of a given order statistic from an unordered list.
    unordered_list: a list of elements (list)
    order_statistic: the location the desired element should be in an
                     ordered array (int)
    >>> pick_element([2, 3, 1, 4, 6], 4)
    6
    >>> pick_element([2, 3, 1, 4, 6], 1)
    2
    """

    n = len(unordered_list)

    if n == 1:
        return unordered_list[0]

    else:

        pivot = random.choice(range(n))
        pivot_value = unordered_list[pivot]
        unordered_list[0], unordered_list[pivot] = unordered_list[pivot], unordered_list[0]
            
        new_list, partition = partition_list(unordered_list)

        if partition-1 == order_statistic:
            element = new_list[0]
        elif partition-1 < order_statistic:
            new_order_statistic = order_statistic - partition
            element = pick_element(new_list[partition:], new_order_statistic)
        else:
            new_order_statistic = order_statistic
            element = pick_element(new_list[1:partition], new_order_statistic)

        return element
    

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
