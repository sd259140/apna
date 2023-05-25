l=[2,8,12,3,7,27]
odd=[]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)        
print(even)
#leap
def leap(a):
    if a%4==0:
        print('leapyear')
    else:
        print('nonleap')    
#laege among 3
def largest(a,b,c):
    if a>=b and a>=c:
        print('largest is a')
    elif b>=a and b>=c:
        print('b is large')    
    else:
        print('c is large')    
largest(10,20,30)
def no(a):
    if a>0:
        print('+ number')
    elif a<0:
        print('- number')    
    else:
        print('zero ')    
no(-25)        
#quad eq
def quad(a,b,c):
    (b**2-4*a*c)*0.5
    f1=b**2-(((b**2-4*a*c)**0.5)/2*a)
    f2=b**2+(((b**2-4*a*c)**0.5)/2*a)
    print(f1)
    print(f2)
quad(2,4,6)    
#swap
a=2
b=3
temp=a 
a=b
b=temp
print('a is:',a)
print('b is:',b)
#random
import random
print(random.random())

#slice
a=['shubham','radha','prasad'] 
print(a[-1][-1])  
#duplicates remove
a=[1,1,8,9,2,3,8,3]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i)    
print(b)    

#prime
def prime(a):
    if a>1:
        if i%2==0:
            print('non prime')
        else:
            print('prime')        
#prime(3)    
def primrange(a,b) :
    for j in range(a,b+1):
        if j>1:
            for i in range(2,j):
                if j%i==0:
                    break
            else:
                print(j)        
#primrange(300,500)
#multiplicatoin
a=18
for i in range(1,11):
    number=a*i
    print(number)
#factorial
a=5
fact=1
if a==1:
    print('factorial is 1')
elif a==0:
    print('zero fact')    
else:
    for i in range(1,a+1):
        fact=fact*i
    print(fact)
#fibbonacy no
f=1
s=2
t=f+s
for i in range(1,26):
    f=s 
    s=t 
    t=f+s 
    print(t)

#
a=153
b=a//100
n=153%100
t=n//10
x=n%10
y=n
print()
