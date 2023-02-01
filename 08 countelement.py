from cmath import e
from itertools import count
from operator import index


print("How many N natural number enter -:")
var=int(input())

l1=[]
cnt=0
print("Enter Some element -:")

while(var):
    l1.append(eval(input()))
    var-=1
print(l1)

print(end="\n")
print([ [e, l1.count(e)] for e in set(l1)])
