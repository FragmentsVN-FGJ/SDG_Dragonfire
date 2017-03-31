init:
    $ event("RuinsStart", "act == 'ruins'", priority=20)

    $ mp_costs = {'Light Barrier': 10, 'Curing Light': 10, 'Furious Strike': 20, 'Blade Sphere Control': 30, 'Hail of Daggers': 30, "Poisoned Blade": 20, "Depths of Slumber": 30}
    $ max_hp = {'Nick': 100, 'Aerith': 100, 'Silvia': 100, 'Rider':70}
    $ max_mp = {'Nick': 100, 'Aerith': 100, 'Silvia': 100}
    $ current_hp = {'Nick': max_hp['Nick'], 'Aerith': max_hp['Aerith'], 'Silvia': max_hp['Silvia'], 'Rider': max_hp['Rider']}
    $ current_mp = {'Nick': max_mp['Nick'], 'Aerith': max_mp['Aerith'], 'Silvia': max_mp['Silvia']}
    $ idtolabel = {}
    $ light_barrier_active = {}
    $ poison_counter = {}
    $ damage = {'Nick': {'blade_sphere_control': 10, 'attack': 20}, 'Silvia': {'sneak_attack': 40, 'attack': 20, 'hail': 20, 'poison_attack': 20}, 'Aerith': {}, 'Rider': {'Spear': 20, 'Fire': 20, 'Charge': 30}, 'poison': 10 }

    $ heal_amount = {"Curing Light": 20}

    $ default_tooltips = {'Light Barrier': "A barrier of light protects the caster from all harm. MP: 10", 'Curing Light': "The light of Luxphoros heals target for 20 damage. MP: 10", 'Furious Strike': "Bash a foe for great justice! Your attack causes a shockwave and breaks the target's weapons if they parry. MP: 20", 'Blade Sphere Control': "The ultimate protective technique prevents physical attacks against you and other party members nearby, retaliating for 10 damage. Upholding the technique requires constant focus. MP 30", 'Hail of Daggers': "Raining death from above hits all foes for 20 damage. Just make sure your own party members are not in range! MP: 30", "Poisoned Blade": "Poisoned blade deals 20 damage and poisons the enemy for 1-3 rounds. Poison deals 10 damage per round. MP: 20", "Depths of Slumber": "Magical powder sends enemies to sleep. MP: 30"}

    image white = Solid((255,255,255,255))

init python:
    def stats_frame(name, level, hp, maxhp, **properties):

        ui.frame(xfill=False, yminimum=None, **properties)

        ui.hbox() # (name, "HP", bar) from (level, hp, maxhp)
        ui.vbox() # name from ("HP", bar)

        ui.text(name, size=20)

        ui.hbox() # "HP" from bar
        ui.text("HP", size=20)
        ui.bar(maxhp, hp,
                xmaximum=150,
                left_bar=Frame("rrslider_full.png", 12, 0),
                right_bar=Frame("rrslider_empty.png", 12, 0),
                thumb=None,
                thumb_shadow=None)

        ui.close()
        ui.close()

        ui.vbox() # Level from (hp/maxhp)

        ui.text("Lv. %d" % level, xalign=0.5, size=20)
        ui.text("%d/%d" % (hp, maxhp), xalign=0.5, size=20)

        ui.close()
        ui.close()

define comp = Character('Computer')
define np = DynamicCharacter('np_name', color="#191970")

