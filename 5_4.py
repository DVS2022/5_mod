import random

class Warrior:
	def __init__(self, name, health=100, endurance=100, armor=100):
		self.name = name
		self.health = health
		self.endurance = endurance
		self.armor = armor
		
	def hit(self, deff, att):
		if att.endurance > 0:
			deff.health -= random.randint(10,30)
			att.endurance -= 10
			print('\n', att.name, 'атаковал', deff.name,
				'очки выносливости:', att.endurance)
			print(' У', deff.name, 'Брони:', deff.armor,
				', осталось здоровья:', deff.health)
		else:
			deff.health -= random.randint(0,10)
			print('\n', att.name, 'атаковал', deff.name,
				'очки выносливости:', att.endurance)
			print(' У', deff.name, 'Брони:', deff.armor,
				', осталось здоровья:', deff.health)

	def attacker_in_armor(self, deff, att):
		if att.endurance > 0 and deff.armor > 0:
			deff.health -= random.randint(0,20)
			deff.armor -= random.randint(0,10)
			att.endurance -= 10
			print('\n', deff.name, 'получил в броню')
			print(' У', deff.name, 'Брони:', deff.armor,
				', осталось здоровья:', deff.health)
			print(' У', att.name, 'очки выносливости:',
				att.endurance)
		elif att.endurance > 0 and deff.armor <= 0: 
			deff.health -= random.randint(10,30)
			att.endurance -= 10
			print('\n', deff.name, 'получил в броню')
			print(' У', deff.name, 'Брони:', deff.armor,
				', осталось здоровья:', deff.health)
			print(' У', att.name, 'очки выносливости:',
				att.endurance)
		elif att.endurance <= 0 and deff.armor > 0:
			deff.health -= random.randint(0,10)
			deff.armor -= random.randint(0,10)
			print('\n', deff.name, 'получил в броню')
			print(' У', deff.name, 'Брони:', deff.armor,
				', осталось здоровья:', deff.health)
			print(' У', att.name, 'очки выносливости:', 
				att.endurance)
		elif att.endurance <= 0 and deff.armor <= 0:
			deff.health -= random.randint(0,10)
			print('\n', deff.name, 'получил в броню')
			print(' У', deff.name, 'Брони:', deff.armor,
				', осталось здоровья:', deff.health)
			print(' У', att.name, 'очки выносливости:', 
				att.endurance)

	def defen(self, deff):
		print('\n Оба воина защищаются')

	# def stat_war(self):
	# 	print('\n', deff.name, 'получил в броню')
	# 	print(' У', deff.name, 'Брони:', deff.armor,
	# 		', осталось здоровья:', deff.health)
	# 	print(' У', att.name, 'очки выносливости:', att.endurance)


warrior1 = Warrior('Воин №1')
warrior2 = Warrior('Воин №2')

while True:
	
	i = random.randint(0, 1)
	if i == 0:	#Воин1 в атакующей позиции
		i = random.randint(0, 1)
		if i == 0:	#Воин2 в атакующей позиции
			warrior1.hit(warrior2, warrior1)
			warrior2.hit(warrior1, warrior2)
		else:	#Воин2 защищается
			warrior1.attacker_in_armor(warrior2, warrior1)

	else:	#Воин1 защищается
		i = random.randint(0, 1)
		if i == 0:	#Воин2 атакует
			warrior2.attacker_in_armor(warrior1, warrior2)
		else: #Воин2 тоже защищается
			warrior1.defen(warrior2)
	
	if warrior1.health <= 10 or warrior2.health <= 10:
		q = input(' Пощадить его?(да/нет?):')
		if q == 'да':
			print(' Вы его пощадили!')
			break
		else:
			print(' Вы его не пощадили!')
			break
