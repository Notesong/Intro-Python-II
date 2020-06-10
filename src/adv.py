from player import Player
from setup import room_setup, player_setup
from ui_messages import UI_Messages


################################################################
# Main
#
# The main game loop for the text adventure game.

def main():
    # Setup the room
    room = room_setup()
    # Setup the player
    player = player_setup(room)
    # Setup the UI messages
    ui_messages = UI_Messages(player)
    # Set the current user input to -1
    choice = -1

    while True:
        # Prints the current room name
        ui_messages.player_status_message()
        # Prints the current room description
        ui_messages.room_status_message()
        # Waits for user input and decides what to do.
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
                player.move(player.current_room.n_to, ui_messages)
            elif (choice == 'e'):
                player.move(player.current_room.e_to, ui_messages)
            elif (choice == 's'):
                player.move(player.current_room.s_to, ui_messages)
            elif (choice == 'w'):
                player.move(player.current_room.w_to, ui_messages)
            else:
                ui_messages.invalid_command_message()
        except ValueError:
            ui_messages.invalid_command_message()


main()
