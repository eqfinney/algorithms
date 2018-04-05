# A Collection of Algorithms
Author: Emily Quinn Finney

My implementations of algorithms discussed in Stanford's Coursera Algorithms 
specialization (https://www.coursera.org/specializations/algorithms). As per 
the Coursera honor code, this does not include any algorithms that solve the 
course's programming assignments. The only algorithms included are those 
described in lectures that are not required as homework, or are modified 
versions of homework algorithms. Algorithms implemented for interview 
practice are also included.


## Features/Details

The following includes a brief description of each module in the repo.
* bfs.py: Creates an object (BFSearcher) that, given a graph, can find the shortest path between two vertices and all connected components of the graph.
* dfs.py: Creates an object (DFSearcher) that, given a graph, can find all strongly connected components of the graph using recursion. Note this tends to hit Python's recursion limit on large graphs. 
* karatsuba.py: Recursively implements the Karatsuba multiplication algorithm for two integers of equal size.
* matrix_multiply.py: Recursively implements Strassen's matrix multiplication algorithm for two NxN matrices. 
* merge_sort.py: Given a list of integers, returns the sorted version of that list using the merge sort algorithm. 
* random_quicksort.py: Given a list of integers, returns the sorted version of that list using the quicksort algorithm, choosing the pivot value randomly. 
* selection.py: Given a list of integers, chooses a random pivot value and divides the list into two sections (values below and above the pivot value).
* substring.py: Given a string and an array of strings, returns the smallest substring in the string that contains all elements of the array.


## Running Tests

Modules are tested with Python's doctests library. Running the code suffices
to run the doctests, and examples are shown in each function's docstrings. 

Last edited 04/05/2018