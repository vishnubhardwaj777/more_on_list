print("How many Odd Natural number enter -:")
var = int(input())

l1=[]
num=1

while(var):
    if(num%2 != 0):
        l1.append(num)
        var-=1
    num+=1    

print(l1)