label Ruins_dragon:
    scene black with dissolve
    show air 7 at left
    with moveinleft
    show sil hmm at right
    with moveinright
    pause 1.0
    show air 9
    a "Just how deep underground are we going? Ewww!"
    show air blush2
    "She steps into a puddle of some black substance."
    show sil lecture
    s "We must recover the treasure for the Order of the Dragon. It must be hidden here."
    np "Wait, treasure? What treasure?"
    show sil wot
    s "I've heard many a tale whispered in the night."
    np "So it was mentioned in the quest log?"
    show sil angry
    "She doesn't seem too thrilled by my refusal to play along with her."
    show sil hm
    s "Yes."
    show sil hmm
    show air 3
    a "If the quest is done, why is there still a threat marker in the quest log?"
    np "Might be some secret enemy we missed."
    show air 10
    a "We've been playing for too long, I'm starting to feel dizzy."
    show sil annoyed
    s "Cease your useless complaints, priestess. We shall not give up now."
    np "We'll be done soon."
    hide air
    hide sil
    with moveoutright
    "We come to the end of the tunnel, and Aerith leans on a gray stone wall, closing her eyes."
    show air 11 at right, flip
    with moveinright
    show sil hmm at left
    with moveinleft
    s "Priestess? You may want to move back."
    show air blush at right, flip
    a "Huh?"
    # Startle anim
    "Aerith is startled as the wall behind her suddenly sprouts a huge slitted eye!"
    "I slowly realize that it's not a wall at all, but the head of a giant serpentine dragon!"
    show sil flmao
    s "Ah. This must be the N'Gashai we heard mention of."
    "Is this really the time to discuss that!?"
    show sil hurt at center
    show air blush2 at right
    with vpunch
    with hpunch
    with vpunch
    "The chamber shakes as the dragon turns toward us!"
    "It's preparing to roast us alive! We have to move fast!"
    hide sil
    hide air
    with moveoutright
    "We hide behind the pillars just as the flames begin to scorch the air around us."
    "It breaks some of the pillars with its tail!"
    "Damn! We have to move!"
    "It burrows into the ground. We eventually learn to anticipate where it'll be, and manage to defeat it with great effort."
    jump .victorious

label .victorious:
    "As the dragon dies with a mighty roar, its tail sweeps out the last of the pillars holding the chamber together!"
    "... And it begins to collapse!"
    np "Run!"
    "We make our way back through the tunnel as it collapses behind us!"
    "Wait, I didn't remember there being a turn to the right here!"
    show sil normal at right, flip
    with moveinright
    s "It's some kind of secret room!"
    "We could turn to the right, but we have no idea where it leads."
    "We might end up dying down here!"
    menu:
        "What should we do?"
        "Turn right":
            hide sil with moveoutright
            "We run to the right just in time as the tunnel collapses entirely."
            "Everyone is panting heavily, but it seems we're in the clear."
            show sil phew at center
            show air 9 at right
            with moveinleft
            pause 0.50
            show air 2
            a "W-wow!"
            "I blink as my eyes readjust to the light of the chamber we've entered."
            "There's gold and treasure everywhere!"
            show air 6
            a "It's amazing!"
            np "Seems we finally found that treasure!"
            show sil hmm
            s "Oh, but where might the weapons lie...?"
            # Crouch transition
            "Aerith picks up a pendant with some kind of dragon amulet on it."
            show air 8
            a "'Pendant of Fire-breathing'? It has 20 charges..."
            "We also find a new sword for me and a special dagger for Silvia."
            show sil lol
            s "It's not as strong as my current one..."
            show sil normal
            "Really? It looks a lot better."
            "Silvia's dagger looks more like the ones they give to newbies..."
            "A teleporter stone appears, floating in the air."
            "Touching it, we return to the cathedral."
            jump .ending
        "Keep going straight":
            "We manage to escape back to the temple as the tunnel collapses completely behind us."
            "A teleporter stone is floating in the air."
            s "We should be able to use this to return to the cathedral."
            a "So we completed the quest? But we didn't find the treasure..."
            np "Damn, maybe it was back there in the tunnels."
            s "Do not be distraught, liege. We may always return..."
            s "For more bloodshed! Hihihi!"
            "R-right... We touch the teleporter stone to return to the cathedral."
            jump .ending

label .ending:
    scene white with dissolve
    pause 0.5
    scene bg_fort with pixellate
    show sil cat2 at right
    show air 9 at left
    s "Was that not fun?"
    show air angry2
    a "It dragged on for too long. I really need to lie down."
    "I wonder if she has a bad framerate or just hasn't been playing for that long."
    "Silvia and I don't feel any strain at all from something like this."
    "But she's as high-level as us. She should have gotten used to it by now..."
    scene black with fade
    play music "bgm/hope(Ver1.00).ogg"
    return

