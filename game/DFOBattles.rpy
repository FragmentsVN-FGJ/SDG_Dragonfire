init:
    define sfx_battlecry = "bgm/SFX_battlecry.mp3"
    define sfx_battlecry_f = "bgm/SFX_battlecry_f.mp3"
    define sfx_battlehorn = "bgm/SFX_Battlehorn_sinister.mp3"
    define sfx_fire = "bgm/SFX_fire.mp3"
    define sfx_running = "bgm/SFX_Footsteps_grass.mp3"
    define sfx_potion = "bgm/SFX_Drink_potion.mp3"
    define sfx_heal= "bgm/SFX_Heal_regen.mp3"
    define sfx_shield = "bgm/SFX_Raise_Shield.mp3"
    define sfx_collapse = "bgm/SFX_Rock_Collapse.mp3"
    define sfx_thump = "bgm/SFX_Rock_Thump.mp3"
    define sfx_block = "bgm/SFX_Hammer_hit_2.mp3"
    define sfx_critical = "bgm/SFX_Sword_hit_flesh.mp3"
    define sfx_critical_short = "bgm/SFX_Sword_hit_flesh_short.mp3"
    define sfx_hit = "bgm/SFX_Sword_hit.mp3"
    define sfx_hit_2 = "bgm/SFX_Sword_hit_2.mp3"
    define sfx_miss = "bgm/SFX_Sword_slash_8.mp3"
    define sfx_dagger = "bgm/SFX_Sword_hit_armor.mp3"

    define sfx_grunt_1 = "bgm/SFX_Grunt_1.mp3"
    define sfx_grunt_2 = "bgm/SFX_Grunt_2.mp3"
    define sfx_grunt_3 = "bgm/SFX_Grunt_3.mp3"
    define sfx_grunt_4 = "bgm/SFX_Grunt_4.mp3"
    define sfx_grunt_5 = "bgm/SFX_Grunt_5.mp3"
    define sfx_grunt_6 = "bgm/SFX_Grunt_6.mp3"
    define sfx_grunt_7 = "bgm/SFX_Grunt_7.mp3"
    define sfx_grunt_8 = "bgm/SFX_Grunt_8.mp3"
    define sfx_grunt_9 = "bgm/SFX_Grunt_9.mp3"
    define sfx_grunt_10 = "bgm/SFX_Grunt_angry_2.mp3"
    define sfx_grunt_1_f = "bgm/SFX_Grunt_1_f.mp3"
    define sfx_grunt_4_f = "bgm/SFX_Grunt_4_f.mp3"
    define sfx_grunt_5_f = "bgm/SFX_Grunt_5_f.mp3"
    define sfx_death_1 = "bgm/SFX_Grunt_pain_1.mp3"
    define sfx_death_2 = "bgm/SFX_Grunt_pain_2.mp3"

