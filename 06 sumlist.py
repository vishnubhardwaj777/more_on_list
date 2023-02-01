print("How many N natural enter in list -:")
var=int(input())

l1=[]

print("Enter Some element is -:")

while(var):
    l1.append(eval(input()))
    var-=1

print(l1)
print("Sum of the list is -:")
num=sum(l1)
print(num)