label Ruins_innertemple_menu:
    menu:
        "Go down the secret entrance":
            jump Ruins_dragon
        "Aerith...":
            call Aerith_oob
        "Silvia...":
            call Silvia_oob
        "Go back out":
            jump Ruins_innerchambers_menu
    jump Ruins_innertemple_menu

label Ruins_innertemple:
    # Hallway straight and stairs to the right

    if 'Ruins_innertemple' in seen_before.keys() and seen_before['Ruins_innertemple']:
        "We reach the temple once more."
        if not battle5_won:
            "The ritual is still continuing."
            jump .attack_menu
        else:
            jump Ruins_innertemple_menu
    $ battle5_won = False
    $ seen_before['Ruins_innertemple'] = True

    "We've finally found the source of the ominous chanting."
    "A group of violet-robed mages is standing in a circle around an altar."
    "A flash of purple light is reflected from an object their leader is holding above his head."
    "It's a curved dagger. And on the altar, lies a man."
    show sil lecture at right
    with moveinright
    show air 10 at left
    with moveinleft
    s "It is worse than we suspected."
    s "We must prevent the completion of this vile ritual, lest they unleash some great darkness from beyond!"
    show air 3
    a "Um... I have less mana for some reason."
    show sil angry
    s "Can you not feel the malice? This area has been consecrated to deities opposed to your own."
    show air 11
    a "Huh?"
    np "I think she means that there's an 'Unhallow' area effect here."
    show air 8
    np "Since you're a priestess of Luxphoros, it weakens your effective level."
    show air disappoint
    a "Oh. That makes sense."
    show air 4
    a "Uh, shouldn't we stop them, by the way?"
    hide sil
    hide air
    with moveoutleft
    "She's got a point. The cult leader is approaching the altar."
    jump .attack_menu

label .attack_menu:
    menu:
        "Attack!":
            jump .attack
        "Wait":
            jump .wait
        "Go back":
            "We silently go back the way we came."
            jump Ruins_innerchambers_menu
        # Spells, techniques etc.

label .attack:
    "The fanatics turn around to face us, eyes widened by the surprise."
    "Then, they regain their bearings."
    "Fanatic" "More sacrifices for the great one!"
    with vpunch
    "Unexpectedly, the leader runs to the altar, killing the man in haste."
    jump .battle

label .wait:
    "The high priest approaches the man lying helpless on the altar."
    "Then, he raises the ceremonial dagger high above his head..."
    with vpunch
    "And strikes!"
    jump .battle

label .battle:
    "From where the dagger pierced the man's heart, a black, half-vaporous ooze spews forth, engulfing the leader."
    "He breathes the vapours in, filling himself with the power of darkness." # Teh cheeze, i luv it
    "He sprouts wings and claws, his entire body taken over by the ethereal form of a monstrous black dragon!"
    "His form is connected by a thin cord of darkness to the corpse on the altar. I wonder..."
    "I run to the altar and cut the cord with my sword, destroying his form."
    "We make short work of the cultists after that."
    jump .victorious

label .victorious:
    "The dagger crumbles into dust, which flows beneath the altar."
    "Hey, wait a minute!"
    "I push the altar forward, revealing a secret entrance!"
    $ battle5_won = True
    jump Ruins_innertemple_menu

label Ruins_innerchambers_menu:
    menu:
        "Go inside the temple.":
            jump Ruins_innertemple
        "Aerith":
            call Aerith_oob
        "Silvia":
            call Silvia_oob
        "Return to the great hall":
            "We make our way back to the hall."
            jump Ruins_training_menu
    jump Ruins_innerchambers_menu

