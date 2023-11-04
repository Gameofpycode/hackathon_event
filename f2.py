al=[2,7,11,15]
sum=13

for i in range(0,len(al)):
    for j in range(0,len(al)):
        if(al[i]+al[j]==sum):
            print(f"[{j},{i}]")
        break