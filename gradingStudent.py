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

    final = []
    for x in grades:
        if x + 3 >= 40:
            if x % 5 == 0:
                final.append(x)
            elif x % 5 == 3:
                final.append(x+2)
            elif x % 5 == 4:
                final.append(x+1)
            else:
                final.append(x)
        else:
            final.append(x)
    return final


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
