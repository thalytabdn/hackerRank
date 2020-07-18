#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    d1 = Counter(a)
    d2 = Counter(b)

    total = (d1 - d2) + (d2 - d1)

    return sum(total.values())


if __name__ == '__main__':
    fptr = sys.stdout

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
