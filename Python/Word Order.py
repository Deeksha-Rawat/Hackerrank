# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d=OrderedDict()
for i in range(int(input())):
    word=input()
    d.setdefault(word,0)
    d[word]+=1
print(len(d))
print(*d.values())  

        
