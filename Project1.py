import random

def game(comp, b):
    if comp==b:
        return None
    elif comp =='s':
        if b=='w':
            return False
        elif b=='g':
            return True
    elif comp=='w':
        if b=='w':
            return False
        elif b=='g':
            return True
    


print("Computer Turn: Snake(s) Water(w) or Gun(g)? \n")
randno=random.randint(1,3)
if randno==1:
    com = 's'
elif randno==2:
    com ='w'
elif randno==3:
    com = 'g'


b=input("Your Turn: Snake(s) Water(w) or Gun(g)? \n")

print("Computer chose:", com)
print("You chose: ", b)
WinorLose=game(com, b)
if WinorLose== None:
    print("It's a Tie")
elif WinorLose:
    print("You Win!")
else:
    print("You Lose!")