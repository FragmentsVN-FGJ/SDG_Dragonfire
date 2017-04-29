init:
    $ event("callCatherine", "act == 'callcat' and not broken_up", event.only(), priority=5)

    $ event("Catherine_afternoon_call_ignored2", "call_ignored and 'Catherine' not in forgotten_promises and unkept_promises_personal_counter['Catherine'] >= 3 and period == 'afternoon'", priority=5)
    $ event("Catherine_afternoon_call_ignored", "call_ignored and 'Catherine' not in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 1 and period == 'afternoon'", priority=5)
    $ event("Catherine_morning_call3", "'Catherine' in unhandled_forgotten_promises.keys() and unkept_promises_personal_counter['Catherine'] > 2 and period == 'morning'", priority=5)
    $ event("Catherine_evening_call3", "call_ignored and 'Catherine' in unhandled_forgotten_promises.keys() and unkept_promises_personal_counter['Catherine'] > 2 and period == 'evening'", priority=210)
    $ event("Catherine_afternoon_call2", "'Catherine' in unhandled_forgotten_promises.keys() and unkept_promises_personal_counter['Catherine'] == 2 and period == 'afternoon'", priority=5)
    $ event("Catherine_morning_call1", "'Catherine' in unhandled_forgotten_promises.keys() and unkept_promises_personal_counter['Catherine'] == 1 and period == 'morning' and not call_ignored", priority=5)
    $ event("Catherine_afternoon_call1", "call_ignored and 'Catherine' in unhandled_forgotten_promises.keys() and unkept_promises_personal_counter['Catherine'] == 1 and period == 'afternoon'", priority=5)
    $ event("Catherine_evening_call1", "call_ignored and 'Catherine' in unhandled_forgotten_promises.keys() and unkept_promises_personal_counter['Catherine'] == 1 and period == 'evening'", priority=5)
    $ event("answer_Catherine_neglected", "not broken_up and period == 'afternoon' and dayswocat >= 3 and (moviepromise or spendtimepromise)", event.once(), priority=5)

    
init python:
    def calculatedayswithoutseeingCatherine():
        global promises
        global day
        daylastseen = 0
        for (place, promiseday) in promises.keys():
            if promiseday <= day:
                if promiseday > daylastseen:
                    if ('Catherine', 'meet') in promises[(place, promiseday)].keys() and promises[(place, promiseday)][('Catherine', 'meet')]:
                        daylastseen = promiseday
        return day - daylastseen
        
    
# Catherine should call after every other date if she was happy with it.

label callCatherine:
    $ i = renpy.random.random()
    if i < 0.333:
        "I listen to the beeps for a long time."
        "Then, Catherine picks it up."
    elif i < 0.666:
        "I call, and Catherine picks up quickly."
    else:
        "It takes a while for Catherine to answer."

    if 'Catherine' in unhandled_forgotten_promises.keys() and unkept_promises_personal_counter['Catherine'] == 1:
        if not call_ignored:
            jump answer_Catherine_morning_call
        else:
            jump answer_Catherine_ignored_call
    elif 'Catherine' in unhandled_forgotten_promises.keys() and unkept_promises_personal_counter['Catherine'] == 2:
        jump answer_Catherine_afternoon_call2

    c "Hi?"
    n "Hi! I was wondering if you'd like to set up a date?"
    c "When?"
    jump Catherine_setupdate
    
label Catherine_setupdate:
    menu:
        "Today":
            $ date_day = day
        "Tomorrow":
            $ date_day = day+1
        "Two days from now":
            $ date_day = day+2
        "Three days from now":
            $ date_day = day+3
        "Next week":
            $ date_day = day+4
        "Never mind.":
            jump .nevermind
    c "Yeah, okay. Where should we meet?"
    menu:
        "Movie theater":
            $ date_location = "movies"
        "VR Arcade":
            $ date_location = "arcade"
        "Never mind":
            jump .nevermind
    c "All right, see you there!"
    n "Yeah, see you!"
    "I can barely wait."
    $ promises[(date_location, date_day)] = {("Catherine", "meet"): False}
    return
    
label .nevermind:
    n "Actually, never mind. I'll call you later."
    "She sounds a bit bemused."
    c "Uh-huh. Later."
    return

label Catherine_afternoon_call_ignored2:
    "For a few seconds, I can feel my wristband vibrate."
    "Seems Catherine called without giving me an opportunity to answer."
    "My hands are shaking a bit. Should I call her back?"
    menu:
        "Call her":
            "For what seems like an eternity, I stand listening to the beeps in my ear."
            "The worst possible scenario comes to mind. But finally, she does pick it up."
            n "Hi."
            c "Look who decided to call. For once."
            jump Catherine_calls_ignored
        "Leave her be":
            "Sorry, Cat. This is better for us both."
            $ affection_modify('Catherine', -1)
            $ stress += stress_modifiers['breakup']
            $ broken_up = True
    return

