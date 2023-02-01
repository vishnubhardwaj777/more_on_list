print("How many Even N natural number enter -:")
var=int(input())

l1=[]
num=2

while(var):
    if(num%2==0):
        l1.append(num)
        var-=1
    num+=1

print("Even N natural number -:")
print(l1)        