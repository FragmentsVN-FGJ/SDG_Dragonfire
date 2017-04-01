# The Dating Sim Engine was written by PyTom,
# with updates added by Andrea Landaker.
#
# For support, see the Lemma Soft forums thread:
# http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=31571
#
# It is released under the MIT License - see DSE-LICENSE.txt
#
#
# This is the main program. This can be changed quite a bit to
# customize it for your program... But remember what you do, so you
# can integrate with a new version of DSE when it comes out.

# Set up a default schedule.

init:
    transform flip:
        xzoom -1.0

    transform distant:
        zoom 0.75

    transform gettingcloser:
        zoom 0.75
        linear 1.0 zoom 1.0

    transform wigglemiddle:
        block:
            linear 0.5 xalign 0.5 yanchor 1.0 ypos 1.1
            linear 0.5 xalign 0.40 yalign 1.0
            linear 0.5 xalign 0.5 yanchor 1.0 ypos 1.1
            linear 0.5 xalign 0.60 yalign 1.0
            repeat

    transform rolling:
        linear 0.5 xalign 0.5 yanchor 1.0 ypos 1.4
        linear 0.5 xalign 0.40 yanchor 1.0 ypos 1.5
        linear 0.5 xalign 0.5 yanchor 1.0 ypos 1.4
        linear 0.5 xalign 0.60 yanchor 1.0 ypos 1.5
        repeat

    transform sleep:
        linear 0.5 xalign 0.5 yanchor 1.0 ypos 1.4

    transform ramming:
        zoom 1.0
        linear 0.5 zoom 1.75 yalign 0.5

    transform backwardsramming:
        zoom 1.75
        linear 1.0 zoom 1.0 yalign 1.0

    transform flash:
        pause 0.1
        ypos 3.0
        pause 0.1
        yalign 0.5
        repeat

    transform closeup:
        zoom 1.75
        yalign 0.0

    transform ghost:
        alpha 0.5

    transform getup:
        yalign 0.0
        linear 1.0 yalign 0.5

    transform getup_and_leave:
        yalign 0.0
        xalign 0.5
        linear 1.0 yalign 0.5
        pause 0.5
        linear 1.0 xalign -10.0


    define bgm_battle = "bgm/BGM_Battle_Encounter.mp3" # changed from Battle1.wav
    define bgm_battle_loop = "bgm/BGM_Battle_Zone_Loop.mp3"
    define bgm_cheerful = "bgm/BGM_Cheerful.mp3" # changed from EnterNewLife.mp3
    define bgm_derp_loop = "bgm/BGM_Dumb_Loop.mp3" # changed from fanfare.mp3
    define bgm_dungeon = "bgm/BGM_Dungeon_Ambience.mp3"
    define bgm_sad_loop = "bgm/BGM_Melancholy_Loop.mp3"
    define bgm_main = "bgm/BGM_Piano_Cinematic.mp3" # changed from hope(ver1.00).ogg
    define bgm_loop = "bgm/BGM_Simple_Drums_Loop.mp3"
    define bgm_scary = "bgm/BGM_Trouble.mp3" # changed from wrong.wav
    #kept ones
    define bgm_buzz = "bgm/buzz.wav" #TODO change into original unless it's CC0 or something??
    define bgm_desert = "bgm/BGM_Dungeon_Ambience.mp3" #TODO change into a proper desert music


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

