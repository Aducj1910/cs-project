import random

# kingdom_name = input("Enter the name of your kingdom: ")
kingdom_name = "Faridabad"
#intro message
print(f"Welcome ruler of {kingdom_name}, in this game you have to \nfight battles, grow your territory and keep your citizens happy!\n")

game_over = False #boolean to check if the game has ended
turns = 0 #to track number of turns

#set up of tiles with territory names
tile_setup = {"Haryana": False, "Punjab": False, "Uttrakhand": False, "Delhi": False, "Rajasthan": False,
	"Chandigarh": False, "Gujarat": False, "Maharashtra": False}

military_setup = {"airplane": 0, "soldiers": 0, "missiles": 0}

decision_options = {"Attack", "Set tax", "Set up factory", "Buy military"}

for tile in tile_setup:
	print(tile)

# starting_tile = input("\nEnter the tile you want to start with: ").title()
starting_tile = "Haryana"
tile_setup[starting_tile] = True

already_passed = ""

def get_setup(input_setup):
	global already_passed

	output_setup = {}
	for i in input_setup:
		if(input_setup[i] == False and i not in already_passed):
			if(random.randint(1,5) == 3):
				output_setup[i] = True
				break
			else:
				output_setup[i] = False
		else:
			output_setup[i] = False

	return output_setup

class Kingdom:

	def __init__(self, name, tiles, tax, money, factories, happy, military):
		self.name = name #name of the kingdom
		self.tiles = tiles #number of tiles owned (dictionary with true false)
		self.tax = tax #current tax rate
		self.money = money #balance to spend on factory and military
		self.factories = factories #number of factories currently set up (each produces ₹100 per turn)
		self.happy = happy #happiness of the citizens (scale of 0 to 100)
		self.military = military #dictionary with the number of each type of unit

#initializing the user's Kingdom
user_kingdom = Kingdom(kingdom_name, tile_setup, 10, 1000, 0, 80, military_setup)

one_kingdom = Kingdom("Maurya", get_setup(tile_setup), 10, 1000, 0, 80, military_setup)
two_kingdom = Kingdom("Mughal", get_setup(tile_setup), 10, 1000, 0, 80, military_setup)

def get_territories():
	territories = {}
	for i in user_kingdom.tiles:
		if(user_kingdom.tiles[i] == False):
			territories[i] = "None"
		elif(user_kingdom.tiles[i] == True):
			territories[i] = user_kingdom.name
	for i in one_kingdom.tiles:
		if(one_kingdom.tiles[i] == True):
			territories[i] = one_kingdom.name
	for i in two_kingdom.tiles:
		if(two_kingdom.tiles[i] == True):
			territories[i] = two_kingdom.name

	ret_string = "Current Territories:\n"
	for i in territories:
		ret_string += (i + " : " + territories[i] + "\n")

	return ret_string

def get_options_string():
	ret_string = "What do you want to do?\n"
	counter = 0
	for i in decision_options:
		counter += 1
		ret_string += (i + " " + "[" + str(counter) + "]\n")

	return ret_string 



while not game_over:
	turns += 1
	print(f"\nTurns: {str(turns)}\nTax: {str(user_kingdom.tax)}%\nFactories: {str(user_kingdom.factories)}\nMoney: {str(user_kingdom.money)}")
	print(f"\nCurrent Military:\nSoldiers: {str(user_kingdom.military['soldiers'])}\nAirplane: {str(user_kingdom.military['airplane'])}\nMissiles: {str(user_kingdom.military['missiles'])}\n")
	print(get_territories())
	decision = input(get_options_string())
	if(decision == 1):
		target = input("\nTerritory to attack: ").title()