init -95 python:
    class PoisonStatus(StatusEffect):
        """docstring for PoisonStatus"""
        def __init__(self, host, turns):
            super(PoisonStatus, self).__init__("poison", host, turns=turns)

        # does poison damage at the end of the turn
        def on_end_turn(self):
            self.host.take_damage(damage[poison])
            self.turns -= 1
            if self.turns == 0:
                self.remove()

    class SleepStatus(StatusEffect):
        """docstring for SleepStatus"""
        def __init__(self, host, turns=2):
            super(SleepStatus, self).__init__("sleep", host, turns=turns, damage_taken_modifier=2)

        def on_start_turn(self):
            return False


    pass
