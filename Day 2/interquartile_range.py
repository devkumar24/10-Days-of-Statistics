#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = []
    
    for i in range(len(values)):
        s = [values[i]]*freqs[i]
        arr.append(s)
    arr = sum(arr,[])
    
    def median(Q):
        try:
            n = len(Q)
            if n%2 == 0:
                return float((Q[int(n/2)-1] + Q[int(n/2)])/2)
            else:
                return float(Q[int(n/2)])
        except:
            return Q 
    n = len(arr)
    arr.sort()     
    if n%2 == 0:
        Q1 = arr[:int(n/2)]
        Q3 = arr[int(n/2):]
        print(median(Q3) - median(Q1))
    else:
        Q1 = arr[:int(n/2)]
        Q3 = arr[int(n/2)+1:]
        print(median(Q3) - median(Q1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
