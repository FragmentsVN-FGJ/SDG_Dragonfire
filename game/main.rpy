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
init python:
    register_stat("Strength", "strength", 10, 100)
    register_stat("Intelligence", "intelligence", 10, 100)

    dp_period("Morning", "morning_act")
    dp_choice("Attend Class", "class")
    dp_choice("Cut Class", "cut")
    
    # This is an example of an event that should only show up under special circumstances
    dp_choice("Fly to the Moon", "fly", show="strength >= 100 and intelligence >= 100")

    dp_period("Afternoon", "afternoon_act")
    dp_choice("Study", "study")
    dp_choice("Hang Out", "hang")

    dp_period("Evening", "evening_act")
    dp_choice("Exercise", "exercise")
    dp_choice("Play Games", "play")

# Define characters
define a = Character("Aerith")
define n = Character("Nicholas")
define s = Character("Silvia")
    

# This is the entry point into the game.
label start:

    # Initialize the default values of some of the variables used in
    # the game.
    $ day = 0
    
    $ blade_sphere_control = False
    $ Aerith_angry = False
    $ Aerith_hurt = False
    $ Aerith_barrier = False
    $ curing_light = False

    # Show a default background.
    scene forest

    # The script here is run before any event.

    # Battle music
    play music "bgm/Battle1.wav"
    
    n "Damnit!"
    
    # Sound effect
    
    "The monster sinks its fangs into my skin, drawing blood!"
    
    # Screen shake & sound
    
    "I can feel the warm liquid trickling down my skin... Damnit!"
    
    "With a huge throwing motion, I manage to shed the weasel, but others are already circling around me."
    
    "They're huge. But I'm not actually worried. Not yet, anyway."
    
    "I see Aerith in the corner of my vision."
    
    "She's surrounded by the creatures as well, trying to keep them away
    with her staff." 
    
    "Um, shouldn't you just cast a spell or something?"
    
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
            
    # We jump to day to start the first day.
    # jump day
    
label WeaselPull:
    "Trampling the weasels around me, I run to protect Aerith!"
    "Damn, they're following me! Of course this would happen!"
    "Now all of them are focused on us. Aerith is holding her hands to her mouth, gasping for air."
    jump WeaselProtectAerith

label WeaselFight:
    # Silvia uses hail of daggers
    
    "I'll just have to beat them off!"
    
    "I slash at the pack with my sword!"
    
    "The weasels screech in pain, flying off in a torrent of blood!"
    
    "But there's too many of them! No matter how many times I attack, more are lashing right at me!"
    
    s "Protect yourself."
    
    "I hear Silvia's voice from somewhere nearby, and instantly understand."
    
    "I raise my shield just in time as a hail of daggers falls all around me, piercing the weasels and spraying
    blood everywhere!"
    
    "The monsters lie dead on the grass, painted crimson with blood." 
    
    "I turn around to thank Silvia, but then I hear Aerith scream from behind."
    
    jump WeaselAerithScream
    
    return
    
label WeaselAerithScream:
    # You can run to Aerith, tell her to use the barrier spell, or tell Silvia to use her hail of daggers again
    
    "She's still surrounded by a pack of weasels, desperately pushing them off!"
    
    "Their gnawing at her health. She won't last at this rate!"
    
    menu:
        "Run to save her!":
            "I run through the pack to her side, seeking to protect her from harm!"
            jump WeaselProtectAerith
        "Tell her to cast her barrier spell":
            jump WeaselAerithBarrier
        "Tell Silvia to use the hail of daggers":
            jump WeaselSilviaHailOfDaggersAerithAlone
            
    return
    
label WeaselSilviaHailOfDaggersAerithAlone:
    n "Silvia! Finish them with a hail of daggers!"
    "Silvia smirks, hesitating a bit."
    s "You sure about that, liege?"
    "Then, her smile turns fiendish, and she shrugs."
    s "Here goes!"
    "She launches into the air and begins her technique."
    "The daggers rain upon the weasels, killing them instantly!"
    "Of course, they hit Aerith as well. I really should have realized that."
    "She falls on her knees, but seems to be alive for the moment."
    "In any case, the weasels are dealt with."
    $ Aerith_angry = True
    $ Aerith_hurt = True
    jump WeaselVictory
    
