#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    s=s.capitalize()
    a=''
    for i in range(len(s)):
        if (s[i]>='a' and s[i]<='z') and s[i-1]==' ':
            a+=s[i].upper()
        else:
            a+=s[i]
    return(a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
