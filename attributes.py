class Attributes:
    def __init__(self):
        self.health = 100
        self.mana = 100
        self.move_speed = 0.025
        self.attack_power = 10
        self.spell_power = 10
        self.defense = 5
        self.cast_speed = 1
        self.attack_speed = 1
        
        # Add more attributes as needed

    def modify_attribute(self, attribute_name, value):
        if hasattr(self, attribute_name):
            setattr(self, attribute_name, value)

    def get_attribute(self, attribute_name):
        return getattr(self, attribute_name, None)

