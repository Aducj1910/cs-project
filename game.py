# kingdom_name = input("Enter the name of your kingdom: ")
kingdom_name = "Test"
#intro message
print(f"Welcome ruler of {kingdom_name}, in this game you have to \nfight battles, grow your territory and keep your citizens happy!\n")

game_over = False #boolean to check if the game has ended
turns = 0 #to track number of turns

#set up of tiles with territory names
tile_setup = {"Haryana": False, "Punjab": False, "Uttrakhand": False, "Delhi": False, "Rajasthan": False,
	"Chandigarh": False, "Gujarat": False, "Maharashtra": False}

for tile in tile_setup:
	print(tile)

starting_tile = input("\nEnter the tile you want to start with: ").title()
tile_setup[starting_tile] = True


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
user_kingdom = Kingdom(kingdom_name, tile_setup, 10, 1000, 0, 80, {"airplane": 0, "soldiers": 0, "missiles": 0, "ships": 0})


while not game_over:
	turns += 1