label Catherine_afternoon_call_ignored:
    "I feel someone's call on my wrist again."
    "Yeah, there's no question who it is."
    "Should I answer her?"
    menu:
        "Answer":
            $ call_ignored = False
            n "Hi."
            c "Why have you been ignoring my calls?"
            n "I, I guess I've been really busy."
            c "You 'guess'?"
            "She sighs audibly."
            c "Whatever. I didn't expect you to understand."
            "She ends the call with that."
        "Ignore":
            $ stress += stress_modifiers['ignore_calls']
            $ call_ignored = True
            "I wonder how long we can keep this up?"
    return

label Catherine_morning_call3:
    scene player_room
    $ unhandled = unhandled_forgotten_promises.pop('Catherine')
    $ time = say_days(day-unhandled[1])
    $ location = unhandled[0]
    $ at_location = say_at_location(location)
    "I gulp as I feel the vibrations of my wristband."
    "Catherine must be furious. I really really really don't want to talk with her."
    menu:
        "Answer":
            $ call_ignored = False
            "There's a moment of silence as I pick up. I just can't get the words out of my throat."
            c "Hello? Nicholas? I know you're there."
            n "H-hi, Cat..."
            c "So, didn't see you [at_location] yesterday."
            n "I-I guess I..."
            c "I don't really care what you're excuse is this time."
            c "I just can't trust you anymore, Nick."
            c "This is as hard on me as it is on you, but... Goodbye, Nick."
            "She hangs up, one last fatal blow to my guts."
            n "C-Catherine..."
            $ stress += stress_modifiers['breakup']
            $ broken_up = True
        "Ignore":
            $ stress += stress_modifiers['ignore_calls']
            $ call_ignored = True
            "I ignore her call, feeling kind of embarrassed."
    $ affection_modify('Catherine', -1)
    return

label Catherine_evening_call3:
    scene player_room
    "Catherine is calling again."
    "Should I just answer it and get it over with?"
    "I can already guess what she is going to say."
    "I really blew it this time."
    menu:
        "Answer":
            $ call_ignored = False
            jump Catherine_calls_ignored
        "Ignore":
            $ stress += stress_modifiers['ignore_calls']
            $ call_ignored = True
            "Please, Cat, just don't call me anymore..."
    return

label Catherine_calls_ignored:
    "Before I have time to respond, Cat starts talking."
    "She sounds like she's on the verge of tears."
    c "Nicky, why are you avoiding me? Am I just that evil?"
    n "I-I didn't mean it like that."
    c "NEVER MIND WHAT YOU MEANT!"
    "For a moment, all I can hear is her heavy breathing. Then..."
    c "Nicholas, it's over. I can't trust you. And you clearly do not like me. Goodbye."
    "Before I can say anything, she hangs up one last time."
    "And I'm left contemplating my life in silence."
    $ stress += stress_modifiers['breakup']
    $ broken_up = True
    return

label Catherine_afternoon_call2:
    "My wristband signals another call from Catherine."
    "She just won't leave me alone, huh?"
    menu:
        "Answer":
            $ call_ignored = False
            jump answer_Catherine_afternoon_call2
        "Ignore":
            $ stress += stress_modifiers['ignore_calls']
            $ call_ignored = True
            "I ignore the call, hoping that she will do likewise."
    return

label answer_Catherine_afternoon_call2:
    $ unhandled = unhandled_forgotten_promises.pop('Catherine')
    $ time = say_days(day-unhandled[1])
    $ location = unhandled[0]
    $ at_location = say_at_location(location)
    $ call_ignored = False
    n "Nicholas."
    c "Oh, I know very well who I'm calling. An inconsiderate jackass!"
    n "What's the problem?"
    "I know full well what the problem is, but..."
    c "You broke your promise the second time in a row! I'm just so... Argh!"
    menu:
        "Promise to meet her again":
            n "Look, I'm sorry I messed up again. Let's meet [at_location] tomorrow, what do you say?"
            c "... I guess that would be nice. But if you ditch me again, it's over!"
            "The threat makes the hair of my neck stand up a bit."
            python:
                if (location, day+1) in promises.keys():
                    promises[(location, day+1)][("Catherine", "meet")] = False
                else:
                    promises[(location, day+1)] = {("Catherine", "meet"): False}
        "Threaten to break up with her":
            # Should test for affection here
            n "Look, this is the way I am. Stop trying to change me, or I'll break up with you!"
            c "You know, maybe that would be for the best."
            n "Eh, what!?"
            c "No need to call back, Nick. Goodbye."
            $ stress += stress_modifiers['breakup']
            $ broken_up = True
        "Apologize":
            n "I'm really sorry, Cat. It won't happen again."
            c "It better not. Or it's over."
    "I'm left listening to the beeping of the ended call."

    return

label Catherine_morning_call1:
    scene player_room
    "I wake up to the vibrations of my wristband."
    "It's Catherine."
    menu:
        "Answer":
            $ call_ignored = False
            jump answer_Catherine_morning_call
        "Ignore":
            $ stress += stress_modifiers['ignore_calls']
            $ call_ignored = True
            $ affection_modify('Catherine', -1)
            "I click the ignore button."
            "I just can't face her this early in the morning."
    return