label Ruins_battle1:
    $ spear_broken = False
    $ rider_asleep = False
    $ rider_poisoned = False
    $ nick_defense = False
    $ blade_sphere_control = False
    $ light_barrier_active['Aerith'] = 0
    $ poison_counter["Rider"] = 0
    $ victorious = False
    $ playerparty = ["Nick", "Aerith", "Silvia"]
    $ playerdeath = False
    $ current_hp = {'Nick': max_hp['Nick'], 'Aerith': max_hp['Aerith'], 'Silvia': max_hp['Silvia'], 'Rider': max_hp['Rider']}
    $ current_mp = {'Nick': max_mp['Nick'], 'Aerith': max_mp['Aerith'], 'Silvia': max_mp['Silvia']}
    $ target_list = ["Rider"]
    $ nick_acted = False
    show screen hp_window(playerparty, target_list, current_hp, current_mp)
    play sound sfx_battlehorn
    "As we approach, trapdoors spring open all around us, sending sand flying in every direction!"
    show sil star
    s "It's an ambush! Hihihi!"
    hide sil
    play sound sfx_battlecry
    show enemy_chicken normal as enemy_chicken2 at left, gettingcloser with moveinbottom:
        yalign 1.0
    show enemy_swordchicken normal as enemy_chicken3 at right, gettingcloser with moveinbottom:
        yalign 1.0
    play sound sfx_battlecry_f
    hide enemy_chicken2 with moveoutleft
    show enemy_chicken normal as enemy_chicken4 at left, gettingcloser with moveinbottom:
        yalign 1.0
    hide enemy_chicken3 with moveoutright
    show enemy_chicken normal at gettingcloser with moveinbottom:
        yalign 1.0
        xalign 0.9

    "Through the sand I see the vague shapes of ostrich-riding warriors, screeching for battle!"
    show fx slash at flash
    show enemy_chicken hurt
    play sound sfx_critical
    pause 0.1
    show enemy_chicken normal
    pause 0.1
    show enemy_chicken hurt as enemy_chicken4
    play sound sfx_critical
    pause 0.1
    show enemy_chicken normal as enemy_chicken4
    hide fx slash
    hide enemy_chicken with moveoutbottom
    hide enemy_chicken4 with moveoutbottom
    show enemy_chicken normal at gettingcloser with moveinbottom:
        yalign 1.0
        xalign 0.9
        linear 1.0 xalign 0.6
    play music "bgm/Battle1.wav"
    show enemy_chicken normal at wigglemiddle
    "The fight rages on for a while, and we manage to finish off two of the warriors."
    "One more to go!"
    call .act_phase
    while not victorious and not playerdeath:
        # Needs to be this way around in order to avoid zombie attacks...
        call .start_round
        call .rider_turn
        if not playerdeath and not victorious:
            call .act_phase
    if playerdeath:
        hide screen hp_window
        return
    jump .victorious

label .start_round:
    if nick_acted:
        $ blade_sphere_control = False
        $ nick_defense = False
        $ nick_acted = False
    python:
        for person in light_barrier_active.keys():
            if light_barrier_active[person] > 0:
                light_barrier_active[person] -= 1
                if light_barrier_active[person] == 0:
                    #TODO add sound for light barrier ending, maybe heavily edited breaking glass?
                    renpy.say(None, "[person]'s light barrier wears off.")
        for person in poison_counter.keys():
            if poison_counter[person] > 0:
                renpy.call("Ruins_battle1.poison", person)

    return

label .poison(person):
    $ poison_counter[person] -= 1
    call .dealdamage(person, damage['poison'], False)
    if target_died:
        if person == "Rider":
            show enemy_chicken hurt
            pause 0.1
            show enemy_chicken
            hide enemy_chicken with moveoutbottom
            play sound sfx_grunt_10
            "The rider can't withstand the poison, and dies."
        else:
            "[person] dies from poisoning."
    else:
        if person == "Rider":
            show enemy_chicken hurt
            pause 0.1
            show enemy_chicken
            play sound sfx_grunt_8
            "The rider is hurt by the poison!"
        else:
            play sound sfx_grunt_9
            "[person] suffers due to the poison!"
    if poison_counter[person] == 0:
        "The poison wears off" #"The poisoning ceases."
    return

label .act_phase:
    menu:
        "Continue Blade Sphere Control" if target_list and blade_sphere_control:
            play sound sfx_shield
            "I keep my focus, waiting for the rider to make his move."
            return
        "Remain vigilant" if not target_list:
            jump .act_defend
        "Attack" if target_list:
            jump .act_attack
        "Techniques...":
            jump .act_techniques
        "Aerith..." if 'Aerith' in playerparty:
            jump .act_Aerith
        "Silvia..." if 'Silvia' in playerparty:
            jump .act_Silvia
        "Defend" if target_list:
            jump .act_defend
        #"KMS":
        #    call .death("Nick")
        #    jump .rider_turn
        #"Kill Aerith":
        #    call .death("Aerith")
        #    jump .rider_turn
        #"Wait":
        #    jump .rider_turn

    return

