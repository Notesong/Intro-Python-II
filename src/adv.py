from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", n_to=[], e_to=[], s_to=[], w_to=[]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
   passages run north and east.""", n_to=[], e_to=[], s_to=[], w_to=[]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
   into the darkness. Ahead to the north, a light flickers in
   the distance, but there is no way across the chasm.""", n_to=[], e_to=[], s_to=[], w_to=[]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
   to north. The smell of gold permeates the air.""", n_to=[], e_to=[], s_to=[], w_to=[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
   chamber! Sadly, it has already been completely emptied by
   earlier adventurers. The only exit is to the south.""", n_to=[], e_to=[], s_to=[], w_to=[]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

choice = -1
error_message = f"\n   Nope, that didn't work. Please enter a valid command."

# Make a new player object that is currently in the 'outside' room.
player_name = input("What is your name, adventurer? ")
player = Player(name=player_name, current_room=room['outside'])
print(
    f"\nGood to meet you, {player.name}! I have a feeling I'll remember that name for years to come.")
print(f"\n   (Enter 'h' at any time to see what you can do.)")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    print(f"\n   You're in the {player.current_room.name}")
    print(f"   {player.current_room.description}")
    choice = input(
        "\nWhat would you like to do? ")
    try:
        if (choice == 'q'):
            print(f"\nThank you for playing, {player.name}!\n")
            break
        elif (choice == 'h'):
            print(
                f"\n n: go north\n e: go east\n s: go south\n w: go west\n q: quit the game")
        elif (choice == 'n'):
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
        elif (choice == 'e'):
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
        elif (choice == 's'):
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
        elif (choice == 'w'):
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
        else:
            print(error_message)
    except ValueError:
        print(error_message)
