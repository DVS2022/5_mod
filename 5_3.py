import random

class Warrior:
	def __init__(self, name, health=100):
		self.name = name
		self.health = health

	def hit(self, target):
			target.health -= 20

warrior1 = Warrior('Воин №1')
warrior2 = Warrior('Воин №2')

while True:
	i = random.randint(0, 1)
	if i == 0:
		attacker = warrior1
		defencer = warrior2
		attacker.hit(defencer)
	else:
		attacker = warrior2
		defencer = warrior1
		attacker.hit(defencer)

	print('\n', attacker.name, 'атаковал', defencer.name)
	print(' У', defencer.name, 'осталось здоровья', defencer.health)
	if defencer.health <= 0:
		print('\n', attacker.name, 'ОДЕРЖАЛ ПОБЕДУ!')
		break
