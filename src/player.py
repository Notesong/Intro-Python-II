# A class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

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
            print(f"\n   Can't go that way...")
