from room import Room
from player import Player

################################################################
# room_setup
#
# Makes all the rooms that are available in the game


def room_setup():
    # Declare all the rooms

    room = {
        'outside':  Room("Outside Cave Entrance",
                         """North of you, the cave mount beckons.""",
                         n_to=[], e_to=[], s_to=[], w_to=[]),

        'foyer':    Room("Foyer",
                         """Dim light filters in from the south. Dusty passages run 
   north and east.""",
                         n_to=[], e_to=[], s_to=[], w_to=[]),

        'overlook': Room("Grand Overlook",
                         """A steep cliff appears before you, falling into the darkness. 
   Ahead to the north, a light flickers in the distance, but 
   there is no way across the chasm.""",
                         n_to=[], e_to=[], s_to=[], w_to=[]),

        'narrow':   Room("Narrow Passage",
                         """The narrow passage bends here from west to north. The smell
   of gold permeates the air.""",
                         n_to=[], e_to=[], s_to=[], w_to=[]),

        'treasure': Room("Treasure Chamber",
                         """You've found the long-lost treasure chamber! Sadly, it has 
   already been completely emptied by earlier adventurers. The 
   only exit is to the south.""",
                         n_to=[], e_to=[], s_to=[], w_to=[]),
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

    return room


################################################################
# player_setup
#
# Makes a new player object that is currently in the 'outside' room.

def player_setup(room):

    player_name = []

    while True:
        player_name = input("\nWhat is your name, adventurer? ")
        if len(player_name) > 10:
            print("Sorry, your name cannot be longer than 10 characters.")
        elif len(player_name) == 0:
            print("You must enter a player name.")
        else:
            break

    player = Player(name=player_name, current_room=room['outside'])

    print(
        f"\nGood to meet you, {player.name}! I have a feeling I'll remember\nthat name for years to come.")
    print(f"\n   (Enter 'h' at any time to see what you can do.)")

    return player
