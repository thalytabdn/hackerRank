import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    n_valleys = 0
    sea_level = 0

    down = False

    i = 0
    while i < n:
        if s[i] == "U":
            sea_level += 1
            i += 1
        elif s[i] == "D":
            sea_level -= 1
            i += 1
        
        if sea_level < 0:
            down = True
        if sea_level == 0 and down:
            down = False
            n_valleys += 1
    
    return n_valleys


if __name__ == '__main__':
    fptr = fptr = sys.stdout

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
