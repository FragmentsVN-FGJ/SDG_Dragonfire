transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
        
screen countdown(time, timer_jump):
    timer time action Jump(timer_jump)

screen countdown_bar(time, timer_jump):
    if timer_vars == None:
        $ timer_vars = {"time": time, "timer_range": time}
    timer 0.01 repeat True action If(timer_vars["time"] > 0, true=SetDict(timer_vars, 'time', timer_vars['time'] - 0.01), false=[Hide('countdown_bar'), SetVariable("timer_vars", None), Jump(timer_jump)])
    bar value timer_vars["time"] range timer_vars["timer_range"] xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
    
label mood_reset(person):
    $ mood[person] = 0
    return
    
label mood_modify(person, amount):
    if amount > 0:
        show screen remember_popup_window(person+" looks a bit happier.")
    if amount < 0:
        show screen remember_popup_window(person+" seems displeased.")
    $ mood[person] += amount
    return
    
label parlorStart:
    call mood_reset("Catherine")
    $ parlor_visited = True
    
    $ timer_vars = None

    play music bgm_main
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
    play music "bgm/SFX_City_ambience_1.mp3"
    "There's a bit of an awkward silence as we sit down. Cat is staring at the table, avoiding eye contact."
    $ parlorwait = False
    $ parlorapology = False
    $ parloridle = False
    
    $ timer_vars = None
    "She's fiddling with a napkin, deliberating something, but can't get the words out."

#    show screen countdown_bar(10, "parlorWait")

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
#    if not parlorwait:
#        show screen countdown_bar(10, "parlorWait")
#    else:
#        show screen countdown_bar(10, "parlorBeg")
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
    call mood_modify("Catherine", 1)
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
    
    if mood["Catherine"] < 0:
        "She doesn't take that too kindly."
        show cat anger
        c "Yeah, just like last time!"
        "She gets up and storms out, leaving her half-eaten ice cream behind."
        $ affection_modify('Catherine', -2)
    else:
        show cat longing
        $ spendtimepromise = True
        "She seems a bit sad."
        c "I guess I just have to believe you. Again."

    window hide
    scene black with Dissolve(5.00)
    pause 3.0

    return

label promiseMovies:
    n "I'll take you to the movies."
    $ moviepromise = True
    
    if mood["Catherine"] < 0:
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

    if mood["Catherine"] < 0:
        show cat something
        "Her expression alternates between anger and frustration."
        c "What makes you think I'd be interested in that stupid game?"
        show cat normal_down
        c "Sorry... But, you know..."
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
    call mood_modify("Catherine", -1)
    show cat something2
    play sound sfx_thud
    with vpunch
    "She slams her fist on the table."
    c "Don't call me that! First you disappear for two weeks, then I call you and you act as if nothing has happened!"
    show cat something

#    if not parlorwait:
#        show screen countdown_bar(10, "parlorWait")
#    else:
#        show screen countdown_bar(10, "parlorBeg")
    
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

    if mood["Catherine"] < 0:
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

    $ stress += stress_modifiers['breakup']
    $ broken_up = True
    $ affection_modify('Catherine', -2)

    return

label parlorArgue:
    n "What you said about me not studying."
    n "I am going to study. I just need to decide what."
    n "I feel like most of the choices available are just pointless."
    n "If only reality was more like a game..."

    if mood["Catherine"] < 0:
        show cat anger
        c "You're a fucking addict, you know that?"
        n "Gaming keeps me together! Why can't you get that!?"
        c "Whatever. Just keep playing your games. No need to call."
        "With that, she storms out."
        show cat at getup_and_leave
        show cat_torso at getup_and_leave
        $ stress += stress_modifiers['breakup']
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

    if mood["Catherine"] < 0:
        show cat angry
        c "It's stressful now! But at least I won't be dying alone in some godforsaken apartment playing a stupid video game because I have no life!"
        show cat something
        c "Whatever. Just keep playing your games. No need to call."
        "With that, she storms out."
        show cat at getup_and_leave
        show cat_torso at getup_and_leave
        $ stress += stress_modifiers['breakup']
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
    call mood_modify("Catherine", 1)
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

    if mood["Catherine"] < 0:
        show cat frown
        "Cat frowns."
        c "That's not the real problem. Even if you stop playing, you won't change."
        show cat normal_downright
        c "Just... Goodbye, Nick."
        "She gets up and leaves."
        show cat at getup_and_leave
        show cat_torso at getup_and_leave
        $ stress += stress_modifiers['breakup']
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

    if mood["Catherine"] < 0:
        c "Yes. Well then, goodbye, Nicholas."
        "With that, she gets up and goes."
        show cat at getup_and_leave
        show cat_torso at getup_and_leave
        $ stress += stress_modifiers['breakup']
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

    if mood["Catherine"] < 0:
        show cat frown
        c "I don't think so. This is it, Nicholas."
        hide cat with dissolve
        hide cat_torso with dissolve
        "Before I have a chance to respond, she gets up and leaves."
        show cat at getup_and_leave
        show cat_torso at getup_and_leave
        $ stress += stress_modifiers['breakup']
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

        if mood["Catherine"] < 0:
            show cat frown
            c "That's what you got me? The cheapest one on the menu?"
            c "Is this some kind of joke?"
        else:
            show cat normal_right
            "Catherine doesn't seem too impressed with the ice cream I got her."
            "Still, she sticks a spoon in it and begins eating."

        call mood_modify("Catherine", -1)

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

        call mood_modify("Catherine", 1)

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
            call mood_modify("Catherine", -1)
        else:
            show cat fuun
            "Catherine seems to slightly cheer up as she sees what I bought her."
            c "Oh, thanks, Nick. That was thoughtful of you."
            call mood_modify("Catherine", 1)

    if parloridle:
        show cat longing
        c "Sorry for lashing out at you earlier."
        c "I'm just... That thesis is really stressing me out."
        c "I didn't mean to be so..."
    n "A-anyway."
    return