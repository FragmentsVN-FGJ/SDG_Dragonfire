init:
    $ event("RuinsStart", "act == 'ruins'", priority=20)
    
    $ mp_costs = {'Light Barrier': 10, 'Curing Light': 10, 'Furious Strike': 20, 'Blade Sphere Control': 30, 'Hail of Daggers': 30, "Poisoned Blade": 20, "Depths of Slumber": 30}
    $ max_hp = {'Nick': 100, 'Aerith': 100, 'Silvia': 100}
    $ max_mp = {'Nick': 100, 'Aerith': 100, 'Silvia': 100}
    $ idtolabel = {}
    $ light_barrier_active = {}
    $ poison_counter = {}
    $ damage = {'Nick': {'blade_sphere_control': 10, 'attack': 20}, 'Silvia': {'sneak_attack': 40, 'attack': 20, 'hail': 20, 'poison_attack': 20}, 'Aerith': {}, 'Rider': {'Spear': 20, 'Fire': 20, 'Charge': 30}, 'poison': 10 }

define comp = Character('Computer')
define np = DynamicCharacter('np_name')


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
    $ current_hp = {'Nick': max_hp['Nick'], 'Aerith': max_hp['Aerith'], 'Silvia': max_hp['Silvia'], 'Rider': 70}
    $ current_mp = {'Nick': max_mp['Nick'], 'Aerith': max_mp['Aerith'], 'Silvia': max_mp['Silvia']}
    $ target_list = ["Rider"]
    $ nick_acted = False
    "As we approach, trapdoors spring open all around us, sending sand flying in every direction!"
    show sil star
    s "It's an ambush! Hihihi!"
    hide sil
    show desert_rider
    "Through the sand I see the vague shapes of ostrich-riding warriors, screeching for battle!"
    play music "bgm/Battle1.wav"
    "The fight rages on for a while, and we manage to finish off two of the warriors."
    "One more to go!"
    call .act_phase
    while not victorious and not playerdeath:
        # Needs to be this way around in order to avoid zombie attacks...
        call .start_round
        call .rider_turn
        call .act_phase
    if playerdeath:
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
            "The rider can't withstand the poison, and dies."
        else:
            "[person] dies from poisoning."
    else:
        if person == "Rider":
            "The rider is hurt by the poison!"
        else:
            "[person] suffers due to the poison!"
    if poison_counter[person] == 0:
        "The poisoning ceases."
    return
    
label .act_phase:
    menu:
        "Continue Blade Sphere Control" if target_list and blade_sphere_control:
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
    return        
    
