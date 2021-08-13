#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def mean(numbers : list):
    n = len(numbers)
    mean_no = sum(numbers)/n

    return mean_no
def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    num = 0
    for i in range(len(arr)):
        num += (arr[i] - mean(arr))**2
    
    den = len(arr)
    result = (num/den)**0.5
    print(round(result,1))
    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