label .act_attack:
    # If len(target_list) > 1, multiple choice menu here.
    $ nick_acted = True
    if rider_asleep:
        "Now's my chance!"
        show fx slash at flash
        play sound sfx_critical
        pause 0.1
        hide fx slash
        "While the rider is fast asleep, I strike at the ostrich with my sword, severing its long neck!"
        show fx slash at flash
        play sound sfx_critical
        pause 0.1
        hide fx slash
        "Time to finish this! I raise my sword and plunge it into the rider's chest!" #TODO make the slash happen at the middle of the line instead of before
        hide enemy_chicken with moveoutbottom
        play sound sfx_grunt_9
        "His eyes shoot open just as he falls into death's icy grasp."
        $ victorious = True
        return
    "Readying my sword for a side slash, I charge full-speed toward the rider!"
    show fx slash at flash
    play sound sfx_miss
    pause 0.1
    hide fx slash
    $ i = renpy.random.random()
    if i <= 0.3:
        "However, using the speed of his mount to his advantage, he manages to evade my attack."
        return
    else:
        $ j = renpy.random.random()
        if j <= 0.05:
            play sound sfx_critical
            "Yes! A critical hit!"
            call .death("Rider")
        else:
            call .dealdamage("Rider", damage['Nick']['attack'])
            if not target_died:
                "He manages to evade my weapon, though I do succeed at landing a wound on his side."
            return
    $ victorious = True
    return

label .act_techniques:
    menu:
        "Furious Strike" if target_list and current_mp["Nick"] > mp_costs["Furious Strike"]:
            $ nick_acted = True
            $ current_mp["Nick"] -= mp_costs["Furious Strike"]
            "This technique requires me to close in on the attacker."
            "I run toward the rider, readying my blade!"
            np "Furious... Strike!"
            show fx slash at flash
            pause 0.1
            hide fx slash
            if rider_asleep:
                play sound sfx_critical
                show enemy_chicken hurt
                pause 0.1
                show enemy_chicken normal
                "Being asleep, he can't avoid my attack."
                call .death("Rider")
                return
            $ i = renpy.random.random()
            if i <= 0.7:
                # Test for spear_broken
                if not spear_broken:
                    play sound sfx_hit_2
                    "He raises his spear to parry my attack."
                    "My sword slams straight through it, shattering it in pieces!"
                    $ spear_broken = True
                    return
                show enemy_chicken hurt
                play sound sfx_critical
                pause 0.1
                show enemy_chicken normal
                play sound sfx_death_1
                "He raises the remnants of his spear, but my attack goes straight through them, his arm and his head."
                hide enemy_chicken with moveoutright
                play sound sfx_running
                "The ostrich, now carrying only a corpse severed in half, sees it best to escape."
                $ victorious = True
                return
            else:
                "Damn! His mount is too fast, and he dodges my incursion."
                return
        "Blade Sphere Control" if current_mp["Nick"] > mp_costs["Blade Sphere Control"] and not blade_sphere_control:
            $ current_mp["Nick"] -= mp_costs["Blade Sphere Control"]
            "I close my eyes to find internal peace."
            play sound sfx_shield
            np "Blade Sphere Control!"
            show overlay lightblue
            "Let's see him get through this technique!"
            hide overlay lightblue #TODO move this to the part in code where blade sphere is deactivated
            $ blade_sphere_control = True
            $ nick_defense = False
            return
        "Return":
            jump .act_phase

label .act_Aerith:
    menu:
        "Light Barrier":
            call .act_Aerith_begin_casting("Light Barrier", 'yourself')
            if spell_successful:
                call LightBarrier("Aerith")
        "Curing Light":
            menu:
                "Heal me!":
                    call .act_Aerith_begin_casting("Curing Light", 'me')
                    if spell_successful:
                        show overlay green
                        play sound sfx_heal
                        "The green light fills me with strength."
                        hide overlay
                        call CuringLight('Aerith', 'Nick')
                "Heal yourself!":
                    call .act_Aerith_begin_casting("Curing Light", 'yourself')
                    if spell_successful:
                        play sound sfx_heal
                        "Green light flows over Aerith, closing her wounds."
                        call CuringLight('Aerith', 'Aerith')
                "Heal Silvia!":
                    call .act_Aerith_begin_casting("Curing Light", 'Silvia')
                    if spell_successful:
                        play sound sfx_heal
                        call CuringLight('Aerith', 'Silvia')
                "Return":
                    jump .act_Aerith
        "Depths of Slumber" if target_list:
            call .act_Aerith_begin_casting("Depths of Slumber", 'warrior')
            if spell_successful:
                $ current_mp["Aerith"] -= mp_costs["Depths of Slumber"]
                a "Gift him with a peaceful sleep! Depths of Slumber!"
                #TODO add sleep spell sound, sound of falling asleep
                show overlay purple
                pause 0.1
                hide overlay purple with dissolve
                show enemy_chicken at sleep #TODO make chicken wiggle again if they wake up
                "The rider falls asleep, leaving his ostrich-mount confused."
                $ rider_asleep = True
                jump .act_phase
        "Return":
            jump .act_phase
    return

