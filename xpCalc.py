import math

def calculate_actions(curr_xp, xp_per_action):
	max_lvl = 13034431
	xp_to_max = math.ceil(max_lvl - curr_xp)

	print(f'xp remaining to max: {xp_to_max}')
	actions_remaining = math.ceil(xp_to_max / xp_per_action)

	return f'{actions_remaining} actions remain'


print(calculate_actions(5089700, 32.8))