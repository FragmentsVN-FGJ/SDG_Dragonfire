init:
    $ event("smith_call1", "period == 'morning' and day>=5 and (not first_login or day>=7)", event.once(), priority=1)
    $ event("smith_call2", "period == 'morning' and day==10", event.depends("smith_call1"), event.once(), priority=1)
    $ event("madman", "act != 'parlor' and (act, day) in promises.keys()", event.once(), priority=150)
    $ event("retro_message", "act == 'arcade'", event.depends("smith_call1"), event.only(), event.once(), priority=180)
    $ event("at_the_bar_once_again", "period == 'evening'", event.depends("smith_call1"), event.once(), event.only(), priority=3)
    $ event("truck", "period == 'evening' and day >= 8", event.only(), event.once(), event.depends("smith_call1"), priority=5)
    
define mv = Character("Synthetic voice")

image static_anim:
    im.MatrixColor("fx/noise_0.png", im.matrix.opacity(0.3))
    pause 0.1
    im.MatrixColor("fx/noise_1.png", im.matrix.opacity(0.3))
    pause 0.1
    im.MatrixColor("fx/noise_2.png", im.matrix.opacity(0.3))
    pause 0.1
    im.MatrixColor("fx/noise_3.png", im.matrix.opacity(0.3))
    pause 0.1
    repeat

image static_anim_weak:
    im.MatrixColor("fx/noise_0.png", im.matrix.opacity(0.1))
    pause 0.1
    im.MatrixColor("fx/noise_1.png", im.matrix.opacity(0.1))
    pause 0.1
    im.MatrixColor("fx/noise_2.png", im.matrix.opacity(0.1))
    pause 0.1
    im.MatrixColor("fx/noise_3.png", im.matrix.opacity(0.1))
    pause 0.1
    repeat
    
image dirty_room_vortex:
    "bg/dirty_room_1.png"
    
    "bg/dirty_room_1 gradient_map.png" with Dissolve(2)
    
    "bg/dirty_room_1_gradient_map_1.png" with dissolve
    pause 0.5
    "bg/dirty_room_1_gradient_map_2.png" with dissolve
    pause 0.5
    "bg/dirty_room_1_gradient_map_3.png" with dissolve
    pause 0.5
    "bg/dirty_room_1_gradient_map_4.png" with dissolve
    pause 0.5
    "bg/dirty_room_1_gradient_map_5.png" with dissolve
    pause 0.5
    Solid((0,0,0,255)) with Dissolve(3)

label smith_call1:
    $ stress += stress_modifiers['unreality']
    show player_room gradient_map
    play music bgm_main
    "Someone is calling."
    "It's not an ordinary call, though."
    "An encrypted call, sent through Signal."
    "I don't normally use Signal for anything."
    "It's not like I need high-level encryption for most of the things I do."
    "Except for one... So I already know who this is."
    "I have to pick it up. Any other choice would be illusory."
    n "H-hi?"
    show static_anim_weak with Dissolve(2.0)
    mv "Well howdy-ho! How you doing, mate?"
    "His question isn't referring to my general well-being, obviously. He doesn't give a crap about that."
    n "My stash is running low."
    mv "What a coincidence. So's mine. If you want more, it's gonna cost ya."
    mv "How's business looking?"
    "Yeah, this is the guy I buy my pills from. At least, I think it's a guy."
    "He calls himself Mr. Smith. He uses a speech synthesizer to mask his real voice."
    "Not one of the fancy new speech synthesizers which I wouldn't be able to distinguish from a human, either."
    "No, he doesn't even want to pretend that I know anything about him. So he's using this extremely creepy, nineties-style
    speech vocoder which doesn't sound even remotely human."
    mv "Listen, I'm gonna be needing a lot of cash pretty soon. So I thought, damn, who'd be willing to help me?"
    "The dry, mechanical laughter of the synthesizer sends chills down my spine."
    mv "I don't have that many friends, you see. Something always happens to them. So I thought of you."
    mv "You've always been a generous guy, Nick. Even though you're not that responsible."
    n "......"
    mv "You know what I'm talking about. You need to learn to pay your debts in time."
    "He pauses, and I can almost hear him grinning through the phone."
    mv "Especially with these interest rates."
    n "How much?"
    mv "Oh, basically nothing for someone as rich as you. 500 000 bits. I'll be needing it by Valentine's day, if you don't mind."
    n "I can't get that much so fast!"
    mv "Of course you can, man, I believe in you!"
    mv "Just sell your furniture, or house or whatever, I don't give a fuck."
    mv "But you're gonna pay, or, you know..."
    "I almost want to cut off there, but I have no idea what he means."
    n "... What?"
    mv "Well, just that, I happen to know who you are, where you live..."
    mv "Where your cute little girlfriend lives..."
    mv "So close to getting a degree. Would be a shame to die in a traffic accident right now."
    mv "Or you know, I can always pick the lock. We can have a nice long shower together..."
    n "Leave her out of this, you sick fuck!"
    mv "Hey hey hey, let's keep it civil, here."
    mv "Although I guess you're on the wrong side of the law for that."
    mv "Shame you went down that road, huh? You had a good life ahead of you, and then you started messing with the wrong folk."
    mv "Shoulda taken the red pill."
    mv "So. Five hundred grand, Valentine's day. Unless you want a present you'll never forget."
    "He hangs up."
    "I'm on my bed, seated in a fetal position. And I think, think, think, too shocked to even cry."
    return

