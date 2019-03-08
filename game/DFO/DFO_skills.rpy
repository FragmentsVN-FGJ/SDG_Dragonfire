init -95 python:
    class PoisonStatus(StatusEffect):
        """docstring for PoisonStatus"""
        def __init__(self, host, turns):
            super(PoisonStatus, self).__init__("poison", host, turns=turns)

        # does poison damage at the end of the turn
        def on_end_turn(self):
            self.host.take_damage(damage[poison], damage_type="poison")
            super(PoisonStatus, self).on_end_turn()

    class SleepStatus(StatusEffect):
        """docstring for SleepStatus"""
        def __init__(self, host, turns=2):
            super(SleepStatus, self).__init__("sleep", host, turns=turns, damage_taken_modifier=2)

        def on_start_turn(self):
            if self.turns > 0:
                return False
            return True

        """ should remove itself after the first attack..
            this is not really the neatest way to achieve this but whatever...
        """
        def on_defense(self, enemy):
            if self.turns <= -1:
                self.remove()
            self.turns = -1

    class HidingStatus(StatusEffect):
        """docstring for HidingStatus"""
        def __init__(self, host, turns=5):
            super(HidingStatus, self).__init__("hide", host, turns=turns, damage_dealt_modifier=2)

        def on_attack(self):
            self.remove()

    class BrokenStatus(StatusEffect):
        """docstring for BrokenStatus"""
        def __init__(self, host):
            super(BrokenStatus, self).__init__("broken", host, turns=0)

        def on_end_turn(self):
            pass

    class BarrierStatus(StatusEffect):
        """docstring for BarrierStatus"""
        def __init__(self, host, turns=5):
            super(BarrierStatus, self).__init__("barrier", host, turns=turns, magical_defense_modifier=2)

    class ShieldStatus(StatusEffect):
        """docstring for ShieldStatus"""
        def __init__(self, host, turns=5, damage=100):
            super(ShieldStatus, self).__init__("shield", host, turns=turns, physical_defense_modifier=2)

        def on_defense(self, enemy):
            enemy.take_damage(self.host.attack*damage, damage_type="physical")
            self.remove()

    pass
