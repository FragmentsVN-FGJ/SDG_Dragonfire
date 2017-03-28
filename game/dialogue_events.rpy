init -50 python:

    all_dialogue_events = []

    class dialogue_event(event):        
        def __init__(self, name, *args, **kwargs):

            self.name = name

            exprs = [ ]

            for i in args:
                if isinstance(i, basestring):
                    exprs.append(event.evaluate(i))
                else:
                    exprs.append(i)

            self.exprs = exprs

            self.priority = kwargs.get('priority', 100)
            
            all_dialogue_events.append(self)
            
# Call this for procedural dialogue
label run_dialogue_events:

    $ dialogue_events = [ ]

    python hide:

        eobjs = [ ]
        egroups = { }
        eingroup = { }

        for i in all_dialogue_events:
            if not i.check(eobjs):
                continue
                
            eobjs.append(i)

            props = i.properties()

            if 'group' in props:
                group = props['group']
                count = props['group_count']

                egroups.setdefault(group, [ ]).extend([ i ] * count)
                eingroup[i] = group

            if 'only' in props:
                break

        echosen = { }

        for k in egroups:
            echosen[k] = renpy.random.choice(egroups[k])
            
        for i in eobjs:

            if i in eingroup and echosen[eingroup[i]] is not i:
                continue
            
            dialogue_events.append(i.name)


    while len(dialogue_events) > 0:

        $ _event = dialogue_events.pop(0)
        $ events_executed[_event] = True

        call expression _event from _call_expression

    return

# START OF DIALOGUE EVENTS

init:
    $ dialogue_event('default_conversation', "conv=='start'", priority=5)
    $ dialogue_event('sunnyweather', "conv=='start' and cloudiness=='sunny'", priority=10)
    $ dialogue_event('rainyweather', "conv=='start' and raining > 1", priority=10)
    $ dialogue_event('coolweather', "conv=='start' and temperature=='cool'", priority=10)
    $ dialogue_event('catherinelate', "conv=='start' and catlate==True", priority=5)
    $ dialogue_event('nicklate', "conv=='start' and nicklate==True", priority=5)
    $ dialogue_event('sweating', "conv=='start' and nickcondition==' sweating heavily,'", priority=15)
    $ dialogue_event('soaked', "conv=='start' and nickcondition==' soaking wet,'", priority=15)

init 100:
    python hide:
        #Sort all events on priority.
        all_dialogue_events.sort(key=lambda i : i.priority)

    python hide:

        for i in all_dialogue_events:
            if not renpy.has_label(i.name):
                raise Exception("'%s' is defined as an event somewhere in the game, but no label named '%s' was defined anywhere." % (i.name, i.name))

    
label default_conversation:
    c "Hi. How are you?"
    n "Hi, how are you."
    return
    
label sunnyweather:
    c "It sure is nice weather we're having."
    n "Yeah, not a cloud on the sky."
    return
    
label rainyweather:
    c "It sure is raining hard."
    n "Let's get inside soon."
    return
    
label coolweather:
    c "The breeze sure is relaxing."
    return
    
label catherinelate:
    $ bitlate = renpy.random.choice(["I'm a bit late", "for being a bit late", "I'm so late", "for being so late"])
    $ reason = renpy.random.choice(["The bus wasn't on time.", "I didn't even notice the time.", "I forgot something and had to turn back.", "I was choosing clothes again...", "It took really long to decide what to wear..."])
    c "Sorry [bitlate]. [reason]"
    c "Did you wait for long?"
    menu:
        "I just got here.":
            c "That's good to hear."
        "That was very thoughtless of you.":
            c "Come on, Nick. I'm not usually like this."
        "Choosing clothes again?":
            c "Well, yeah, you know how I am."
    return
    
label nicklate:
    if trust['Catherine'] < 0:
        c "Late as usual, huh."
    n "Sorry, did you wait for long?"
    $ i = renpy.random.random()
    if i < 0.5:
        if affection['Catherine'] > 2:
            c "No, I just got here."
        else:
            c "Well, you shouldn't keep a woman waiting."
    else:
        if affection['Catherine'] < 0:
            c "Yes. Yes I did, Nick."
        else:
            if trust['Catherine'] < 0:
                "She sighs."
                c "I'm used to it."
            else:
                c "Yes, but I suppose you must have a reason."
                c "I won't inquire further."
    return
    
label sweating:
    c "Oh, you're sweating."
    if not handkerchief:
        c "Want a handkerchief?"
        menu:
            "Sure.":
                c "Here you go."
                $ handkerchief = True
            "I'll pass.":
                c "All right then."
    return
    
label soaked:
    c "You're all wet!"
    if not umbrella:
        c "Where's your umbrella?"
        n "I left it at home."
        c "Didn't you check the forecast?"
    else:
        c "Even though you have an umbrella..."
        c "Did you slip?"
    return

label Catherine_ask_about_sauna:
    c "By the way, what the hell were you doing back there at the sauna?"
    n "Oh, that..."
    return