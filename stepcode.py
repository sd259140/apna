'''a=[1,2,3,4,5,2,3,4,7,9,5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i) 
'''
#remove 
c='hello_@#buddy[]_'
a="@#%$_&*{}[]?"
uni=""
for i in c:
    if i not in a:
        uni=uni+i
       
#print(uni)    
list = [10, 20, 30, 40, 50, 10, 20, 10]  
only_dupli=[]         

for i in list:
    if i not in only_dupli:
        only_dupli.append(i)
#print(only_dupli) 
#find second large
list = [20, 30, 40, 25, 10]
list.sort()
#print(list[-2])
#print(array)
'''list = [20, 30, 40, 25, 10]
for i in range(len(list)): for i in range(5)
    print(list[i])
for i in range(len(list)-1,-1,-1):(4,-1,-1)
    print(list[i])'''
'''
l = [1,6, 2, 3, 8, 7, 4]
e=[]
d=[]
for i in l:
    if i % 2 == 0:
        e.append(i)      
    else:
        d.append(i)   
print(e+d) 
print(d)  '''
'''
a='MH42ACD'    
b=''
c=''
for i in a:
    if i.isdigit():
        b=b+i 
    else:
        c=c+i

print(b)    
print(c)
'''
#even no letters in word print
'''a='this is happen imn house'
b=a.split()
for i in b:
    if len(i)%2==0:
        print(i)'''
'''
a=[3,7,8,4,2,8,9]
b=[3456,7356,5768588,4363,35632,83536,2329]
c={a[i]:b[i] for i in range(len(a))}
print(c)
'''
a=[3,7,8,4,2,8,9]
b=[3456,7356,5768588,4363,35632,83536,2329]
#print(dict(zip(a,b)))
'''
a=[3,7,8,4,2,8,9]
a.sort()
print(a[0])'''
# square compression
'''numbers = [1, 2, 3, 4, 5]
c=[i*i for i in numbers]
print(c)'''
'''
nested list to plan list
lst = [[11, 22, 33, 44], [55, 66, 77], [88, 9]]
print(lst[0]+lst[1]+lst[2])'''
'''
lst = [[11, 22, 33, 44], [55, 66, 77], [88, 9]]
d=[i for j in lst for i in j]
print(d)'''
'''
#Operation on only values in dict

my_dict_2 = {'a': 2, 'b': 3, 'c': 4}

m={i:j*2 for i,j in my_dict_2.items()}
print(m)'''

def f1(s1):

    a=len(s1)
    temp=s1[0]
    s1[0]=s1[a-1]
    s1[a-1]=temp
    print(s1)
#f1([1,9,10,15,21])    
#counting element
a="sbhammrtbhb"
count={}
for i in a:
    if i in count:
        count[i] +=1
    else:
        count[i]=1
print(count)  
   #  Second minimum number in list:
a = [10, 13, 17, 11, 34, 21]
#a.sort
#print(a[1])

#swap key value nd key
b={'a': 1, 'b': 2, 'c': 3}
c={value:key for key,value in b.items()}
#print(c)

#reverse the number
a=425893
reverse_no=0
while a!=0:
    digit=a%10                         
    reverse_no=reverse_no*10+digit
    a//=10
print(reverse_no+digit)    
a=425893
reverse_no=0
digit=a % 10
reverse_no=reverse_no*10+digit
#print(reverse_no)
#print(a//10)
dict1 = {'a': 10, 'b': 8}
dict2 = {'c': 6, 'd': 4}
d=dict(zip(dict1.keys(),dict2.values()))
print(d)
dict1 = {'a': 10, 'b': 8}
dict2 = {'c': 6, 'd': 4}
output=(dict(zip(dict1.keys(),dict2.values())))
#sum of all element
'''a = [10, 13, 17, 11, 34, 21]
sum=0
for i in range(len(a)):
    sum= sum+a[i]
print(sum)'''
'''
list1 = ["hello", "how", "are", "you"]
for i in range(len(list1)):
    list1[i]=list1[i].capitalize()
print(list1)'''


'''a='shubham'
str=''
for i in a:
    str=i+str
print(str)'''
'''
a=[5,1,25,78,85,45]
b=float(len(a)/2)
if b % 2!=0:
    print(a[b-0.5])
else:
    print(a[b-1])    
print(b)'''
#length without space
a = 'indexial solution is the best'
b=a.split()
print(b)
all=''
for i in b:
    all=all+i
print(len(all))
a = 'indexial solution is the best'
b=a.split()
for i in b:
    if len(i)%2==0:
        print(i)















