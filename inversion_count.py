# My implementation of a divide-and-conquer inversion counter
# Author: Emily Quinn Finney


def count_inversions(numlist):
    """
    Counts the inversions present in an array.
    Input: numlist, a list of numbers
    Output: count, the number of inversions
            
    >>> count_inversions([2,1,3])
    ([1, 2, 3], 1)
    >>> count_inversions([3,2,1])
    ([1, 2, 3], 3)
    >>> count_inversions([3,5,6,7,2])
    ([2, 3, 5, 6, 7], 4)
    >>> count_inversions([3,4,5,1])
    ([1, 3, 4, 5], 3)
    """

    n = len(numlist)

    if n <= 1:
        return numlist, 0

    else:
        first_half, count1 = count_inversions(numlist[:int(n/2)])
        second_half, count2 = count_inversions(numlist[int(n/2):])

        merge_list, count_merge = count_split(first_half, second_half)

        return merge_list, count1+count2+count_merge


def count_split(list1, list2):
    """
    Counts the number of inversions split across a divided array.
    Input: numlist, a list of numbers
    Output: count, the number of split inversions.
    """
    
    count = 0
    pointer1 = 0
    pointer2 = 0
    n = len(list1+list2)
    sorted_list = []
    
    # test to see which list is the smaller list    
    for i in range(n):
        
        # end of the list
        if pointer1 == len(list1):
            sorted_list += list2[pointer2:]
            count += 0
            break
        elif pointer2 == len(list2):
            sorted_list += list1[pointer1:]
            count += 0
            break

        # not at the end of the list
        elif list1[pointer1] <= list2[pointer2]:
            sorted_list += [list1[pointer1]]
            pointer1 += 1
            count += 0
        else:
            sorted_list += [list2[pointer2]]
            pointer2 += 1
            count += len(list1[pointer1:])
            
    return sorted_list, count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
