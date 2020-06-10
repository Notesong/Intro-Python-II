# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to, e_to, s_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return f"\n\nself.name: {self.name}\nself.description: {self.description}\nself links:\n  n: {self.n_to}\n  e: {self.e_to}\n  s: {self.s_to}\n  w: {self.w_to}"
