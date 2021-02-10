import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps = 0
    
    i = 0
    while i <= (len(c)-2):
        if i == (len(c) - 2):
            steps += 1
            i += 1
        elif c[i+2] == 1:
            steps += 1
            i += 1
        else:
            steps += 1
            i += 2 

    return steps

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
