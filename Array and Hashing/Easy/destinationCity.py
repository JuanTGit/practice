# 1436. Destination City
# Easy
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
# Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

# Example 1:

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
# Example 2:

# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".
# Example 3:

# Input: paths = [["A","Z"]]
# Output: "Z"
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

def destCity(paths):

	outgoingCity = {}

	for city in paths:
		outgoingCity[city[0]] = outgoingCity.get(city[0], 0) + 1
	
	for city in paths:
		if city[1] not in outgoingCity:
			return city[1]


print(destCity(paths))