label smith_call2:
    $ stress += stress_modifiers['unreality']
    play music bgm_main
    scene player_room gradient_map
    "My wristband is vibrating."
    "It's not Catherine. A call through signal."
    "Should I... maybe I can just ignore it."
    menu:
        "Answer":
            jump .answer
        "Ignore the call":
            "Eventually, the patience of the caller runs out, and I'm left wondering whether my decision was the wisest possible."
            return

label .answer:
    show static_anim_weak with dissolve
    mv "Surprised to hear from me, mister Anderson?"
    "No. Not in the least."
    n "Can't you give me more time?"
    mv "Hey, sorry man. I need it real bad."
    mv "Remember what day it is tomorrow?"
    mv "A day for lovers to unite and to part. So romantic."
    mv "If you don't get me those bits, you can kiss your kitten goodbye."
    mv "Or nevermind. I'll do it for you."
    mv "She good in bed? I'll find out."
    n "You f-"
    "I'm left seething in rage as he hangs up."
    return

label ending_for_now:
    $ stress += stress_modifiers['unreality']
    play music bgm_main
    scene player_room gradient_map
    "My wristband vibrates, and I shudder."
    "It's another call through Signal. I didn't get the money in time."
    "And now it's payback time."
    scene black with fade
    "For a moment, I listen to the buzzing of the flies in my room, afraid to pick up the call."
    "And then, there's silence."
    scene player_room grayscale2 with fade
    "I open my eyes to see everything turned gray and frozen."
    n "W-wha...?"
    "The flies... are frozen in mid-air!"
    "I hold my head and scream!"
    n "This can't be happening! I'm going insane I'm going insane I'm going...!"
    "There's only one thing which isn't frozen in time."
    "My wristband is still vibrating. The call... I can't escape from this, can I?"
    "Shaking heavily, I pick up the call."
    "At first, I hear nothing from the other side."
    n "I-is anybody there?"
    "There's no response."
    "Then, at the edges of my hearing, a sound."
    "A sound comes through, faint and distant."
    "Someone is crying in the background. A woman."
    "{color=#f00}Catherine!{/color}"
    show city_street gradient_map with dissolve
    "I run through the streets to her house. I don't even know how I got here, but it doesn't matter."
    "Catherine! Please, Catherine! No...!"
    "That bastard! That fucking bastard...!"
    "I stagger to the door to her apartment, and stumble to push the key into the lock!"
    "Not yet...!"
    "I keep turning the key in the lock, too nervous to think straight."
    "Finally, the door opens, and I run inside!"
    scene black with dissolve
    play sound sfx_heartbeat
    "It's dark. All dark. The curtains are closed."
    "I step into a puddle of water on the floor."
    "Wait. Why's there water on the floor?"
    "I stumble around in the dark, looking for the light switch."
    "Finding it, I turn on the lights."
    scene dirty_room_1 with dissolve
    stop sound
    "And I'm struck speechless by the scene that unfolds in that electric glow."
    "I break down sobbing. Because..."
    # Scream
    play sound "bgm/SFX_Scream_Death.mp3"
    "It's blood! Blood everywhere!"
    "And its source is..."
    # Blood
    play sound "bgm/SFX_Soup.mp3"
    "The knife planted deep inside her chest!"
    "No... No...!"
    show static_anim with Dissolve(2.0)
    "Static. Why is there static, why now, at a time like this?"
    "Wait. The knife."
    "It's not one of Catherine's kitchen knifes."
    "What is this!?"
    "It's Silvia's dagger! That's not possible...!"
    window hide
    scene dirty_room_vortex
    $ renpy.pause(8, hard = True)
    window show
    play music bgm_sad_loop
    "It's a strange sensation. Screaming without hearing your own scream. Without feeling it."
    "Just some awareness in the background of the hurricane storming through your mind, telling you that you're screaming."
    scene black with dissolve
    "Blackness. Inky blackness everywhere. I'm not sitting on the floor anymore."
    "I... am... {i}not{/i} sitting on the floor anymore."
    show sil angry at flip, right with moveinright
    n "Silvia...?"
    s "I'm sorry it had to go like this, Nicholas."
    n "What do you mean...? Hey, Sil, what do you mean?"
    "My mind is too confused to pick up on the fact that she knows my real name."
    n "You're sorry!? Do you mean... Y-you did this!? What the hell do you mean!?"
    "She doesn't even try to object to my accusation."
    show sil herp at flip, right
    s "I'm sorry. Just calm down..."
    n "Calm down!? Calm fucking down!? She was killed. She was killed... because of me!"
    "For some reason, I start laughing. The laughter of the damned."
    n "Hahaha... Hahahaaahaa!" # Fast
    show sil annoyed at flip, right
    with hpunch
    "Without warning, Silvia slaps me right on my cheek."
    s "Calm down, liege. It's not over yet. We can still fix things..."
    scene black with Dissolve(3.0)
    return
    # Dissolve to black. Thanks for playing.

