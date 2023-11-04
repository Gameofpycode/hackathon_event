n = [1,2,4,6,8,10]
number=(input("enter the each number separated by comma:"))
n=number.split(",")
print(n)
l = len(n)
for i in range(0,l):
    a=int(n[i])
    b=int(n[i-1])
    if(i == 0):
        pass
    elif(i>0):
        if(a ==( b + 1)):
            pass
        else:
            print(a-1)