label WeaselAerithBarrier:
    n "Aerith! A barrier!"
    "Aerith's eyes flit from foe to foe in terror, but then she begins casting."
    a "Phopassus, protect thy faithful in a time of need. Light Barrier!"
    "I watch as a sphere of searing white light envelops Aerith."
    $ Aerith_barrier = True
    "The weasels can't get to her now. However, they are turning towards me instead!"
    menu:
        "Run to Aerith":
            "I run towards the pack, ready to protect Aerith!"
            jump WeaselProtectAerith
        "Better retreat!":
            # Barrier wears off
            jump WeaselRetreat
    
label WeaselProtectAerith:
    "The weasels are baring their fangs at us, and Silvia is nowhere to be seen."
    
    "Aerith is cowering behind me, trying to think of a spell to cast."
    
    if Aerith_barrier:
        "Her light barrier is still protecting her, but who knows how long it'll last."
    
    "Well, I'm a guardian, so I should be able to do this, right?"
    
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
    else:
        "The blades fall upon us, a rain of scathing edges!"
        if curing_light:
            "But due to the healing, we manage to survive despite the wounds."
        else:
            "And we're hit! I can almost taste the pain!"
            "Damnit! I don't think I can move anymore!"
            if Aerith_barrier:
                "At least Aerith was saved by her barrier."
            else:
                "Still, it seems both of us remain alive."
                $ Aerith_hurt = True

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
    
    "My sword strikes each and every one of them, cutting of their heads and piercing their beating hearts!"
    
    jump WeaselVictory
    
label WeaselAerithCuringLight:
    n "Aerith! Cast Curing Light on us!"
    
    "Aerith seems flustered for a moment, then begins chanting the spell."
    
    a "Thou art the sun which giveth life and light to the creatures of the earth..."
    
    a "Lord Phopassus, lend us your power. Curing light!"
    
    "I feel the warm, green glow closing the wounds on my arms."
    
    "Freshly invigorated, we return our focus to the battle at hand."
    
    "The weasels are already getting ready to pounce. We have to react fast!"
    
    $ curing_light = True
    
    menu:
        "Offensive technique: Furious strike!":
            jump WeaselFuriousStrike
        "Silvia technique: Hail of Daggers!":
            jump WeaselSilviaHailOfDaggers
    
    return

label WeaselFuriousStrike:
    "Time to go on the offensive!"
    
    "I raise my blade above my head, preparing to unleash my technique."
    
    "But I am interrupted as one of the animals jumps right at me!"
    
    "Its fangs and claws tear into my arm!"
    
    if curing_light:
        "However, thanks to the healing, I barely feel it."
    else:
        "Aah, I'm not gonna survive for much longer at this rate!"
    
    "I shake it off my gauntlet, and prepare the technique again."
    
    n "Furious Strike!"
    
    "I slam the critter with my sword!"
    
    "The steel runs right through its torso, hitting the ground with unbelievable power!"
    
    "The earth trembles as a shockwave emanates from where the weasel was crushed."
    
    "The rest of the weasels flee in terror."
    
    jump WeaselVictory
    
label AerithDepthsOfSlumber:
    n "Aerith! Cast Depths of Slumber!"
    
    "Aerith blinks, then nods and begins casting the spell."
    
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
            "Her spell is interrupted as she grapples with the weasel."
            "The rest of the pack is already preparing to pounce. We need to act fast!"
            menu:
                "Offensive technique: Furious strike!":
                    jump WeaselFuriousStrike
                "Silvia technique: Hail of Daggers!":
                    jump WeaselSilviaHailOfDaggers
    return
    
