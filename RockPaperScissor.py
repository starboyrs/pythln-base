import random
print("Welcome ! Lets play Rock , Paper , scissors ")
name = input("Enter your name to continue: ")
print()
print("Welcome ", name,"." 'Lets start the game ')
player_score = 0
computer_score = 0
i = 1
while i <=5:
    print()
    player_choise = input("Enter an option (Rock ,  Paper ,  Scissors  : ").lower()
    print()
    actions = ["rock", "paper", "scissors"]
    computer_choise = random.choice(actions)
    print("Game Level : ", i)
    i += 1
    print("\n", name, "chose" ,player_choise,  "&", "computer chose" , computer_choise , "\n")
    
    if player_choise == computer_choise:
        print("Both players selected ",player_choise,"."," Sorry, It's a tie!")
    elif player_choise == "rock":
        if computer_choise == "scissors":
            print("Rock smashes scissors!",name, "win!")
            player_score += 1
        else:
            print("Paper covers rock!",name, "lose.")
            computer_score +=1
    elif player_choise == "paper":
        if computer_choise == "rock":
            print("Paper covers rock!",name, "win!")
            player_score += 1

            
        else:
            print("Scissors cuts paper!",name, "lose.")
            computer_score +=1
    elif player_choise == "scissors":
        if computer_choise == "paper":
            print("Scissors cuts paper!",name, "win!")
            player_score += 1
        
        else:
            print("Rock smashes scissors!",name, "lose.")
            computer_score +=1
    else:
        
        print("Sorry!",name,"You have entered a wrong option")
   
    print("\n\t##########Game Score##########")
    print("\t ", name,":",player_score, "| Computer:" ,computer_score)
    print("\t##############################")
    print()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    

print("\n\n##### Game Over #####")
print()
print("+-+-+-+-+-+-+-+-+-+-++-+---+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")
print()
if player_score < computer_score:
    print("Sorry",name,"!" ".", "You loose the game with the computer")
    print( 'score is' , computer_score)
 
elif player_score == computer_score:
    print("Game is Tie ")
else:
   print( name, 'wins!', 'Your score is ', player_score)