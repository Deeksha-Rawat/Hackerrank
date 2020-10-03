#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
b=[]
def matchingStrings(strings, queries):
    for i in queries:
        a=0
        for j in strings:
            if i==j:
                a=a+1
        b.append(a)
    return b
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
