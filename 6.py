'''mystr = "My favourite TV Series is \"Game of Thrones\""
print(mystr)
my=[i for i in range(200) if i%2==0 if i%3==0 if i%5==0]
print(my)'''
'''
mystr = "One 1 two 2 three 3 four 4 five 5 six 6789"
a=[i for i in mystr if type(i)==str]
print(a)
'''
A = {1,2,3,4,5}
B = {4,5,6,7,8}
C={8,9,10}
f=A.union(B,C)
print(f)