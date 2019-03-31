#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join(w[:1].upper() + w[1:] for w in s.split(' '))     
    return s.title()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
