label start_baudrillard:
    scene black

    show baudrillard at truecenter with dissolve
    pause 5.0

    scene black with dissolve
    scene bg_twilight_fields with dissolve

    play music bgm_battle
    
    # Refactoring needed, DFO_character_init should take gamestate and characters as parameters
    call DFO_character_init
    $ gamestate.init_battle()
    #show screen hp_window(gamestate.players, gamestate.enemies)
    show screen single_ally_hp_window(gamestate.players['Nick'], 0)
 
    $ dfoMode = True
    
    $ gamestate.take_damage("Nick", 15000)
    $ gamestate.take_damage("Aerith", 2000)

    n "Damnit!"

    play sound sfx_grunt_1
    with hpunch

    # Sound effect
    
    $ gamestate.take_damage("Nick", 2000)

    # Note: Size 24 is good for FONTC_AEROMATICS
    "The monster sinks its fangs into my skin, drawing blood!"

    # Screen shake & sound

    play sound sfx_blood

    "I can feel the warm liquid trickling down my skin... Damnit!"
    
    hide screen single_ally_hp_window
    
    with hpunch

    "With a huge throwing motion, I manage to shed the weasel, but others are already circling around me."

    "They're humongous. But I'm not actually worried. Not yet, anyway."

    show air 10 at distant, left with moveinleft

    "I see Aerith in the corner of my vision."
    
    show screen single_ally_hp_window(gamestate.players['Aerith'], 0)

    "She's surrounded by the creatures as well, trying to keep them away
    with her staff."

    show screen remember_popup_window("Aerith will remember this for the rest of her life.")

    "Um, shouldn't she just cast a spell or something?"

    hide air with moveoutleft
    hide screen single_ally_hp_window

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

label FX_Silvia_Hail:
    show fx daggers
    with vpunch
    with vpunch
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
    return

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

    show fx slash at flash
    play sound sfx_critical
    with vpunch
    hide fx slash

    "The weasels screech in pain, flying off in a torrent of blood!"

    "But there's too many of them! No matter how many times I attack, more are lashing right at me!"

    s "Protect yourself."

    "I hear Silvia's voice from somewhere nearby, and instantly understand."

    "I raise my shield just in time as a hail of daggers falls all around me, piercing the weasels and spraying blood everywhere!"

    call FX_Silvia_Hail

    "The monsters lie dead on the grass, painted crimson with blood."

    "I turn around to thank Silvia, but then I hear Aerith scream from behind."

    jump WeaselAerithScream

    return

label WeaselAerithScream:
    # You can run to Aerith, tell her to use the barrier spell, or tell Silvia to use her hail of daggers again

    show air 10 at distant, right with moveinright

    "She's still surrounded by a pack of weasels, desperately pushing them off!"
    
    show screen single_ally_hp_window(gamestate.players['Aerith'], 0)

    pause 0.5
    
    $ gamestate.take_damage("Aerith", 100)
    
    "Their gnawing at her health. She won't last at this rate!"

    $ tooltips = {}
    $ tooltips["Tell her to cast her barrier spell"] = "A barrier of light temporarily protects the caster from all attacks."
    $ tooltips["Tell Silvia to use the hail of daggers"] = "Raining death from above. Just make sure your allies are not caught in the range!"

    menu:
        "Run to save her!":
            "I run through the pack to her side, seeking to protect her from harm!"
            hide screen single_ally_hp_window
            show air 10 at left with moveinright
            jump WeaselProtectAerith
        "Tell her to cast her barrier spell":
            hide screen single_ally_hp_window
            jump WeaselAerithBarrier
        "Tell Silvia to use the hail of daggers":
            hide screen single_ally_hp_window
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
    call FX_Silvia_Hail
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
    show white with dissolve
    show air 8
    hide white with dissolve
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

    call FX_Silvia_Hail

    if blade_sphere_control:
        "As the flurry of thrown knifes falls upon us, I block each and every one coming towards me and Aerith!"
        show fx slash at flash
        play sound sfx_hit
        with vpunch
        with vpunch
        hide fx slash
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

    show fx slash at flash
    play sound sfx_critical
    with vpunch
    pause 0.1
    play sound sfx_critical
    with hpunch
    pause 0.1
    play sound sfx_critical
    with vpunch
    hide fx slash

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
    show overlay green
    play sound sfx_heal
    "I feel the warm, green glow closing the wounds on my arms."
    hide overlay green

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

    play sound sfx_grunt_2
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

    show fx slash at flash
    play sound sfx_hit_2
    with vpunch
    with vpunch
    hide fx slash

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

    show fx slash at flash
    play sound sfx_hit
    pause 0.1
    hide fx slash

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
            $ tooltips["Offensive Technique: Furious Strike!"] = "Bash a foe with utmost fury. If they attempt to parry, their weapons will surely be broken, and their allies shall flee in terror!"
            $ tooltips["Silvia Technique: Hail of Daggers!"] = "Raining death from above. Just make sure your allies are not caught in the range!"

            menu:
                "Offensive Technique: Furious Strike!":
                    jump WeaselFuriousStrike
                "Silvia Technique: Hail of Daggers!":
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
    show overlay purple
    pause 0.1
    hide overlay purple with dissolve
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

    hide screen hp_window

    play music bgm_cheerful

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
    $ dfoMode = False
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
    "{color=#f00}Catherine.{/color}"
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
    play sound sfx_thud
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
    scene black with dissolve
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

    scene player_room with dissolve
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