import random
from warrior import Warrior
from explorer import Explorer

class Game:
    def __init__(self, role):
        self.role = role
        if role == "Explorer":
            self.player = Explorer()
        elif role == "Warrior":
            self.player = Warrior()
       

    def play(self):
        print(f"You are the {self.role}. Your adventure begins now!\n")
        
        for challenge_num in range(1, 4):
            print(f"Challenge {challenge_num}:")
            input("Press enter to roll the dice...")
            
            roll_dice=self.player.roll_dice() 

            print(f"You rolled a {roll_dice}!\n")
            
            challenge_result = self.player.play_challenge(challenge_num)
            
            if challenge_result == "Critical Loss":
                print("You failed the challenge horribly, and your attributes have dropped!\n")
            elif challenge_result == "Loss":
                print("You lost the challenge, but your attributes stay the same.\n")
            elif challenge_result == "Win":
                print("You won the challenge! Your attributes stay the same.\n")
            elif challenge_result == "Critical Win":
                print("You outperformed in the challenge, and your attributes have enhanced!\n")
        
        if self.player.is_winning():
            print("Congratulations! You have successfully completed your adventure.")
        else:
            print("Sorry, you couldn't complete your adventure. Better luck next time!")
