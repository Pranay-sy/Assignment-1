import random

class Explorer:
    def __init__(self):
        self.ST = random.randint(-2, 1)
        self.DX = random.randint(-2, 1)
        self.IQ = random.randint(-2, 2)
        self.HT = random.randint(-2, 2)
    
    def roll_dice(self):
         return random.randint(1, 12)
         
    def play_challenge(self, challenge_num):
        
        # Challenge 1: Strength Test
        if challenge_num == 1:
            challenge_attribute = self.ST
            print(f"Challenge: You encounter a boulder. You need to break it down with your strength (ST {self.ST}).")
        
        # Challenge 2: Dexterity Test
        elif challenge_num == 2:
            challenge_attribute = self.DX
            print(f"Challenge: You come across a maze. Your dexterity (DX {self.DX}) will help you navigate it.")
        
        # Challenge 3: Intelligence Test
        else:
            challenge_attribute = self.IQ
            print(f"Challenge: You find an cipher code. Your intelligence (IQ {self.IQ}) will aid you in solving it.")

        dice_roll=self.roll_dice()
        total_roll = dice_roll + challenge_attribute

        
        if total_roll <= 3:
            self.ST -= 1
            return "Critical Loss"
        elif 4 <= total_roll <= 7:
            return "Loss"
        elif 8 <= total_roll <= 10:
            return "Win"
        else:
            self.IQ += 1
            return "Critical Win"

    def is_winning(self):
        # win/loss criteria for the Explorer role
        if self.ST > 0 and self.DX > 0 and self.IQ > 0:
            return True
        else:
            return False

