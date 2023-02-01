print("How many N natural number enter -:")
var=int(input())

l1=[]

print("Enter Some element is -:")

while(var):
    l1.append(eval(input()))
    var-=1

print(l1)
print("Minimum element of list is -:")
num=min(l1)
print(num)