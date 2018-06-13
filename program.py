import random

print('----------------------')
print('   The Number Game')
print('----------------------')

randomNo = random.randint(0, 100)

inputToInt = -1

name = input("Player, please enter your name: ")

while inputToInt != randomNo:
    userInput = input("Please guess a number between 1 and 100: ")
    inputToInt = int(userInput)
    if inputToInt > randomNo:
        print("Your guess of {0} was too high. Try again.".format(inputToInt))
    elif inputToInt < randomNo:
        print("Your guess of {0} was too low. Try again.".format(inputToInt))
    else:
        print("Congratulations {}, you win.".format(name))