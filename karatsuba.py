# My implementation of a Karatsuba multiplication problem
# Reminder about recursion!
# Author: Emily Quinn Finney

m = 0

def karatsuba(num1, num2):
    """
    Implements Karatsuba multiplication for two integers of equal size.
    int1: an integer to be multiplied, even number of numbers
    int2: another integer to be multiplied, even number of numbers
    product: the product of int1 and int2
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

num1 = '3141592653589793238462643383279502884197169399375105820974944592'
num2 = '2718281828459045235360287471352662497757247093699959574966967627'

product = karatsuba(num1, num2)
print(' '.join(["My Karatsuba", str(product)]))
print(' '.join(["Python's calculated value", str(int(num1)*int(num2))]))
assert product == int(num1)*int(num2)
