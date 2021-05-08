import random

def main():
    favourite= ''
    gamble =random.random() 
    #print('gamble:' + str(gamble))
    if gamble < 0.1:
      favourite="bats"
    elif (gamble > 0.1) and (gamble < 0.2):
      favourite="cats"
    elif (gamble > 0.2):
      favourite="dogs"

    print("I love " + favourite) 


main()
