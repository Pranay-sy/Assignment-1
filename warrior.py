import random

class Warrior:
    def __init__(self):
        self.ST = random.randint(-2, 5)
        self.DX = random.randint(-2, 5)
        self.IQ = random.randint(-2, 1)
        self.HT = random.randint(-2, 4)
    
    def roll_dice(self):
        return random.randint(1, 12)

    def play_challenge(self, challenge_num):
        
        # Challenge 1: Strength Test
        if challenge_num == 1:
            challenge_attribute = self.ST
            print(f"Challenge: You must defent a lower rank demon using your strength (ST {self.ST}).")
        
        # Challenge 2: Dexterity Test
        elif challenge_num == 2:
            challenge_attribute = self.DX
            print(f"Challenge: You face a series of traps that require your dexterity (DX {self.DX}) to evade.")
        
        # Challenge 3: Intelligence Test
        else:
            challenge_attribute = self.IQ
            print(f"Challenge: You need to decipher a complex code with your intelligence (IQ {self.IQ}).")
        
       
        dice_roll=self.roll_dice()
        total_roll = dice_roll + challenge_attribute

        if total_roll <= 3:
            self.HT -= 1
            return "Critical Loss"
        elif 4 <= total_roll <= 7:
            return "Loss"
        elif 8 <= total_roll <= 10:
            return "Win"
        else:
            self.ST += 1
            return "Critical Win"

    def is_winning(self):
        # win/loss criteria for the Warrior role
        if self.ST > 0 and self.DX > 0 and self.IQ > 0:
            return True
        else:
            return False