label .act_Aerith_begin_casting(spell, target):
    np "Aerith! [spell]!"
    if mp_costs[spell] > current_mp["Aerith"]:
        a "Uh, I don't have enough mana..."
        n "Damn..."
        jump .act_phase
    a "G-got it!"
    if "Rider" in target_list:
        "Aerith begins casting, but the rider is not going to just stand there and take it!"
        $ spell_successful = False
        call .rider_interrupt('Aerith')
    else:
        $ spell_successful = True
    return

label .rider_interrupt(caster):
    call .rider_attack(caster, None)
    if not attack_successful:
        $ spell_successful = True
    return

label .act_Silvia:
    menu:
        "Sneak Attack" if silvia_hidden and target_list:
            np "Silvia!"
            "She immediately grasps my intent!"
            "Silvia appears from the shadows, striking at the rider!"
            "He has no time to dodge."
            $ silvia_hidden = False
            call .dealdamage("Rider", damage['Silvia']['sneak_attack'], False)
            if target_died:
                play sound [sfx_critical, sfx_death_2]
                "Already wounded, the rider can't survive Silvia's attack."
                hide enemy_chicken with moveoutbottom
                "He falls off the ostrich, and it escapes to the desert."
                $ victorious = True
            else:
                play sound sfx_miss
                "Silvia's blade strikes a deep wound into the rider's back."
            return
        "Attack" if not silvia_hidden and target_list:
            np "Silvia, attack!"
            "She has a go at it, lunging toward the rider!"
            play sound sfx_miss
            $ i = renpy.random.random()
            if i <= 0.3:
                "But the ostrich is too fast even for her!"
                s "I'm sorry, liege..."
                return
            else:
                show enemy_chicken hurt
                pause 0.1
                show enemy_chicken normal
                play sound sfx_grunt_6
                "She lands a strike on the rider's back!"
                call .dealdamage("Rider", damage['Silvia']['attack'], False)
                if target_died:
                    hide enemy_chicken with moveoutbottom
                    play sound sfx_death_1
                    "The rider can't take it any longer, and succumbs to his wounds."
                    "The ostrich, left without master, escapes into the desert."
                    $ victorious = True
                    return
                else:
                    play sound sfx_grunt_4
                    "He screams in pain and fury."
                    return
        "Hide" if not silvia_hidden:
            np "Silvia! Hide!"
            s "Very well."
            "She melds into the shadows."
            $ silvia_hidden = True
            return
        "Hail of Daggers" if target_list and current_mp['Silvia'] > mp_costs["Hail of Daggers"]:
            $ current_mp['Silvia'] -= mp_costs["Hail of Daggers"]
            $ silvia_hidden = False
            np "Say, Silvia, did you see the forecast?"
            "She smiles a little."
            s "It's raining daggers, right?"
            "She leaps into the air."
            "The rider realizes something is off and..."
            $ i = renpy.random.random()
            if i <= 0.3:
                show fx daggers
                pause 0.05
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.09
                stop sound
                pause 0.05
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.09
                stop sound
                pause 0.05
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.09
                stop sound
                hide fx daggers
                hide enemy_chicken with moveoutright
                play sound sfx_running
                "... turns around to run!"
                s "It seems I have lost sight of him and his ridiculous mount, liege."
                "Damn!"
                jump .rider_escape
            else:
                show fx daggers
                pause 0.14
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.14
                play sound sfx_dagger
                pause 0.03
                play sound sfx_hit
                pause 0.03
                play sound sfx_dagger
                pause 0.14
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                hide fx daggers
                show enemy_chicken hurt
                pause 0.1
                show enemy_chicken normal
                pause 0.05
                show enemy_chicken hurt
                pause 0.1
                show enemy_chicken normal
                pause 0.05
                show enemy_chicken hurt
                pause 0.1
                show enemy_chicken normal
                "... cowers in place as he sees the blades falling toward him!"
                play sound sfx_grunt_4 #TODO add ostritch screech sound
                "Strike! The ostrich screeches in pain!"
                call .dealdamage('Rider', damage['Silvia']['hail'], False)
                if target_died:
                    hide enemy_chicken with moveoutbottom
                    #TODO add sound of person falling on sand
                    play sound sfx_grunt_3
                    "The ostrich goes into a frenzy, dropping the rider to the ground."
                    "He can't hold on any longer, and dies quickly, the red of his blood mixing with the desert sand."
                else:
                    play sound sfx_grunt_6
                    "The ostrich starts to frenzy, but the rider barely manages to calm it down."
                    "They're not going to hold out for much longer, though." # This is a damage message, need to proceduralize...
                    return
        "Poisoned Blade" if target_list and current_mp["Silvia"] > mp_costs["Poisoned Blade"]:
            $ current_mp['Silvia'] -= mp_costs["Poisoned Blade"]
            $ silvia_hidden = False
            np "Poison him!"
            s "Your wish..."
            "She leaps and disappears into thin air, appearing right behind the rider!"
            s "... is my command!"
            $ i = renpy.random.random()
            if i <= 0.3:
                show fx daggers at flip
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.09
                stop sound
                hide fx daggers at flip
                "However, the rider barely manages to dodge her nefarious strike."
                return
            else:
                show fx daggers at flip
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.03
                play sound sfx_hit
                pause 0.09
                hide fx daggers at flip
                show enemy_chicken hurt
                pause 0.1
                show enemy_chicken normal
                "There's no way the rider can dodge."
                call .dealdamage("Rider", damage['Silvia']['poison_attack'], False)
                if target_died:
                    hide enemy_chicken with moveoutbottom
                    play sound sfx_grunt_2
                    "He falls off his mount and speedily succumbs to his wounds."
                    "The ostrich runs into the horizon."
                    $ victorious = True
                else:
                    play sound sfx_grunt_5
                    "The blade goes straight through his right arm."
                    "He seems disoriented by the poison, but still has will to fight left in him!"
                    $ poison_counter["Rider"] = renpy.random.randint(1, 3)
                return
        "Return":
            jump .act_phase
    return

