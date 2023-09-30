import time

class Skill:
    def __init__(self, owner):
        self.owner = owner
        self.last_used_time = 0

    def can_use(self):
        """Check if the skill is off cooldown."""
        return time.time() - self.last_used_time >= self.cooldown

    def use(self, *args, **kwargs):
        """Use the skill. To be overridden by subclasses."""
        self.last_used_time = time.time()

    def update(self):
        """Update the skill's state. To be overridden by subclasses."""
        pass
