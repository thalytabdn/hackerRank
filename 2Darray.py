#!/bin/python3

import math
import os
import random
import re
import sys


def calcSumHourglass(arr,linha,coluna):
    return arr[linha][coluna] + arr[linha][coluna + 1] + arr[linha][coluna + 2] + arr[linha + 1][coluna + 1] + arr[linha + 2][coluna] + arr[linha + 2][coluna + 1] + arr[linha + 2][coluna + 2]
    
# Complete the hourglassSum function below.
def hourglassSum(arr):
    valores = [calcSumHourglass(arr,linha,coluna) for linha in range(4) for coluna in range(4)]
    return max(valores)


if __name__ == '__main__':
    fptr = sys.stdout

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
