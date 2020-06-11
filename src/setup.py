from room import Room
from player import Player
from item import Item


################################################################
# item_setup
#
# Generates all items

def item_setup():
    item = {
        'key': Item("Key", "An old key burnished over time."),

        'flashlight': Item("Flashlight", "A heavy duty flashlight from the hardware store."),

        'chest': Item("Chest", "Despite its age, it's still firmly intact."),

        'necklace': Item("Necklace", "You recognize it from an old painting in your grandmother's house."),

        'stone': Item("Stone", "Just an ordinary piece of rock."),
    }

    return item


################################################################
# room_setup
#
# Makes all the rooms that are available in the game

def room_setup(item):

    # Declare all the rooms
    room = {
        'outside':  Room("Outside Cave Entrance",
                         """North of you, the cave mount beckons.""",
                         []),

        'foyer':    Room("Foyer",
                         """Dim light filters in from the south. Dusty passages run 
   north and east.""",
                         []),

        'overlook': Room("Grand Overlook",
                         """A steep cliff appears before you, falling into the darkness. 
   Ahead to the north, a light flickers in the distance, but 
   there is no way across the chasm.""",
                         []),

        'narrow':   Room("Narrow Passage",
                         """The narrow passage bends here from west to north. The smell
   of gold permeates the air.""",
                         []),

        'treasure': Room("Treasure Chamber",
                         """You've found the long-lost treasure chamber! Sadly, it has 
   already been completely emptied by earlier adventurers. The 
   only exit is to the south.""",
                         []),
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


def player_setup(room, item):

    player_name = []

    while True:
        player_name = input("\nWhat is your name, adventurer? ")
        if len(player_name) > 10:
            print("Sorry, your name cannot be longer than 10 characters.")
        elif len(player_name) == 0:
            print("You must enter a player name.")
        else:
            break

    current_inventory = [
        item['flashlight'].name.lower(),
        item['key'].name.lower()
    ]

    player = Player(
        name=player_name,
        current_room=room['outside'],
        inventory=current_inventory,
    )

    print(
        f"\nGood to meet you, {player.name}! I have a feeling I'll remember\nthat name for years to come.")
    print(f"\n   (Enter 'h' at any time to see what you can do.)")

    return player