# Mr. Smith, uses a speech synthesiser to mask his voice

label madman:
    $ stress += stress_modifiers['unreality']
    scene city_street
    play music bgm_main
    "It's raining."
    "We're making our way back to Catherine's apartment."
    show cat_torso orange at left
    show cat normal_down at left
    with moveinleft
    "She's letting me stand under her umbrella, but to be honest, it's pretty annoying to have to match her pace."
    n "Yeesh. There was nothing about this in the forecast."
    show cat smile
    c "That's pretty rare nowadays. Remember how everyone made fun of the weather forecasts back in elementary school."
    n "Oh, yeah. They were already pretty accurate in middle school, though."
    "At the start of this decade, developments in deep neural networks led to nigh impeccable weather forecasts."
    "You can count the amount of times the forecast is wrong in a year using one hand."
    "Up ahead, someone is shambling toward us, shouting loudly in a brown trenchcoat."
    show cat question
    n "Is that guy drunk or something?"
    show cat normal
    show image static_anim_weak
    "Man" "It's a sign, a sign I tell you! The apocalypse draws near!"
    "The man comes uncomfortably close, standing in front of me and staring into my eyes with an almost hypnotic strength."
    "Man" "Rejoice, for the last days are coming!"
    menu:
        "What the hell are you talking about?":
            n "Excuse me sir, what is your problem?"
            "Man" "The rain which is beyond prophecy. It is a sign from God!"
            menu:
                "What do you mean?":
                    n "Sign? What?"
                "You need to get some meds.":
                    n "Did you forget to take your pills today or something?"
            "He doesn't even seem to hear me."
            "Man" "God. All of reality is simulation in the mind of a superintelligence beyond our ken."
            jump .luxphoros
        "Ignore the man":
            "We try to walk around the man, but he won't let us leave."
            "Man" "God. God will destroy the world, end the simulation! The apocalypse, the singularity is nigh!"
            jump .luxphoros