label .act_attack:
    # If len(target_list) > 1, multiple choice menu here.
    $ nick_acted = True
    if rider_asleep:
        "Now's my chance!"
        "While the rider is fast asleep, I strike at the ostrich with my sword, severing its long neck!"
        "Time to finish this! I raise my sword and plunge it into the rider's chest!"
        "His eyes shoot open just as he falls into death's icy grasp."
        $ victorious = True
        return
    "Readying my sword for a side slash, I charge full-speed toward the rider!"
    $ i = renpy.random.random()
    if i <= 0.5:
        "However, using the speed of his mount to his advantage, he manages to evade my attack."
        return
    else:
        $ j = renpy.random.random()
        if j <= 0.1:
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
            if rider_asleep:
                "Being asleep, he can't avoid my attack."
                call .death("Rider")
                return
            $ i = renpy.random.random()
            if i <= 0.5:
                # Test for spear_broken
                if not spear_broken:
                    "He raises his spear to parry my attack."
                    "My sword slams straight through it, shattering it in pieces!"
                    $ spear_broken = True
                    return
                "He raises the remnants of his spear, but my attack goes straight through them, his arm and his head."
                "The ostrich, now carrying only a corpse severed in half, sees it best to escape."
                $ victorious = True
                return
            else:
                "Damn! His mount is too fast, and he dodges my incursion."
                return
        "Blade Sphere Control" if current_mp["Nick"] > mp_costs["Blade Sphere Control"]:
            $ current_mp["Nick"] -= mp_costs["Blade Sphere Control"]
            "I close my eyes to find internal peace."
            np "Blade Sphere Control!"
            "Let's see him get through this technique!"
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
                        "The green light fills me with strength."
                        call CuringLight('Aerith', 'Nick')
                "Heal yourself!":
                    call .act_Aerith_begin_casting("Curing Light", 'yourself')
                    if spell_successful:
                        "Green light flows over Aerith, closing her wounds."
                        call CuringLight('Aerith', 'Aerith')
                "Heal Silvia!":
                    call .act_Aerith_begin_casting("Curing Light", 'Silvia')
                    if spell_successful:
                        call CuringLight('Aerith', 'Silvia')
                "Return":
                    jump .act_Aerith
        "Depths of Slumber" if target_list:
            call .act_Aerith_begin_casting("Depths of Slumber", 'warrior')
            if spell_successful:
                $ current_mp["Aerith"] -= mp_costs["Depths of Slumber"]
                a "Gift him with a peaceful sleep! Depths of Slumber!"
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
                "Already wounded, the rider can't survive Silvia's attack."
                "He falls off the ostrich, and it escapes to the desert."
                $ victorious = True
            else:
                "Silvia's blade strikes a deep wound into the rider's back."
            return
        "Attack" if not silvia_hidden and target_list:
            np "Silvia, attack!"
            "She has a go at it, lunging toward the rider!"
            $ i = renpy.random.random()
            if i <= 0.5:
                "But the ostrich is too fast even for her!"
                s "I'm sorry, liege..."
                return
            else:
                "She lands a strike on the rider's back!"
                call .dealdamage("Rider", damage['Silvia']['attack'], False)
                if target_died:
                    "The rider can't take it any longer, and succumbs to his wounds."
                    "The ostrich, left without master, escapes into the desert."
                    $ victorious = True
                    return
                else:
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
            if i <= 0.5:
                "... turns around to run!"
                s "It seems I have lost sight of him and his ridiculous mount, liege."
                "Damn!"
                jump .rider_escape
            else:
                "... cowers in place as he sees the blades falling toward him!"
                "Strike! The ostrich screeches in pain!"
                call .dealdamage('Rider', damage['Silvia']['hail'], False)
                if target_died:
                    "The ostrich goes into a frenzy, dropping the rider to the ground."
                    "He can't hold on any longer, and dies quickly, the red of his blood mixing with the desert sand."
                else:
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
            if i <= 0.5:
                "However, the rider barely manages to dodge her nefarious strike."
                return
            else:
                "There's no way the rider can dodge."
                call .dealdamage("Rider", damage['Silvia']['poison_attack'], False)
                if target_died:
                    "He falls off his mount and speedily succumbs to his wounds."
                    "The ostrich runs into the horizon."
                    $ victorious = True
                else:
                    "The blade goes straight through his right arm."
                    "He seems disoriented by the poison, but still has will to fight left in him!"
                    $ poison_counter["Rider"] = renpy.random.randint(1, 3)
                return
        "Return":
            jump .act_phase
    return

label .act_defend:
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
        $ i = renpy.random.random()
        if i <= 0.5:
            jump .rider_escape
        else:
            if j > 0.5:
                "The rider circles around us, waiting for an opening."
            return
        #jump .act_phase
    else:
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
    $ target_died = False
    $ current_hp[target] -= amount
    if current_hp[target] < 0:
        $ current_hp[target] = 0
        if handle_death:
            call .death(target)
        $ target_died = True
    return

