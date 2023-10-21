def f1(a):
    def f2():
        temp=a()
        midd=temp.upper()
        return midd
    return f2

@f1 
def f3():
    return 'hello hi there'

g=f3()      
print(g)
'''
a = "MH10CD7172"
b=[]
for i in a:
    if i.isdigit():
        b.append(i)
    else:
        print(i)   
         
def midd(a):
    n=float(len(a))/2
    if n%2!=0:
        return a[int(n-0.5)]
    else:
        return (a[int(n-1)],a[int(n)])
a=[1,2,3,4,5,7,9]
print(midd(a))

def fact(a):
    if a==0:
        result= 1
    else:
        result=a*fact(a-1)
    return result   

print(fact(5))    

x=lambda x:x**2

print(x(5))

a='pradip'
print(a[::-1])
str=' '
for i in a:
    str=i+str

print(str)

def fibo(n):
    a=1
    b=0
    for i in range(n):
        print(b)
        a,b=b+a,a 

fibo(10)

a=[10,20,30,40,50,60]
b=len(a)
print(b)
sum=0
for i in a:
    sum =sum+i
    avg=(sum/b)
print(sum)  
print(avg)

#Odd Number Square using Lambda
l1 = [4, 2, 13, 21, 5]  
l2=list(map(lambda u:u**2,filter(lambda u:u%2!=0,l1)))
print(l2)

list = ['akash','akki']

d=[i for i in list if i.endswith('h')]
print(d)

list = [[1,44,33],[52,66,44],[10,11,10]]

d=[i for j in list for i in j]
print(d)

import copy
list1=[4, 2, 13, 21, 5]
d=copy.copy(list1)

print(d)        

a=[1,[10,20,30],[40,60],[40,[60,70]]]
b=[]
for i in a:
    if type(i)==int:
        b.append(i)
    elif type(i)==list:
        for j in i:
            if type(j)==int:
                b.append(j)
            elif type(j)==list:
                for k in j:
                    b.append(k)
print(b)    
''''
class Parent():
    def __init__ (self):
        self.value = "Inside Parent"
    def show(self):
        print(self.value)
class Child(Parent):
    def __init__ (self):
        self.value = "Inside Child"
    def show(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()
obj1.show()
obj2.show()       
