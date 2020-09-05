# WORKING WITH LISTS
lucky_numbers = [4, 6, 8, 2, 5, 9]
teams = ["Arsenal", "Arsenal", "Liverpool", "Chelsea", "Man City", "Man utd", "Everton"]
print(teams)
print(teams[3])
print(teams[0])
print(teams[-1])
print(teams[1:])
print(teams[0:3])

# Modifying items in a list
teams[4] = "Spurs"
print(teams)

# Using functions with lists
#teams.extend(lucky_numbers)     # Combines to lists
#print(teams)
teams.append("Barca")       # Adds an item at the end of the list
print(teams)
teams.insert(1, "Real Madrid")     # Adds an item at the specified location in the list
print(teams)
teams.remove("Spurs")
print(teams)
teams.pop()      # Removes the last item on the list
print(teams)
print(teams.index("Chelsea"))
print(teams.count("Arsenal"))
teams.sort()
lucky_numbers.sort()
print(lucky_numbers)
print(teams)
lucky_numbers.reverse()
print(lucky_numbers)

# Copying contents of a list
teams2 = teams.copy()
print(teams2)

teams.clear()
print(teams)
