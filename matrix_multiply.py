#
# Matrix multiplication using Strassen's algorithm
# Author: Emily Quinn Finney
#

import numpy as np

def matrix_multiply(matrix1, matrix2):
    """
    Multiplies two NxN matrices using Strassen's algorithm
    >>> matrix_multiply(np.array([[1, 0], [0, 1]]), np.array([[2, 3],[4, 5]]))
    array([[2, 3],
           [4, 5]])
    """
    assert np.shape(matrix1) == np.shape(matrix2)

    n = np.shape(matrix1)[0]

    # could add a row of zeros to have this work in the general case
    # but I want to spend time learning other stuff
    assert n%2 == 0
    
    if n == 2:
        A, B, C, D = matrix1[0, 0], matrix1[0,1], matrix1[1, 0], matrix1[1, 1]
        E, F, G, H = matrix2[0, 0], matrix2[0,1], matrix2[1, 0], matrix2[1, 1]

    else:
        A = matrix1[:int(n/2)][:int(n/2)]
        B = matrix1[:int(n/2)][int(n/2):]
        C = matrix1[int(n/2):][:int(n/2)]
        D = matrix1[int(n/2):][int(n/2):]
        E = matrix2[:int(n/2)][:int(n/2)]
        F = matrix2[:int(n/2)][int(n/2):]
        G = matrix2[int(n/2):][:int(n/2)]
        H = matrix2[int(n/2):][int(n/2):]
    
    quad1, quad2, quad3, quad4 = get_quads(A, B, C, D, E, F, G, H)

    final_matrix = np.array([[quad1, quad2], [quad3, quad4]])
        
    return final_matrix


def get_quads(A, B, C, D, E, F, G, H):
    """ Get some pieces of matrices
    """

    p1, p2, p3, p4, p5, p6, p7 = get_products(A, B, C, D, E, F, G, H)
        
    # calculate the matrix products
    quad1 = p5 + p4 - p2 + p6
    quad2 = p1 + p2
    quad3 = p3 + p4
    quad4 = p1 + p5 - p3 - p7

    return quad1, quad2, quad3, quad4


def get_products(A, B, C, D, E, F, G, H):
    """ get some pieces of products
    """

    p1 = A*(F-H)
    p2 = (A+B)*H
    p3 = (C+D)*E
    p4 = D*(G-E)
    p5 = (A+D)*(E+H)
    p6 = (B-D)*(G+H)
    p7 = (A-C)*(E+F)

    return p1, p2, p3, p4, p5, p6, p7

if __name__ == '__main__':
    import doctest
    doctest.testmod()
