import time

class SkillHandler:
    def __init__(self, owner):
        self.owner = owner
        self.skills = owner.skills  # Use the skills already initialized in the Player class

    def add_skill(self, skill_name, skill_instance):
        self.skills[skill_name] = skill_instance

    def use_skill(self, skill_name, screen, *args, **kwargs):
        if skill_name in self.skills and self.skills[skill_name].can_use():
            self.skills[skill_name].use(screen, *args, **kwargs)
            
    def handle_input(self, keys, screen, mouse_pos, screen_center):
        for hotkey, skill_name in self.owner.hotkeys.items():
            if keys[hotkey]:
                dx = mouse_pos[0] - screen_center[0]
                dy = mouse_pos[1] - screen_center[1]
                self.use_skill(skill_name, screen, (self.owner.x, self.owner.y), (self.owner.x + dx, self.owner.y + dy))

    def update_skills(self):
        for skill in self.skills.values():
            skill.update()
             