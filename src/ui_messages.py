from helper_functions import get_key

# Please note, player creation messages are contained in setup.py.
# This is because the player object is set up before UI_Messages.
# The player object needs to be created before UI_Messages so that
# UI_Messages can display player data.


class UI_Messages:
    def __init__(self, player):
        self.player = player

    ################################################################
    # Player Command Prompt
    def user_input(self):
        return input("\nWhat would you like to do? ").split(" ")

    ################################################################
    # Player and Room Status
    def player_status_message(self):
        print(f"\n   You're in the {self.player.current_room.name}.")

    def room_status_message(self, room):
        key = get_key(self.player.current_room, room)
        print(f"   {self.player.current_room.description}")
        print(f"   {room[key].inventory}")

    ################################################################
    # Quit Game
    def quit_message(self):
        print(f"\nThank you for playing, {self.player.name}!\n")

    ################################################################
    # Invalid Commands
    def invalid_direction_message(self):
        print(f"\n   Can't go that way...")

    def invalid_command_message(self):
        print(f"\n   Nope, that didn't work. Please enter a valid command.")

    ################################################################
    # Inventory
    def no_inventory_message(self):
        print(f"\n   Your inventory is empty.")

    def print_inventory(self, inventory):
        print("\n   Inventory:\n")
        for i in inventory:
            print(f"   - {i}")

    def item_not_found_message(self):
        print(f"\n   Item not found in your inventory.")

    def item_info_message(self, item):
        print(f"\n   {item}")

    def drop_item_error_message(self):
        print(f"\n   You must specify an item to drop.")

    def take_item_error_message(self):
        print(f"\n   You must specify an item to take.")

    def item_in_possession_message(self):
        print(f"\n   That item is already in your possession.")

    def item_not_in_area_message(self):
        print(f"\n   That item isn't in this area.")

    ################################################################
    # Help Menu
    def menu(self):
        menu = (
            "\n   n: go north",
            "   e: go east",
            "   s: go south",
            "   w: go west",
            "   l object: look at object",
            "   t object: take object",
            "   d object: drop object",
            "   u object on object: use object on object",
            "   i: check inventory",
            "   q: quit the game"
        )
        for i in menu:
            print(i)
