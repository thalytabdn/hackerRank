import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    num_a = 0
    
    for i in s:
        if i == "a":
            num_a += 1
    
    result = n//len(s) * num_a

    for i in s[:n%len(s)]:
        if i == "a":
            result += 1
    
    return result

if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
