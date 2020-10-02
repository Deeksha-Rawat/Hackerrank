#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    a=[0]*26
    b=[0]*26
    for i in s1:
        a[ord(i)-97]+=1
    for i in s2:
        b[ord(i)-97]+=1
    
    for i in range(23):
        if(a[i]!=0 and b[i]!=0):
            return "YES"
            break
    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
