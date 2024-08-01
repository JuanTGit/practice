

def calculate_actions(curr_xp, xp_per_action):
	max_lvl = 13034431
	xp_to_max = max_lvl - curr_xp

	actions_remaining = xp_to_max / xp_per_action

	return actions_remaining


print(calculate_actions(5089700, 32.8))