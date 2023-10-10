import random
wins = 0
answers = ['rock', 'paper', 'scissors']

def game():
    global wins

    ans = input("Type rock, paper or scissors to start game or q to exit: ")
    if(ans == 'q'):
        quit()
    compchoice = random.choice(answers)
    print( "Computer chose " + compchoice + " You chose: " + ans)

    if(ans == compchoice):
        print("It was a draw, you both picked " + ans)
    elif(ans != compchoice):
        if(ans == "rock" and compchoice == "scissors"):
            print("You win!")
            wins+=1
        if(ans == "rock" and compchoice == "paper"):
            print("You lose!")
            wins-=1
        if(ans == "paper" and compchoice == "rock"):
            print("You win!")
            wins+=1
        if(ans == "paper" and compchoice == "scissors"):
            print("You lose!")
            wins-=1
        if(ans == "scissors" and compchoice == "paper"):
            print("You win!")
            wins+=1
        if(ans == "scissors" and compchoice == "rock"):
            print("You lose!")
            wins-=1
    print("Would you like to play again? ")
    print(wins)
    again = input("y or n? : ")
    if(again == "n"):
        quit()
    else:
        game()
        

def main():
    game()
    
main()

