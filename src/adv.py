from player import Player
from setup import room_setup, player_setup
from ui_messages import UI_Messages


################################################################
# Main
#
# The main game loop for the text adventure game.

def main():

    room = room_setup()
    player = player_setup(room)
    ui_messages = UI_Messages(player)
    choice = -1

    while True:
        # * Prints the current room name
        # * Prints the current description (the textwrap module might be useful here).
        # * Waits for user input and decides what to do.
        ui_messages.player_status_message()
        ui_messages.room_status_message()
        choice = ui_messages.user_input()
        try:
            # If the user enters "q", quit the game.
            if (choice == 'q'):
                ui_messages.quit_message()
                break
            # If the user enters "h", display the help menu
            elif (choice == 'h'):
                ui_messages.menu()
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
                ui_messages.invalid_command_message()
        except ValueError:
            ui_messages.invalid_command_message()


main()
