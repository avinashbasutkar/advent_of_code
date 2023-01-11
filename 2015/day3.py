#  Open the text file in read mode
with open(r"D:\Advent of Code\2015\day3_input.txt", "r") as file:
    # Read the contents of the file into a string
    directions = file.read()

# Part 1

# Initialize an empty set to store the houses that Santa has visited
visited_houses = set()

# Add the starting location to the set
visited_houses.add((0, 0))

current_location = (0, 0)

# Loop through the directions given by the elf
for direction in directions:
    # Update Santa's location based on the direction
    if direction == "^":
        current_location = (current_location[0], current_location[1] + 1)
    elif direction == "v":
        current_location = (current_location[0], current_location[1] - 1)
    elif direction == ">":
        current_location = (current_location[0] + 1, current_location[1])
    elif direction == "<":
        current_location = (current_location[0] - 1, current_location[1])
    
    # Add the new location to the set of visited houses
    visited_houses.add(current_location)

# Return the number of unique houses that received at least one present
print(len(visited_houses))

# Part 2

# Set the starting location for Santa and Robo-Santa
santa_location = (0, 0)
robo_santa_location = (0, 0)

# Initialize empty sets to store the visited houses for each
visited_houses_santa = set()
visited_houses_robo_santa = set()

# Add the starting location to each set
visited_houses_santa.add(santa_location)
visited_houses_robo_santa.add(robo_santa_location)

# Split the directions string into two lists for Santa and Robo-Santa
santa_directions = directions[::2]
robo_santa_directions = directions[1::2]

# Loop through the directions for Santa
for direction in santa_directions:
    # Update Santa's location based on the direction
    if direction == "^":
        santa_location = (santa_location[0], santa_location[1] + 1)
    elif direction == "v":
        santa_location = (santa_location[0], santa_location[1] - 1)
    elif direction == ">":
        santa_location = (santa_location[0] + 1, santa_location[1])
    elif direction == "<":
        santa_location = (santa_location[0] - 1, santa_location[1])
        
    # Add the new location to the set of visited houses
    visited_houses_santa.add(santa_location)

# Loop through the directions for Robo-Santa
for direction in robo_santa_directions:
    # Update Robo-Santa's location based on the direction
    if direction == "^":
        robo_santa_location = (robo_santa_location[0], robo_santa_location[1] + 1)
    elif direction == "v":
        robo_santa_location = (robo_santa_location[0], robo_santa_location[1] - 1)
    elif direction == ">":
        robo_santa_location = (robo_santa_location[0] + 1, robo_santa_location[1])
    elif direction == "<":
        robo_santa_location = (robo_santa_location[0] - 1, robo_santa_location[1])

    # Add the new location to the set of visited houses
    visited_houses_robo_santa.add(robo_santa_location)

# Combine the two sets of visited houses and count the number of unique houses
unique_houses = len(visited_houses_santa.union(visited_houses_robo_santa))

# Print the number of unique houses that received at least one present
print(unique_houses)


