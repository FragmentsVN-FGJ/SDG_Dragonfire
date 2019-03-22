init:
    transform closeupzoomoutcenter:
        zoom 1.75
        yalign 0.0
        linear 2.0 zoom 1.0

    transform zoomoutcenter:
        zoom 1.0
        xalign 0.5
        yalign 0.5
        linear 1.5 zoom 0.6

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

    transform spooked:
        linear 0.1 ypos 0.9 yanchor 1.0
        linear 0.1 yalign 1.0

    transform shake:
        linear 0.2 xpos 0.3
        linear 0.4 xpos 0.7
        linear 0.2 xpos 0.5

    transform digging:
        linear 1.0 ypos 2.0
        pause 3.0
        xpos 0.7
        linear 0.5 ypos 0.5
        pause 0.2

        linear 1.0 ypos 2.0
        pause 2.0
        xpos 0.3
        linear 0.5 ypos 0.5
        pause 0.2

        linear 1.0 ypos 2.0
        pause 3.0
        xpos 0.5
        linear 0.5 ypos 0.5
        pause 0.2
        repeat


    transform breathefire:
        linear 1.0 xpos 0.65 ypos 0.45
        linear 0.8 xalign 0.5 yalign 0.5

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
    define sfx_digging = "bgm/SFX_Footsteps_gravel.mp3"
    define sfx_potion = "bgm/SFX_Drink_potion.mp3"
    define sfx_heal= "bgm/SFX_Heal_regen.mp3"
    define sfx_shield = "bgm/SFX_Raise_Shield.mp3"
    define sfx_collapse = "bgm/SFX_Rock_Collapse.mp3"
    define sfx_thump = "bgm/SFX_Rock_Thump.mp3"
    define sfx_thud = "bgm/SFX_Hammer_hit.mp3"
    define sfx_block = "bgm/SFX_Hammer_hit_2.mp3"
    define sfx_critical = "bgm/SFX_Sword_hit_flesh.mp3"
    define sfx_critical_short = "bgm/SFX_Sword_hit_flesh_short.mp3"
    define sfx_hit = "bgm/SFX_Sword_hit.mp3"
    define sfx_hit_2 = "bgm/SFX_Sword_hit_2.mp3"
    define sfx_miss = "bgm/SFX_Sword_slash_8.mp3"
    define sfx_dagger = "bgm/SFX_Sword_hit_armor.mp3"
    define sfx_scream = "bgm/SFX_Scream_Death.mp3"
    define sfx_blood = "bgm/SFX_Soup.mp3"
    define sfx_heartbeat = "bgm/SFX_Heart_Beat.mp3"

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
    define sfx_dragon = "bgm/SFX_Grunt_Angry_1.mp3"