label .death(target):
    if target == "Nick":
        "Blood trickles over my eyes, and I begin a long descent into darkness..."
        $ playerdeath = True
    elif target == "Aerith":
        "Aerith falls to the ground as her body disintegrates into fine purple dust, blown away by an intangible wind."
        $ playerparty.remove("Aerith")
    elif target == "Silvia":
        $ playerparty.remove("Silvia")
        "Silvia disappears in a cloud of lavender mist."
    elif target == "Rider":
        # I'd like to do some cool procedural stuff with Tracery here, but it'll have to wait until after NaNo
        $ victorious = True
        $ i = renpy.random.randint(1, 4)
        if i == 1:
            "I land a deep wound on his side, and he falls off his mount, which escapes into the desert."
            "He quietly bleeds to death."
        elif i == 2:
            "He screams as my blade cuts his stomach open."
            "He falls to the ground, a bloody mess."
            "The ostrich runs off."
        elif i == 3:
            "My strike goes right through him, splitting his body in half."
            "The ostrich runs away."
        elif i == 4:
            "I strike at him with full force, causing him to fall off!"
            "The ostrich runs away, leaving its rider moaning on the ground."
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
        "He comes a bit closer. Suddenly, the ostrich breathes fire on me!"
    else:
        "He goes closer to [rider_target]. Then, he commands his ostrich to breathe fire!"
    if blade_sphere_control:
        "Damn! Blade Sphere Control can't protect against breath weapons!"
    if rider_target == "Nick" and nick_defense:
        "Haha! My shield heats up a bit, but that's no problem at all."
        return
    if rider_target == "Aerith" and light_barrier_active['Aerith'] > 0:
        "The fire reflects off of Aerith's barrier."
        "Seems the rider got a taste of his own poison. He bursts into flames, jumps off his mount, and rolls in the sand."
        "I finish him with a single strike."
        $ victorious = True
        return
    if rider_target == "Nick":
        "The flames sear painfully into my flesh."
        call .dealdamage('Nick', damage["Rider"]['Fire'])
    elif rider_target == "Aerith":
        "Aerith screams as the flames burn her skin."
        call .dealdamage('Aerith', damage["Rider"]['Fire'])
    else:
        "Silvia grits her teeth as the skin on her arms is charred by the flames."
        call .dealdamage('Silvia', damage["Rider"]['Fire'])
    $ attack_successful = True
    return

label .rider_charge(rider_target):
    if rider_target == "Nick":
        "He lunges right at me!"
    else:
        "He charges toward [rider_target]!"
    if blade_sphere_control:
        "He can't get through Blade Sphere Control, though!"
        call .dealdamage("Rider", damage['Nick']['blade_sphere_control'], False)
        if target_died:
            "He is hit off his mount, and dies whimpering pitifully on the sands."
            $ victorious = True
            return
        else:
            "He screams as my blade cuts into his arm!"
            if not spear_broken:
                "His spear breaks as well."
                $ spear_broken = True
            return
    if rider_target == "Aerith" and light_barrier_active['Aerith'] > 0:
        "He slams right into Aerith. She's protected by the sphere, but still falls prone."
        return
    if rider_target == "Nick" and nick_defense:
        "My shield is of no use as he rams right into me, sending me flying to the ground."
        "Blood splatters everywhere, and my body is full of bruises."
        call .dealdamage("Nick", damage["Rider"]["Charge"])
        return
    if rider_target == "Nick":
        "His pounce catches me by surprise, and I have no time to leap out of the way!"
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
    return
        
