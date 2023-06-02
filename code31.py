#show only duplicates 
'''a=[1,2,3,4,5,2,3,4,7,9,5]
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)#elent not rpeat
    else:
        c.append(i) #elemnt repeat  
print(b)  
print(c)  '''
#odd & even separation
'''list1 = [3, 5, 4, 9, 8, 5, 7, 8, 12]
odd = []
even = []
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)        
print(even)'''
#secondlarge
'''list = [20, 30, 40, 25, 10] 
list.sort()
print(list[2])'''
#print the elements of an array
'''arr = [1, 2, 3, 4, 5,6,7]
for i in range(len(arr)):
    print(arr[i])'''
#even at back and even at front
'''
l = [1,6, 2, 3, 8, 7, 4]
odd = []
even = []
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd+even)'''
#elements of an array in reverse order
'''arr = [1, 2, 3, 4, 5]
print(arr[::-1])
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=',')'''
#Merge two dictionaries
'''dict1 = {'a': 10, 'b': 8}
dict2 = {'c': 6, 'd': 4}

c=dict1|dict2
print(c)'''
#lower using decorator
'''
def lower(fun):
    def ab():
        text=fun()    

        mod=text.lower()
        return mod
    return ab   
@lower
def mess():
    return 'HELLO WHO R U' 

a=mess()   
print(a) 
'''
#int and string separation :-
'''a = "MH10CD7172"
b=''
c=''
for i in a:
    if i.isdigit():
        b=b+i
    else:
        c=c+i  
print(b) 
print(c)'''
#   4.legnth of without space string
'''a = 'indexial solution is the best'  
print(len(a))
b=a.replace(" ","")
print(len(b))'''

# print even length words in string
'''n="This is a python language"
b=n.split(" ")
c=[]
d=[]
for i in b:
    if len(i)%2==0:
        print(c.append(i))
    else:
        d.append(i)   
print(c) 
print(d)       '''
'''from functiontools import reduce
x=filter(lambda x,y:x+y,[1,2,3,4,8,14,12])
print(list(x))'''
#capitalize each word
'''
list = ["Hello", "how", "are", "you"]
for i in range(len(list)):
    list[i]=list[i].capitalize()
    print(list[i])'''

#fibconcce series
a=1
b=2
c=a+b    
for i in range(1,50):
    a=b
    b=c
    c=a+b 
    print(c)
#swap dict    
dict = {'a': 1, 'b': 2, 'c': 3}
'''
a={value:key for key,value in dict.items()}
print(a)
'''
#swap first and last
'''a=[20,50,80,10]

temp = a[0]
a[0]=a[len(a)-1] 
a[len(a)-1]=temp
print(a)'''
lst = [[11, 22, 33, 44], [55, 66, 77], [88, 9]]

'''sd=[]
for i in lst:
    for j in i:
        sd.append(j)

print(sd) '''
'''a=[j for i in lst for j in i]
print(a)'''
'''
arr=[10,52,85,79]   
n=len(arr)  
k=2
for i in range(n):
    arr[i:i+k]=arr[i:i+k][::-1]
    print(arr)'''

def palidrome(b):
    a=str(b)     
    if list(a)==list(reversed(a)):
        print('palidrome')
    else:
        print('nonpalidrome')    
palidrome(2589)

    





