"""Documentation about the zdd_adventure module."""
class Game:
    def __init__(self):
        self.inventory = ["Stundenausweis"]
        self.events = []
        self.drunken = False
        
    def start(self):
        pass

    def make_choice(self, choices):
        # input()
        if self.drunken:
            pass
        pass
    
    
class Floor:  # maybe not needed?
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        

class Room:
    def __init__(self, name,
                 items=[], 
                 story=["Nur ein langweiliger Raum.",
                        "Wow... immer noch langweilig."]):
        self.name = name
        self.items = items
        self.story = story
        self.visited = 0
        
    def enter_room(self):#, story_function):
        if self.visited == 0:
            print(self.story[0])
        else:
            print(self.story[1])
        self.visited += 1

    def look_around(self):
        print("Einmal umschauen....")
        for item in self.items:
            item.describe()
        
class Item:
    def __init__(self, name,
                 description,
                 portable=False):
        self.name = name
        self.description = description
        self.portable = portable
        
    def describe(self):
        print(self.description)
        
    def interact(self):#, interaction_pattern):
        pass
    
    def take(self):
        if self.portable:
            print(f"{self.name} wurde ins Inventar aufgenommen.")
            return self
        return None
