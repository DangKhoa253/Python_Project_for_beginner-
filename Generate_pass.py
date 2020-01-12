import random as rd 
import string as st 
A=[]
B=[]
a=int(input("1: "))
b=int(input("2: "))
for x in range(int(a)) :
    x= rd.randrange(0,11)
    A.append(x)
    x +=1
rd.shuffle(A)
for x in range(int(b)) :
    y= rd.choice(st.ascii_letters)
    B.append(y)
    x +=1 
rd.shuffle(B)
S= A + B 
rd.shuffle(S)
password="".join([str(ele) for ele in S])
print(password)