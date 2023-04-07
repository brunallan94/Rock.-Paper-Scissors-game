# Rock, paper, scissors game

import random, logging
from typing import List

logging.basicConfig(level = logging.DEBUG,
                    format = "%(asctime)s --> %(levelname)s --> %(message)s")

choices: List[str] = ["rock", "paper", "scissors"]
computer_names: List[str] = ["John", "Jenny", "Mark", "George", "Lisa"]

computer_pick = random.choice(choices)
comp_names = random.choice(computer_names)

draw: int = 0
player: int = 0
computer: int = 0


 
if __name__ == "__main__":
    player_name = input("Welcome, enter you name to continue or q to quit: ")
    
    try player_name == "q":
        quit()
        
    except:
        logging.info("Welcome")
    
    while True:
        
        question = input("Pick rock/paper/scissors or q to quit: ")
        
        if question.lower() == "rock" and computer_pick == "rock":
            logging.info("Draw")
            draw += 1
            
        elif question.lower() == "paper" and computer_pick == "paper":
            logging.info("Draw")
            draw += 1
            
        elif question.lower() == "scissors" and computer_pick == "scissors":
            logging.info("Draw")
            draw += 1
            
        elif question.lower() == "scissors" and computer_pick == "paper":
            logging.info(f"{player_name} won!")
            player += 1
            
        elif question.lower() == "rock" and computer_pick == "scissors":
            logging.info(f"{player_name} won!")
            player += 1
            
        elif question.lower() == "paper"  and computer_pick == "rock":
            logging.info(f"{player_name} won!")
            player += 1
            
        elif question.lower() == "q":
            logging.info("Goodbye!")
            break
        
        else:
            logging.info("computer wins")
            computer += 1
       