label .rider_spear(rider_target):
    if rider_target == "Nick":
        "He comes close and attempts to impale me with his spear."
    else:
        "The rider makes an attempt to impale [rider_target]!"
        
    if blade_sphere_control:
        "Yeah, just try to get past my technique!"
        call .dealdamage("Rider", damage['Nick']['blade_sphere_control'], False)
        if target_died:
            call .death("Rider")
        else:
            if not spear_broken:
                "His spear breaks as my sword splits it in half."
                "Damn. Almost got his hand too."
                $ spear_broken = True
            else:
                "I cut a deep wound into his arm."
        return
    if rider_target == "Aerith" and light_barrier_active['Aerith'] > 0:
        "It's no use. The attack harmlessly bounces off Aerith's barrier."
        return
    if rider_target == "Nick" and nick_defense:
        "The attack is easily deflected by my shield. Why even bother trying?"
        return
    if rider_target == "Nick":
        "I raise my arm just in time, but the spear still manages to land a blow."
        call .dealdamage("Nick", damage["Rider"]["Spear"])
    elif rider_target == "Aerith":
        "Aerith crosses her arms in front of her, but that offers no protection at all!"
        "The spear pierces deep into her arms."
        call .dealdamage("Aerith", damage["Rider"]["Spear"])
    else:
        "Silvia attempts to dodge the attack, but can't get out of the way in time."
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
    hide desert_rider
    np "Whew! That wasn't too easy!"
    if "Silvia" in playerparty:
        show sil wot
        s "Did it not match your expectations, liege?"
        np "Sure it did. Well, let's move on."
    return
        
label RuinsStart:
    $ silvia_hidden = False
    $ light_barrier_nick = False
    $ light_barrier_silvia = False
    $ light_barrier_aerith = False
    call DFO_login
    call DFO_init
    call Ruins_entrance
    call Ruins_courtyard
    jump events_skip_period
    return
    
label Ruins_courtyard:
    "Broken pillars loom ominously around us, and I feel as if someone is gazing at us, hidden somewhere beyond sight..."
    a "This place looks abandoned... Maybe there's no-one here?"
    np "Why would they make a new dungeon without enemies?"
    a "R-right. I guess they wouldn't!"
    np "Wait, what's that?"
    "I point at something glimmering in the distance."
    show sil proud
    s "It appears to be an underground entrance. Well done, liege."
    jump .courtyard_menu
    
label .courtyard_menu:
    menu:
        "Should we approach?"
        "Let's go!":
            "We approach the entrance as it glitters in the sunlight."
            jump Ruins_battle1
        "[np_name]...":
            call Nicholas_oob
        "Aerith...":
            call Aerith_oob
        "Silvia...":
            call Silvia_oob
        "Maybe we should just head back to the forest...":
            np "Actually, Aerith, you've got a point. Let's head back."
            s "What? Liege, you can't be earnest!"
            menu:
                "You're right. I was just kidding.":
                    np "It was just a joke!"
                    s "....."
                    jump .courtyard_menu
                "I'm serious.":
                    np "No, I'm serious. This is probably too tough for us right now."
                    s "I would not have expected such behavior from you."
                    "She looks disappointed. Well, it can't be helped."
                    $ affection_modify('Silvia', -1)
                    return

label Nicholas_oob:
    menu:
        "Return":
            return
    return
                    
label Aerith_oob:
    menu:
        "Cast Light Barrier":
            call LightBarrier("Aerith")
            #call .light_barrier_target
        "Cast Cure on...":
            call .cure_target
        #"Cast Mass Cure"
        #    call .mass_cure
        #"Cast Heal on...":
        #    call .heal_target
        #"Cast Mass Heal"
        #    call .mass_heal
        #"Return":
        #    return
    return

label .light_barrier_target:
    menu:
        "[np_name]":
            $ target = "Nick"
            $ target_desc = "me"
        "Aerith":
            $ target = "Aerith"
            $ target_desc = "yourself"
        "Silvia":
            $ target = "Silvia"
            $ target_desc = "Silvia"
        "Return":
            jump Aerith_oob
    call ask_Aerith_to_cast("Light Barrier", target_desc, target)
    return

label .cure_target:
    menu:
        "[np_name]":
            $ target = "Nick"
            $ target_desc = "me"
        "Aerith":
            $ target = "Aerith"
            $ target_desc = "yourself"
        "Silvia":
            $ target = "Silvia"
            $ target_desc = "Silvia"
        "Return":
            jump Aerith_oob
    call ask_Aerith_to_cast("Cure", target_desc, target)
    return