label Ruins_innerchambers:
    "As we move past the great hall, we come upon a structure which looks like a small temple."
    if 'Ruins_innerchambers' in seen_before.keys() and seen_before['Ruins_innerchambers']:
        if not battle4_won:
            "There's a brass gate guarded by stone statues on both sides."
            jump .approach_menu
        else:
            "The brass gate is open, and the statues have been reduced to rubble."
            jump Ruins_innerchambers_menu
    $ battle4_won = False
    $ seen_before['Ruins_innerchambers'] = True
    show sil this_is_fine at left
    with moveinleft
    s "A temple within a temple? How unexpected."
    "The entrance to the temple is blocked by a brass gate, and guarded on either side by a warrior statue of stone."
    s "The lock appears easy enough to pick. Shall I?"
    hide sil
    jump .approach_menu

label .approach_menu:
    menu:
        "The only way is forward.":
            jump .approach
        "Go back to the hall":
            "We move back the way we came."
            jump Ruins_training_menu

label .approach:
    show sil normal at left
    with moveinleft
    "As Silvia approaches the gates, purple flames light up in the eyes of the statues."
    np "Look out!"
    "The statues jolt to life, lifting their scimitars into the air."
    show sil scared
    "They approach Silvia with heavy steps leaving their mark on the sand-covered floor."
    show sil trick
    "Silvia evades them easily, and we go on the offensive."
    "The statues are too slow to strike us with their blades, but they also seem impervious to all our techniques."
    "Eventually we manage to get them to strike each other, taking them out."
    hide sil
    jump .victorious

label .victorious:
    show sil hmm at left
    with moveinleft
    s "We must hope that the defence of our future enemies is not as impenetrable."
    "Now undisturbed, Silvia picks the lock with ease, and the gate opens with a creak."
    hide sil
    $ battle4_won = True
    jump Ruins_innerchambers_menu


label Ruins_training_menu:
    menu:
        "Go forward.":
            jump Ruins_innerchambers
        "Aerith...":
            call Aerith_oob
        "Silvia...":
            call Silvia_oob
        "Log out":
            show sil proud
            with moveinleft
            np "I think we should call it a day now."
            s "Very well. Our attempt was heroic nonetheless."
            "We say our farewells and log out."
            hide sil
            scene black with dissolve
            play music "bgm/hope(Ver1.00).ogg"
            return
    jump Ruins_training_menu

label Ruins_training:
    if 'Ruins_training' in seen_before.keys() and seen_before['Ruins_training']:
        "We go down the spiraling staircase, and the great hall unfolds before our eyes."
        jump .goin_menu
    $ battle3_won = False
    $ seen_before['Ruins_training'] = True
    show air 7 at left
    with moveinleft
    show sil normal at right
    with moveinright
    "The woeful chanting grows ever louder, as we move past the living quarters deeper into the dungeon."
    "With trembling steps we walk down a spiraling stairway small enough to induce claustrophobia."
    "At the bottom, a doorway opens to a colossal underground hall."
    show air lip_bite
    a "Wow, it's huge!"
    show sil hmm
    s "And offers no place to hide. We ought to be careful."
    hide air
    hide sil
    jump .goin_menu

label .goin_menu:
    menu:
        "Go in.":
            jump .goin
        "Turn back":
            "We move back up the stairs into the living quarters."
            jump Ruins_outer_menu

label .goin:
    show air 7 at left
    with moveinleft
    show sil normal at right
    with moveinright
    "Everywhere around us, the walls, ceiling and columns are covered with ancient carvings."
    "Curiously, none of the carvings depict dragons. They must be relics from an older time."
    show air 8
    a "Beautiful..."
    "Aerith puts her hand on one of the columns."
    show sil lecture
    s "Do not let down your guard, faithful one!"
    "Silvia's reservations turn out to be appropriate."
    "All of a sudden, we hear a huge thump behind us."
    "A stone slab has fallen over the doorway, blocking the way back!"
    "I'm deafened by the shrieking ostriches and their shouting riders, emerging from hidden compartments in the walls."
    "From the other end of the hallway, a huge ostrich with dragon wings approaches, threatening us with the flames it spits out of its throat."
    show air you_kidding
    show sil annoyed
    "Looks like it's time to..."
    "Fight!"
    "I charge right at the dragon-ostrich! Furious Strike!"
    "Fatality! Superb!"
    "My sword pierces deep into its head, killing the monstrosity instantly."
    show air angry_shout
    show sil rage
    "Aerith and Silvia have already dealt with the rest of the riders."
    hide air
    hide sil
    $ battle3_won = True
    jump Ruins_training_menu

