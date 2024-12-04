// libraries
import cmd
import textwrap
import sys
import os
import time
import random
screen_width = 100

// Player Class
class player:
    def __init__(self):
        self.name = ''
        self.feeling = ''
        self.exp = ''
        self.position = 'ground'
        self.won = False
        self.solves = 0
player1 = player()

################
# Title Screen #
################
def title_screen_options():
	#Allows the player to select the menu options, case-insensitive.
	option = input("> ")
	if option.lower() == ("play"):
		setup_game()
	elif option.lower() == ("quit"):
		sys.exit()
	elif option.lower() == ("help"):
		help_menu()		
	while option.lower() not in ['play', 'help', 'quit']:
		print("Invalid command, please try again.")
		option = input("> ")
		if option.lower() == ("play"):
			setup_game()
		elif option.lower() == ("quit"):
			sys.exit()
		elif option.lower() == ("help"):
			help_menu()

def title_screen():
	#Clears the terminal of prior code for a properly formatted title screen.
	os.system('clear')
	#Prints the pretty title.
	print('#' * 45)
	print('#    Welcome to the application process!    #')
	print("#           Presented by Team WEx           #")
	print('#' * 45)
	print("                 .: Play :.                  ")
	print("                 .: Help :.                  ")
	print("                 .: Quit :.                  ")
	title_screen_options()

#main loop
def main_game_loop():
	total_puzzles = 6
	while player1.won is False:
		#print_location()
		prompt()

