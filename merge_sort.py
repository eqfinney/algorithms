# My implementation of the merge sort algorithm
# Author: Emily Quinn Finney

"""
Challenge extensions:
- can we get this to work with any iterable?
- GENERATORS???
"""

def merge_sort(unsorted_list):
    """
    Given an unsorted list, returns the sorted version.
    unsorted_list: a list, unsorted.
    sorted_list: a list, sorted.
    """

    n = len(unsorted_list)

    # base case
    if n <= 1:
        return unsorted_list

    else:
        # split the lists in half
        first_list = merge_sort(unsorted_list[(n/2):])
        second_list = merge_sort(unsorted_list[:(n/2)])

        # run through a for loop and sort accordingly
        first_pointer = 0
        second_pointer = 0
        sorted_list = []
        
        for i in range(n):
            # dealing with the end of the list            
            if first_pointer == len(first_list):
                sorted_list += second_list[second_pointer:]
            elif second_pointer == len(second_list):
                sorted_list += first_list[first_pointer:]

            # dealing with cases that are not the end of the list
            elif first_list[first_pointer] <= second_list[second_pointer]:
                sorted_list += [first_list[first_pointer]]
                first_pointer += 1
            else:
                sorted_list += [second_list[second_pointer]]
                second_pointer += 1
        
        return sorted_list
