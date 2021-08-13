#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    n = len(arr)
    arr.sort()
    def median(Q):
        try:
            n = len(Q)
            if n%2 == 0:
                return int((Q[int(n/2)-1] + Q[int(n/2)])/2)
            else:
                return Q[int(n/2)]
        except:
            return Q      
    if n%2 == 0:
        Q1 = arr[:int(n/2)]
        Q3 = arr[int(n/2):]
        return median(Q1),median(arr),median(Q3)
    else:
        Q1 = arr[:int(n/2)]
        Q3 = arr[int(n/2)+1:]
        return median(Q1),median(arr),median(Q3)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