label Ruins_outer_menu:
    menu:
        "Move forward":
            jump Ruins_training
        "Aerith...":
            call Aerith_oob
        "Silvia...":
            call Silvia_oob
        "Go back outside":
            "We return outside."
            jump Ruins_courtyard_menu
    jump Ruins_outer_menu

label Ruins_outer:
    if 'Ruins_outer' in seen_before.keys() and seen_before['Ruins_outer']:
        "We go down the bronze door, arriving at the living quarters."
        if not battle2_won:
            "The novice and the priest are still here, talking."
            jump .approach_menu
        else:
            jump Ruins_outer_menu
    $ battle2_won = False
    $ seen_before['Ruins_outer'] = True
    show air 7 at left
    with moveinleft
    show sil normal at right
    with moveinright
    np "The only way is forward. Let's go in."
    "We open the bronze door beneath us, revealing a steep staircase leading only to the depths of darkness."
    show air blush
    a "W-we aren't going in there, right?"
    show sil taunt
    s "Does your heart not yearn for battle?"
    show air 12
    a "No."
    "This game is like 50 \% fighting..."
    show sil normal
    s "Lead the way, liege."
    "We start walking down the stairs into the black dungeons."
    np "There's light ahead."
    show air angry2
    a "Why is it purple...?"
    show sil  uwot
    s "The dark magic of the Harvester, without doubt."
    "We walk past the torches shining purple in the dark hallway."
    "It must be my imagination, but I can almost feel some malign force emanating from the purple flames and marble floor."
    "Aerith is shivering, and I doubt it's the cold. I can feel a dread chill flowing down my spine."
    show air blush5
    a "D-do you hear something?"
    "She tries to whisper, but the echoes annul her attempt."
    show sil annoyed
    s "They're chanting evil spells to honor their dark deities. This heresy must be stopped!"
    show air disgust
    a "Maybe we could do it later?"
    show sil herp
    s "You are curiously lacking in zeal, priestess."
    show air suspic
    a "Uh, thanks?"
    s "I did not intend a compliment."
    "We really need to get into a battle before they're at each other's throats."
    "It seems my wish will be granted."
    "The ominous chanting grows louder, and the hallway ahead extends to the left and right."
    "I can see bedrolls and an assortment of utilities strewn messily on the stone floor."
    "And people."
    "A man in simple brown robes is talking to a woman wearing purple robes with elaborate embroidery depicting a crimson dragon on each side."
    "They both have blank, stoic expressions, but their eyes glimmer with a zealous spirit."
    "They haven't noticed us just yet."
    hide air
    hide sil

label .approach_menu:
    menu:
        "What should we do?"
        "Approach":
            jump .approach
        "Aerith...":
            call Aerith_oob
        "Silvia...":
            call Silvia_oob
        "Turn back":
            jump .turnback

label .approach:
    "The man looks shocked and points at us, then calls others to his aid!"
    "Novice" "My blood for N'Gashai!"
    "He charges us, wielding a kukri decorated with a dragon's head!"
    "The woman behind him starts casting a spell, materializing the ephemeral form of a dragon over her body."
    jump .victorious

label .turnback:
    "We head back outside, careful to avoid detection."
    jump Ruins_courtyard_menu

label .victorious:
    show air angry_shout at left
    with moveinleft
    show sil rage at right
    with moveinright
    "The fight rages on forever, but eventually we are left the victors, bathed in the blood of the novices."
    show air blush2
    a "Ew, ew, ew, ew!"
    show sil evil_laugh
    s "Yes, the life of our enemies spills on the ground! Mwahahahaa!"
    "The worst part is, this isn't even the weirdest group I've played with."
    hide air
    hide sil
    $ battle2_won = True
    jump Ruins_outer_menu


