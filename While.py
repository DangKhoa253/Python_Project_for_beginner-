import random as rd

list_option= ['Rock','Paper','Scissor']
result=rd.choice(list_option)
print(result)

def handgame():
    x=str(input('What is your option? '))
    return x 
def ongame():
    x=  handgame()
    if x == result:
        print("Draw, Do you want play more")
        more=input("Yes/No?")
        if more == "Yes":
            return ongame()
        else:
            return
    else:
        if x =='Rock':
            if result =='Paper':
                print("You lose")
                return 
            if result =='Scissor':
                print("You win") 
                return 
        if x =='Papaer':
            if result =='Rock':
                print("You win")
                return
            if result =='Scissor':
                print("You lose ")
                return 
        if x =='Scissor':
            if result =='Rock':
                print("You lose")
                return
            if result =='Paper':
                print("You win")
                return
        return
ongame()