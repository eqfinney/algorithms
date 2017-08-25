# My implementation of a Karatsuba multiplication problem
# Reminder about recursion!
# Author: Emily Quinn Finney

def karatsuba(int1, int2):
    """
    Implements Karatsuba multiplication for two integers of equal size.
    int1: an integer to be multiplied, even number of numbers
    int2: another integer to be multiplied, even number of numbers
    product: the product of int1 and int2
    """

    n = len(str(int1))

    # base case
    if n == 1:
        return int1 * int2

    else:
        # split the integers into first and second halves
        int1firsthalf = int(str(int1)[:int(n/2)])
        int1secondhalf = int(str(int1)[int(n/2):])
        int2firsthalf = int(str(int2)[:int(n/2)])
        int2secondhalf = int(str(int2)[int(n/2):])

        # assign values according to karatsuba algorithm
        first_value = 10**n*(karatsuba(int1firsthalf, int2firsthalf))
        second_value = karatsuba(int1secondhalf, int2firsthalf)
        third_value = karatsuba(int1firsthalf, int2secondhalf)
        fourth_value = karatsuba(int1secondhalf, int2secondhalf)

        return int(first_value + (10**(n/2))*(second_value+third_value)
                   + fourth_value)

product = karatsuba(1234, 5678)
print(product)
assert product == 1234*5678