# label Ruins_cultists:
    # s "Cultists..."
    # "Most of them seem to be novices, wearing brown woolen robes."
    # "In the front, there are two wearing more extravagant robes with embroidery portraying a crimson dragon, one on each side."
    # "One of the novices is bowing down, and they're anointing her head with a strange oil."
    # s "This is worse even than we suspected. We must bring this rite to an end, lest they unleash some great darkness from beyond!"
    # np "You don't have to roleplay all the time, you know."
    # s "I know not what you mean."
    # "I sigh."
    # "For a while at least, they're so focused on the ritual that they haven't even noticed us."
    # menu:
        # "What should we do?"
        # "Silvia, sneak up on them.":
            # jump .sneak
        # "Aerith, try casting...":
            # jump .aerith_cast
        # "Go back outside.":
            # jump .go_back
        # "Wait and see what happens.":
            # jump .wait
    # return





label RuinsStart:
    $ silvia_hidden = False
    call DFO_login
    call DFO_init
    call Ruins_entrance
    call Ruins_courtyard
    jump events_skip_period
    return

label Ruins_courtyard_menu:
    menu:
        "Let's go in.":
            jump Ruins_outer
        "Aerith...":
            call Aerith_oob
        "Silvia...":
            call Silvia_oob
        "I guess we can call it a day.":
            show sil normal at left
            with moveinleft
            np "I guess that's enough for today."
            s "Aren't we going all the way to the end?"
            np "Nah, let's come back and try again some other time."
            s "All right, I suppose."
            scene black with dissolve
            return
    jump Ruins_courtyard_menu

label Ruins_courtyard:
    show air 10 at left
    with moveinleft
    show sil normal at right
    with moveinleft
    "Broken pillars loom ominously around us, and I feel as if someone is gazing at us, hidden somewhere beyond sight..."
    a "This place looks abandoned... Maybe there's no-one here?"
    np "Why would they make a new dungeon without enemies?"
    a "R-right. I guess they wouldn't!"
    np "Wait, what's that?"
    "I point at something glimmering in the distance."
    show sil proud
    s "It appears to be an underground entrance. Well done, liege."
    hide air
    hide sil
    jump .courtyard_menu

label .courtyard_menu:
    menu:
        "Should we approach?"
        "Let's go!":
            "We approach the entrance as it glitters in the sunlight."
            $ seen_before = {}
            $ tooltips = default_tooltips
            jump Ruins_battle1
        "[np_name]...":
            call Nicholas_oob
        "Aerith...":
            call Aerith_oob
        "Silvia...":
            call Silvia_oob
        "Maybe we should just head back to the forest...":
            show air 7 at left
            with moveinleft
            show sil normal at right
            with moveinleft
            np "Actually, Aerith, you've got a point. Let's head back."
            show sil uwot3
            s "What? Liege, you can't be earnest!"
            menu:
                "You're right. I was just kidding.":
                    np "It was just a joke!"
                    s "....."
                    jump .courtyard_menu
                "I'm serious.":
                    np "No, I'm serious. This is probably too tough for us right now."
                    show sil shock
                    s "I would not have expected such behavior from you."
                    "She looks disappointed. Well, it can't be helped."
                    hide air
                    hide sil
                    $ affection_modify('Silvia', -1)
                    play music "bgm/hope(Ver1.00).ogg"
                    return
    jump .courtyard_menu

label Nicholas_oob:
    menu:
        "Return":
            return
    return

label Aerith_oob:
    menu:
        "Cast Light Barrier on...":
            call .light_barrier_target
        "Cast Curing Light on...":
            call .cure_target
        #"Cast Mass Cure"
        #    call .mass_cure
        #"Cast Heal on...":
        #    call .heal_target
        #"Cast Mass Heal"
        #    call .mass_heal
        "Return":
            return
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
            return
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
            return
    call ask_Aerith_to_cast("Curing Light", target_desc, target)
    return

#label .mass_cure:

#label .heal_target:

#label .mass_heal:

