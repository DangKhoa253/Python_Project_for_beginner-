import random as rd 
import string as st 

def gene_pass():
    a=int(input("How long letter of password you want?"))
    b=int(input("How long number of password you want?"))
    c= a+b
    if c < 6:
        print("Not accepted password, please set again")
        return gene_pass()
    else:
        #create 2 lists for letter and number    
        A=[]
        B=[]
        for x in range(int(a)) :
            x= rd.randrange(0,11)
            A.append(x)
            x +=1
        for x in range(int(b)) :
            y= rd.choice(st.ascii_letters)
            B.append(y)
            x +=1 
        #create 1 list combines A & B and shuffle
        C=A+B
        rd.shuffle(C)
        password="".join([str(elem) for elem in C])
        print("Here is your password: ",password)

gene_pass()