label .luxphoros:
    n "What?"
    "I glance over at Catherine, but her expression is perfectly blank. Maybe she doesn't want to talk with the guy."
    n "Look, we don't want your fliers or whatever. Just, you know, piss off."
    "Man" "Fliers? No fliers. Luxphoros. God!"
    "That's a god from DFO. The one Aerith worships."
    n "Huh? Luxphoros is just a character in a virtual reality game."
    n "I think you should lay off the games for a while. You seem pretty confused."
    "Man" "Game? The game is a lie!" # And you lost it
    "Man" "A false simulacrum, an open illusion meant to convince you that one world is real and the other is false!"
    "Man" "But they're both false! All is simulation, I tell you."
    "He is trying to grab my shoulders now."
    n "Woah! Hey, you just keep your hands to yourself, pal!"
    "We walk around the guy, leaving him behind."
    "He just stands there, getting soaked in the rain."
    n "Man. Some people just lose all touch with reality."
    hide cat_torso
    hide cat
    with moveoutleft
    hide static_anim_weak
    "Catherine stops in her tracks."
    show cat_torso green at closeup
    show cat eyes_closed at closeup
    n "Cat...?"
    "Did I say something wrong?"
    scene city_street gradient_map with dissolve
    show cat_torso orange at closeup
    show cat not_normal at closeup
    show static_anim_weak
    play music bgm_scary
    "I look in her eyes, and I can see that something is very wrong here."
    "Am I... hallucinating? Why doesn't she look like a human anymore?"
    c "You shouldn't act like that, Nicholas."
    c "Someone might kill you one day."
    "H-huh? Kill me?"
    c "Don't ask stupid questions. Just ignore them."
    c "Don't lose touch with reality."
    scene city_street with dissolve
    show cat_torso orange at closeup
    show cat eyes_closed_smile at closeup
    c "Okay?"
    "W-what the hell does she mean, okay...?"
    return

label retro_message:
    $ stress += stress_modifiers['unreality']
    play music bgm_main
    scene arcade
    show static_anim_weak
    "I boot up some of the retro games again."
    "Oh, sweet, they have a new game! A shoot-em-up, by the looks of it."
    "I try my best to get on the leaderboard, but it's no use. These scores are seriously out of my league."
    "The names are limited to three capital letters, so it's impossible for me to tell who got those scores."
    "There's no date. Maybe they're really old."
    "Some of these names are really weird, anyway. Like the last one is just 'HER'."
    scene arcade gradient_map with dissolve
    play music bgm_scary
    "I blink as I take a closer look at the rest of the names."
    "Wait a minute."
    "These aren't names."
    "I start reading the letters in order."
    "IMG... OIN... TOK.. ILL... HER"
    "I am going to kill her!?"
    "My hands tremble on the joystick as I stare at the screen in shock."
    "Is it a coincidence? Am I, am I just imagining it?"
    scene city_street gradient_map with dissolve
    "I leave quickly, and as I walk the night streets, I can't help but feel I am being watched."
    play music bgm_main
    return

label at_the_bar_once_again:
    $ stress += stress_modifiers['unreality']
    play music bgm_main
    scene techno_bar with fade
    "I blink."
    "I am... in the bar? Wait, why am I here again?"
    "How did I get here? I don't remember anything after..."
    "I feel a bit sick. Are those drugs really messing with my head that much?"
    "I need to stop this. It's not healthy. It's not..."
    "My nausea grows, and I move into the bathroom, more to check on my on reflection than anything else."
    play music bgm_buzz
    show static_anim_weak
    "I do look a bit pale. And my eyes are bloodshot, perhaps from a lack of sleep."
    "I splash my face with cold water, hoping to regain my bearings."
    "Just me and my reflection, watching each other in silence."
    "Wait, in silence?"
    "It slowly dawns on me that I cannot hear the music coming from the bar anymore."
    "The sound isolation was never that good here. Why would the music stop?"
    "Then, the lights start flickering, and soon I stand in darkness."
    scene black with dissolve
    "Why do I feel a presence? Is someone watching me?"
    "As if someone was right behind me, breathing down my neck..."
    "The lights flicker back on."
    scene techno_bar gradient_map with dissolve
    show static_anim_weak
    "There's no-one there. Just my own eyes staring back at me."
    "It was probably just a power outage. Those are rare, but I hear there's been strange storms lately..."
    "Still, I can't help glancing around the room."
    "My eyes are drawn to the graffiti. Were they always there?"
    "Most of them are just artists senselessly professing their existence because they have nothing deeper to say."
    "But then I notice the one right in the middle, written with blood-red paint."
    "It's a message."
    "'Remember to keep your promises, Nicholas.'"
    stop music
    "For a moment, I can't even breathe. Then I walk away, far away from that bar, that message."
    scene city_street gradient_map with dissolve
    "It was definitely meant for me. Who else could it be for?"
    "My pace gradually quickens to a sprint, and I run, back home, back to safety, away from all this..."
    "... Insanity!"
    play music bgm_main
    jump events_skip_period
    return

