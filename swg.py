import random

computer = random.choice([-1,0,1])
you = input("Enter your choice (s for Snake, w for Water, g for Gun):")
dic = {"s":1, "w":0, "g":-1}
revdic = {1:"Snake",0:"Water",-1:"Gun"}

if you in dic:
    youdic = dic[you]
    print(f'You choose {revdic[youdic]}\nComputer Choose {revdic[computer]}')

    if(computer == youdic):
        print("Game Draw!")
    elif(computer == 0 and youdic == 1):
        print("You win")
    elif(computer == 0 and youdic == -1):
        print("You loose")
    elif(computer == 1 and youdic == 0):
        print("You loose")
    elif(computer == 1 and youdic == -1):
        print("You win")
    elif(computer == -1 and youdic == 0):
        print("You win")
    elif(computer == -1 and youdic == 1):
        print("You loose")
else:
    print("Invalid input.Please enter 's' for Snake, 'w' for Water, 'g' for Gun.")