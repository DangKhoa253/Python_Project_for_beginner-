import random as rd


def handgame():
    x=str(input('What is your option? '))
    return x 
def ongame():
    list_option = ['Rock', 'Paper', 'Scissor']
    result = rd.choice(list_option)
    print(result)
    x= handgame()
    if x == result:
        print("Draw, Do you want play more")
        more = input("Yes/No?")
        if more == "Yes":
            return ongame()
        else:
            return print(" Thank you for playing game")
    else:
        if x == 'Rock':
            if result == 'Paper':
                print("You loses and Computer wins - Fighting, Thank you")
                return 
            if result == 'Scissor':
                print("You win and Computer loses - Thank you ")
                return 
        elif x == 'Paper':
            if result == 'Rock':
                print("You wins and Computer loses - Thank you ")
                return
            if result == 'Scissor':
                print("You loses and Computer wins - Try more, Thank you")
                return 
        elif x == 'Scissor':
            if result == 'Rock':
                print("You loses and Computer wins - Unlucky, good luck another time, Thank you")
                return
            if result == 'Paper':
                print("You win and Computer loses - Thank you")
                return
        return
ongame()