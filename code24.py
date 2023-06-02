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

# postive element list 
n="This is a python language"
b=n.split()
for i in b:
    if len(i)%2!=0:
        print(i)
#even at strt odd at end
l = [1,6, 2, 3, 8, 7, 4]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)    
print(even)
print(odd)
print(even+odd)
#unpack list/flatten list
l = [[1,6, 2],[10,5],[8,12],[25]]
l2=[]
for i in l:
    for j in i:
        print(l2.append(j))
print(l2) 

#array in reverse order
arr = [1, 2, 3, 4, 5]
n=len(arr)

for i in range(n-1,-1,-1):
    print(arr[i])

#find vlaue 
arr=[26,85,89,25,74,100]
k=5
n=len(arr)
for i in range(0,n,k):
    arr[i:i+k]=arr[i:i+k][::-1]
#print(arr)  
#countig elemrt
'''arr='hellooo'
out={}
for i in arr:
    if i in out:
        out[i] +=1
    print(out)
a=['radhika','shubham','prasad',86,95] 
b=[]
for i in a:
    if isinstance(i,str):
        c=i[::-1]
        b.append(c)
    else:    
        b.append(i)
print(b)'''
#square of element using list comp
'''a=[4,8,58,7,9]

b=[i*i for i in a if i%2==0]
print(b)'''
'''
a=[2,2.5,2.44,8,9,8.9]
c=['radhika','shubham','prasad',86,45]
b=[i[::-1] for i in c if isinstance(i,str)]
print(b)
'''
#div by 7
b=[i for i in range(0,1000) if i%7==0]
print(b)
#no have 3 in list
c=[i for i in range(0,1000) if '3' in str(i)]
print(c)
#count spaxe
'''
some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
d=[i for i in some_string if i==" "]
print(len(d))
a='On a summer day somner smith went simming in the sun and his red skin stung'
c=a.split(" ")
print(c)
d=[i for i in c if len(i)<=4]
print(d) 'In 1984 there were 13 instances of a protest with over 1000 people attending'.  Result is a list of numbers like [3,4,5]
'''
sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
d=sentence.split(" ")
c=[i for i in d if  i.isdigit()]
#print(c)
'''
a=['radhika','shubham','prasad',86,95] 
b=[]
for i in a:
    if i.isinstance(i,str):
        c=i[::-1]
        b.append(c)
    else:    
        b.append(i)
#print(b)
'''
#find only number
'''sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
f=sentence.split(" ")
d=[i for i in f if  not i.isalpha()]
print(d)'''
#odd even rint
s=['even' if i%2==0 else 'odd' for i in range(0,20)]
#print(s)

#Find the common numbers in two lists (without using a tuple or set) list_a = [1, 2, 3, 4], list_b = [2, 3, 4, 5]

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
d=[ a for a in list_a if a in list_b]
#print(d)


#Get the index and the value as a tuple for items in the list ["hi", 4, 8.99, 'apple', ('t,b','n')].  Result would look like [(index, value), (index, value)]

items = ["hi", 4, 8.99, 'apple', ('t,b','n')]
result = [(index, item) for index, item in enumerate(items)]
#print(result)
#Produce a list of tuples consisting of only the matching numbers in these lists list_a = [1, 2, 3,4,5,6,7,8,9], list_b = [2, 7, 1, 12].  Result would look like (4,4), (12,12)
list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]

result = [(a,b) for a in list_a for b in list_b if a==b]          
print(result)
sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

result = [letter for letter in sentence if letter not in 'a,e,i,o,u, " "']
print(result)
d=[[20,23],[25,85],[96,5]]
c=[i for g in d for i in g]
print(c)
