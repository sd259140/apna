a=[1,2,[6,5],[6,[2,3],8],10]
c=[]
for i in a:
    if type(i)==int:
        c.append(i)
    elif type(i)==list :
        for j in i:
            if type(j)==int:
                c.append(j)
            elif type(j)==list:
                for k in j:
                    if type(k)==list:
                        c.append(k) 
print(c)