label .act_defend:
    play sound sfx_shield
    "I raise my shield in defense."
    "Let's see you get through this!"
    $ nick_defense = True
    $ blade_sphere_control = False
    return

label .rider_turn:
    if "Rider" in target_list:
        $ j = renpy.random.random()
        if j <= 0.5:
            call .rider_attack
        if playerdeath:
            return
        $ i = renpy.random.random()
        if i <= 0.5:
            hide enemy_chicken with moveoutleft
            play sound sfx_running
            pause 0.5
            jump .rider_escape
        else:
            if j > 0.5:
                play sound sfx_running
                hide enemy_chicken with moveoutleft
                show enemy_chicken normal at wigglemiddle with moveinright
                "The rider circles around us, waiting for an opening."
            return
        #jump .act_phase
    else:
        show enemy_chicken normal at wigglemiddle
        play sound sfx_running
        "Suddenly, the rider ambushes us!"
        $ target_list.append("Rider")
        call .rider_attack
        return

label .rider_escape:
    "The rider escapes beyond sight."
    $ target_list.remove("Rider")
    if 'Silvia' in playerparty:
        s "Do not let your guard down. He shall return."
    return
    #jump .wait_phase

label .dealdamage(target, amount, handle_death = True):
    with vpunch
    $ target_died = False
    $ current_hp[target] -= amount
    if current_hp[target] < 0:
        $ current_hp[target] = 0
        if handle_death:
            call .death(target)
        $ target_died = True
    #if not target_died:
        #$ stats_frame(target, 90, current_hp[target], max_hp[target], xalign=0.5, yalign=0.0)
        #pause 2
    return