label AerithDepthsOfSlumberSuccess:
    a "Gift them with a peaceful sleep!"
    a "Depths of Slumber!"
    "All around us, a glowing powder descends on the weasels, and they fall asleep one by one."
    "We retreat, and Silvia finishes them off with a flurry of daggers."
    "They shall trouble us no more."
    jump WeaselVictory
    
label WeaselRetreat:
    # Silvia appears in front of you: "Good thinking!"
    "I turn around to run!"
    "Out of nowhere, Silvia appears beside me with a teasing smile."
    s "Good thinking, liege! You're pulling all of them towards you."
    "Glancing behind, I see the whole pack on my tail!"
    "Heheh, this wasn't really my intention, but no way I'm admitting that..."
    "Silvia slips back into the shadows. From the corner of my eye, I see Aerith
    running from the pack behind me!"
    $ Aerith_angry = True
    if Aerith_barrier:
        "Damn! Her barrier must have worn off!"
        $ Aerith_barrier = False
    "I stop in my tracks, and she runs behind me."
    jump WeaselProtectAerith
    
label WeaselVictory:

    play music "bgm/fanfare.mp3"
    
    "Silvia emerges from her hiding place, and I walk to her."
    
    s "Whew! Nice workout, eh?"
    
    "She flashes a wide grin."
    
    s "Seeing all that blood really makes my stomach tickle!"
    
    if Aerith_hurt:
        "Aerith comes towards us, visibly hurt."
    else:
        "Aerith approaches as well."
        
    if Aerith_angry:
        a "What the hell were you doing!? I could have died!"
        "I touch the back of my neck, slightly embarrassed."
        n "I'm sorry, don't know what I was thinking, really."
        n "Don't take it too seriously. It's just a game, right?"
        n "You would just have revived at the cathedral's teleporter."
        "Aerith pouts, folding her arms."
        a "Don't you think I know that?"
    else:
        "Her earlier terror has been replaced by disgust."
        a "Aah, there's blood everywhere, even my robes are all red... Eek!"
        "She is startled by a weasel head, rolling on the ground."
        a "Why is this game so gory!?"
        n "Uh, you know you can turn it down in the settings, right?"
        a "Y-yes, of course I do. Which is why I'll do that now."
        s "Come on, the gore is the best part!"
        "Aerith gives her a mean look, but doesn't retort."
        n "Well, I just think it's good for realism."
    
    n "Anyway, thanks for grinding with me. I guess I'll call it a day."
    "We say our farewells, and I log off."
    scene black with dissolve
    "Taking off my headset, it takes a while for my eyes to adjust to the dim lighting of my room."
    return

# This is the label that is jumped to at the start of a day.
label day:

    # Increment the day it is.
    $ day += 1

    # We may also want to compute the name for the day here, but
    # right now we don't bother.

    "It's day %(day)d."

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available.

    $ morning_act = None
    $ afternoon_act = None
    $ evening_act = None
    $ narrator("What should I do today?", interact=False)

    # Now, we jump the day planner, which may set the act variables
    # to new values. We jump it with a list of periods that we want
    # to compute the values for.
    call screen day_planner(["Morning", "Afternoon", "Evening"])

    
    # We process each of the three periods of the day, in turn.
label morning:

    # Tell the user what period it is.
    centered "Morning"

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

    centered "Afternoon"

    $ period = "afternoon"
    $ act = afternoon_act

    call events_run_period


label evening:
    
    # The evening is the same as the afternoon.
    if check_skip_period():
        jump night

    centered "Evening"

    $ period = "evening"
    $ act = evening_act
    
    call events_run_period


label night:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    centered "Night"

    "It's getting late, so I decide to go to sleep."

    # We jump events_end_day to let it know that the day is done.
    jump events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day
         

# This is a callback that is called by the day planner. 
label dp_callback:

    # Add in a line of dialogue asking the question that's on
    # everybody's mind.
    $ narrator("What should I do today?", interact=False)
    
    return

