#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n_bribes = 0

    for i in range(len(q)):
        if q[i] - (i+1) > 2:
            return "Too chaotic"

        for j in range(max(0,q[i]-2,i)):
            if q[j] > q[i]:
                n_bribes += 1
    
    return n_bribes

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        result = minimumBribes(q)

        fptr.write(str(result) + '\n')

    fptr.close()