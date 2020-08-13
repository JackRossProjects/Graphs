from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

'''
YOUR CODE HERE
'''

# Initialize visited dicr
visited = {}

# Initialize exit path
exit_path = []

# Dict containing inverse of cardinal directions
inverse_direction = {"n":"s", "e":"w", "s":"n", "w":"e"}

# Add starting room to visited dict
visited[player.current_room.id] = player.current_room.get_exits()

# While all the rooms have not been visited
while len(visited) < len(room_graph):
    # If the player is in a new room
    if player.current_room.id not in visited:
        # add room to visited dict
        visited[player.current_room.id] = player.current_room.get_exits() 
        # Add the last value in exit path to directions
        direction = exit_path[-1]
        # then remove the direction you came from
        visited[player.current_room.id].remove(direction)
    # in a room with exhausted directions:
    if len(visited[player.current_room.id]) == 0:
        # Remove the exit path step we just moved
        direction = exit_path.pop()
        # Add that direction to the traversal path
        traversal_path.append(direction)
        # Go back to the room you came from
        player.travel(direction)
    else:
    # in a room with unexplored directions:
        # remove the direction you will go from the room
        direction = visited[player.current_room.id].pop()
        # Append the new direction to the traversal path
        traversal_path.append(direction)
        # Append the opposite direction we came in to the exit path
        exit_path.append(inverse_direction[direction])
        # Travel in an unexplored direction
        player.travel(direction)

'''
YOUR CODE ENDS
'''

# TRAVERSAL TEST
visited = set()
player.current_room = world.starting_room
visited.add(player.current_room)

# get the first room and exits added to the visited
#

for move in traversal_path:
    player.travel(move)
    visited.add(player.current_room)

if len(visited) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
'''
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
'''