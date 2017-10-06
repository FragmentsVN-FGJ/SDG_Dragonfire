label DFO_character_init:
    $ nick_skills = []

    # Bugs when reloading???
    $ nick = BattleParticipant("Nicholas", "nick", nick_skills, "nickdeath",
        hp= 6736, mp= 2350,
        physical_defense= 0.3,
        magical_defense= 0.6,
        attack= 1,
        critical_player=True)
    $ air = BattleParticipant("Aerith4ever", "air", nick_skills, "airdeath",
        hp= 2141, mp= 5941,
        physical_defense= 0.8,
        magical_defense= 0.3,
        attack= 1.25)
    $ sil = BattleParticipant("Silvia", "sil", nick_skills, "airdeath",
        hp= 2704, mp= 2825,
        physical_defense= 0.6,
        magical_defense= 0.6,
        evasion= 0.2,
        attack= 2)

    $ rider = BattleParticipant("Elite Rider", "bird", nick_skills, "riderdeath",
        hp= 8603, mp= 3419,
        physical_defense= 0.6,
        magical_defense= 0.6,
        evasion= 0.2,
        attack= 2)

    $ gamestate = Gamestate()
    $ gamestate.players = {'Nick':nick, 'Silvia':sil, 'Aerith':air}
    $ gamestate.enemies = {'Rider':rider}

#python:
    #def set_nick_nick(name):
        #nick_skills = []

        #nick = BattleParticipant(name, nick_skills, "nickdeath",
        #    hp= 6736, mp= 2350,
        #    physical_defense= 0.3,
        #    magical_defense= 0.6,
        #    attack= 1,
        #    critical_player=True)
        #gamestate.players["Nick"].name = name # this does not work, or maybe it does?
        #gamestate.add_player(nick, "Nick")
