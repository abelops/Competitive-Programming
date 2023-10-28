#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def rec(val):
    # print(val)
    if len(val) == 1:
        return int(val)
    ans = 0
    for i in val:
        ans+= int(i)
    return rec(str(ans))

def superDigit(n, k):
    # Write your code here
    n = str(n)
    nbac = n
    ans = 0
    for i in list(str(n)):
        ans+= int(i)
    n = ans * k
    return rec(str(n))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
