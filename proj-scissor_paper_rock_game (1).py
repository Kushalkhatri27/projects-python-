"""
logic for game :

1) give list to computer of scissor, paper and rock to choose between them .
2) compare the choice of computer and user 
3) if computer choice = user choice -> game draw/ computer choice rock and user choice paper -> user win
/ computer choice paper and user choice rock -> computer win

"""
import random 
options = ['scissor', 'paper' , 'rock']

play_continue = True

while play_continue==True:
    
    
    computer_choice = random.choice(options)
    
    user = input(" what would you choose !! scissor or paper or rock :").lower()
    
    print(f"Computer -- {computer_choice}")
    print(f"User -- {user}")


    if computer_choice == user :
        print (f' -- Game Draw -- You both choose {user}')
        
    elif computer_choice == "scissor" :
        if user == "paper" :
            print("compuer won")
        
        else :
            print("You won")
            
    elif computer_choice =="paper":
        if user == "rock":
            print(" computer won")
            
        else :
            print("you won")
    elif computer_choice =="rock":
        if user== "scissor":
            print("computer won")
            
        else:
            print("user won")
            
    
    play_again = input("Do you want to play Y/N ??").lower()
    
    if play_again != "y":
        play_continue = False
        