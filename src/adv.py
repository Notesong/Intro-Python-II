from player import Player
from setup import room_setup, player_setup


################################################################
# Main
#
# The main game loop for the text adventure game.

def main():

    room = room_setup()
    player = player_setup(room)
    choice = -1
    error_message = f"\n   Nope, that didn't work. Please enter a valid command."
    menu = (
        "\n   n: go north",
        "   e: go east",
        "   s: go south",
        "   w: go west",
        "   q: quit the game"
    )

    while True:
        # * Prints the current room name
        # * Prints the current description (the textwrap module might be useful here).
        # * Waits for user input and decides what to do.
        print(f"\n   You're in the {player.current_room.name}.")
        print(f"   {player.current_room.description}")
        choice = input(
            "\nWhat would you like to do? ")
        try:
            # If the user enters "q", quit the game.
            if (choice == 'q'):
                print(f"\nThank you for playing, {player.name}!\n")
                break
            # If the user enters "h", display the help menu
            elif (choice == 'h'):
                for i in menu:
                    print(i)
            # If the user enters a cardinal direction, attempt to move to the room there.
            # Print an error message if the movement isn't allowed.
            elif (choice == 'n'):
                player.move(player.current_room.n_to)
            elif (choice == 'e'):
                player.move(player.current_room.e_to)
            elif (choice == 's'):
                player.move(player.current_room.s_to)
            elif (choice == 'w'):
                player.move(player.current_room.w_to)
            else:
                print(error_message)
        except ValueError:
            print(error_message)


main()
