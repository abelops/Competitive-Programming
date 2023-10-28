#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    c = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                c+=1
    fin = f"Array is sorted in {c} swaps.\nFirst Element: {a[0]}\nLast Element: {a[len(a)-1]}"
    print(fin)
    return fin

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