label .death(target):
    with hpunch
    if target == "Nick":
        screen black
        with dissolve
        play sound sfx_grunt_2
        "Blood trickles over my eyes, and I begin a long descent into darkness..."
        $ playerdeath = True
    elif target == "Aerith":
        play sound sfx_grunt_4_f #TODO add aerith screams
        "Aerith falls to the ground as her body disintegrates into fine purple dust, blown away by an intangible wind."
        $ playerparty.remove("Aerith")
    elif target == "Silvia":
        $ playerparty.remove("Silvia")
        play sound sfx_grunt_5_f
        "Silvia disappears in a cloud of lavender mist."
    elif target == "Rider":
        # I'd like to do some cool procedural stuff with Tracery here, but it'll have to wait until after NaNo
        $ victorious = True
        $ i = renpy.random.randint(1, 4)
        if i == 1:
            show enemy_chicken hurt
            pause 0.1
            show enemy_chicken normal
            hide enemy_chicken with moveoutleft
            play sound sfx_grunt_5
            "I land a deep wound on his side, and he falls off his mount, which escapes into the desert."
            "He quietly bleeds to death."
        elif i == 2:
            show enemy_chicken hurt
            pause 0.1
            show enemy_chicken normal
            play sound sfx_battlecry
            "He screams as my blade cuts his stomach open."
            "He falls to the ground, a bloody mess."
            hide enemy_chicken with moveoutright
            "The ostrich runs off."
        elif i == 3:
            show enemy_chicken hurt
            pause 0.1
            show enemy_chicken normal
            play sound sfx_critical
            play sound sfx_grunt_10
            "My strike goes right through him, splitting his body in half."
            hide enemy_chicken with moveoutleft
            "The ostrich runs away."
        elif i == 4:
            show enemy_chicken hurt
            pause 0.1
            show enemy_chicken normal
            play sound [sfx_block, sfx_grunt_3]
            "I strike at him with full force, causing him to fall off!"
            hide enemy_chicken with moveoutright
            play sound sfx_running
            "The ostrich runs away, leaving its rider moaning on the ground."
            play sound sfx_critical
            "I finish him with a well-aimed strike right through the chest."
    return

label .rider_attack(rider_target = None, attack = None):
    # If rider_target is not supplied, choose randomly. Ditto with attack.
    if rider_target == None:
        python:
            possible_targets = list(playerparty)
            if silvia_hidden:
                possible_targets.remove('Silvia')
            rider_target = renpy.random.choice(possible_targets)
    if attack == None:
        python:
            possible_attacks = ['Fire', 'Charge']
            if not spear_broken:
                possible_attacks.append('Spear')
            attack = renpy.random.choice(possible_attacks)
    $ attack_successful = False
    if attack == "Fire":
        call .rider_fire(rider_target)
    elif attack == "Charge":
        call .rider_charge(rider_target)
    else:
        call .rider_spear(rider_target)
    return

