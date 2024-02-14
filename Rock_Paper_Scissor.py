#Game (rock, paper, scissors)


print('\nWinning rules of the game ROCK PAPER SCISSORS are :\n\n'
      + "Rock vs Paper -> Paper wins \n\n"
      + "Rock vs Scissors -> Rock wins \n\n"
      + "Paper vs Scissors -> Scissor wins \n\n")


import random
from secrets import choice

def try_again():
    r=["ROCK","PAPER","SCISSORS"]
    ran=random.choice(r)
    rps=(input("Choose from ROCK,PAPER and SCISSORS -> " ))
    
    if(rps=="paper" or rps=="rock" or rps=="scissors" or rps=="SCISSORS" or rps=="PAPER" or rps=="ROCK" ):
        print("\nUser choice is -> ",rps,"\n") 
        print("Now its Computers Turn....","\n")
        print("computer choice is -> ",ran,"\n")
        
        ##paper
        
        if ran=="paper" or rps=="PAPER":
            if rps == "paper" or rps=="PAPER":
                print("Its a tie \n")
            elif rps == "scissors" or rps=="SCISSORS":
                print("User Win ! \n")
            elif rps == "rock" or rps=="ROCK":
                print("Computer Win ! \n")
            else:
                print("Enter a valid choice please ☺ \n")
                
        ##rock
        
        if ran=="rock" or rps=="ROCK":
            if rps == "paper" or rps=="PAPER":
                print("User Win ! \n")
            elif rps == "scissors" or rps=="SCISSORS":
                print("Computer Win! \n")
            elif rps == "rock" or rps=="ROCK":
                print("Its a tie \n")
            else:
                print("Enter a valid choice please ☺ \n")
        ##scissors
        if ran=="scissors" or rps=="SCISSORS":
            if rps == "paper" or rps=="PAPER":
                print("Computer Win! \n")
            elif rps == "scissors" or rps=="SCISSORS":
                print("Its a tie \n")
            elif rps == "rock" or rps=="ROCK":
                print("User Win ! \n")
            else:
                print("Enter a valid choice please ☺ \n")


        que= input("Do you want to play again? (Y/N) \n")
        if que =="yes" or que =="Yes" or que =="YES" or que=="y" or que=="Y":
            try_again()
        elif que=="no" or que=="No" or que=="NO" or que=="n" or que=="N":
            print("thanks for playing")
        
    else:
         print("\nEnter a valid choice please ☺ \n")
         try_again()
         
try_again()






