from room import Room
from helper_functions import get_key


# A class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory, ui_messages=None):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        self.ui_messages = ui_messages

    def __str__(self):
        return f"{self.name} is in the {self.current_room.name}."

    def __repr__(self):
        return f"self.name: {self.name} ; self.current_room: {self.current_room}."

    def move(self, link_to_room):
        # if a link exists to the room, set the current_room to that room
        if link_to_room:
            self.current_room = link_to_room
        # if the link doesn't exist, display an error message
        else:
            self.ui_messages.invalid_direction_message()

    def take(self, item_name, item_list, room):
        if [x for x in self.inventory if x.lower() == item_name.lower()]:
            self.ui_messages.item_in_possession_message()
        else:
            key = get_key(self.current_room, room)
            if item_name in room[key].inventory:
                self.inventory.append(item_name.lower())
                room[key].remove_item(item_name)
            else:
                self.ui_messages.item_not_in_area_message()

    def look_at_item(self, item_name, item_list):
        if [x for x in self.inventory if x.lower() == item_name.lower()]:
            self.ui_messages.item_info_message(item_list[item_name])
        else:
            self.ui_messages.item_not_found_message()

    def drop(self, item_name, item_list, room):
        if [x for x in self.inventory if x.lower() == item_name.lower()]:
            self.inventory.remove(item_name.lower())
            key = get_key(self.current_room, room)
            room[key].add_item(item_name)
        else:
            self.ui_messages.item_not_found_message()

    def check_inventory(self):
        if len(self.inventory) == 0:
            self.ui_messages.no_inventory_message()
        else:
            self.ui_messages.print_inventory(self.inventory)
