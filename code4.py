'''a=[40,80,90,41,50]
n=float(len(a)/2)
if n%2 != 0:
    print(a[int(n-.5)])
else:
    print(a[int(n-1)])    '''
'''
b='hello  am the best aaaa thres is way '
counter=0
for i in b:
    if i=='a':
        counter +=1
print(counter)
'''
#capitalize first letter
'''list1 = ["hello", "how", "are", "you"]

for i in range(len(list1)):
    list1[i]=list1[i].capitalize()
print(list1)
d=[list1[i].capitalize() for i in range(len(list1))]
print(d)'''

l1=[12,32,45,64,5,6,7,4]
l2=[12,5,4]
d=['present' if i==j else 'not' for i in l1 for j in l2 ]
print(d)

