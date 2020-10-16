from collections import Counter
X = int(input())
size = list(map(int,input().split()))
n=int(input())
p =0
S = Counter(size)
for i in range(n):
    s,price = map(int,input().split())
    if s in S and S[s] > 0:
        S[s]-=1
        p+=price


print(p)
