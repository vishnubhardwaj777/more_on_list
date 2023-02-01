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

l2=[]
print(end="\n")
for e in set(l1):
    print([cnt, e])
    cnt+=1   

