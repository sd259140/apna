'''a=[1,2,3,4,5,2,3,4,7,9,5]
res={}
for i in a:
    res[i]=a.count(i)
    
print(res)    

a=[1,35,6,3,7,3,8,2,0]
n=len(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)            

a=[1,35,6,3,7,3,8,2,0]
n=len(a)
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)            

arr = [1, 2, 3, 4, 5]
print(arr[::-1])
for i in range(len(arr)-1,-1,-1):
    print(arr[i])

s = ['I','am','very','happy']
print('_'.join(s))

t1 = [1, 2, 3, 4, 5]

def reverse(t1):
    if len(t1)==1:
        return t1

    return reverse(t1[1:])+t1[0:1]
    
print(reverse(t1))        

list1 = [1, 2, 3, 4, 5]
def reverse_fun(numbers):
    if len(numbers) == 1:
        return numbers
# Otherwise
    return reverse_fun(numbers[1:])+numbers[0:1]
print(reverse_fun(list1))

def middle(c):
    n=float(len(c))//2
    if n % 2!=0:
        return c[int(n-.5)]
    else:
        return (c[int(n)],c[int(n-1)])

c=[4,5,8,9,6,4]        
print(middle(c))
my_dict = {"one": 1,"two":2,"three":3,"four":4}
print(my_dict.keys())
print(my_dict.values())

a='prdip'
print(a[::-1])
str=' '
for i in a:
    str=i+str

print(str)
print(reversed(a))
print(a)
t1 = ["Hello", "how", "are", "you"]
for i in range(len(t1)):
    t1[i]=t1[i].capitalize()

print(t1)

arr = [1, 2, 3, 4, 5]
sum = 0
for i in arr:
    sum +=i

print(sum)    

s = [4, 2, 13, 21, 5]

d=list(map(lambda u:u**2,filter(lambda u:u%2==1,s)))
print(d)
'''
d=[1,4,7,8,4,3,2]
e=[]
f=[]
x=[]
for i in d:
    if i%2==0:
        e.append(i)
    else:
        f.append(i)   
for j in range(len(e)):
    x.append(e[i])
    x.append(f[i])

print(x)    
