#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    newGrades = []
    for i in range(0,len(grades)):
        if(grades[i]>=38):
            nextFiveMult = int(grades[i]/5)*5+5
            if(nextFiveMult - grades[i] <3):
                newGrades.append(nextFiveMult)
            else:
                newGrades.append(grades[i])
        else:
            newGrades.append(grades[i])        
    return newGrades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
