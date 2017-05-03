init -99 python:
    class Gamestate(store.object):
        """ docstring for Gamestate
            All variables related to battles that are just laying around should be moved here
        """
        battle_label = "Ruins_battle1"

        def __init__(self):
            super(Gamestate, self).__init__()
            self.players = {}
            self.enemies = {}

        def init_battle(self):
            self.turn_number = 0
            for name in self.players:
                player = self.players[name]
                player.full_heal()
            for name in self.enemies:
                enemy = self.enemies[name]
                enemy.full_heal()

        def add_player(self, player, name):
            self.players[name] = player
        def add_enemy(self, enemy):
            self.enemies[enemy.name] = enemy

        """ removes participant BattleParticipant from battle if it exists on either side
        """
        def remove(self, participant):
            if participant in self.players:
                del self.players[participant]
            elif participant in self.enemies:
                del self.enemies[participant]
        """ wins battle and returns or jumps or something
        """
        def win():
            pass

        """ loses battle and returns or sth
        """
        def lose():
            pass

        """ shows choice menu to choose target enemy if more than one possible target
            returns target BattleParticipant or None
        """
        def target_enemy(self):
            target_group = self.enemies
            if len(target_group) > 1:
                target = menu([(enemy, enemy) for enemy in target_group])
            elif  len(target_group) == 1:
                for enemy in target_group:
                    target = enemy
            else:
                return None
            return target_group[target]


    class BattleParticipant(store.object):
        """ docstring for BattleParticipant
            Any entity that can participate in battles
            contains stats used for battles

            name String name shown in the status panel
            skills Skill[] list of all skills character can use     # not used
            death_label String name of label to call on death       # not used

            max_hp Int maximum health points
            max_mp Int maximum mana points
            level Int current level
            xp Int xp towards the next level
            physical_defense Int physical defense multiplier, 0 immune to physical, 1: no extra armour
            magical_defense Double multiplier for magic damage taken, 0: immune to magic, 1: magic does normal damage
            evasion Double default dodge chance added to dodge checks, 0: no dodge, 1: dodge about everything
            attack Int attack related stat, for damage etc
            critical_player Boolean killing this character will end the battle  # not used

            The stats displayed on the gui are taken from here
        """
        def __init__(   self,
                        name,
                        skills,
                        death_label,
                        hp=100,
                        mp=100,
                        level=90,
                        xp=0,
                        physical_defense=0,
                        magical_defense=0,
                        evasion=0,
                        attack=0,
                        critical_player=False,
                        *args, **kwargs):

            super(BattleParticipant, self).__init__()
            self.name = name

            self.max_hp = hp
            self.max_mp = mp
            self.hp = hp
            self.mp = mp

            self.xp = xp
            self.level = level
            self.max_xp = self.get_xp_cap()

            self.physical_defense = physical_defense
            self.magical_defense = magical_defense
            self.attack = attack
            self.critical_player = critical_player

            self.status_effects = []

        def full_heal(self):
            self.hp = self.max_hp
            self.mp = self.max_mp

        def heal(self, amount):
            self.hp += amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp

        def take_damage(self, amount):
            status_mod = reduce(lambda a,b: a.damage_taken_modifier * b, self.status_effects, 1)
            self.hp -= ceil(amount * self.physical_defense * status_mod)
            if self.hp <= 0:
                self.die()

        def die(self):
            gamestate.remove(self.name)
            #renpy.call(gamestate.battle_label+".death", self.name) # will use the .death local death label
            renpy.call(self.death_label)

        def end_turn(self):
            for status_effect in self.status_effects:
                status_effect.end_turn()

        """ Called when the unit begins their turn
            enemies need to be subclassed to have ai pick their targets and
            calls start turn for all status effects
            shows choice menu for skills
            picks target or shows a choice menu for choosing target
            calls skill call_label
        """ #TODO make it possible to return from choosing target?
        def start_turn(self):
            for status_effect in self.status_effects:
                status_effect.start_turn()
            # filter skills that can be used and map them to tuples
            choices = [skill.get_menu_tuple() for skill in skills if skill.can_be_used(self)]
            skill = renpy.display_menu(choices)
            target = skill.target()
            renpy.call(skill.call_label, self, target, skill)

        def clear_effects(self):
            self.status_effects = set()

        """ Adds xp and checks if there is enough xp to level up
            will only check for one level,
            assuming the amount of xp added is much less than xp limit,
            add while loop to check for more than one level
        """
        def add_xp(self, amount):
            self.xp += amount
            if self.xp > self.max_xp:
                self.level += 1
                self.level_up()
                self.xp -= self.max_xp
                self.max_xp = self.get_xp_cap()

        """ Calculates an xp amount required to level up
        """
        def get_xp_cap(self):
            lev = 10 * self.level               # 10 per level, 900 at 90
            diff = max(0, 5*(self.level-30))    # 0 until lv 30, after which 5 per level, 300 at 90
            base = 5 * self.level + 100         # 5 per level + 100, 550 at 90
            return (lev + diff) * base          # N^2 growth, 660000 at 90, 674325 at 91

        """ Increases all stats by 1% or 1
        """
        def level_up(self):
            self.p_def += max(1, int(self.p_def*0.01))
            self.m_def += max(1, int(self.m_def*0.01))
            self.attack += max(1, int(self.attack*0.01))


    class StatusEffect(store.object):
        """ docstring for StatusEffect
            superclass for status effects,
            all status effects should be subclassed from this class

            name String the type of the effect
            host BattleParticipant the character the effect is applied on
            turns Int tells the amount of turns the effect lasts
            positive Boolean tells whether effect is seen as debuff or buff
            modifiers Double multiply the described stat

            Adds itself to the host when created
        """
        def __init__(   self,
                        name,
                        host,
                        turns = 2,
                        positive = False,
                        p_def_modifier = 1,
                        m_def_modifier = 1,
                        attack_modifier = 1,
                        damage_taken_modifier = 1,
                        damage_caused_modifier = 1):
            super(StatusEffect, self).__init__()
            self.name = name
            self.positive = positive

            self.p_def_mod = p_def_modifier
            self.m_def_mod = m_def_modifier
            self.attack_mod = attack_modifier
            self.dmg_caused_mod = damage_caused_modifier
            self.dmg_taken_mod = damage_taken_modifier

            self.turns = turns
            self.host = host
            self.add_for(host)

        """ called when the character turn ends
            now that I think of it, this might bug if there are multiple status effects and one is removed
            if sth like that appears maybe a copied version of the status effects should be used when iterating over it
            the same might happen on any other version of the
        """
        def on_end_turn(self):
            self.turns -= 1
            if self.turns == 0:
                self.remove()

        """ called at the beginning of a turn
            returns True if player can act on the turn, False if player can't
        """
        def on_start_turn(self):
            return True

        """ called when the character is attacked
            e.g. if the effect can block one attack or sth?
            TODO add some way for these to actually block attacks?
        """
        def on_defense(self):
            pass

        """ called when the character attacks
            e.g. if the effect can block one attack or sth
        """
        def on_attack(self):
            pass

        """ Removes itself from its host and lets hope garbage collection does its job
        """
        def remove(self):
            self.host.status_effects.remove(self)
            dfo_narrator(self.host.name + " has no longer status: " + self.name)

        """ Adds itself to the host character, and writes a piece of dialogue describing the effect
            called when the status is first applied to a character
            should not be called outside __init__
        """
        def add_for(self, host):
            host.status_effects += self
            dfo_narrator(host.name + " got status: "+ self.name) #TODO add dfo_narrator character with the dfo say panel bg


    class Skill(store.object):
        """ docstring for Skill
            Superclass for skills

            name String skill name shown in choice menu
            call_label String label to be called when using the skill, parameters user, target, skill
            mp_cost Int amount of mp required to use the skill

            TODO use multiple inheritance instead of simply reclassing for functions?
        """
        def __init__(self, name, call_label, mp_cost=0):
            super(Skill, self).__init__()
            self.name = name
            self.call_label = call_label

        """ returns (String, Skill) tuple for the battleparticipant
            to use in a menu
        """
        def get_menu_tuple(self):
            return (self.name, self)

        """ shows choice menu to choose target enemy if more than one possible target
            override if skill targets allies or all enemies at once
            returns target BattleParticipant or None
        """
        def target(self):
            return gamestate.target_enemy()

        #""" user uses the skill on target
        #    calls label defined in call label, with user target and this skill as parameters
        #"""
        #def use(self, user, target):
        #    renpy.call(self.call_label, user, target, self)

        """ Checks if the skill can be used by user
            Override in a subclass if it uses charges or sth instead
        """
        def can_be_used(self, user):
            return user.mp > self.mp_cost
