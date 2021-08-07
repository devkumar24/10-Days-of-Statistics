# Calculate mean, median and mode of the given data

# Import required Library
import numpy as np

# Mean function
def mean(numbers : list):
    n = len(numbers)
    mean_no = sum(numbers)/n

    return mean_no

# Median Function
def median(numbers : list):
    n = len(numbers)
    numbers = np.array(numbers)
    numbers.sort()
    if n%2 == 0:
        median_no = (numbers[int(n/2)-1] + numbers[int(n/2)] ) / 2
    else:
        median_no = numbers[int(n/2)-1]

    return median_no

# Mode Function
def mode(numbers : list) -> int:
    numbers = np.array(numbers)
    unq, counts = np.unique(numbers, return_counts=True)
    mode_no = unq[np.argmax(counts)]

    return mode_no

