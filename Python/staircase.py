#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    simbol = 1

    for i in range(n-1,-1,-1):
        print(" " * i + "#" * simbol)
        simbol += 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