label truck:
    $ stress += stress_modifiers['unreality']
    scene city_street
    "As I'm walking home, I'm struck by the beauty of the weather."
    "It sure is nice and cool, the evening air. I close my eyes, breathe it in and let it rejuvenate me."
    play music bgm_scary
    "As I open my eyes, I realize something strange."
    "I don't remember getting here. I was over there a moment ago."
    "Furthermore, this is no time to be in the middle of the road...!"
    "I don't have the time to finish that thought."
    "I barely even register the lights of the truck as my body is smashed into a fine pulp."
    scene black with dissolve
    pause 3
    show player_room with dissolve
    show static_anim_weak
    "I awaken screaming. It was... a dream? A nightmare? None of that... happened?"
    "It felt so real... I stare at my hand, trying to ensure its authenticity."
    play music bgm_main
    "I'm glad to be alive, at least."
    "Still disoriented, I begin to make breakfast."
    $ truck_handled = False
    $ morning_act = None
    $ afternoon_act = None
    $ evening_act = None

    window hide
    scene black with dissolve
    centered "{size=+10}{color=#fff}Morning{/color}{/size}{w=1.0}{nw}"

    call screen image_planner("Morning")
    jump morning

label truck_after:
    $ stress += stress_modifiers['unreality']
    scene player_room
    "Before going to sleep, I browse through the news stories for the day."
    "It's mostly the usual click-bait. Nothing too interesting."
    "One story does catch my attention, though."
    play music bgm_scary
    scene player_room gradient_map with dissolve
    show static_anim_weak
    "'Local man hit by truck: manufacturers blame a bug in the mapping system'"
    "I click on the story to read more. Someone was hit by a self-driving truck earlier today."
    "I look at the film captured by the truck's on board cameras."
    "It's the same intersection. At the same time."
    "And the man... I can't see his face with this resolution, but..."
    "His clothes! Why does he wear the same clothes!?"
    "I close the browser. I just can't take this anymore!"
    "I experience great difficulty falling asleep that night, tormented by visions of approaching headlights..."
    play music bgm_main
    scene black with Dissolve(2.0)
    return
    
    
label DFO_again:
    scene white with dissolve
    scene bg_plains with pixellate
    show sil normal at center
    play music bgm_main
        
    "I... huh?"
    "I blink as my eyes adjust to the vibrant hyper-reality around me."
    "Silvia is here with me."
    "But why am I here?"
    s "You look confused, liege."
    menu:
        "Why am I here?":
            np "Why am I here?"
            show sil question
            s "Whatever do you mean, liege?"
        "Sorry, I'm just feeling a bit dizzy.":
            np "Sorry. I got dizzy there for a moment."
            show sil question
    s "Do you not want to continue grinding?"
    np "Grinding?"
    show sil normal
    menu:
        "What do you mean?":
            np "What do you mean, grinding?"
            s "Vanquishing weak enemies in order to gain experience."
            show sil question
            s "You ought to know this, liege. Did you hit your head, perchance?"
            np "No, I mean, we've been grinding? For how long?"
        "How long have we been grinding?":
            np "Just how long have we been grinding?"
    s "The hourglass has turned twice."
    "Two hours?"
    # Promise with Catherine?
    s "Do you desire rest?"
    menu:
        "Yes.":
            np "Yeah, I think I need to sit down for a moment."
            "We find a safe area and sit down to rest."
        "No.":
            np "No, we can keep going. I'm sure it was just momentary."
            "We grind for a while longer, then go to a safe area to sit down and rest."
    show sil at closeup
    s "Back there, it was not mere dizziness which confused you."
    "Damn. She's perceptive."
    s "You did not remember what we had been doing. What is wrong, my liege?"
    
    return