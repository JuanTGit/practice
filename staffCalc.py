# Staff Price: 8260 gp
# Shop Price: 7000 gp

def staff_profit():
	tier = {
		'easy': 15,
		'medium': 30,
		'hard': 60,
		'elite': 120
	}
	amount = input('What tier are you?(easy, medium, hard, elite) ')
	days = int(input('How many days? '))

	profit_per_staff = 8260 - 7000
	daily_profit = profit_per_staff * tier[amount]
	print(f'{days * daily_profit} gp')

staff_profit()