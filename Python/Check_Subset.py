'''
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set A is subset of set , print True.
If set B is not a subset of set , print False.

Input Format

The first line will contain the number of test cases,T .
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.

Constraints

Output Format

Output True or False for each test case on separate lines

'''

~~~~~~~~~~~~~~~~~~~~~~Solution~~~~~~~~~~~~~~~~~~~~~``
t=int(input())
for i in range(t):
    n = int(input())
    c=0
    A = list(map(int,input().split()))
    m = int(input())
    B = list(map(int,input().split()))
    for i in A:
        if i in B:
            c+=1
    if(c==n):
        print("True")        
    else:
        print("False")
