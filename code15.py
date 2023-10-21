#show only duplicates :
a=[1,2,3,4,5,2,3,4,7,9,5]
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i)

#print(b)  
#unique      
'''a="bdbac353@#2c&191#"
unique="#$%^&*()@!><{}[]|"
b=[]
for i in a:
    if i not in unique:
        b.append(i)
    else:
        print(i)    '''
'''#odd & even separation :-
list1 = [3, 5, 4, 9, 8, 5, 7, 8, 12]
odd = []
even = []
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)  
print(odd)          
print(even)'''
 #6. print the elements of an array :-
'''arr = [1, 2, 3, 4, 5,6,7]
for i in range(0,len(arr)):
    print(arr[i])'''
'''
list1 = [3, 5, 4, 9, 8, 5, 7, 8, 12]
odd = []
even = []
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)  
print(odd+even)          '''
#7. elements of an array in reverse order
arr = [1, 2, 3, 4, 5]
#arr.reverse()
print(arr)
'''for i in range(0,len(arr)):
    print(arr[i])
for i in range(len(arr)-1,-1,-1):
    print(arr[i])'''
'''#Duplicate words from sentence
s = "I am very happy mow am very"     
s1=s.split(" ")
print(s1)
s2=[]
for i in range(0,len(s1)):
    for j in range(i+1,len(s1)):
        if s1[i]==s1[j]:
            s2.append(i)
        else:
            print(i)    
print(s2)       '''
'''def upper(fun):
    def gen():
        text=fun() 
        msed=text.upper()   
        return msed
    return gen
@upper
def hello():
    return 'hello ji what can i do'

a1=hello()  
print(a1)  '''
#duplicates output in dictionary format :-
'''a = [10, 11, 12, 15, 20, 21,21]
b=[]
c={}
for i in a:
    c[i]=a.count(i)
    if i not in b:
        b.append(i)
    else:
        print(i)
print(b) 
print(c)  '''
#enumerate   
'''a=[5,6,7,8] 
for i,j in enumerate(a):
    print(i,j)'''
'''
a = "MH10CD7172"
num = ""
word = ""    
for j in a:
    if j.isdigit():
        num=num+j 
    else:
        word=word+j    
print(num)        
print(word)'''
 
a=[5,6,7,8] 
b={}
for i,j in enumerate(a):
    b[i]=j
print(b)    
a=['a','b','c','d']
b=[5,6,7,8] 
c=dict(zip(a,b))
print(c)

f={'a': 5, 'b': 6, 'c': 7, 'd': 8}
print(f.keys())
print(f.values())
#
n="This is a python  fgf language"
s=n.split()
for i in s:
    if len(i)%2==0:
        print(i)
#middle of list
'''def midd(list):
    n=float(len(list))/2
    if n%2!=0:
        return list[int(n-0.5)]
    else:
        return list[int(n-1)]
        

print(midd([4,8,9,5,8,10,15]))    '''
'''# fibbo
f=1
s=2
t=f+s 
for i in range(0,26):
    f=s 
    s=t 
    t=f+s 
    print(t)'''

#
'''
def f1(a):
    return a*a

x=map(f1,[1,2,3,4])  
print(list(x))  
'''

#bubblesort
'''a=[5,8,9,10,25]
n=len(a)
for i in range(n):
    for j in range(n-i-1):
        a[j],a[j+1]=a[j+1],a[j]
print(a)    
#insertion sort
a=[5,8,9,10,25]
n=len(a)
for i in range(n):
    for j in range(i+1,n):
        a[i],a[j]=a[j],a[i]
print(a)'''
#factorial
'''def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(4)) '''
'''def f1(a):
    if a%2==0:
        return a

d=filter(f1,(10,12,3,4))
print(list(d))
#reducce
from functools import reduce 
d=reduce(lambda x,y:x+y,[1,8,6,7])
print(d)'''
'''a='shubham'
b=a[::-1]

str=''
for i in a:
    str = i + str
print(str)
'''
'''#capitalize first word
list1 = ["Hello", "how", "are", "you"]
for i in range(len(list1)):
    list1[i]= list1[i].capitalize()

print(list1) '''
'''a='shubhams' 
out={}
for i in a:
    if i in out:
        out[i] += 1
    else:
        out[i] = 1
print(out)       
'''
#swap
'''a=10
b=20
temp=a 
a=b 
b=temp 
print(a)
print(b)
#swap 1and last
def swap(a):
    n=len(a)
    temp=a[0]
    a[0]=a[n-1]
    a[n-1]=temp
    return a 

a=[9,25,84,24]    
print(swap(a))   '''
'''
a='apnaname'
print(len(a))
counter=0
for i in a:
    counter=counter+1
print(counter)    
'''
#capitalize first letetr abbravation
'''a= "Your Are My Hero"
b=a.split(" ")
print(b)
c=" "
for i in b:
    c +=i[0].upper()
print(c)    
'''
'''
#etract user name from email
a=(input('enter email'))
b=a.index('@')
print(a[0:b])
'''
'''
The cost of a stock on each day is given in an array. Find the maximum profit that you can make by buying and selling on those days. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

Examples:

Input: arr[] = {100, 180, 260, 310, 40, 535, 695}
Output: 865
Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210
                       Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655
                       Maximum Profit  = 210 + 655 = 865

Input: arr[] = {4, 2, 2, 2, 4}
Output: 2
Explanation: Buy the stock on day 1 and sell it on day 4 => 4 – 2 = 2
                       Maximum Profit  = 2
'''
#a=[int(i) for i in input('enter element array by spaces:').split()]
#print(a)
'''n=len(a)
d1=int(input('enter day'))
d2=int(input('enter day'))
for i in range(n):
    p=a[d2]-a[d1]
print(p)   '''
#n=[int(i)for i in input('enter_no').split()]
'''n=9008
print(n)
no=n[0]
no += 1
n[0]=no
print(no)'''

def f1(a):
    result=a+1
    print(result)
f1(9009)    
        

             
