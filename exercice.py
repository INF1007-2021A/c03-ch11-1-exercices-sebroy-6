"""
Chapitre 11.1
"""

from game import *

def main():
	c1 = Character("Äpik", 200, 150, 70, 70)
	c2 = Character("Gämmor", 250, 100, 120, 60)

	c1.weapon = Weapon("BFG", 100, 69)
	c2.weapon = Weapon("Deku Stick", 120, 1)

	turns, victor, loser = run_battle(c1, c2)
	finish = random.choice(["finished", "decapitated", "annihilated", "man handled", "slaughtered"])

	print(f"The victor is {victor.name} who {finish} {loser.name} in {turns} turns!")

if __name__ == "__main__":
	main()

