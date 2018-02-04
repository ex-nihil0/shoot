import random
import time

def RPS():
    rpsNames = {1:'rock', 2:'paper', 3:'scissors'}
    firstTime = True

    print("I love Rock, Paper, Scissors!")
    time.sleep(1)
    while True:
        response = input("Want to play a round? Y/N ")
        response = response.lower()
        if response not in ["y","n"]:
            print("Please just enter Y/N. I'm not that sophisticated!")
            continue
        elif response != 'y':
            print("Ok, bye!")
            exit()
        else:
            break
    while True:
        x = random.randrange(1,4,1)
        computer = rpsNames[x]
        if firstTime == True:
            print("Great! When I say shoot, just type rock, paper, or scissors.")
            time.sleep(3.5)
        else:
            while True:
                response = input("Want to play again? Y/N ")
                response = response.lower()
                if response not in ["y","n"]:
                    print("Please just enter Y/N. I'm not that sophisticated!")
                    continue
                elif response != 'y':
                    print("Ok, thanks for playing. Bye!")
                    exit()
                else:
                    print("Great!")
                    time.sleep(1)
                    break
        firstTime = False
        print("Ready?")
        time.sleep(1)
        print("Rock...")
        time.sleep(1)
        print("Paper...")
        time.sleep(1)
        print("Scissors...")
        time.sleep(1)
        while True:
            player = input('Shoot! ')
            player = player.lower()
            if player not in ["rock","paper","scissors"]:
                print("Please just type rock, paper, or scissors. I'm not that sophisticated!")
            else:
                break
        if player == computer: 
            print("Wow, it's a tie! Looks like we both threw " + player + "!")
            continue
        elif player == 'rock':
            if computer == 'paper':
                print("You lost, I threw paper! Better luck next time!")
                continue
            else:
                print("You won, I threw scissors!")
                continue
        elif player == 'paper':
            if computer == 'scissors':
                print("You lost, I threw scissors! Better luck next time!")
                continue
            else:
                print("You won, I threw rock!")
                continue
        elif player == 'scissors':
            if computer == 'rock':
                print("You lost, I threw rock! Better luck next time!")
                continue
            else:
                print("You won, I threw paper!")
                continue