label ask_Aerith_to_cast(technique_name, target_desc, target):
    show air 7 at left
    with moveinleft
    np "Aerith, could you cast [technique_name] on [target_desc]?"
    if mp_costs[technique_name] <= current_mp['Aerith']:
        show air blush5
        a "S-sure."
        #call usetechnique('Aerith', technique_name, target)
        if technique_name == "Curing Light":
            call CuringLight("Aerith", target)
            #$ stats_frame(target, 90, current_hp[target], max_hp[target])
        elif technique_name == "Light Barrier":
            call LightBarrier("Aerith", target)
        hide air
        # "She chants the spell, and I'm momentarily blinded by the white light enveloping my body."
    else:
        show air blush6
        a "I'm afraid I don't have enough mana."
        hide air
    return

label Silvia_oob:
    menu:
        "Hide" if not silvia_hidden:
            show sil normal at left
            with moveinleft
            np "Silvia, could you hide yourself?"
            hide sil with dissolve
            "Wordlessly, she conceals herself in the shadows."
            $ silvia_hidden = True
            return
        "Come back from hiding" if silvia_hidden:
            np "Uh, Silvia? You can come out now."
            show sil normal at left with dissolve
            with moveinleft
            "Silvia returns from the shadows."
            hide sil
            $ silvia_hidden = False
            return
        "Return":
            return

label Ruins_entrance:
    scene bg_temple with fade
    play music "bgm/LanayruDesert.mp3"
    show air eyes_wide at left
    with moveinleft
    show sil cat at right
    with moveinleft
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
    show air 10
    a "Uh, can't we just go to the forest like normal...?"
    show sil annoyed
    s "Silence! We shan't run away."
    a "I think you mean 'can't...'"
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
    if not broken_up:
        show air 8 at left
    else:
        show air 7 at left
    "I blink as my eyes adjust to the vibrant hyper-reality surrounding me."
    show air 7 at left with dissolve
    with moveinleft
    show sil normal at right with dissolve
    with moveinleft
    "Silvia and Aerith are already here."
    s "Hi there."
    if broken_up:
        show air 13
        a "Hi..."
        "Aerith looks a bit dismayed. Did I anger her somehow?"
    else:
        "Aerith puts her hands together."
        show air blush7
        a "Great to see you!"
    show sil cat2
    s "Well then, liege, riddle me this. Where are we heading next?"
    "Silvia has a rather, how should I say it, peculiar way with words."
    show air 8
    np "I was thinking we could hit the Ruins of Kvaagwyr today."
    show sil proud
    s "Oh, is that not from the new expansion? Finally, we shall face a proper challenge!"
    show air 9
    a "A challenge? It's not too difficult, is it?"
    show sil hmm
    s "Does your cowardice know no bounds, priestess?"
    show air 7
    np "We can level up way more effectively if we try something a bit harder for a change."
    show air 10
    a "I-if you say so..."
    hide air
    hide sil
    return

label DFO_login2:
    scene bg_vr
    "I pop a pill, put on the equipment, and start up the game."
    jump DFO_init