label .rider_fire(rider_target):
    if rider_target == "Nick":
        show fx fire
        play sound sfx_fire
        pause 0.8
        hide fx fire
        "He comes a bit closer. Suddenly, the ostrich breathes fire on me!"
    else:
        "He goes closer to [rider_target]. Then, he commands his ostrich to breathe fire!"
        play sound sfx_fire
    if blade_sphere_control:
        play sound sfx_grunt_4
        "Damn! Blade Sphere Control can't protect against breath weapons!"
    if rider_target == "Nick" and nick_defense:
        "Haha! My shield heats up a bit, but that's no problem at all."
        return
    if rider_target == "Aerith" and light_barrier_active['Aerith'] > 0:
        "The fire reflects off of Aerith's barrier."
        show enemy_chicken hurt
        pause 0.1
        play sound sfx_battlecry
        show enemy_chicken at rolling
        "Seems the rider got a taste of his own poison. He bursts into flames, jumps off his mount, and rolls in the sand."
        play sound sfx_running
        hide enemy_chicken with moveoutbottom
        pause 0.2
        play sound sfx_critical
        "I finish him with a single strike."
        $ victorious = True
        return
    if rider_target == "Nick":
        show overlay red
        pause 0.25
        show overlay red at ghost
        play sound sfx_battlecry
        "The flames sear painfully into my flesh."
        hide overlay
        call .dealdamage('Nick', damage["Rider"]['Fire'])
    elif rider_target == "Aerith":
        play sound sfx_grunt_4_f #TODO add aerith screams
        "Aerith screams as the flames burn her skin."
        call .dealdamage('Aerith', damage["Rider"]['Fire'])
    else:
        play sound sfx_grunt_1_f
        "Silvia grits her teeth as the skin on her arms is charred by the flames."
        call .dealdamage('Silvia', damage["Rider"]['Fire'])
    $ attack_successful = True
    return

label .rider_charge(rider_target):
    if rider_target == "Nick":
        play sound sfx_running
        "He lunges right at me!"
        play sound sfx_hit
        pause 0.09
        stop sound
        show enemy_chicken normal at ramming
    else:
        play sound sfx_running
        "He charges toward [rider_target]!"
        play sound sfx_hit
        pause 0.09
        stop sound
    if blade_sphere_control:
        play sound [sfx_block, sfx_hit]
        "He can't get through Blade Sphere Control, though!"
        call .dealdamage("Rider", damage['Nick']['blade_sphere_control'], False)
        if target_died:
            hide enemy_chicken with moveoutbottom
            play sound sfx_grunt_3
            "He is hit off his mount, and dies whimpering pitifully on the sands."
            $ victorious = True
            return
        else:
            play sound sfx_grunt_4
            "He screams as my blade cuts into his arm!"
            if not spear_broken:
                "His spear breaks as well."
                $ spear_broken = True
            return
    if rider_target == "Aerith" and light_barrier_active['Aerith'] > 0:
        play sound sfx_grunt_5_f #TODO add aerith screams
        "He slams right into Aerith. She's protected by the sphere, but still falls prone."
        return
    if rider_target == "Nick" and nick_defense:
        with hpunch
        play sound sfx_grunt_5
        "My shield is of no use as he rams right into me, sending me flying to the ground."
        show overlay red
        play sound sfx_critical
        pause 0.15
        hide overlay
        pause 0.1
        show overlay red
        pause 0.15
        hide overlay
        pause 0.2
        show enemy_chicken normal at backwardsramming
        pause 1.0
        show enemy_chicken normal at wigglemiddle
        "Blood splatters everywhere, and my body is full of bruises."
        call .dealdamage("Nick", damage["Rider"]["Charge"])
        return
    if rider_target == "Nick":
        with hpunch
        "His pounce catches me by surprise, and I have no time to leap out of the way!"
        show overlay red
        play sound sfx_critical
        pause 0.15
        hide overlay
        pause 0.1
        show overlay red
        pause 0.15
        hide overlay
        pause 0.2
        show enemy_chicken normal at backwardsramming
        pause 1.0
        show enemy_chicken normal at wigglemiddle
        "The ostrich tramples all over me, leaving painful bruises."
        call .dealdamage("Nick", damage["Rider"]["Charge"])
    elif rider_target == "Aerith":
        "Aerith cries in terror as the ostrich runs her over."
        "Damn! You'll pay for that!"
        call .dealdamage("Aerith", damage["Rider"]["Charge"])
    else:
        "Silvia's expression turns pained as the ostrich tramples over her!"
        call .dealdamage("Silvia", damage["Rider"]["Charge"])
    $ attack_successful = True
    play sound sfx_running
    return

