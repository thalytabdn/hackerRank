#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for number in range(1,n):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0 and number % 5 != 0:
            print("Fizz")
        elif number % 3 != 0 and number % 5 == 0:
            print("Buzz")
        else:
            print(number)
     

if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())

    print(fizzBuzz(n))