#label .mass_cure:

#label .heal_target:

#label .mass_heal:    

label ask_Aerith_to_cast(technique_name, target_desc, target):
    np "Aerith, could you cast [technique_name] on [target_desc]?"
    if mp_costs[technique_name] <= current_mp['Aerith']:
        a "S-sure."
        call usetechnique('Aerith', technique_name, target)
        # "She chants the spell, and I'm momentarily blinded by the white light enveloping my body."
    else:
        a "I'm afraid I don't have enough mana."
    return    

label Silvia_oob:
    menu:
        "Hide" if not silvia_hidden:
            np "Silvia, could you hide yourself?"
            "Wordlessly, she conceals herself in the shadows."
            $ silvia_hidden = True
            return
        "Come back from hiding" if silvia_hidden:
            np "Uh, Silvia? You can come out now."
            "Silvia returns from the shadows."
            $ silvia_hidden = False
            return
        "Return":
            return
    
label Ruins_entrance:
    scene bg_temple with fade
    show sil cat
    "The cathedral's teleporter sends us to the entrance of the dungeon."
    np "This is just a test run, so I didn't want to get spoiled."
    np "Have you researched this place, Silvia?"
    "No need to ask Aerith..."
    show sil lecture
    s "The Ruins of Kvaagwyr, a temple built to a deity long since forgotten, hidden in the most desolate reaches of the Crystalline Desert."
    s "Caravans and wanderers report of suspicious activity and screams echoing in the night."
    s "Rumors tell of human sacrifice, and those who wander in its vicinity never return."
    show sil cat
    s "The Order of the Dragon has promised a reward to any who figure out its secrets."
    np "T-that's great. Any idea about the enemies?"
    show sil mwerrllyy
    s "None whatsoever, liege."
    show sil normal
    np "W-well, let's go in."
    a "Uh, can't we just go to the forest like normal...?"
    show sil annoyed
    s "Silence! We shan't run away."
    a "I think you mean can't..."
    show sil chu
    s "I do not."
    show sil normal
    np "A-anyway! Let's go!"
    show sil cat2
    s "Lead the way, and we shall follow."
    return
    
    
label DFO_init:
    scene white with dissolve
    scene bg_fort with pixellate
    show sil normal at right
    "I blink as my eyes adjust to the vibrant hyper-reality surrounding me."
    "Silvia and Aerith are already here."
    s "Hi there."
    if broken_up:
        a "Hi..."
        "Aerith looks a bit dismayed. Did I anger her somehow?"
    else:
        "Aerith puts her hands together."
        a "Great to see you!"
    show sil cat2
    s "Well then, liege, riddle me this. Where are we heading next?"
    "Silvia has a rather, how should I say it, peculiar way with words."
    np "I was thinking we could hit the Ruins of Kvaagwyr today."
    show sil proud
    s "Oh, is that not from the new expansion? Finally, we shall face a proper challenge!"
    a "A challenge? It's not too difficult, is it?"
    show sil hmm
    s "Does your cowardice know no bounds, priestess?"
    np "We can level up way more effectively if we try something a bit harder for a change."
    a "I-if you say so..."
    return
    
