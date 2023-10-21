'''a=[10,20,78,75,89,41,15]
n=len(a)
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)            
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a[-2])   
arr = [1, 2, 30, 4, 5,60,7]   
for i in range(len(arr)):
    print(arr[i])

dict1 = {'a': 10, 'b': 8}
dict2 = {'c': 6, 'd': 4}  

dict3=dict1.update(dict2)
print(dict1)
def upper(a):
    def f1():
        temp=a()
        men=temp.upper()
        return men
    return f1
@upper
def h1():
    return 'hello hi three'

g=h1()
print(g)

a ='indexial solution is the best'
b=a.replace(' ','')
print(len(b))

a="This is a python language"
c=a.split(' ')
d=[]
for i in c:
    if len(i)%2==0:
        d.append(i)
print(d)

from collections import counter
a=[10,20,30,50,78,89]
print(counter(a))

def middle(list):
    n=float(len(list))/2
    if n%2!=0:
        return list[int(n-0.5)]
    else:
        return(list[int(n-1)],list[int(n)])  

list = [4, 3, 2, 7, 10, 44]
print(middle(list))  

def factorial(a):
    if a==0:
        result=1 
    else:
        result=a*factorial(a-1)
    return result
print(factorial(4))

def f1(ls1):
    return ls1**3
ds=map(f1,(1,2,3,4)) 
print(list(ds) ) 

a='shubham'
print(a[::-1])

str=' '
for i in a:
    str=i+str
print(str)   

list1 = ["hello", "how", "are", "you"] 

for i in range(len(list1)):
    list1[i]=list1[i].capitalize()
    print(list1)
    

def fibo(n):
    a=1
    b=0
    for i in range(n):
        a,b=b+a,a   
        print(b)
fibo(10)        

rr = [1, 2, 3, 4, 5]
sum=0
for i in range(len(rr)):
    sum =sum+rr[i]

print(sum)    
from functools import reduce
x=reduce(lambda a,b:a+b,[1, 2, 3, 4, 5])
print(x)
c=2112
a=str(c)
if list(a)==list(a[::-1]):
    print('palidrome')
else:
    print('nonpalidrome')    

a=['radhika','shubham','pune',86,74] 
b=[] 
for i in a:
 ,   if isinstance(i,str):
        b.append(i[::-1])
    else:
        b.append(i)    

print(b)


a=[1,8,6,7,9,5,7]
d=['even' if i%2==0 else 'odd' for i in a]
print(d)

dict1 = {'a': 10, 'b': 8}
dict2 = {'c': 6, 'd': 4}  
dict3=dict(zip(dict1.keys(),dict2.values()))
print(dict3) 
a=[1,8,6,7,9,5,7]
d=[i**2 for i in a]
print(d)

#Odd Number Square using =[],
a1= [4, 2, 13, 21, 5]
filter(lambda u:u%2!=0,a1)
a=list(map(lambda u:u**2,filter(lambda u:u%2!=0,a1)))
print(a)


x=list(map(lambda u:u**2,filter(lambda u:u%2!=0,a1)))
print(x)
a = 'quhkjhsjklvsnk'
b=[]
c={}
for i in a:
    c[i]=a.count(i)
    if i not in b:
        b.append(i)
    else:
        print(i)   
print(c)    

vowels = 'aeiouAEIOU'
string = "Hi, I love eating ice cream and junk"
d=[]
c={}
for i in string:
    c[i]=string.count(i)
    if i in vowels:
        d.append(i)
print(c)    
print(d)    

a=[1,4,8,5,25]
c=[]
for i,num in enumerate(a):
    if i%2==0:
        if num%2!=0:
            c.append(num)
    else:
        if num%2==0:
            c.append(num)
            
a=lambda a,b: a if a>b else b            

print(a(10,40))  

a=[int(i) for i in input('enterno').split()] 
print(a) 

a='data science is the bset' 
b=a.split()      
form=' '
for i in b:
    form +=i[0].upper()
print(form)  

def gen():
    count=0
    while True:
        count +=1
        yield count

g=gen()
print(next(g))
print(next(g))

a=[[1,44,33],[52,66,44],[10,11,10]]
d=[i for j in a for i in j]
print(d)
s1 = [1,2,3,4]
s2 = ["a","b","c","d"]
d1=dict(zip(s2,s1))
print(d1)
s1 = [1,2,3,4,5,2,]
c=[]
d=[]
n=[]
for i in s1:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)   
for i in range(len(c)):
    n.append(c[i])  
    n.append(d[i])   
print(n)     
l1 = [4, 2, 13, 21, 5]
c=[]
for i in l1:
    if i%2!=0:
        c.append(i**2)
    else:
        c.append(i)    
print(c)        
s1 = [4, 2, 13, 21, 5]
d=list(map(lambda u:u**2,filter(lambda u:u%2==1,s1)))
print(d)

def fibo(n):
    a=1
    b=0
    for i in range(n):
        print(b)
        a,b=b,b+a

fibo(20)    
'''
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

print(factorial(4))    

def factorial(a):
    if a==0:
        result=1
    else:
        result=a*factorial(a-1)  
    return result      
print(factorial(4))   

list1 = [1, 2, 3, 4, 5]
def reverse(number):
    if len(number)==1:
        return number
    
    return reverse(number[1:])+number[0:1]  
print(reverse(list1))         
list1 = [1, 2, 3, 4, 5]
def reverse_fun(numbers):
    if len(numbers) == 1:
        return numbers
# Otherwise
    return reverse_fun(numbers[1:])+numbers[0:1]

a=[1,2,[5,6],[6,[5,9],7]]    
c=[]
for i in a:
    if type(i)==int:
        c.append(i)
    elif type(i)==list:
        for j in i:
            if type(j)==int:
                c.append(j)
            elif type(j)==list:
                for k in j:
                    c.append(k)
print(c)                


