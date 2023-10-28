#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
# some more comment


def countingSort(arr):
    # Write your code here
    ma = max(arr)
    if(ma%2==0):
        ma+=2
    else:
        ma+=1
    nums = [0 for i in range(0,ma)]
    # print(len(nums))
    for i in arr:
         nums[i] += 1
    return nums

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
