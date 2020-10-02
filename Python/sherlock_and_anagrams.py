#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    a=[]
    sum1=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            a.append(tuple(sorted(Counter(s[i:j]).items())))
    a=tuple(a)
    b=Counter(a)
    for i in b.values():
        sum1+=int(i*(i-1)/2)
        
    return sum1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
