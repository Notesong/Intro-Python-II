from player import Player
from setup import item_setup, room_setup, player_setup
from ui_messages import UI_Messages


################################################################
# Main
#
# The main game loop for the text adventure game.

def main():
    # Setup the items
    item = item_setup()
    # Setup the room
    room = room_setup(item)
    # Setup the player
    player = player_setup(room, item)
    # Setup the UI messages
    ui_messages = UI_Messages(player)
    # Set ui_messages in the player so it can be accessed there
    player.ui_messages = ui_messages
    # Set the current user input to -1
    choice = -1

    while True:
        # Prints the current room name
        ui_messages.player_status_message()
        # Prints the current room description
        ui_messages.room_status_message(room)
        # Waits for user input and decides what to do
        choice = ui_messages.user_input()
        choice[0] = choice[0].lower()
        try:
            # If the user enters "q", quit the game
            if (choice[0] == 'q'):
                ui_messages.quit_message()
                break
            # If the user enters "h", display the help menu
            elif (choice[0] == 'h'):
                ui_messages.menu()
            # If the user enters a cardinal direction, attempt to move to the room there
            # Print an error message if the movement isn't allowed
            elif (choice[0] == 'n'):
                player.move(player.current_room.n_to)
            elif (choice[0] == 'e'):
                player.move(player.current_room.e_to)
            elif (choice[0] == 's'):
                player.move(player.current_room.s_to)
            elif (choice[0] == 'w'):
                player.move(player.current_room.w_to)
            # Take an object
            elif (choice[0] == 't'):
                if len(choice) == 1:
                    ui_messages.take_item_error_message()
                elif len(choice) == 2:
                    player.take(choice[1], item, room)
            # Look at an object
            elif (choice[0] == 'l'):
                if len(choice) == 1:
                    print('')
                    ui_messages.room_status_message(room)
                elif len(choice) == 2:
                    player.look_at_item(choice[1], item)
            # Drop an object
            elif (choice[0] == 'd'):
                if len(choice) == 1:
                    ui_messages.drop_item_error_message()
                elif len(choice) == 2:
                    player.drop(choice[1], item, room)
            # Check inventory
            elif (choice[0] == 'i'):
                player.check_inventory()
            # Use an object on an object
            elif (choice[0] == 'u'):
                pass
            else:
                ui_messages.invalid_command_message()
        except ValueError:
            ui_messages.invalid_command_message()


main()
