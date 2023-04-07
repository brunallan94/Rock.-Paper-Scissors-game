# Rock, paper, scissors game

import random, logging, requests
from typing import List

# Setting up the logging module
logging.basicConfig(level = logging.DEBUG,
                    format = "%(asctime)s --> %(levelname)s --> %(message)s")

# Setting up an API that can requests multiple names of people
response = requests.get('https://randomuser.me/api')

first_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']

# logging.debug(f'{first_name} {last_name}')

# Creating the rock/paper/scissors choices selection and a list of computer names to randomize
choices: List[str] = ["rock", "paper", "scissors"]
computer_names: List[str] = ["John", "Jenny", "Mark", "George", "Lisa", "Jeremy", "Paul"]
random_lst: List[str] = ["rock", "paper", "scissors", "q"]


computer_pick = random.choice(choices)
# comp_names = random.choice(computer_names)
comp_names = first_name + " " + last_name

# Initializing the amount of points to be awarded to the winner or the number of draws gotten when playing
draw: int = 0
player: int = 0
computer: int = 0


 
if __name__ == "__main__":
    player_name = input("Welcome, enter you name to continue or q to quit: ")
    
    if player_name.lower() == "q":
        print("Maybe next time :( ")
        quit()
        
    logging.info(f"Welcome, your opponent is {comp_names}")
    
    while True:
        
        question = input("Pick rock/paper/scissors or q to quit: ")
        
        if question.lower() not in random_lst:
            logging.warning("Please type in the correct characters!! \n")
        
        elif question.lower() == "rock" and computer_pick == "rock":
            logging.info("Draw \n")
            draw += 1
            
        elif question.lower() == "paper" and computer_pick == "paper":
            logging.info("Draw \n")
            draw += 1
            
        elif question.lower() == "scissors" and computer_pick == "scissors":
            logging.info("Draw \n")
            draw += 1
            
        elif question.lower() == "scissors" and computer_pick == "paper":
            logging.info(f"{player_name} won! \n")
            player += 1
            
        elif question.lower() == "rock" and computer_pick == "scissors":
            logging.info(f"{player_name} won! \n")
            player += 1
            
        elif question.lower() == "paper"  and computer_pick == "rock":
            logging.info(f"{player_name} won! \n")
            player += 1
            
        elif question.lower() == "q":
            logging.info("Goodbye!")
            break
    
        else:
            logging.info(f"{comp_names} drew {computer_pick} and wins \n")
            computer += 1
       
logging.info(f"{comp_names} got: {computer} wins \n")
logging.info(f"{player_name} got: {player} wins \n")
logging.info(f"The game ended with {draw} draws \n")