label DFO_login:
    if not first_login:
        jump DFO_login2
    $ first_login = False
    scene player_room
    play music "bgm/EnterNewLife.mp3"
    nvl clear
    nvlNarrator "Oh yeah, it's time to play some DFO!"
    nvlNarrator "I've assembled the equipment and I'm raring to go!"
    nvlNarrator "It took some soldering, but the mod is ready now too."
    nvlNarrator "With this mod, I'll be skirting the limits of possibility in terms of the level of realism that modern technology can offer."
    nvl clear
    nvlNarrator "It's kind of sad, actually."
    nvlNarrator "I've been improving my immersion with new gadgets for almost half of my life until now."
    nvlNarrator "Every time, it just felt so much more real."
    nvlNarrator "Getting better headsets, a treadmill, my first haptic suit, every time the increase in realism left me gasping in awe."
    nvl clear
    nvlNarrator "And now it's over."
    nvlNarrator "Until we get neural interfaces, I doubt it will be possible to increase immersion any further."
    nvlNarrator "Damn! I can't let the nostalgia get to me. This is it."
    nvlNarrator "For a moment, I look wistully at the white pill I'm holding in my hands."
    nvlNarrator "I place it on my tongue, downing it with a gulp of tap water."
    scene player_room gradient_map with dissolve
    nvl clear
    nvlNarrator "It will take around 10 minutes for the effects to start."
    nvlNarrator "Meanwhile, I'll just boot up the system."
    nvlNarrator "I've been using these pills for a while now."
    nvlNarrator "They're supposed to increase the realism of the VR experience further by messing with neuro-transmitters in your temporal lobe."
    nvlNarrator "Maybe it's just placebo, but I feel like it's working, and strongly."
    nvl clear
    nvlNarrator "Whenever I use these, I completely lose my sense of reality, and can fully immerse myself in the world of games."
    nvlNarrator "They're not supposed to be addictive. I wouldn't have started using them otherwise."
    nvlNarrator "But once you've tried them, there's no going back. Ordinary VR begins to feel too bland, too colorless."
    nvlNarrator "Maybe you could say I'm addicted in that sense."
    nvl clear
    nvlNarrator "They're psychotropic, so they're not exactly legal, of course."
    nvlNarrator "I bought them off the dark web. If cybersec has figured it out, they haven't come knocking yet."
    nvlNarrator "They probably have better things to do. I'm not a seller, after all."
    nvl clear
    nvlNarrator "The guy who {i}is{/i} selling them is really shady, though."
    nvlNarrator "He has been raising his prices recently. Says his stash is running out."
    nvlNarrator "Not sure I buy that. But I have to get these from somewhere, right?"
    nvlNarrator "Buying ware from the black market has its disadvantages. I can't exactly report him to the police..."
    "The login screen boots up in front of me."
    comp "Initializing..."
    comp "Welcome back. Please state username and write password."
    "The accounts are voice-locked, so you'd think you wouldn't need a password."
    "But it's actually a good idea to use two or more authentication methods at once."
    "Double-factor authentication. It's way more secure."
    "You might be able to fake my voice with a recording, but you'd still need to get the password on top of that."
    "Time to log in! My username is..."
    call nameNP
    return

label nameNP:
    $ np_name = ""
    while not np_name:
        $ np_name = renpy.input("Your name was?", allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", length = 32)
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
        if np_name.strip('0123456789_').lower() in atleasttryNames:
            comp "That would be a rather boring name."
            jump nameNP
    comp "Input password."
    comp "Thank you, [np_name]. Logging in..."
    return


# Profanities and stuff, don't look...
init python:
    profanity = ['anal', 'anus', 'arse', 'ass', 'ballsack', 'balls', 'bastard', 'bitch', 'biatch', 'bloody', 'blowjob', 'blow job', 'bollock', 'bollok', 'boner', 'boob', 'bugger', 'bum', 'butt', 'clitoris', 'cock', 'coon', 'crap', 'cunt', 'damn', 'dick', 'dildo', 'dyke', 'fag', 'feck', 'fellate', 'fellatio', 'felching', 'fuck', 'f u c k', 'fudgepacker', 'fudge packer', 'flange', 'hell', 'homo', 'jerk', 'jizz', 'knobend', 'knob end', 'labia', 'lmao', 'lmfao', 'muff', 'nigger', 'nigga', 'omg', 'penis', 'piss', 'poop', 'prick', 'pube', 'pussy', 'queer', 'scrotum', 'sex', 'shit', 's hit', 'sh1t', 'slut', 'smegma', 'spunk', 'tit', 'tosser', 'turd', 'twat', 'vagina', 'wank', 'whore', 'wtf']
    takenNames = ['aerith', 'silvia', 'lucia', 'grayknight', 'nekochan']
    atleasttryNames = ['q', 'qw', 'qwe', 'qwer', 'qwert', 'qwerty', 'a', 'as', 'asd', 'asdf', 'asdfg', 'z', 'zx', 'zxc', 'zxcv', 'zxcvb']