label .rider_spear(rider_target):
    if rider_target == "Nick":
        #show enemy_chicken normal at ramming
        play sound sfx_running
        "He comes close and attempts to impale me with his spear."
        show fx slash_spear
        play sound sfx_hit
        pause 0.09
        stop sound
        pause 0.01
        hide fx
    else:
        play sound sfx_running
        "The rider makes an attempt to impale [rider_target]!"
        play sound sfx_hit
        pause 0.09
        stop sound

    if blade_sphere_control:
        play sound [sfx_block, sfx_hit]
        "Yeah, just try to get past my technique!"
        play sound sfx_grunt_7
        show enemy_chicken hurt
        pause 0.1
        show enemy_chicken normal
        call .dealdamage("Rider", damage['Nick']['blade_sphere_control'], False)
        if target_died:
            call .death("Rider")
        else:
            if not spear_broken:
                "His spear breaks as my sword splits it in half."
                "Damn. Almost got his hand too."
                $ spear_broken = True
            else:
                play sound sfx_critical
                "I cut a deep wound into his arm."
        return
    if rider_target == "Aerith" and light_barrier_active['Aerith'] > 0:
        play sound sfx_dagger #TODO add aerith scream even if she does not take damage, "eep"
        "It's no use. The attack harmlessly bounces off Aerith's barrier."
        return
    if rider_target == "Nick" and nick_defense:
        play sound sfx_block
        "The attack is easily deflected by my shield. Why even bother trying?"
        return
    if rider_target == "Nick":
        play sound sfx_hit_2
        show overlay red
        pause 0.1
        hide overlay
        "I raise my arm just in time, but the spear still manages to land a blow."
        play sound sfx_grunt_8
        call .dealdamage("Nick", damage["Rider"]["Spear"])
    elif rider_target == "Aerith":
        play sound sfx_grunt_4_f #TODO add aerith screams
        "Aerith crosses her arms in front of her, but that offers no protection at all!"
        play sound sfx_grunt_1_f
        "The spear pierces deep into her arms."
        call .dealdamage("Aerith", damage["Rider"]["Spear"])
    else:
        #TODO add a less squishy hitting flesh sound, liky something you'd get from piercing flesh in leather armor
        "Silvia attempts to dodge the attack, but can't get out of the way in time."
        play sound sfx_grunt_9
        "It's painful to see the spear sink into her back."
        call .dealdamage("Silvia", damage["Rider"]["Spear"])
    $ attack_successful = True
    return

# label .wait_phase:
    # menu:
        # "Remain vigilant":
            # "I wait, trying to listen to the approaching footsteps."
            # $ nick_defense = True
        # "Blade Sphere Control":
            # "I refocus my attention."
            # np "Blade Sphere Control!"
            # $ blade_sphere_control = True
            # "Wherever you are, I'm ready for you!"
        # "Aerith Spell: Curing Light" if "Aerith" in playerparty:
            # menu:
                # "Heal me.":
                    # "She casts the spell, and the green light suffuses my body with peace."
                    # call .curinglight("Nick")
                # "Heal yourself.":
                    # "She puts her hands together, and a green light fills every pore of her skin, taking away her wounds."
                    # call .curinglight("Aerith")
                # "Heal Silvia." if not silvia_hidden:
                    # "A green glow emanates from Aerith's hand and spreads over Silvia as she touches her wounds."
                    # call .curinglight("Silvia")
                # "Return":
                    # jump .wait_phase
        # "Aerith Spell: Light Barrier" if "Aerith" in playerparty:
            # "Aerith chants the spell, and a white sphere of light encloses her in the protection of her god."
            # $ light_barrier_active['Aerith'] = 1
        # "Tell Silvia to hide." if "Silvia" in playerparty and not silvia_hidden:
            # np "Silvia, this would be a good time to hide yourself."
            # s "Your rhetoric is convincing, liege."
            # np "I-it is?"
            # "Silvia disappears into thin air."
            # $ silvia_hidden = True
    # "Suddenly, the rider ambushes us!"
    # call .rider_attack
    # return

label .victorious:
    hide enemy_chicken
    np "Whew! That wasn't too easy!"
    if "Silvia" in playerparty:
        show sil wot
        s "Did it not match your expectations, liege?"
        np "Sure it did. Well, let's move on."
        show sil normal
    hide screen hp_window
    play music "bgm/LanayruDesert.mp3"
    jump Ruins_courtyard_menu
    return
