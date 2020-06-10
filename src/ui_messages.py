# Please note, player creation messages are contained in setup.py.
# This is because the player object is set up before UI_Messages.
# The player object needs to be created before UI_Messages so that
# UI_Messages can display player data.

class UI_Messages:
    def __init__(self, player):
        self.player = player

    def user_input(self):
        return input("\nWhat would you like to do? ")

    def player_status_message(self):
        print(f"\n   You're in the {self.player.current_room.name}.")

    def room_status_message(self):
        print(f"   {self.player.current_room.description}")

    def quit_message(self):
        print(f"\nThank you for playing, {self.player.name}!\n")

    def invalid_direction_message(self):
        print(f"\n   Can't go that way...")

    def invalid_command_message(self):
        print(f"\n   Nope, that didn't work. Please enter a valid command.")

    def menu(self):
        menu = (
            "\n   n: go north",
            "   e: go east",
            "   s: go south",
            "   w: go west",
            "   q: quit the game"
        )
        for i in menu:
            print(i)