label DFO_login:
    "Oh yeah, it's time to play some DFO!"
    "I've assembled the equipment and I'm raring to go!"
    "It took some soldering, but the mod is ready now too."
    "With this mod, I'll be skirting the limits of possibility in terms of the level of realism that modern technology can offer."
    "It's kind of sad, actually."
    "I've been improving my immersion with new gadgets for almost half of my life until now."
    "Every time, it just felt so much more real."
    "Getting better headsets, a treadmill, my first haptic suit, every time the increase in realism left me gasping in awe."
    "And now it's over."
    "Until we get neural interfaces, I doubt it will be possible to increase immersion any further."
    "Damn! I can't let the nostalgia get to me. This is it."
    "For a moment, I look wistully at the white pill I'm holding in my hands."
    "I place it on my tongue, downing it with a gulp of tap water."
    "It will take around 10 minutes for the effects to start."
    "Meanwhile, I'll just boot up the system."
    "I've been using these pills for a while now."
    "They're supposed to increase the realism of the VR experience further by messing with neuro-transmitters in your temporal lobe."
    "Maybe it's just placebo, but I feel like it's working, and strongly."
    "Whenever I use these, I completely lose my sense of reality, and can fully immerse myself in the world of games."
    "They're not supposed to be addictive. I wouldn't have started using them otherwise."
    "But once you've tried them, there's no going back. Ordinary VR begins to feel too bland, too colorless."
    "Maybe you could say I'm addicted in that sense."
    "They're psychotropic, so they're not exactly legal, of course."
    "I bought them off the Dark Web. If the cyber surveillance unit has figured it out, they haven't come knocking yet."
    "They probably have better things to do. I'm not a seller, after all."
    "The guy who {i}is{/i} selling them is really shady, though."
    "He has been raising his prices recently. Says his stash is running out."
    "Not sure I buy that. But I have to get these from somewhere, right?"
    "Buying ware from the black market has its disadvantages. I can't exactly report him to the police..."
    "The login screen boots up in front of me."
    comp "Initializing..."
    comp "Welcome back. Please state username and write password."
    "The accounts are voice-locked, so you'd think you wouldn't need a password."
    "But it's actually a good idea to use two or more authentication methods at once."
    "It's called double-factor authentication. It's a lot more secure."
    "You might be able to fake my voice with a recording, but you'd still need to get the password on top of that."
    "Time to log in! My username is..."
    call nameNP
    return
    
label nameNP:
    $ np_name = ""
    while not np_name:
        $ np_name = renpy.input("Your name was?", allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", length = 15)
        $ np_name = np_name.strip()
        if len(np_name) <= 2:
            comp "Username length inadequate."
            jump nameNP
        if np_name.isdigit():
            comp "Name must contain letters."
            jump nameNP
        python:
            contains_profanity = False
            already_in_use = False
            np_name_lower = np_name.lower()
            for profane in profanity:
                if profane in np_name_lower:
                    contains_profanity = True
            for name in takenNames:
                if name in np_name_lower:
                    already_in_use = True
        if contains_profanity:
            comp "Tut tut. That name is not allowed."
            jump nameNP
        if already_in_use:
            comp "Username and voice do not match."
            jump nameNP
    comp "Input password."
    comp "Thank you, [np_name]. Logging in..."
    return
    
    
# Profanities and stuff, don't look...
init python:
    profanity = ['anal', 'anus', 'arse', 'ass', 'ballsack', 'balls', 'bastard', 'bitch', 'biatch', 'bloody', 'blowjob', 'blow job', 'bollock', 'bollok', 'boner', 'boob', 'bugger', 'bum', 'butt', 'clitoris', 'cock', 'coon', 'crap', 'cunt', 'damn', 'dick', 'dildo', 'dyke', 'fag', 'feck', 'fellate', 'fellatio', 'felching', 'fuck', 'f u c k', 'fudgepacker', 'fudge packer', 'flange', 'hell', 'homo', 'jerk', 'jizz', 'knobend', 'knob end', 'labia', 'lmao', 'lmfao', 'muff', 'nigger', 'nigga', 'omg', 'penis', 'piss', 'poop', 'prick', 'pube', 'pussy', 'queer', 'scrotum', 'sex', 'shit', 's hit', 'sh1t', 'slut', 'smegma', 'spunk', 'tit', 'tosser', 'turd', 'twat', 'vagina', 'wank', 'whore', 'wtf']
    takenNames = ['aerith', 'silvia', 'lucia', 'grayknight', 'nekochan']