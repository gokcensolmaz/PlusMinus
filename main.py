#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            pos = pos + 1
        elif arr[i] < 0:
            neg = neg + 1
        else:
            zero = zero + 1
    print(pos / len(arr), "\n", neg / len(arr), "\n", zero / len(arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
