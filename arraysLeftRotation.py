#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    newArray = [0] * len(a)

    for i in range(len(a)):
        newArray[(i-d)%len(a)] = a[i]
        
    return newArray

if __name__ == '__main__':
    fptr = sys.stdout
    
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