init python:
    credits = ('Script', 'MagusDei'), ('Sprites and hand-drawn backgrounds', 'Qazhax'), ('Background images', 'Snehadri'), ('Programming', 'MagusDei'), ('Programming', 'Qazhax'), ('Logo', 'John Smith'), ('Music', 'xZidene'), ('Sound effects', 'xZidene'), ('Sound effects', 'Qazhax'), ('Dungeon and MMO design', 'Bahafyr')
    credits_s = "{size=80}Credits\n\n"
    e1 = ''
    for e in credits:
        if not e1==e[0]:
            credits_s += "\n{size=40}" + e[0] + "\n"
        credits_s += "{size=60}" + e[1] + "\n"
        e1=e[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.99.12.4\n\nDSE\n3.11\nCalendar Animation\nby Zetsubou\n"
    credits_s += "\n{size=40}SFX Attributions\n{size=60}death_scream.wav\nby Syna-Max\n\n Pouring Soup in a Metal Pan\nHitrison"

    crt = ImageDissolve("images/crt.png", 0.5, 0)
    #register_stat("Strength", "strength", 10, 100)
    #register_stat("Intelligence", "intelligence", 10, 100)
    register_stat("Fitness", "fitness", 50, 100)
    register_stat("Stress", "stress", 3, 10)
    register_stat("μBC (bits)", "cash", 27126, 999999)

    dp_period("Morning", "morning_act")
    dp_choice("Swimming hall", "swimming", x=300, y=350, tooltip="Entrance fee 3000 bits.")
    dp_choice("Gym", "gym", x=400, y=450, tooltip="Daily fee is 1000 bits.")
    dp_choice("Running Track", "track", x=150, y=200, tooltip="Free entry. A good way to build up fitness.")
    dp_choice("Call Catherine", "callcat", x=200, y=150, show="not broken_up and day > 1", tooltip="I could try setting up a date...")
    dp_choice("Clean room", "clean", x=350, y=550, tooltip="My room is as unkempt as my hair. Very. (-1 stress)")


    dp_period("Afternoon", "afternoon_act")
    dp_choice("Ice Cream Parlor", "parlor", x=175, y=450, show="stress < 8", tooltip="Queens Gelateria, best ice cream in town. Prices from 6000 bits up. (-2 stress)")
    dp_choice("Restaurant", "restaurant", x=400, y=350, tooltip="Good in case I'm too lazy to cook for myself. Fries for 12 000 bits. (-1 stress)")
    #dp_choice("Bowling", "bowling")
    dp_choice("Mall", "mall", x=425, y=180, show="stress < 8", tooltip="I could look for sales, if it's not too crowded. (may decrease stress)")
    dp_choice("Library", "library", x=550, y=200, tooltip="Books, computers and a makerspace. Free, of course.")
    dp_choice("Work", "work", x=150, y=550, show="stress < 8", tooltip="The pay is 9000 bits per day. Not bad. (+2 stress)")
    dp_choice("Business school", "business", x=200, y=100, show="stress < 8", tooltip="I've got no business there, probably.")
    dp_choice("Ruins of Kvaagwyr", "ruins", x=755, y=450, tooltip="A high-level dungeon released as a part of the new expansion for DFO. It will take the whole day to play it. (-4 stress)")


    dp_period("Evening", "evening_act")

    dp_choice("Bar", "bar", x=650, y=400, tooltip="Techno bar. Should I get a drink? It's 7000 bits. (-1 stress)")
    dp_choice("Movie theatre", "movies", x=340, y=470, tooltip="I could go watch some movies. By myself. For 15 000 bits. (-2 stress)")
    dp_choice("VR Arcade", "arcade", x=150, y=400, tooltip="VR Arcade, though I'll probably end up playing retro games. 7000 bits. (-1 stress)")
    dp_choice("Catherine's apartment", "cathouse", x=200, y=150, show="stress < 8", tooltip="I wonder if she's home...?")
    dp_choice("Clean room", "clean", x=350, y=550, tooltip="I wonder how it always gets so dirty... (-1 stress)")

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
        if amount < 0:
            renpy.show_screen("remember_popup_window", person+" does not seem happy.")
        elif amount > 0:
            renpy.show_screen("remember_popup_window", person+" seems pleased.")
        return

    def trust_modify(person, amount):
        global trust
        trust[person] = trust[person] + amount
        if trust[person] > max_trust:
            trust[person] = max_trust
        if trust[person] < 0:
            trust[person] = 0
        if amount < 0:
            renpy.show_screen("remember_popup_window", person+" looks suspicious.")
        elif amount > 0:
            renpy.show_screen("remember_popup_window", person+" trusts you.")
        return

image DFO_blinking_arrow:
    alpha 0.3
    zoom 0.5
    yoffset 9
    xoffset 2
    "images/arrow3.png"
    pause 0.5
    alpha 0.0
    pause 0.5
    repeat
    
image blinking_arrow:
    alpha 0.3
    zoom 0.4
    yoffset 7
    xoffset 2
    "images/arrow3.png"
    pause 0.5
    alpha 0.0
    pause 0.5
    repeat

image nvl_blinking_arrow:
    alpha 0.3
    zoom 0.4
    yoffset 10
    xoffset 2
    "images/arrow3.png"
    pause 0.5
    alpha 0.0
    pause 0.5
    repeat
    
image choice_background_hover:
    "gui/dfo_textbox8.png"
    #im.MatrixColor("images/bg/movie_theatre.png", im.matrix.brightness(-0.5))
    "gui/dfo_textbox6.png" with Dissolve(2.0, alpha=True)
    pause 1.0
    repeat

# Define characters
define a = Character("Aerith", color="#FF1493", ctc="DFO_blinking_arrow")
define n = Character("Nicholas", color="#191970", ctc=ConditionSwitch("dfoMode", "DFO_blinking_arrow", "True", "blinking_arrow"))
define s = Character("Silvia", color="#9932CC", ctc="DFO_blinking_arrow")
define c = Character("Catherine", color="DC143C", ctc="blinking_arrow")
define nvlNarrator = Character(None, kind=nvl, what_xsize = 950, what_size=28, what_xpos=200, ctc="nvl_blinking_arrow")
define narrator = Character(None, ctc=ConditionSwitch("dfoMode", "DFO_blinking_arrow", "True", "blinking_arrow"))

image SDG_DF_fade1_big = "SDG_DF_fade1_big.png"

define endingNarrator = Character(None,
                          color="#191970",
                          what_size=36,
                          what_xpos=0.4,
                          window_xalign=0.5,
                          window_yalign=0.5,
                          window_background=None,
                          what_outlines=[(3, "#191970", 0, 0)],
                          what_cps=20
                          )

define endingSilvia = Character(None,
                          color="#9932CC",
                          what_size=36,
                          what_xpos=0.4,
                          window_xalign=0.5,
                          window_yalign=0.5,
                          window_background=None,
                          what_outlines=[(3, "#9932CC", 0, 0)],
                          what_cps=20
                          )

define endingAerith = Character(None,
                          color="#fff",
                          what_size=36,
                          what_xpos=0.4,
                          window_xalign=0.5,
                          window_yalign=0.5,
                          window_background=None,
                          what_outlines=[(3, "#FF1493", 0, 0)],
                          what_cps=20
                          )

define endingCatherine = Character(None,
                          color="#DC143C",
                          what_size=36,
                          what_xpos=0.4,
                          window_xalign=0.5,
                          window_yalign=0.5,
                          window_background=None,
                          what_outlines=[(3, "#DC143C", 0, 0)],
                          what_cps=20
                          )


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
image gameover = Text("{size=40}Game Over. \n\n Return to challenge again.", text_align=0.5)

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
    $ spendtimepromise = False
    $ moviepromise = False

    $ truck_handled = True

    $ mood = {"Catherine": 0, "Silvia": 0, "Aerith": 0}

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

    jump start_baudrillard
    
label morning_screen:
    scene black
    centered "{size=+10}{color=#fff}Morning{/color}{/size}{w=1.0}{nw}"
    return

label evening_screen:
    scene black
    centered "{size=+10}{color=#fff}Evening{/color}{/size}{w=1.0}{nw}"
    return

# This is the label that is jumped to at the start of a day.
label day:

    call play_cheerful

    # Increment the day it is.
    $ day += 1

    # Calculate dayswocat
    $ dayswocat = calculatedayswithoutseeingCatherine()

    window hide
    # "It's day %(day)d."
    call calendar(1)
    
    if day == 1:
        call morning_screen
        call gymintro
        call Catherine_gym_together
        call evening_screen
        call RuinsStart
    elif day == 2:
        call morning_screen
        call parlorStart
        call evening_screen
        call RuinsStart
    elif day == 3:
        call morning_screen
        call cleanintro
        call DFOServers
        call evening_screen
        call RuinsStart
    elif day == 4:
        call morning_screen
        call smith_call1
        call evening_screen
        call RuinsStart
    elif day == 5:
        call morning_screen
        call Catherine_study_together
        call evening_screen
        call RuinsStart
    # elif day == 6:
        # call RuinsStart
    # elif day == 7:
        # call RuinsStart
    # elif day == 8:
        # call RuinsStart
    # elif day == 9:
        # call RuinsStart
    # elif day == 10:
        # call RuinsStart
    else:
        call ending_for_now
        call events_end_day
        jump Ending_Credits

    jump day

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

    if stress >= 10:
        call events_end_day
        jump stress_ending

    # Now, we jump the day planner, which may set the act variables
    # to new values. We jump it with a list of periods that we want
    # to compute the values for.
    $ renpy.choice_for_skipping()
    call screen image_planner("Morning")
    #(["Morning", "Afternoon", "Evening"])


    # We process each of the three periods of the day, in turn.
label morning:
    call play_cheerful
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
    call play_cheerful
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
    call play_cheerful
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
    call play_cheerful
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
        if stress <= 2:
            "That was quite the day. Time to hit the bed!"
        elif stress >= 8:
            "It's difficult to fall asleep, and I spend hours rolling about in my bed."
        elif stress >= 5:
            "I yawn. What a tiring day."
            "I'm glad to cover myself with the blanket, falling into the world of dreams."
        else:
            "It's quite late. I'm a bit tempted to boot up DFO, but I'd better get some sleep."

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


    if stress == 0:
        "I sleep well, heart light with joy."
    elif stress == 1:
        "I sleep well."
    elif stress == 2:
        "I dream about Catherine."
    elif stress == 3:
        "I'm dreaming about work again."
    elif stress == 4:
        "In my dream, something bad happens at work, but I can't quite remember what..."
    elif stress == 5:
        "My dreams are a bit dark that night."
    elif stress == 6:
        "My sleep is all but restful. There's just too much going on..."
    elif stress == 7:
        "All the stress caused by recent events makes my dreams dark and uneasy."
    elif stress == 8:
        "I awaken during the night, covered in sweat. The nightmare soon leaves my memory, however."
    elif stress == 9:
        "I wake up screaming in the middle of the night."
        "I can't catch any sleep after that."

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
    $ renpy.full_restart()

label stress_ending:
    scene black with dissolve
    "I am on a bridge, staring at the ocean below."
    "The waves look so gray, so peaceful..."
    "I just want peace..."
    "Why can't I have peace?"
    "I look at the waves one last time, closing my eyes, and then..."
    "I'm flying. I'm flying! I'm f...!"
    "Strange. It feels as if time has frozen."
    "Was it only a dream? Was it all just a dream?"
    mv "This will not do."
    "What?"
    "All around me, time starts to rewind. I'm back on the bridge."
    "I'm back home."
    "The days move past, my memories with them..."
    "And I return, return to the beginning of it all."
    scene white with Dissolve(2)
    show gameover with dissolve
    pause 5
    hide gameover with dissolve
    $ renpy.full_restart()

label ending_celebration:
    $ tooltips = {}
    play music bgm_cheerful
    scene white
    "Well, that was weird."
    scene bg_fort with pixellate
    show air 2 at left
    show cat_torso green
    show cat smile
    show sil normal at right, flip
    n "Don't you agree?"
    n "Kind of took a dark turn there."
    show air 7
    a "I don't really get what that 'it was a great demo' thing was at the end."
    show sil nervous_laugh
    s "Surely a reference to some antiquated game. Think nothing of it."
    show sil normal
    n "Yes, they can't actually have meant it."
    show cat question
    c "So, when is the full version coming out?"
    show sil cat2 at flip
    s "Rumor tells that the game shall be out before summer."
    show air 4
    a "I wonder if they can actually do it, though..."
    n "Well, I'll have to keep practicing my game design skills."
    show air 6
    show cat question
    show sil mwerrllyy at flip
    n "Maybe they'll hire me!"
    c "You wish, Nick. Have you even made a single game yet?"
    n "I'll have you know that yes, in fact, I have made a single game yet."
    show cat surprise
    c "What? Seriously?"
    n "I'm serious. It really exists."
    show sil flmao at flip
    s "As real as the fabled invisible pink unicorn, I am sure."
    n "Hah! Here it is, I'll show you!"
    play music bgm_derp_loop
    scene white with dissolve
    "{size=36}Nick's T-shirt Game{/size}"
    scene white with dissolve
    show cat_torso green at closeup
    show cat smile at closeup
    "This is Catherine."
    menu:
        "Take off Catherine's T-shirt."
        "Okay.":
            show cat blush_smile at closeup
            show cat_torso naked at closeup with dissolve
            c "Hihihi, that tickles!"
            "You won the game."
        "No way!":
            show cat pissed_but_hiding_it_under_a_poker_face
            "You lost the game."
    play music bgm_cheerful
    scene bg_fort with pixellate
    show air blush at left
    show cat_torso green
    show cat surprise
    show sil shock at right, flip
    n "Now do you believe me?"
    n "Just leave it to the game master!"
    "Everyone" "{cps=2}......{/cps}{nw}"
    show air angry_shout
    show cat angry
    show sil rage at flip
    with hpunch
    "Everyone" "YOU ARE DEAD, NICK!"
    hide air
    hide cat_torso
    hide cat
    hide sil
    with moveoutright
    "Aaaaahhh!!!"
    "Why does it always have to end like thiiiis!?"
    return

label trailer:
    play music bgm_scary
    scene black
    window hide
    endingNarrator "It will end.{w=1.0}{nw}"

    scene bg_field
    show sil hmm at closeup, flip
    endingNarrator "This world isn't real.{w=1.0}{nw}"
    show sil annoyed at closeup, flip
    with hpunch
    endingSilvia "Doesn't it feel real?{w=1.0}{nw}"

    pause 2

    scene bg_fort
    show air blush2 at closeupzoomoutcenter
    endingAerith "Nicholas!{w=1.0}{nw}"
    scene bg_field
    show sil annoyed at closeupzoomoutcenter, flip
    endingSilvia "Liege!{w=1.0}{nw}"
    scene player_room
    show cat_torso green at closeupzoomoutcenter
    show cat scream at closeupzoomoutcenter
    endingCatherine "Nicky...!{w=1.0}{nw}"

    scene bg_fort with dissolve
    endingNarrator "Damnit! What the hell is going on!?{w=1.0}{nw}"
    show sil lecture at right with moveinright
    endingSilvia "All will be explained once we reach the top.{w=1.0}{nw}"

    pause 2

    scene black with dissolve
    show air 2 at right, closeup
    endingAerith "There's an inscription here:{w=1.0}{nw}"

    show air 7 at right, closeup
    endingAerith "{i}Lasciate ogne speranza, voi ch'intrate{/i}{w=1.0}{nw}"

    hide air
    show sil lecture at left, closeup
    endingSilvia "Abandon all hope, ye who enter here.{w=1.0}{nw}"

    pause 2

    scene white with dissolve
    show sil taunt at flip
    endingSilvia "It's time to make your choice.{w=1.0}{nw}"
    scene white with Dissolve(3)
    show SDG_DF_fade1_big at zoomoutcenter
    play sound sfx_fire
    show fx fire behind SDG_DF_fade1_big

    pause 2

    return

label play_cheerful:
    if day <= 7:
        if not renpy.music.get_playing() == "bgm/BGM_Cheerful.mp3":
            play music bgm_cheerful
    else:
        if not renpy.music.get_playing() == "bgm/BGM_Piano_Cinematic":
            play music bgm_main
    return
