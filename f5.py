a="("
b=")"
x=""
y=""
flag1=""
flag2=""

print(a+b)

n=int(input("enter the number:"))

for i in range(0,n):
    x+=a
for j in range(0,n):
    y+=b

z=x+y

l=len(z)

half_value=(int(l/2))

for i in range(0,l):
    if(i==half_value-1): 
        flag1+=(z[i+1])
        
    elif(i==half_value):
        flag1+=z[i-1]
    else:
        print(i)
        flag1+=z[i]

for j in range(0,l):
    
        
    if(i==half_value+2):
        flag1+=z[j+1]
    else:
        print(i)
        flag2+=z[j]
   
        
print(flag1)
# print(flag2)
    
        
        
    


    


