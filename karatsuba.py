# My implementation of a Karatsuba multiplication problem
# Author: Emily Quinn Finney


def karatsuba(num1, num2):
    """
    Implements Karatsuba multiplication for two integers of equal size.
    int1: an integer to be multiplied, even number of numbers
    int2: another integer to be multiplied, even number of numbers
    product: the product of int1 and int2
    >>> karatsuba(10, 10)
    100
    """
    
    n = len(num1)

    # base case
    if n == 1:
        return int(num1) * int(num2)

    else:
        print(num1, num2)
        # split the integers into first and second halves
        int1firsthalf = num1[:int(n/2)]
        int1secondhalf = num1[int(n/2):]
        int2firsthalf = num2[:int(n/2)]
        int2secondhalf = num2[int(n/2):]

        # assign values according to karatsuba algorithm
        first_value = 10**n*(karatsuba(int1firsthalf, int2firsthalf))
        second_value = karatsuba(int1secondhalf, int2firsthalf)
        third_value = karatsuba(int1firsthalf, int2secondhalf)
        fourth_value = karatsuba(int1secondhalf, int2secondhalf)
        print(first_value, second_value, third_value, fourth_value)

        return first_value + (10**(n/2))*(second_value+third_value) + fourth_value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
