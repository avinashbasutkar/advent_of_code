#  Open the text file in read mode
with open("day3_input.txt", "r") as file:
    # Read the contents of the file into a string
    directions = file.read()

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
