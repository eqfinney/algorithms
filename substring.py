def get_shortest_unique_substring(arr, string):
    """
    >>> get_shortest_unique_substring(["A"], "")
    ''
    >>> get_shortest_unique_substring(["A"], "B")
    ''
    >>> get_shortest_unique_substring(["A"], "A")
    'A'
    >>> get_shortest_unique_substring(["x", "y", "z", "r"], "xyyzyzyx")
    ''
    >>> get_shortest_unique_substring(["A", "B", "C", "E", "K", "I"], "KAD0BEC0DEBANCDDDEI")
    'KAD0BEC0DEBANCDDDEI'
    >>> get_shortest_unique_substring(["A", "B", "C"], "AD0BEC0DEBANCDDD")
    'BANC'
    >>> get_shortest_unique_substring(["x", "y", "z"], "xyyzyzyx")
    'zyx'
    """
    
  
    element_index = return_indices(arr, string)

    if element_index == []:
        return ''

    else:
        # this creates our window
        window_size = max(element_index) - min(element_index) + 1
        smallest_string = string[min(element_index):max(element_index)+1]
            
        for i in range(min(element_index), len(string)):
            new_str = string[i:i+window_size]
            new_element_index = return_indices(arr, new_str)
            
            if new_element_index == []:
                continue
            
            new_window_size = max(new_element_index) - min(new_element_index) + 1
            
            if new_window_size < window_size:
                window_size = new_window_size
                i = min(new_element_index)
                string = new_str[min(new_element_index):]
                smallest_string = new_str[min(new_element_index):max(new_element_index)+1]

                if len(smallest_string) == len(arr):
                    break
                    
        return smallest_string


def return_indices(arr, string):
    
    element_index = []
    # the edge case where the substring doesn't exist
    for index, element in enumerate(arr):
        if element not in string:
            return []
        else:
            # find the first instance of that element in the string
            element_index.append(string.index(element))

    return element_index
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
