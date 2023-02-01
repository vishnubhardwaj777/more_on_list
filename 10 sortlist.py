print("How many number enter in list \n")
var = int(input())

l1=[]
print("Enter some elemnt in list -:")

while(var):
    l1.append(eval(input()))
    var-=1

print(l1)
print("After sorted -:")
s=sorted(l1)
print(s)    