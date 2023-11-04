a=[1,2,3]
op=[]

for i in a:
    for j in a:
        for k in a:
            if(i!=j and j!=k and i!=k ):
                x=[]
                x.append(i)
                x.append(j)
                x.append(k)
                
                op1=x
                op.append(op1)
                
                
print(op) 