################
# Execute Game #
################
def setup_game():
	#Clears the terminal for the game to start.
	os.system('clear')

	#QUESTION NAME: Obtains the player's name.
	question1 = "Hello there, what is your name?\n"
	for character in question1:
		#This will occur throughout the intro code.  It allows the string to be typed gradually - like a typerwriter effect.
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	player_name = input("> ")
	player1.name = player_name

	#QUESTION FEELING: Obtains the player's feeling.
	question2 = "Okay " + player1.name + ", how are you feeling?\n"
	for character in question2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	feeling = input("> ")
	player1.feeling = feeling.lower()

	#Creates the adjective vocabulary for the player's feeling.
	good_adj = ['good', 'great', 'rohit', 'happy', 'aight', 'understanding', 'great', 'alright', 'calm', 'confident', 'not bad', 'courageous', 'peaceful', 'reliable', 'joyous', 'energetic', 'at', 'ease', 'easy', 'lucky', 'k', 'comfortable', 'amazed', 'fortunate', 'optimistic', 'pleased', 'free', 'delighted', 'swag', 'encouraged', 'ok', 'overjoyed', 'impulsive', 'clever', 'interested', 'gleeful', 'free', 'surprised', 'satisfied', 'thankful', 'frisky', 'content', 'receptive', 'important', 'animated', 'quiet', 'okay', 'festive', 'spirited', 'certain', 'kind', 'ecstatic', 'thrilled', 'relaxed', 'satisfied', 'wonderful', 'serene', 'glad', 'free', 'and', 'easy', 'cheerful', 'bright', 'sunny', 'blessed', 'merry', 'reassured', 'elated', '1738', 'love', 'interested', 'positive', 'strong', 'loving']
	hmm_adj = ['idk', 'concerned', 'lakshya', 'eager', 'impulsive', 'considerate', 'affected', 'keen', 'free', 'affectionate', 'fascinated', 'earnest', 'sure', 'sensitive', 'intrigued', 'intent', 'certain', 'tender', 'absorbed', 'anxious', 'rebellious', 'devoted', 'inquisitive', 'inspired', 'unique', 'attracted', 'nosy', 'determined', 'dynamic', 'passionate', 'snoopy', 'excited', 'tenacious', 'admiration', 'engrossed', 'enthusiastic', 'hardy', 'warm', 'curious', 'bold', 'secure', 'touched', 'brave', 'sympathy', 'daring', 'close', 'challenged', 'loved', 'optimistic', 'comforted', 're', 'enforced', 'drawn', 'toward', 'confident', 'hopeful', 'difficult']
	bad_adj = ['bad', 'meh', 'sad', 'hungry', 'unpleasant', 'feelings', 'angry', 'depressed', 'confused', 'helpless', 'irritated', 'lousy', 'upset', 'incapable', 'enraged', 'disappointed', 'doubtful', 'alone', 'hostile', 'discouraged', 'uncertain', 'paralyzed', 'insulting', 'ashamed', 'indecisive', 'fatigued', 'sore', 'powerless', 'perplexed', 'useless', 'annoyed', 'diminished', 'embarrassed', 'inferior', 'upset', 'guilty', 'hesitant', 'vulnerable', 'hateful', 'dissatisfied', 'shy', 'empty', 'unpleasant', 'miserable', 'stupefied', 'forced', 'offensive', 'detestable', 'disillusioned', 'hesitant', 'bitter', 'repugnant', 'unbelieving', 'despair', 'aggressive', 'despicable', 'skeptical', 'frustrated', 'resentful', 'disgusting', 'distrustful', 'distressed', 'inflamed', 'abominable', 'misgiving', 'woeful', 'provoked', 'terrible', 'lost', 'pathetic', 'incensed', 'in', 'despair', 'unsure', 'tragic', 'infuriated', 'sulky', 'uneasy', 'cross', 'bad', 'pessimistic', 'dominated', 'worked', 'up', 'a', 'sense', 'of', 'loss', 'tense', 'boiling', 'fuming', 'indignant', 'indifferent', 'afraid', 'hurt', 'sad', 'insensitive', 'fearful', 'crushed', 'tearful', 'dull', 'terrified', 'tormented', 'sorrowful', 'nonchalant', 'suspicious', 'deprived', 'pained', 'neutral', 'anxious', 'pained', 'grief', 'reserved', 'alarmed', 'tortured', 'anguish', 'weary', 'panic', 'dejected', 'desolate', 'bored', 'nervous', 'rejected', 'desperate', 'preoccupied', 'scared', 'injured', 'pessimistic', 'cold', 'worried', 'offended', 'unhappy', 'disinterested', 'frightened', 'afflicted', 'lonely', 'lifeless', 'timid', 'aching', 'grieved', 'shaky', 'victimized', 'mournful', 'restless', 'heartbroken', 'dismayed', 'doubtful', 'agonized', 'threatened', 'appalled', 'cowardly', 'humiliated', 'quaking', 'wronged', 'menaced', 'alienated', 'wary']

	#Identifies what type of feeling the player is having and gives a related-sounding string.
	if player1.feeling in good_adj:
		feeling_string = "I am glad you feel"
	elif player1.feeling in hmm_adj:
		feeling_string = "that is interesting you feel"
	elif player1.feeling in bad_adj:
		feeling_string = "I am sorry to hear you feel"
	else:
		feeling_string = "I do not know what it is like to feel"

	#Combines all the above parts.
	question3 = "Alright, " + player1.name + ", " + feeling_string + " " + player1.feeling + ".\n"
	for character in question3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

	#Leads the player into the cube puzzle now!
	speech1 = "Okay, " + player1.name + ". Nice meeting you I guess..\n"
	speech2 = "I need to go now, " + player1.name + ".\n"
	speech3 = "Bye Bye.\n"  
	speech4 = "Oh you need help finding an internship? How would I know.\n"
	speech5 = "Just do whatever, as long as you make Microsoft your goal.\n"
	speech6 = "Don't quit till it's Microsoft.\n"
	for character in speech1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.1)
	for character in speech4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech5:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech6:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.2)
	time.sleep(1)

	os.system('clear')
	print("################################")
	print("#   Let the process begin!     #")
	print("################################\n")
	print("You find yourself looking for work experience.\n")


title_screen()