label Catherine_afternoon_call1:
    "My wristband is vibrating again."
    "Seems Catherine is trying to call again."
    menu:
        "Answer":
            $ call_ignored = False
            call answer_Catherine_ignored_call
        "Ignore":
            $ stress += stress_modifiers['ignore_calls']
            $ call_ignored = True
            "I click the ignore button again."
            "I'm too busy, okay?"
    return

label Catherine_evening_call1:
    "I shudder as my wristband vibrates yet again."
    "I don't even have to look to know who it is."
    menu:
        "Answer":
            $ call_ignored = False
            call answer_Catherine_ignored_call
        "Ignore":
            $ stress += stress_modifiers['ignore_calls']
            $ call_ignored = True
            "I click the ignore button and hope she doesn't call again."
    return

label answer_Catherine_morning_call:
    n "Hi there."
    $ call_ignored = False
    $ unhandled = unhandled_forgotten_promises.pop('Catherine')
    $ time = say_days(day-unhandled[1])
    $ location = unhandled[0]
    $ at_location = say_at_location(location)
    c "Nick, what the hell? Weren't we supposed to meet [time]?"
    menu:
        "Claim you forgot":
            n "Oh, we were? I guess I forgot."
        "Claim you were busy":
            n "Sorry, Catherine. Something came up."
        "Say you were tired":
            n "I was just too tired to come."
    c "Just as long as you weren't playing that freaking game again!"
    n "Look, I'll meet you [at_location] tomorrow, okay?"
    c "You'd better come this time!"
    python:
        if (location, day+1) in promises.keys():
            promises[(location, day+1)][("Catherine", "meet")] = False
        else:
            promises[(location, day+1)] = {("Catherine", "meet"): False}
    "With that, she hangs up."
    return

label answer_Catherine_ignored_call:
    $ unhandled = unhandled_forgotten_promises.pop('Catherine')
    $ time = say_days(day-unhandled[1])
    $ location = unhandled[0]
    $ at_location = say_at_location(location)
    $ call_ignored = False
    n "H-hi."
    c "What's going on? Why didn't you answer me before?"
    c "First you break your promise, then you don't even return my calls."
    n "Oh, that? Let's meet tomorrow, [at_location]. Sound good?"
    c "This time, you'd better actually be there!"
    python:
        if (location, day+1) in promises.keys():
            promises[(location, day+1)][("Catherine", "meet")] = False
        else:
            promises[(location, day+1)] = {("Catherine", "meet"): False}
    "She hangs up."
    return

label .cat_question:
    menu:
        "Claim you didn't notice her call":
            n "Sorry, I hadn't noticed it until now."
        "Claim you forgot":
            n "Sorry, I was going to, but then I did something else and forgot entirely."
        "Claim you were busy":
            n "Sorry, Catherine. I've been too busy the whole day."
    c "Too busy playing DFO, I venture."
    n "C'mon, that's not fair."
    return

label answer_Catherine_neglected:
    "Catherine is calling."
    menu:
        "Should I answer?"
        "Answer":
            "I pick up the call."
        "Ignore":
            "Sorry, Cat."
            return
    n "H-hi."
    c "Hi! Um, how are you doing?"
    menu:
        "Ask her what this is about.":
            n "What do you want?"
            c "I was thinking..."
        "Tell her you're fine.":
            n "Fine, thanks. You?"
            c "Fine, fine. Um, I was just wondering..."
    menu:
        "Tell her to spit it out.":
            n "Spit it out."
            "Her voice turns irritated."
        "Wait":
            c "You know..."
    jump .promise
    
label .promise:
    python:
        if spendtimepromise:
            yourpromise = "spend more time"
        else:
            yourpromise = "go to the movies"
        spendtimepromise = False
        moviespromise = False
    c "Last time, at the parlor, didn't you promise to [yourpromise] with me?"
    menu:
        "Now that you mention it...":
            n "Umm, I might have..."
        "Nope.":
            n "Nope. I don't think I did."
            c "Uh-huh."
            c "Oh really? I remember you saying something like that."
    c "It's been three days now, so I was starting to wonder..."
    menu:
        "Ask her out.":
            n "Uh, well let's go out!"
            c "Wh- really?"
            n "What do you say?"
            c "O-of course. When?"
            jump Catherine_setupdate
        "Apologize.":
            n "I'm sorry, Catherine. I'll, I'll spend more time with you from now on."
            c "Yeah... I believe you, Nicky..."
            c "Although sometimes I'm not sure why."
        "Blame her.":
            n "It's all your fault, you know."
            c "H-huh?"
            n "At first, I was thinking of spending more time with you."
            n "Then I realized what a total bitch you are!"
            n "You're always trying to cont..."
            "She hangs up."
            "Good riddance."
            $ broken_up = True
    return