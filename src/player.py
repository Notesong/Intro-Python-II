# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} is in the {self.position.name}."

    def __repr__(self):
        return f"self.name: {self.name} ; self.position: {self.position}."
