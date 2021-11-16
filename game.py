"""
Chapitre 11.1

Classes pour représenter un personnage.
"""

import random

UNARMED_POWER = 20

class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	def __init__(self, name="Unarmed", power=UNARMED_POWER, min_level=0):
		self.name = name
		self.power = power
		self.min_level = min_level

	def make_unarmed(self):
		self.name = "Unarmed"
		self.power = UNARMED_POWER
		self.min_level = 0

class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name="No name", max_hp=100, attack=1, defense=1, level=1):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.hp = self.max_hp
		self.weapon = Weapon()


def compute_damage(attacker, defender):
	damage_equation = (((((2/5)*attacker.level)+2)*attacker.weapon.power*(attacker.attack/defender.defense)/50) + 2)

	crit = 2 if random.randint(1, 16) == 1 else 1
	modifier = crit * (random.randint(85, 100)/100)

	return crit, damage_equation * modifier


def deal_damage(attacker, defender):
	print(f"{attacker.name} used {attacker.weapon.name}")
	crit, damage = compute_damage(attacker, defender)

	if crit == 2:
		print("  Critical hit!")

	print(f"  {defender.name} took {damage} dmg")
	defender.hp -= damage

	return defender


def run_battle(c1, c2):
	attacker = c1
	defender = c2
	turn = 1

	print(f"{attacker.name} starts a battle with {defender.name}!")

	while True:
		defender = deal_damage(attacker, defender)

		if defender.hp <= 0:
			print(f"{defender.name } is sleeping with the fishes.")
			break

		swap = attacker
		attacker = defender
		defender = swap
		turn += 1

	return turn, attacker, defender

