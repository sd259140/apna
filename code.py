def areatriagle(b,h):
    n=0.5*b*h
    print(int(n))

#areatriagle(6,4)

import cmath
def qud(a,b,c):
    d=b**2-4*a*c
    n1=-b+cmath.sqrt(d)
    n2=-b-cmath.sqrt(d)
    print(n1)
    print(n2)

#qud(4,8,12)    
def swap(a,b):
    temp=a
    a=b
    b=temp
    print('a variable after swapping:{}'.format(a))
    print('b variable after swapping:{}'.format(b))

#swap(4,5)    
def swp(a,b):
    a,b=b,a 
    print('a variable after swapping:{}'.format(a))
    print('b variable after swapping:{}'.format(b))
#swp(2,3)    
def positive(a):
    if a>0:
        print('positive')
    elif a==0:
        print('zero')    
    else:
        print('negative')    
#positive(-15)

def leap(a):
    if a in range(1000,2100):
        if a%4==0:
            print('leap')
        else:
            print('regular')   
    else:
        print('enter valid year')       
#leap(2023)  
def prime(a):
    if a>1:
        if a%2==0:
            print('nonprime')       
        else:
            print('prime')    
    else:
        print('enter no grt thn 1')   
#prime(7) 

def  rangeprime(a,b):
    for c in range(a,b):
        if c>1:
            for i in range(2,c):
                if c%i==0:
                    break
            else:
                print(c)
                             
#rangeprime(500,900)        

def largeno(a,b,c):
    if (a>=b) and (a>=c):
        largest=a
    elif (b>a) and (b>c):
        largest=b   
    else:
        largest=c
    print('the largest',largest)    
#largeno(70,600,10)         
def mul(no,end):
    for i in range(1,end+1):
        mul=no*i
        print(mul)
#mul(12,30)

def palidrome(a):
    if list(str(a))==list(str(a[::-1])):
        print('palidrome')
    else:
        print('nonpalidrome') 

#palidrome('24342')         
def removepun(a):
    punctions='''"@#$%_-:;'></,.[]{}()!'''
    no_punction=""
    for char in a:
        if char not in punctions:
            no_punction=no_punction+char
    print(no_punction)
#removepun('hello hihjjj@#')    
def sort(a):
    words=[word.lower() for word in a.split()]
    words.sort()
    for word in words:
        print(word)
#sort("Hello hi How these gone wrong")  
def lastno(l1):
    print(l1[len(l1)-1])
#lastno([15,12,25])
l1=['a','b']
l2=[1,2]
b=dict(zip(l1,l2))
#print(b)
a=[[1,2],[3,4,5],[6,7]]
b=[]
for i in a:
    for j in i:
        b.append(j)
#print(b)
import itertools
a=[[1,2],[3,4,5],[6,7]]
#print(list(itertools.chain(*a)))
a=[1,2,3,4,5]
len(a)
if len(a)==0:
    print('list is empty')
else:
    print('not empty')    

 
a=123456 
b=str(a)
#print(b[::-1])
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))