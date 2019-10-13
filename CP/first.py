#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    arr = sorted(arr)
    for x in range(len(arr) - 1):
        current = arr[x]
        next = arr[x+1]
        if current == next:
            pairs += 1
            # go to next one and check
            x = next+1
        else:
            x = next

    

fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input())

ar = list(map(int, input().rstrip().split()))

print (ar)

result = sockMerchant(n, ar)

fptr.write(str(result) + '\n')

fptr.close()


