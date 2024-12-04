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

