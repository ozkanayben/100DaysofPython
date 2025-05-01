# Random module - The Mersenne Twister is a pseudorandum number genertor PRNG 
import random 
import Day4my_module
random_number = random.randint(1, 10) 
print(random_number)
print(Day4my_module.my_favorite_number)

friends = [ "Bob", "jess", "Kyle"]

print(random.choice(friends))


rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
'''
print(rock)

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|
'''

scissors = '''          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
'''
game_images = [rock, paper, scissors]

user = input("What do you chose? 0 for rock, 1 for paper 2 for scissors")
computer = random.randint(0, 2)
print("Computer choice", game_images[computer])