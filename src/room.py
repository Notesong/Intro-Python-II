# A class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, inventory, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to

    def __str__(self):
        return f"str: {self.name}: {self.description}"

    def __repr__(self):
        return f"\n\nself.name: {self.name}\nself.description: {self.description}\nself.inventory: {self.inventory}\nnself links:\n  n: {self.n_to}\n  e: {self.e_to}\n  s: {self.s_to}\n  w: {self.w_to}"

    # Add item to the room's inventory
    def add_item(self, item):
        print(self.inventory)
        self.inventory.append(item)

    # Remove item from the room's inventory
    def remove_item(self, item):
        self.inventory.remove(item)