init python:
    credits = ('Script', 'MagusDei'), ('Sprites and hand-drawn backgrounds', 'Qazhax'), ('Background images', 'Snehadri'), ('Programming', 'MagusDei'), ('Programming', 'Qazhax'), ('Logo', 'John Smith'), ('Future music and SFX', 'xZidene'), ('Dungeon and MMO design', 'Bahafyr')
    credits_s = "{size=80}Credits\n\n"
    e1 = ''
    for e in credits:
        if not e1==e[0]:
            credits_s += "\n{size=40}" + e[0] + "\n"
        credits_s += "{size=60}" + e[1] + "\n"
        e1=e[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.99.12.4"

    crt = ImageDissolve("images/crt.png", 0.5, 0)
    #register_stat("Strength", "strength", 10, 100)
    #register_stat("Intelligence", "intelligence", 10, 100)
    register_stat("Fitness", "fitness", 50, 100)
    register_stat("Stress", "stress", 3, 10)
    register_stat("μBC (bits)", "cash", 27126, 999999)

    #dp_period("Morning", "morning_act")
    #dp_choice("Attend Class", "class")
    #dp_choice("Cut Class", "cut")

    # This is an example of an event that should only show up under special circumstances
    #dp_choice("Fly to the Moon", "fly", show="strength >= 100 and intelligence >= 100")

    dp_period("Morning", "morning_act")
    dp_choice("Swimming hall", "swimming", x=300, y=350, tooltip="Entrance fee 3000 bits.")
    dp_choice("Gym", "gym", x=400, y=450, tooltip="Daily fee is 1000 bits.")
    dp_choice("Running Track", "track", x=150, y=200, tooltip="Free entry. A good way to build up fitness.")
    dp_choice("Call Catherine", "callcat", x=1100,y=675, show="not broken_up and day > 1", tooltip="I could try setting up a date...")
    dp_choice("Clean room", "clean", x=350, y=550, tooltip="My room is as unkempt as my hair. Very.")


    dp_period("Afternoon", "afternoon_act")
    #dp_choice("Study", "study")
    #dp_choice("Hang Out", "hang")
    dp_choice("Ice Cream Parlor", "parlor", x=175, y=450, tooltip="Queens Gelateria, best ice cream in town. Prices from 6000 bits up.")
    dp_choice("Restaurant", "restaurant", x=400, y=350, tooltip="Good in case I'm too lazy to cook for myself. Fries for 12 000 bits.")
    #dp_choice("Bowling", "bowling")
    dp_choice("Mall", "mall", x=425, y=180, tooltip="I could look for sales, if it's not too crowded.")
    dp_choice("Library", "library", x=550, y=200, tooltip="Books, computers and a makerspace. Free, of course.")
    dp_choice("Work", "work", x=150, y=550, tooltip="The pay is 9000 bits per day. Not bad.")
    dp_choice("Business school", "business", x=200, y=100, tooltip="I've got no business there, probably.")
    dp_choice("Ruins of Kvaagwyr", "ruins", x=755, y=450, tooltip="A high-level dungeon released as a part of the new expansion for DFO. It will take the whole day to play it.")


    dp_period("Evening", "evening_act")
    #dp_choice("Exercise", "exercise")
    #dp_choice("Play Games", "play")

    dp_choice("Bar", "bar", x=650, y=400, tooltip="Techno bar. Should I get a drink? It's 3000 bits.")
    dp_choice("Movie theatre", "movies", x=350, y=500, tooltip="I could go watch some movies. By myself. For 15 000 bits.")
    dp_choice("VR Arcade", "arcade", x=150, y=400, tooltip="VR Arcade, though I'll probably end up playing retro games. 7000 bits.")
    dp_choice("Catherine's apartment", "cathouse", x=200, y=150, tooltip="I wonder if she's home...?")

    # HELPER FUNCTIONS

    # CASH SYSTEM
    def paycash(amount):
        global cash
        if amount > cash:
            return False
        cash -= amount
        return True

    def say_days(days):
        if days == 1:
            return "yesterday"
        elif days < 7:
            return str(days)+" days ago"
        elif days < 14:
            return "over a week ago"
        elif days < 21:
            return "over two weeks ago"
        elif days < 30:
            return "over three weeks ago"
        else:
            return "over a month ago"

    def say_at_location(location):
        if location == "parlor":
            return "at the ice cream parlor"
        elif location == "movies":
            return "at the movie theater"
        elif location == "arcade":
            return "at the VR arcade"
        else:
            return "somewhere"

    def affection_modify(person, amount):
        global affection
        affection[person] = affection[person] + amount
        if affection[person] > max_affection:
            affection[person] = max_affection
        if affection[person] < 0:
            affection[person] = 0
        return

    def trust_modify(person, amount):
        global trust
        trust[person] = trust[person] + amount
        if trust[person] > max_trust:
            trust[person] = max_trust
        if trust[person] < 0:
            trust[person] = 0
        return

# Define characters
define a = Character("Aerith", color="#FF1493")
define n = Character("Nicholas", color="#191970")
define s = Character("Silvia", color="#9932CC")
define c = Character("Catherine", color="DC143C")
define nvlNarrator = Character(None, kind=nvl, what_xsize = 950, what_size=28, what_xpos=200)

define falldown = CropMove(0.2, "wipedown")

image cat_torso red flip = im.Flip("images/cat/cat_torso red.png", horizontal = True)
image cat normal_down flip = im.Flip("images/cat/cat normal_down.png", horizontal = True)
#image cat_torso red close = im.Scale("images/cat/cat_torso red.png", width=1660, height=1540)
#image cat normal close = im.Scale("images/cat/cat normal.png", width=1660, height=1540)
image cat fast_blink:
    "images/cat/cat normal.png"
    pause 0.25
    "images/cat/cat eyes_closed.png"
    pause 0.25
    "images/cat/cat normal.png"

image baudrillard = Text("{size=36}{color=#fff}\"We will live in this world, which for us has all the disquieting strangeness of the desert and the simulacrum.\" \n \n - {i}Jean Baudrillard{/i}", text_align=0.5)
image thankyou = Text("{size=40} Thank you for playing!", text_align=0.5)
image cred = Text(credits_s, text_align=0.5)
image theend = Text("{size=40}Conglaturation ! ! !\n \n This story is not so happy end. \n \n You have completed a great demo. \n \n And prooved the justice of our culture. \n \n Being the wise and courageour Nick you are, you feel strongth welling in your body. \n \n Now go and wait to challenge again, for ever lasting peace!", text_align=0.5)


image fx daggers:
    "images/fx/fx daggers_0.png"
    pause 0.05
    "images/fx/fx daggers_1.png"
    pause 0.05
    "images/fx/fx daggers_2.png"
    pause 0.05
    "images/fx/fx daggers_3.png"
    pause 0.05
    repeat

image fx fire:
    "images/fx/fx fire_0.png"
    pause 0.1
    "images/fx/fx fire_1.png"
    pause 0.1
    "images/fx/fx fire_2.png"
    pause 0.1
    "images/fx/fx fire_3.png"
    pause 0.1
    "images/fx/fx fire_4.png"
    pause 0.1
    "images/fx/fx fire_5.png"
    pause 0.1
    "images/fx/fx fire_6.png"
    pause 0.1
    "images/fx/fx fire_7.png"
    pause 0.1

label pay(amount):
    $ pay_successful = paycash(amount)
    if pay_successful:
        "I validate the transaction with my wristband."
    else:
        "As I'm about to pay, my wristband flashes a red light with the message: 'Transaction rejected. Bitcoin wallet balance exceeded.'"
    return

label check_wallet:
    "I covertly check my bitcoin wallet."
    "It seems I've got [cash] bits."
    return

# This is the entry point into the game.
label start:

    # Initialize the default values of some of the variables used in
    # the game.
    $ day = 0
    $ calDate = calDate.replace(second=00, hour=8, minute=00, day=3, month=2, year=2024)

    $ broken_up = False
    $ call_ignored = False

    $ truck_handled = True


    # Tooltips for menus
    $ tooltips = {}

    # PROMISE SYSTEM

    $ promises = {}
    $ forgotten_promises = set()
    $ unhandled_forgotten_promises = {}
    $ unkept_promises_personal_counter = {}
    # Promises are stored in a dictionary mapping (act, day) -tuples to [person, activity, boolean]-lists indicating
    # the person the promise was made to, the promise itself, and whether the promise is
    # fulfilled (True), or not (False). The label night checks whether the promises for that day have been fulfilled and
    # gives a warning if they haven't. There're special date events linked to promises.

    # WORK SYSTEM
    $ work_counter = 6
    $ work_payment = 9000
    # At the start of each week, you get work_payment bits for each day you've worked during the last week

    # AFFECTION AND TRUST
    $ max_affection = 10
    $ max_trust = 10
    $ affection = {'Catherine': 5, 'Silvia': 5}
    $ trust = {'Catherine': 5, 'Silvia': 5}

    # Variables
    $ parlor_visited = False
    $ first_login = True

    $ blade_sphere_control = False
    $ Aerith_angry = False
    $ Aerith_hurt = False
    $ Aerith_barrier = False
    $ curing_light = False

    scene black

    show baudrillard at truecenter with dissolve
    pause 5.0

    scene black with dissolve
    # Show a default background.
    scene bg_field with dissolve

    # The script here is run before any event.

    # Battle music
    play music bgm_battle

    n "Damnit!"

    with hpunch

    # Sound effect

    "The monster sinks its fangs into my skin, drawing blood!"

    # Screen shake & sound

    "I can feel the warm liquid trickling down my skin... Damnit!"

    with hpunch

    "With a huge throwing motion, I manage to shed the weasel, but others are already circling around me."

    "They're huge. But I'm not actually worried. Not yet, anyway."

    show air 10 at distant, left with moveinleft

    "I see Aerith in the corner of my vision."

    "She's surrounded by the creatures as well, trying to keep them away
    with her staff."

    "Um, shouldn't she just cast a spell or something?"

    hide air with moveoutleft

    "Silvia is nowhere to be seen. Hiding somewhere in plain sight, no doubt."

    "The weasels are circling me, staring at my wound with blood-hungry eyes."

    menu:
        "Okay, let's go!"
        "Fight!":
            jump WeaselFight
        "Protect Aerith!":
            # You pull the weasels to Aerith
            jump WeaselPull
        "Time to retreat!":
            jump WeaselRetreat

label WeaselPull:
    "Trampling the weasels around me, I run to protect Aerith!"
    "Damn, they're following me! Of course this would happen!"
    show air blush12 at left with moveinleft
    "Now all of them are focused on us. Aerith is holding her hands to her mouth, gasping for air."
    jump WeaselProtectAerith

label WeaselFight:
    # Silvia uses hail of daggers

    "I'll just have to beat them off!"

    "I slash at the pack with my sword!"

    with vpunch

    "The weasels screech in pain, flying off in a torrent of blood!"

    "But there's too many of them! No matter how many times I attack, more are lashing right at me!"

    s "Protect yourself."

    "I hear Silvia's voice from somewhere nearby, and instantly understand."

    "I raise my shield just in time as a hail of daggers falls all around me, piercing the weasels and spraying blood everywhere!"

    with vpunch
    with vpunch

    "The monsters lie dead on the grass, painted crimson with blood."

    "I turn around to thank Silvia, but then I hear Aerith scream from behind."

    jump WeaselAerithScream

    return

label WeaselAerithScream:
    # You can run to Aerith, tell her to use the barrier spell, or tell Silvia to use her hail of daggers again

    show air 10 at distant, right with moveinright

    "She's still surrounded by a pack of weasels, desperately pushing them off!"

    "Their gnawing at her health. She won't last at this rate!"

    $ tooltips = {}
    $ tooltips["Tell her to cast her barrier spell"] = "A barrier of light temporarily protects the caster from all attacks."
    $ tooltips["Tell Silvia to use the hail of daggers"] = "Raining death from above. Just make sure your allies are not caught in the range!"

    menu:
        "Run to save her!":
            "I run through the pack to her side, seeking to protect her from harm!"
            show air 10 at left with moveinright
            jump WeaselProtectAerith
        "Tell her to cast her barrier spell":
            jump WeaselAerithBarrier
        "Tell Silvia to use the hail of daggers":
            jump WeaselSilviaHailOfDaggersAerithAlone

    return

label WeaselSilviaHailOfDaggersAerithAlone:
    hide air with moveoutright
    show sil normal at center with moveinleft
    n "Silvia! Finish them with a hail of daggers!"
    show sil mwerrllyy
    "Silvia smirks, hesitating a bit."
    s "You sure about that, liege?"
    show sil taunt
    "Then, her smile turns fiendish, and she shrugs."
    s "Here goes!"
    hide sil with vpunch
    "She launches into the air and begins her technique."
    show air blush12 at center with vpunch
    "The daggers rain upon the weasels, killing them instantly!"
    show air 12
    "Of course, they hit Aerith as well. I really should have realized that."
    hide air with falldown
    with vpunch
    "She falls on her knees, but seems to be alive for the moment."
    "In any case, the weasels are dealt with."
    $ Aerith_angry = True
    $ Aerith_hurt = True
    jump WeaselVictory

label WeaselAerithBarrier:
    n "Aerith! A barrier!"
    show air 2
    "Aerith's eyes flit from foe to foe in terror, but then she begins casting."
    show air chant
    a "Luxphoros, protect thy faithful in a time of need. Light Barrier!"
    show air chant2
    pause 0.5
    show air 8
    "I watch as a sphere of searing white light envelops Aerith."
    $ Aerith_barrier = True
    "The weasels can't get to her now. However, they are turning towards me instead!"
    menu:
        "Run to Aerith":
            "I run towards the pack, ready to protect Aerith!"
            show air at gettingcloser, left with moveinleft
            jump WeaselProtectAerith
        "Better retreat!":
            hide air with moveoutleft
            # Barrier wears off
            jump WeaselRetreat

label WeaselProtectAerith:
    "The weasels are baring their fangs at us, and Silvia is nowhere to be seen."

    "Aerith is cowering behind me, trying to think of a spell to cast."

    if Aerith_barrier:
        "Her light barrier is still protecting her, but who knows how long it'll last."

    "Well, I'm a guardian, so I should be able to do this, right?"

    $ tooltips = {}
    $ tooltips["Offensive technique: Furious strike!"] = "Bash a foe with utmost fury. If they attempt to parry, their weapons will surely be broken, and their allies shall flee in terror!"
    $ tooltips["Protective technique: Blade Sphere Control!"] = "Ultimate protective technique. Blocks all physical attacks around you regardless of direction."
    $ tooltips["Aerith Spell: Depths of Slumber!"] = "Sleeping powder causes weak enemies to fall asleep."
    $ tooltips["Silvia Technique: Hail of Daggers!"] = "Raining death from above. Just make sure your allies are not caught in the range!"
    $ current_tooltip = "What should I do?"

    menu:
        "Offensive technique: Furious strike!":
            jump WeaselFuriousStrike
        "Protective technique: Blade Sphere Control!":
            jump WeaselBladeSphereControl
        "Aerith Spell: Depths of Slumber!":
            jump AerithDepthsOfSlumber
        "Silvia Technique: Hail of Daggers!":
            jump WeaselSilviaHailOfDaggers

    return

label WeaselBladeSphereControl:
    if Aerith_barrier:
        "Aerith's barrier is beginning to fade."
        $ Aerith_barrier = False

    "I close my eyes and focus to find the calm within."

    "Blade Sphere Control!"

    $ blade_sphere_control = True

    "I hold my blade in a protective stance, ready to block any attack, from any direction!"

    "The weasels are still scuttling around us, but they don't dare to approach."

    "It seems we have reached a standstill."

    $ tooltips = {}
    $ tooltips["Special Technique: Taunt"] = "A taunt so scathing as to send all enemies into blind fury."
    $ tooltips["Aerith Spell: Curing Light"] = "Green light cures one person's wounds."
    $ tooltips["Aerith Spell: Depths of Slumber"] = "Sleeping powder causes weak enemies to fall asleep."
    $ tooltips["Silvia Technique: Hail of Daggers"] = "Raining death from above. Just make sure your allies are not caught in the range!"

    menu:
        "Special Technique: Taunt":
            jump WeaselTaunt
        "Aerith Spell: Curing Light":
            jump WeaselAerithCuringLight
        "Aerith Spell: Depths of Slumber":
            jump AerithDepthsOfSlumber
        "Silvia Technique: Hail of Daggers":
            jump WeaselSilviaHailOfDaggers

    return

label WeaselSilviaHailOfDaggers:
    n "Silvia! Use your hail of daggers, now!"

    "Silvia doesn't need to be told twice."

    if blade_sphere_control:
        "As the flurry of thrown knifes falls upon us, I block each and every one coming towards me and Aerith!"
        with vpunch
        with vpunch
    else:
        "The blades fall upon us, a rain of scathing edges!"
        with vpunch
        if curing_light:
            "But due to the healing, we manage to survive despite the wounds."
        else:
            show air 12
            "And we're hit! I can almost taste the pain!"
            "Damnit! I don't think I can move anymore!"
            if Aerith_barrier:
                "At least Aerith was saved by her barrier."
            else:
                "Still, it seems both of us remain alive."
                $ Aerith_hurt = True

    hide air with moveoutleft
    "The weasels aren't as lucky, and the blades pierce their hearts and throats."

    "Only a pitiful whimper is left of them now."

    jump WeaselVictory

label WeaselTaunt:
    "I can't help but smirk."

    "I happen to know a technique for situations exactly like this."

    n "What, you afraid or something? Here I thought I was fighting a pack of weasels..."

    n "... but turns out you're just a bunch of chickens!"

    "You'd think they couldn't understand me."

    "But this is a special guardian technique, passed down from ancient times through generations of invincible warriors!"

    "I'm almost laughing as I see the weasels seething with rage."

    "Suddenly, the entire pack pounces on us, claws flashing in the air!"

    "But they can't get through my perfect defense!"

    with vpunch
    with hpunch
    with vpunch

    "My sword strikes each and every one of them, cutting of their heads and piercing their beating hearts!"

    jump WeaselVictory

label WeaselAerithCuringLight:
    n "Aerith! Cast Curing Light on us!"

    show air blush
    "Aerith seems flustered for a moment, then begins chanting the spell."

    show air chant2
    pause 0.5
    show air chant
    a "Thou art the sun which giveth life and light to the creatures of the earth..."
    show air 13
    a "Lord Luxphoros, lend us your power. Curing light!"
    show air 2
    "I feel the warm, green glow closing the wounds on my arms."

    "Freshly invigorated, we return our focus to the battle at hand."

    "The weasels are already getting ready to pounce. We have to react fast!"

    $ curing_light = True

    $ tooltips = {}
    $ tooltips["Offensive Technique: Furious Strike!"] = "Bash a foe with utmost fury. If they attempt to parry, their weapons will surely be broken, and their allies shall flee in terror!"
    $ tooltips["Silvia Technique: Hail of Daggers!"] = "Raining death from above. Just make sure your allies are not caught in the range!"

    menu:
        "Offensive Technique: Furious Strike!":
            jump WeaselFuriousStrike
        "Silvia Technique: Hail of Daggers!":
            jump WeaselSilviaHailOfDaggers

    return

label WeaselFuriousStrike:
    hide air moveoutleft
    "Time to go on the offensive!"

    "I raise my blade above my head, preparing to unleash my technique."

    "But I am interrupted as one of the animals jumps right at me!"

    with hpunch

    "Its fangs and claws tear into my arm!"

    if curing_light:
        "However, thanks to the healing, I barely feel it."
    else:
        "Aah, I'm not gonna survive for much longer at this rate!"

    with hpunch

    "I shake it off my gauntlet, and prepare the technique again."

    n "Furious Strike!"

    "I slam the critter with my sword!"

    with vpunch
    with vpunch

    "The steel runs right through its torso, hitting the ground with unbelievable power!"

    "The earth trembles as a shockwave emanates from where the weasel was crushed."

    "The rest of the weasels flee in terror."

    jump WeaselVictory

label AerithDepthsOfSlumber:
    n "Aerith! Cast Depths of Slumber!"

    show air blush9
    pause 0.25
    show air blush8
    pause 0.25
    show air blush9
    "Aerith blinks, then nods and begins casting the spell."
    show air chant

    "The weasels aren't about to let that happen!"

    "Three of them jump right at us!"

    if blade_sphere_control:
        # Success
        "I smirk. They're never getting through my perfect defense!"
        "A single swing deals with all of them. Meanwhile, Aerith finishes her spell."
        jump AerithDepthsOfSlumberSuccess
    else:
        "I manage to fend off two, but the remaining one catches Aerith by surprise."
        if Aerith_barrier:
            "Still protected by her barrier, she manages to finish the spell!"
            jump AerithDepthsOfSlumberSuccess
        else:
            show air blush with hpunch
            "Her spell is interrupted as she grapples with the weasel."
            "The rest of the pack is already preparing to pounce. We need to act fast!"
            $ tooltips = {}
            $ tooltips["Offensive technique: Furious strike!"] = "Bash a foe with utmost fury. If they attempt to parry, their weapons will surely be broken, and their allies shall flee in terror!"
            $ tooltips["Silvia Technique: Hail of Daggers!"] = "Raining death from above. Just make sure your allies are not caught in the range!"

            menu:
                "Offensive technique: Furious strike!":
                    jump WeaselFuriousStrike
                "Silvia technique: Hail of Daggers!":
                    jump WeaselSilviaHailOfDaggers
    return

label AerithDepthsOfSlumberSuccess:
    show air 4
    pause 0.25
    show air 5
    pause 0.25
    show air 6
    a "Gift them with a peaceful sleep!"
    show air 8
    a "Depths of Slumber!"
    "All around us, a glowing powder descends on the weasels, and they fall asleep one by one."
    show effect_sleep at truecenter with dissolve
    hide air with moveoutleft
    hide effect_sleep with dissolve
    pause 0.5
    "We retreat, and Silvia finishes them off with a flurry of daggers."
    "They shall trouble us no more."
    jump WeaselVictory

label WeaselRetreat:
    # Silvia appears in front of you: "Good thinking!"
    "I turn around to run!"
    show sil taunt at flip, right with moveinright
    "Out of nowhere, Silvia appears beside me with a teasing smile."
    s "Good thinking, liege! You are pulling all of them towards you."
    "Glancing behind, I see the whole pack on my tail!"
    show sil cat
    "Heheh, this wasn't really my intention, but no way I'm admitting that..."
    hide sil with dissolve
    "Silvia slips back into the shadows. From the corner of my eye, I see Aerith
    running from the pack behind me!"
    show air blush2 at flip, right with moveinright
    $ Aerith_angry = True
    if Aerith_barrier:
        "Damn! Her barrier must have worn off!"
        $ Aerith_barrier = False
    "I stop in my tracks, and she runs behind me."
    hide air with moveoutleft
    show air 10 at left with moveinleft
    jump WeaselProtectAerith

label WeaselVictory:

    play music bgm_derp_loop

    hide air

    show sil normal at left with moveinleft

    "Silvia emerges from her hiding place, and I walk to her."

    show sil phew

    s "Whew! An enjoyable workout, was it not?"

    show sil cat2

    "She flashes a wide grin."

    s "Seeing all that blood really makes my stomach tickle!"

    if Aerith_hurt:
        show air angry2 at flip, center with moveinright
        "Aerith comes towards us, visibly hurt."
    else:
        show air 9 at flip, center with moveinright
        "Aerith approaches as well."

    if Aerith_angry:
        show air angry_shout
        a "What the hell were you doing!? I could have died!"
        "I touch the back of my neck, slightly embarrassed."
        n "I'm sorry, don't know what I was thinking, really."
        show air angry
        n "Don't take it too seriously. It's just a game, right?"
        n "You would just have revived at the cathedral's teleporter."
        show air 7
        "Aerith pouts, folding her arms."
        a "Don't you think I know that?"
    else:
        "Her earlier terror has been replaced by disgust."
        show air blush2
        a "Aah, there's blood everywhere, even my robes are all red... Eek!"
        "She is startled by a weasel head, rolling on the ground."
        show air 9
        a "Why is this game so gory!?"
        n "Uh, you know you can turn it down in the settings, right?"
        show air 2
        a "Y-yes, of course I do. Which is why I'll do that now."
        show sil hm
        s "Come now, the gore is the best part!"
        show air 7
        "Aerith gives her a mean look, but doesn't retort."
        n "Well, I just think it's good for realism."

    n "Anyway, thanks for grinding with me. I guess I'll call it a day."
    show sil normal
    show air 8
    "We say our farewells, and I log off."
    scene black with crt
    "Taking off my headset, it takes a while for my eyes to adjust to the dim lighting of my room."
    jump RoomDescription
    return

label RoomDescription:
    play music bgm_buzz

    scene player_room with dissolve

    nvlNarrator "Not that there's much to see, in any case."
    nvlNarrator "It's a small, dirty one-room apartment overlooked by a single, large window with eternally closed curtains."
    nvlNarrator "There's not anything meaningful behind them anyway. Just the gray exterior of another apartment building."
    nvlNarrator "Why they even bothered making a window so large for such a dreadful view is beyond me."
    nvlNarrator "My eyes linger on the shadows of empty coke bottles and assorted trash littering the small, barely sun-lit floor space."
    nvlNarrator "I really should throw that pizza slice away."
    nvl clear
    nvlNarrator "The only thing of note here is the VR equipment, which has eaten all of my wages to date."
    nvlNarrator "I've got the full setup. Head-mounted display, omnidirectional treadmill, haptic feedback suit, everything I could buy."
    nvlNarrator "This project already started in middle school, when I got the Oculus Rift as a gift from my parents."
    nvlNarrator "Since then, I've been obsessively buying more and more amazing gadgets in search of ever-deepening immersion."
    nvlNarrator "And to top it all of, due to the weight of the HMD and the suit, and the exercise provided by the omnidirectional treadmill, I'm actually in great shape!"
    nvl clear
    nvlNarrator "Well, I have to be, to be able to use this for longer than an hour at a time."
    nvlNarrator "Most other people don't care about immersion as much as I do, so they just have a basic setup that they can use seated."
    nvlNarrator "Plebs."
    nvlNarrator "I detach the treadmill's harness from my waist, proceeding to hop off."
    nvl clear
    play music bgm_main
    scene bg_vr with dissolve
    nvlNarrator "After the natural disorientation and nausea of entering the bleaker tonalities of reality has passed away, I place the HMD on the floor."
    nvlNarrator "The headset is brand new, with fresnel lens and dual 8k-screens providing a 210-degree field of view at 120 frames per second."
    nvlNarrator "In other words, virtually indistinguishable from reality. Though just try to run photorealistic graphics at those speeds!"
    nvlNarrator "Only the new line of GPUs Nvidia released last year is anywhere near capable of outputting those resolutions. I need eight of them just to run Dragonfire Online."
    nvl clear
    scene player_room with dissolve
    nvlNarrator "I start to take off the haptic feedback suit."
    nvlNarrator "This is the most annoying part of the process. It takes forever to set up and disassemble all the equipment."
    nvlNarrator "I've gotten rather skilled at it, though, getting down from about half an hour to just around ten minutes."
    nvlNarrator "At least the suit looks cool. Kind of like Batman in the 8k remaster of the Dark Knight."
    nvlNarrator "It uses electric feedback to generate haptic impressions all around your body. There's also a sort of reverse
    exoskeleton with electric motors to simulate the feeling of weight and pressure."
    nvl clear
    nvlNarrator "There's still some things I've been thinking of trying. It's possible to modify the suit to produce actually painful
    shocks."
    nvlNarrator "It's a bit dangerous, though. I saw a news story about a man who was found dead in his home. He had botched the modding,
    and his rig gave him a jolt of over 80 milliamperes. Instant cardiac arrest."
    nvlNarrator "I already have everything set up to try it out. I just need to gather the courage to do so."
    nvlNarrator "One of these days, for certain..."
    "Suddenly, my wristband vibrates to signal a call."
    "I read the name projected on my forearm."
    "{color=#f00}Catherine.{/color}" # Can this be colored red?
    "My heart skips a beat, and I hover my finger over the ignore button."
    "Then, I manage to get a hold of myself. Lifting my index finger to my ear, I pick up the call."
    n "Hi."
    "A cold, smooth voice responds from the other side. A woman I know all too well."
    c "Hello there, Nicky."
    n "It's been a while, huh."
    c "Indeed." # Change font?
    "Could this atmosphere get any more tense? Just get to the point already!"
    c "Have you had fun? With that little game of yours?"
    "She sounds more hurt than angry now."
    n "Listen, Cat, I've just been busy with work and..."
    show cat angry at flip, ghost, right, closeup
    show cat_torso yellow at flip, ghost, right, closeup
    with Dissolve(0.1)
    with hpunch
    c "That's a lie!" # Furious sprite
    "In my mind's eye, I see her face contort with rage."
    hide cat
    hide cat_torso
    with Dissolve(0.15)
    c "Just, please Nick, just don't lie to me."
    "There's an awkward silence as I stumble for words."
    c "Nick, we... we need to talk."
    n "Cat, I... I'm sorry. Look, let's go out sometime. We can go to that ice cream parlor you like."
    c "I... yes. That... let's do that."
    n "Let's meet there tomorrow afternoon, 2pm. It's on me."
    c "Thanks, Nicky. You're sweet... sometimes."
    "She hangs up, and I immediately begin to regret the recklessness of my promise."
    "I'm not getting pay until Monday, and my wallet's practically empty. If she wants something expensive..."
    "I sigh. What won't a man do for love?"
    $ promises[('parlor', 1)] = {("Catherine", "meet"): False}

    window hide
    pause 2
    nvl clear
    window show

    play music bgm_scary

    nvlNarrator "My dreams are uneasy that night."
    nvlNarrator "I am lying on the floor of my apartment."
    nvlNarrator "Catherine comes to me, laughing."
    nvlNarrator "She hates me. Hates me."
    nvlNarrator "There’s a knife in her hands now."
    nvlNarrator "I don’t love her enough."

    # nvl clear

    nvlNarrator "That’s Silvia’s dagger! Why do you have that?"
    nvlNarrator "Silvia appears from the shadows. She’s enraged."
    nvlNarrator "Cat stole her knife."
    nvlNarrator "Only she has the right to use it."
    nvlNarrator "It was her gift to me."
    nvlNarrator "She grabs the knife, and there’s a hail of daggers, and everything is red and Sil laughs and laughs and laughs and I wake up."

    nvl clear

    play music bgm_main

    nvlNarrator "My eyes blink open as the timed lights in my room reach their brightest setting."
    nvlNarrator "For a moment, I just lie in bed, doing my most to calm down."
    nvlNarrator "It was just a dream. Just a dream."
    nvlNarrator "I can’t even remember what happened in it. Can’t remember."
    nvlNarrator "Something about Cat or Dragonfire Online or something. I’d better just forget it."
    nvl clear
    nvlNarrator "Rising from the bed, I feel the pangs of oncoming headache as my earlier promise re-emerges into my consciousness."
    nvlNarrator "I sigh yet again. I’m not sure I’m ready to face Cat in this state."
    nvlNarrator "I’m tempted to just boot up Dragonfire Online and play ‘til evening."
    nvlNarrator "But I can’t do that. I’m a man of my word."
    nvlNarrator "At least, I hope to be."
    nvlNarrator "I wouldn’t break a promise if it got me killed!"
    nvl clear
    nvlNarrator "My stomach growls as I stretch my arms far towards the ceiling, careful not to hit the lamp."
    nvlNarrator "Time to make some breakfast, I guess. And then, a plan for the day."

    # Quest Log
    #call createlog

    # $ log.keyon()
    # $ log.assign("Meet Catherine at the Ice Cream Parlor")

    # show screen tracker

    jump day

label parlorStart:
    $ cat_mood = 0
    $ parlor_visited = True

    scene parlour_in

    $ ice_cream = None
    "Queens Gelateria is a mixed Italian-American -style ice cream parlor close to the center."
    "The place is surprisingly full even though it's already February."
    "I mean, summer's basically over, right?"
    "It's only 21 degrees Celsius outside. After the heat wave last week, you almost need a jacket."
    "We used to come to this place often with Catherine."
    "She can't get enough of the ice cream here."
    "It is good, I'll admit. But also ridiculously expensive."
    "I suppose being right across from the stock exchange guarantees rich customers."

    show cat normal_down at right, flip
    show cat_torso red flip at right behind cat
    with moveinright

    "Today she's not as elated as usual. Something's on her mind."
    "Well, I guess it's obvious what."
    c "Which one should I choose...?"
    "How about the cheapest one on the menu?"
    "No way I'm saying that out loud though."
    c "I can't decide..."
    "I make a small smirk."
    n "Just close your eyes and I'll decide for you."
    show cat eyes_closed_smile at right, flip
    "My little kittie has never been good at making up her mind."
    "She is always overthinking things, trying to balance every possible variable so as to reach the optimal decision."
    "For her, it's not so simple as choosing the one that tastes best."
    "Right now, she's probably trying to account for the taste, the price, the calories, the amount of exercise she got last week, and the temperature outside."
    "I guess business people can also be like that sometimes."
    "Well, let's have a look at the choices."
    "The cheapest choice would be 'Strawberry-Chocolate mix'. Two large scoops of the titular flavors at a price of 6000 bits."
    "I'm not sure Cat would appreciate me being a cheapskate, but it would be easier on my wallet."
    "Going to the other end of the price range, there's Rockefeller Parfait."
    "A whopping 12 scoops of ice cream with six different toppings including marshmellows and cherries. Costs 24 000 bits."
    "On the plus side, we could eat it together."
    "Or I could go with her favorite. The Chocolate-Peanut butter Sundae with maple syrup sauce. Mouth-wateringly delicious, but ridiculously fatty."
    "I'm sure she would love it, but glancing at her T-shirt, I see a small problem with that choice."
    "Catherine is very strict about her physique. She does cross-fit, and always
    buys into these fitness fads."
    "She's wearing an activity-tracking T-shirt which changes color to indicate her movement during the day."
    "It's bright red, so she must have skipped her morning gym. In that case, she might not want anything too fatty."
    "Anyway, the sundae costs 12 000 bits. Not exactly cheap, but you're paying for quality."
    "While her eyes are closed, I tap my wristband to check the status of my bitcoin wallet."
    "The numbers are projected on my wrist. I've got [cash] bits."
    if cash >= 30000:
        "Easily enough even for the most expensive one."
    elif cash >= 24000:
        "Just barely enough for the most expensive one, should I decide to go with that."
    elif cash >= 12000:
        "That's enough for her favorite, at least. Although I can forget about getting the most expensive one."
    elif cash >= 6000:
        "Barely enough to get the cheapest one..."
    else:
        "Damn. Not even enough to get the cheapest one!?"
    menu:
        "Well, which should I take?"
        "The expensive one" if cash >= 24000:
            "Well, at least I won't go hungry with this choice."
            $ ice_cream = "expensive"
            $ paycash(24000)
        "The cheap one":
            "Sorry, Cat. I just don't have the money."
            $ ice_cream = "cheap"
            if cash < 6000:
                "I show the cashier the balance of my wallet, and he winks, lowering the price so I can just barely pay it."
                $ cash = 0
            $ paycash(6000)
        "Her favorite" if cash >= 12000:
            "She might not admit it, but I'm sure she'll be happy."
            $ ice_cream = "favorite"
            $ paycash(12000)
    n "I'll have this one."
    show cat normal at right, flip
    cashier "Excellent choice, sir. Will you be eating here?"
    n "Yes."
    cashier "I'll bring it to your table."
    "I press my finger on the reader to validate the transaction, and we go sit at a fancy table outside."
    scene parlour_out with fade
    show cat normal_down at center, closeup
    show cat_torso red at center, closeup behind cat
    "There's no knowing when the next heat wave will hit us, so better make use of the cool weather while it lasts!"
    jump parlorConversation

label parlorConversation:
    "There's a bit of an awkward silence as we sit down. Cat is staring at the table, avoiding eye contact."
    "She's fiddling with a napkin, deliberating something, but can't get the words out."
    $ parlorwait = False
    $ parlorapology = False
    $ parloridle = False
    menu:
        "Wait for her to say something":
            jump parlorWait
        "Try to make conversation":
            jump parlorIdle
        "Apologize":
            jump parlorApology

label parlorApology:
    $ parlorapology = True
    show cat normal_downright
    n "Look, Cat, I'm sorry for not calling you for a while. I've been really busy."
    "She squeezes the napkin with her hands."
    c "Busy with Dragonfire Online, that is."
    "I'm surprised she remembered the name. She's not much of a gamer."
    n "T-that too. I mean, you know me, right?"
    c "Sometimes, Nicholas, I think I know you too well."
    "I swallow. She's not going to..."
    menu:
        "Promise to make it up to her":
            jump parlorMakeUp
        "Try to console her" if not parloridle:
            jump parlorConsole
        "Get angry" if parloridle:
            jump parlorAngry
        "Remain silent" if not parlorwait:
            jump parlorWait
        "Beg her not to leave you" if parlorwait:
            jump parlorBeg

label parlorMakeUp:
    n "Look, I'll make it up to you! I'm honestly sorry for what I did. You can't stay mad at me, right?"
    "She frowns."
    show cat frown
    $ cat_mood += 1
    c "We'll just have to see about that, won't we?"
    n "I'll take you somewhere, let's go to the movies or..."
    c "Nick, you don't have to take me anywhere. Just - please - don't ignore me."
    menu:
        "Promise to spend more time with her":
            call parlorInterrupt
            jump promiseTime
        "Promise to go to the movies with her":
            call parlorInterrupt
            jump promiseMovies
        "Offer to play DFO with her":
            call parlorInterrupt
            jump offerDFO

label promiseTime:
    n "I'll spend more time with you from now on. I promise."

    if cat_mood < 0:
        "She doesn't take that too kindly."
        show cat anger
        c "Yeah, just like last time!"
        "She gets up and storms out, leaving her half-eaten ice cream behind."
        $ affection_modify('Catherine', -2)
    else:
        show cat longing
        "She seems a bit sad."
        c "I guess I just have to believe you. Again."

    window hide
    scene black with Dissolve(5.00)
    pause 3.0

    return

label promiseMovies:
    n "I'll take you to the movies."

    if cat_mood < 0:
        show cat tired
        "She purses her lips."
    else:
        show cat teary2
        "She flashes a sad smile."

    c "Which one?"
    n "Erm, whatever you'd like?"
    show cat eyes_closed_smile
    c "Lover's Abandon."
    show cat teary2
    "Darn, that's some boring chick flick."
    n "Ahaha, sounds great!"
    $ affection_modify('Catherine', +2)

    window hide
    scene black with Dissolve(5.00)
    pause 3.0

    return

label offerDFO:
    n "Cat, I'm a gamer. If you really want to spend time with me..."
    "She raises an eyebrow."
    n "... Let's play some DFO together! What do you say?"

    if cat_mood < 0:
        show cat something
        "Her expression alternates between anger and frustration."
        c "What makes you think I'd be interested in that stupid game?"
    else:
        show cat longing
        "She looks away from me. I guess that's a no."
        c "I'm willing to accept that you like the game. But..."

    show cat normal

    c "You really need to return to reality, Nicholas. You get too easily obsessed with these things."
    n "Come on, just try it out. I never expected to actually like your dance lessons when you dragged me there!"
    show cat normal_downright
    c "... You just don't get it."

    window hide
    scene black with Dissolve(5.00)
    pause 3.0


    return

label parlorIdle:
    "I try to force a smile."
    n "You curious about the ice cream I ordered?"
    show cat something
    "She clenches her teeth."
    c "Not particularly."
    "Darn, she's really upset, isn't she?"
    jump parlorConsole

label parlorConsole:
    $ parloridle = True
    n "Kittie..."
    $ cat_mood -= 1
    show cat something2 with vpunch
    "She slams her fist on the table."
    c "Don't call me that! First you disappear for two weeks, then I call you and you act as if nothing has happened!"
    show cat something

    menu:
        "Get angry":
            n "It's because you're such a psycho!"
            show cat surprise
            "Catherine's eyes widen in shock, and I immediately regret saying that."
            show cat something
            "However, empowered by fury, I go on."
            jump parlorAngry
        "Apologize" if not parlorapology:
             jump parlorApology
        "Promise to make it up to her" if parlorapology:
            jump parlorMakeUp
        "Remain silent" if not parlorwait:
            jump parlorWait
        "Beg her not to leave you" if parlorwait:
            jump parlorBeg

label parlorAngry:
    n "You don't control my life, and you can't tell me what to do!"
    show cat angry
    c "Nick, I'm only trying to help you! Can't you see you're hurting yourself!?"
    show cat anger
    c "You're 23 and working as some cleaner because you can't be bothered to study and actually get yourself somewhere in life!"
    menu:
        "Threaten to break up with her":
            call parlorInterrupt
            jump parlorBreakUp
        "Argue with her":
            call parlorInterrupt
            jump parlorArgue
        "Call her out on her hypocrisy":
            call parlorInterrupt
            jump parlorHypocrisy

label parlorBreakUp:
    "I gulp, trying to gather strength."
    n "I think we need to break up."
    n "I... I'm sorry, Catherine."

    if cat_mood < 0:
        show cat fast_blink
        "She blinks, her eyes wet with tears."
        show cat sad
        "Without showing me any, she gets up and leaves."
        show cat at getup
        show cat_torso at getup
        pause 0.75
        show cat at offscreenright
        show cat_torso at offscreenright
        with moveoutright
    else:
        show cat sad
        "She licks on her spoon, but says nothing."
        "For what feels like an eternity, we just sit there, together yet separate."

    window hide
    scene black with Dissolve(5.00)
    pause 3.0

    $ broken_up = True
    $ affection_modify('Catherine', -2)

    return

label parlorArgue:
    n "What you said about me not studying."
    n "I am going to study. I just need to decide what."
    n "I feel like most of the choices available are just pointless."
    n "If only reality was more like a game..."

    if cat_mood < 0:
        show cat anger
        c "You're a fucking addict, you know that?"
        n "Gaming keeps me together! Why can't you get that!?"
        c "Whatever. Just keep playing your games. No need to call."
        "With that, she storms out."
        show cat at getup_and_leave
        show cat_torso at getup_and_leave
        $ broken_up = True
        $ affection_modify('Catherine', -2)
    else:
        show cat normal_down
        "She looks down at her ice cream."
        c "It wouldn't be any better."

    window hide
    scene black with Dissolve(5.00)
    pause 3.0

    return

label parlorHypocrisy:
    n "You're critisizing me for not studying. But you're the one who's always complaining how stressful it is to not have time for anything else!"

    if cat_mood < 0:
        show cat angry
        c "It's stressful now! But at least I won't be dying alone in some godforsaken apartment playing a stupid video game because I have no life!"
        show cat something
        c "Whatever. Just keep playing your games. No need to call."
        "With that, she storms out."
        show cat at getup_and_leave
        show cat_torso at getup_and_leave
        $ broken_up = True
        $ affection_modify('Catherine', -2)
    else:
        c "It's stressful now. But at least I'll get a proper job."
        show cat longing
        c "Nick, please just let me help you..."
        show cat sad
        "She tries to look endearingly into my eyes, but I avoid her gaze."
        window hide
        $ affection_modify('Catherine', 1)

    window hide
    scene black with Dissolve(5.00)
    pause 3.0

    return

label parlorWait:
    $ parlorwait = True
    "After a little bit of silence, she speaks up."
    show cat normal_downright
    c "Nick... I think we should break up."
    "There. She said it. But I didn't expect it to hurt this much."
    n "Catherine... please..."
    menu:
        "Beg her not to do it":
            jump parlorBeg
        "Change the subject" if not parloridle:
            jump parlorIdle
        "Get angry" if parloridle:
            jump parlorAngry
        "Apologize" if not parlorapology:
            jump parlorApology
        "Promise to make up for your negligence" if parlorapology:
            jump parlorMakeUp

label parlorBeg:
    n "Please, Catherine. Not yet. I'll change."
    show cat longing
    c "I wish I could believe that."
    $ cat_mood += 1
    "I blink so as to hide the tears."
    "I want to just go under the table and cry."
    menu:
        "Promise to quit DFO":
            call parlorInterrupt
            jump quitDFO
        "Accept the situation":
            call parlorInterrupt
            jump parlorAccept
        "Plead with her":
            call parlorInterrupt
            jump parlorPlead

label quitDFO:
    n "If you want, I'll... I'll even stop playing DFO. Just, please..."

    if cat_mood < 0:
        show cat frown
        "Cat frowns."
        c "That's not the real problem. Even if you stop playing, you won't change."
        show cat normal_downright
        c "Just... Goodbye, Nick."
        "She gets up and leaves."
        show cat at getup_and_leave
        show cat_torso at getup_and_leave
        $ broken_up = True
        $ affection_modify('Catherine', -2)
    else:
        "Catherine doesn't say anything."
        "Then, she closes her eyes."
        c "Fine, if you promise. Nicholas, this is for your own good."
        $ affection_modify('Catherine', 1)

    window hide
    scene black with Dissolve(5.00)
    pause 3.0


    return

label parlorAccept:
    n "If you really want to leave me, I guess I just have to... accept it."
    "Cat sighs."
    show cat normal_down

    if cat_mood < 0:
        c "Yes. Well then, goodbye, Nicholas."
        "With that, she gets up and goes."
        show cat at getup_and_leave
        show cat_torso at getup_and_leave
        $ broken_up = True
        $ affection_modify('Catherine', -2)
    else:
        c "I don't want to leave you. But things can't go on like this anymore."
        n "Can we try? Just a little bit longer?"
        show cat normal
        c "One more time. Don't blow it."

    window hide
    scene black with Dissolve(5.00)
    pause 3.0

    return

label parlorPlead:
    n "Please don't give up on me yet. We'll figure this out."
    show cat longing
    "At first, just for a moment, she hesitates."

    if cat_mood < 0:
        show cat frown
        c "I don't think so. This is it, Nicholas."
        hide cat with dissolve
        hide cat_torso with dissolve
        "Before I have a chance to respond, she gets up and leaves."
        show cat at getup_and_leave
        show cat_torso at getup_and_leave
        $ broken_up = True
        $ affection_modify('Catherine', -2)
    else:
        show cat normal
        c "Fine. Let's try one last time."
        n "You don't realize how happy that makes me."
        show cat frown
        "Contrary to my intentions, my comment just makes her sulk."

    window hide
    scene black with Dissolve(5.00)
    pause 3.0

    return

label parlorInterrupt:
    "We're interrupted as the cashier comes to our table."

    if ice_cream == "cheap":
        # Strawberry-Chocolate mix
        cashier "One Strawberry-Chocolate mix."
        n "Thank you."

        if cat_mood < 0:
            show cat frown
            c "That's what you got me? The cheapest one on the menu?"
            c "Is this some kind of joke?"
        else:
            show cat normal_right
            "Catherine doesn't seem too impressed with the ice cream I got her."
            "Still, she sticks a spoon in it and begins eating."

        $ cat_mood -= 1

    elif ice_cream == "expensive":
        # Rockefeller parfait
        cashier "One Rockefeller parfait. Careful so it doesn't tip over."
        n "Thank you."

        if cat_mood < 0:
            show cat surprise
            "Catherine looks a bit surprised."
            c "Why'd you get such a big one? I can't eat that much!"
        else:
            show cat surprise
            "Catherine gasps."
            c "Nicholas, isn't that the most expensive thing on the menu? Why did you..."

        n "I thought we could eat it together."
        show cat fuun
        "Catherine says nothing, but seems placated, and we start eating."

        $ cat_mood += 1

    else:
        # Chocolate-Peanut butter sundae

        cashier "One Chocolate-Peanut butter sundae."
        n "Thank you."

        if cat_mood < 0:
            show cat frown
            "Catherine doesn't look as happy as I had hoped."
            c "Oh, I get it. You saw that I hadn't exercised today..."
            c "... and bought that just to tease me!"
            c "Well, thanks a lot, Nick."
            "If more sarcasm was dripping from her voice, we would have a flood."
            $ cat_mood -= 1
        else:
            show cat fuun
            "Catherine seems to slightly cheer up as she sees what I bought her."
            c "Oh, thanks, Nick. That was thoughtful of you."
            $ cat_mood += 1

    n "A-anyway."
    return

# This is the label that is jumped to at the start of a day.
label day:

    # Increment the day it is.
    $ day += 1


    window hide
    # "It's day %(day)d."
    call calendar(1)

    if (day-1)%7 == 1:
        $ payment = work_counter*work_payment
        window show
        if payment == 0:
            "I realize that I didn't go to work at all last week."
            "I wonder if my boss is mad at me? Nah."
        else:
            "I get paid [payment] bits for last week's work."
        $ cash += payment
        $ work_counter = 0

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available.

    $ morning_act = None
    $ afternoon_act = None
    $ evening_act = None
    #$ narrator("What should I do today?", interact=False)

    window hide

    # Tell the user what period it will be.
    centered "{size=+10}{color=#fff}Morning{/color}{/size}{w=1.0}{nw}"

    if day >= 11:
        call ending_for_now
        call events_end_day
        jump Ending_Credits

    # Now, we jump the day planner, which may set the act variables
    # to new values. We jump it with a list of periods that we want
    # to compute the values for.
    $ renpy.choice_for_skipping()
    call screen image_planner("Morning")
    #(["Morning", "Afternoon", "Evening"])


    # We process each of the three periods of the day, in turn.
label morning:
    window show

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below.
    $ period = "morning"
    $ act = morning_act

    # Execute the events for the morning.
    call events_run_period

    # That's it for the morning, so we fall through to the
    # afternoon.

label afternoon:
    # It's possible that we will be skipping the afternoon, if one
    # of the events in the morning jumped to skip_next_period. If
    # so, we should skip the afternoon.
    if check_skip_period():
        jump evening

    # The rest of this is the same as for the morning.

    window hide
    scene black
    centered "{size=+10}{color=#fff}Afternoon{/color}{/size}{w=1.0}{nw}"
    $ renpy.choice_for_skipping()
    call screen image_planner("Afternoon")

    window show

    $ period = "afternoon"
    $ act = afternoon_act

    call events_run_period


label evening:
    # The evening is the same as the afternoon.
    if check_skip_period():
        jump night

    window hide
    scene black
    centered "{size=+10}{color=#fff}Evening{/color}{/size}{w=1.0}{nw}"
    $ renpy.choice_for_skipping()
    call screen image_planner("Evening")

    window show

    $ period = "evening"
    $ act = evening_act

    call events_run_period


label night:
    scene black with dissolve
    window show

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    centered "{size=+10}{color=#fff}Night{/color}{/size}{w=1.0}{nw}"


    if not truck_handled:
        call truck_after
        $ truck_handled = True
    else:
        "It's getting late, so I decide to go to sleep."

    $ fitness -= 2

    python:
        forgotten_promises = set()
        for promise_event in promises.keys():
            if promise_event[1] == day:
                if not all(promises[promise_event].values()):
                    for promise in promises[promise_event].keys():
                        if not promises[promise_event][promise]:
                            # An unfulfilled promise today
                            forgotten_promises.add(promise[0])
                            unhandled_forgotten_promises[promise[0]] = (promise_event[0], day)
                            if promise[0] in unkept_promises_personal_counter:
                                unkept_promises_personal_counter[promise[0]] += 1
                            else:
                                unkept_promises_personal_counter[promise[0]] = 1

    if len(forgotten_promises) != 0:
        python:
            if len(forgotten_promises) == 1:
                forgotten_people = next(iter(forgotten_promises))
                promise_pluralized = "promise"
            else:
                list_forgotten = list(forgotten_promises)
                forgotten_people = ", ".join(list_forgotten[0:len(list_forgotten)-1]) + " and " + list_forgotten[-1]
                promise_pluralized = "promises"

        "Just as I'm going to sleep, I realize I forgot my [promise_pluralized] to [forgotten_people]."

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day


# This is a callback that is called by the day planner.
label dp_callback:

    # Add in a line of dialogue asking the question that's on
    # everybody's mind.
    #$ narrator("What should I do today?", interact=False)

    return

label Ending_Credits:
    window hide
    $ credits_speed = 20 #scrolling speed in seconds
    scene black with dissolve #replace this with a fancy background
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(5, hard=True)
    pause 10
    hide theend
    show cred at Move((0.5, 4.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    $ renpy.pause(credits_speed, hard=True)
    hide cred with dissolve
    show thankyou at truecenter
    pause 4
    hide thankyou with dissolve
    return
