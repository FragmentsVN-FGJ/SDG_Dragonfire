init python:
    def andlisting(alist):
        if len(alist) == 0:
            return ""
        elif len(alist) == 1:
            return alist[0]
        else:
            return ", ".join(alist[0:len(alist)-1]) + " and " + alist[-1]
            
init:
    $ cat_mood = 0

# Movie theatre

label MonsterInTheHouse:
    $ cat_opinion = 0
    "House Alone 12 tried to break away from the established conventions by flirting with the horror genre."
    "A grown-up Kevin moves to a haunted house and is tormented by the ghosts of the criminals his antics killed back in the seventh installment."
    "To be honest, they've been milking this franchise for way too long."
    return
    
label Immanence:
    $ cat_opinion = -1
    "Immanence is a near-future sci-fi flick about a man whose consciousness is uploaded to the internet, which turns him into a low-level superintelligence." "He uses his newfound powers to take over the world and shapes it in his image, but ends up realizing that having god-like powers may not be the best of things for a fundamentally flawed creature."
    "In the dramatic ending, he sacrifices himself to turn back time by reconstructing the world as it used to be before his ascension."
    "The movie ends with his parting words in an e-mail he sent to his lover, who is the only one that can still remember the other world."
    "'The utility function of humanity may be flawed and inherently contradictory, but it's what allows us to feel love.'"
    "What a great movie! I'm not sure if Catherine liked it, though..."
    return
    
label DrMachine:
    $ cat_opinion = 0
    "Dr. Machine is a modern-day film noir about a former Cyber Crime Prevention Center investigator who meets a mysterious black-hat hacker titling herself Dr. Machine."
    "Dr. Machine has a scheme to destroy the oppressive capitalist system controlling the world from the shadows by destroying the loan databases of various megacorps."
    "The investigator is in dire need of cash and pretends to take the deal, soon being swept up in a conspiracy far beyond anyone's wildest imaginings."
    "It's pretty cool, and there's some weird narrative tricks being played out as well."
    return
    
label ItHappenedOnOneRoad:
    $ cat_opinion = 1
    "It Happened on One Road is a road movie about a reporter and a runaway girl walking the world in the aftermath of a nuclear war of some sort."
    "They're seeking a device called the 0-Grail, which will allow the world to recover. Except it's never really made clear whether the object of their questing even exists."
    "The movie focuses on the development of their relationship, ending tragically with them both dying from radiation poisoning, the reporter reassuring the girl that they will find the Grail as soon as morning comes."
    "Sorrowful and deeply symbolic, I wonder if Catherine enjoyed it...?"
    return
    
label OneLifeOneGame:
    $ cat_opinion = -1
    "One Life One Game tells the tale of a gaming addict who tries to shut off reality but is constantly pulled back into it by her circumstances."
    "It puts a twist on the usual scheme by implying that the gaming world might be better for her than the real one anyway."
    "Still, it's fairly traditional, so I'm not too impressed. And I doubt Catherine appreciates the message..."
    return
    
label NordicValley:
    $ cat_opinion = 1
    "Nordic Valley is a comedy about the startup hipster scene in Sweden. It documents the rise and fall of an unicorn company seeking to better the lives of Stockholm university students with a new and innovative app."
    "In the meantime, it pokes fun at the scene, but I hear startup people in the nordics don't like it that much. They consider it almost too accurate."
    "I wonder if this kind of humor strikes Catherine the right way? She didn't laugh that much, but the comedy was kind of low-key..."
    return
    
label ABoyAndHisGlob:
    $ cat_opinion = 0
    "A Boy and His Glob is, sadly, yet another bad adaptation of a popular video game on the big screen. All of the original plot is lost and replaced with one that was obviously stolen from some Rin Tin Tin film."
    "I fall asleep halfway through, so I have little idea of Catherine's reactions to it. She's not a gamer, so maybe she even liked it?"
    return
    
label BrotherPowa:
    $ cat_opinion = -1
    "Superhero movies hit a slump after basically every important hero had starred in a trilogy or two. The few still getting made tend to be based on comics so obscure, it borders on the ridiculous."
    "I mean, this one, Brother Powa the Nerd, is about a freaking mannequin coming to life after getting hit by a lightning bolt. It looks like the movie is trying to be dark and edgy..."
    "But in all sincerity, it comes across as comical instead."
    return
    
label CardUpMy:
    $ cat_opinion = 1
    "Card Up My... is a weird dramedy about an economist trying to survive the historic collapse of 2018 famously caused by the last president of the United States (whose name has been stricken from the record)."
    "It's actually pretty funny. Every other scene evokes a burst of laughter."
    return

label ForestGuy2:
    $ cat_opinion = 1
    "Forest Bump 2: the Foresting is a sequel to the famous film classic. Do they really have to monetize everything in existence?"
    "Frankly, this just leaves me feeling cynical..."
    return

label VRArcadeDate:
    scene city_street
    call date_arrival 
    $ cat_mood = 0
    call .payment
    scene arcade with dissolve
    show cat normal at left
    show cat_torso orange at left behind cat
    call .what_to_do 
    jump date_end
    
label .payment:
    if not visited['arcade']:
        "Like most arcades of the modern era, TechnoLazers has an entrance fee. The games themselves are completely free."
    "I wonder if I should pay for Catherine as well?"
    show cat normal at left
    show cat_torso orange at left behind cat
    with moveinleft
    call check_wallet 
    $ entrance_fee = prices['arcade']
    "The entrance fee is [entrance_fee], eh."
    jump .payment_menu
    
label .payment_menu:
    menu:
        "Go for it." if cash > prices['arcade_both']:
            n "I'll pay for you, Cat."
            show cat smile
            c "Oh? Thanks, Nick."
            call pay(prices['arcade_both']) 
            if not pay_successful:
                "It seems I don't have enough money after all..."
                jump .payment_menu
            $ cat_mood += 2
        "Better just pay for yourself.":
            call pay(prices['arcade']) 
            if not pay_successful:
                n "Well, this is embarrassing."
                call .cat_pays 
        "No, no. She's the one who should pay.":
            call .cat_pays 
    return

label .cat_pays:
    n "Cat, do you think you could pay for me?"
    n "I'm in dire straits."
    show cat eyes_closed
    "She sighs and pays for my ticket."
    "Sorry..."
    $ cat_mood -= 2
    return
        
label .what_to_do:
    "Cat looks around the hall, her face displaying nothing but mild disinterest."
    menu:
        "Let's play retro games.":
            n "Here, you've tried any retro games before?"
            show cat normal_downright
            c "With you, yes. I wasn't too impressed."
            n "Um, I'm sure you'll like it this time."
            show cat normal
            c "I hope so too."
            menu:
                "Show her a fighting game.":
                    $ game = renpy.random.choice(["Mortal Kombat", "Garou: Mark of the Wolves", "Super Street Fighter II"])
                    "I show her [game], but she's not too interested in playing it."
                    show cat frown
                    c "So you like these kinds of violent games, huh..."
                    $ cat_mood -= 1
                "Show her a racing game.":
                    $ game = renpy.random.choice(["F-Zero AX", "Crazy Taxi", "Race Driver: GRID"])
                    "We play [game] for a while."
                    "As expected, she's pretty terrible at it."
                    show cat normal_left
                    c "See, this is why I'm getting an autonomous as soon as they become affordable..."
                "Show her a quiz game.":
                    $ game = renpy.random.choice(["Quiz: Ah! My Goddess", "Professor Pac-Man", "Quiz & Dragons"])
                    "We spend our time playing [game]."
                    "Suprisingly, she actually seems to find the game exciting."
                    show cat fuun
                    c "That was pretty fun. Weird, but fun."
                    $ cat_mood += 1
        "I'll show you some of the VR demos.":
            "I have to check the selection myself. Most of the time, I just play at home..."
            menu:
                "Show her something artsy.":
                    "Desaline is a slow, mystic virtual reality experience where movement is controlled by breathing."
                    "Catherine seems disoriented as she takes off the headset."
                    show cat question
                    c "That... was... perplexing."
                    show cat smile
                    c "But somehow eye-opening."
                    $ cat_mood += 2
                "Time for some horror.":
                    "There they die is one of the great classics of VR horror games."
                    "You navigate a city with a foul secret, doing your best to escape the clutches of the many abominable stalkers of the night, looking for prey."
                    show cat shock
                    c "That was horrible! Nick, why did you make me play that!?"
                    show cat surprise_down
                    n "See? I told you you would like it!"
                "A galactic shooter should do.":
                    "EVA: Keres is one of the most iconic space shooters in the history of virtual reality games."
                    "It's also one of the oldest ones here."
                    "The early age of modern VR is almost synonymous with space shooters, since being stuck in a cockpit provides a natural reason for the player to sit."
                    "And it's also effective for alleviating the nausea."
                    "Catherine doesn't seem to be very good at this game, though."
                    show cat question
                    c "I can't decide whether that was exhilarating or frustrating."
        "Want to play laser tag?":
            "Her eyes light up as she processes the suggestion."
            show cat fuun
            c "That sounds interesting!"
            c "Do you know how to play?"
            menu:
                "No, but we'll figure it out.":
                    show cat smile
                    c "Uh-uh. Maybe it'll be more fun that way."
                "Yes, I'm a pro.":
                    show cat seductive_or_something
                    c "Hah, we'll see about that!"
                    $ cat_mood += 1
                "I'm alright.":
                    show cat blush
                    c "Remember to go easy on me."
            "We spend our time playing with Catherine. She looks pretty happy."
        "Let's watch a robot brawl!":
            c "Okay. No harm in trying it out."
            "You can also remote control the robots here, but it's pretty costly, so better stick to just watching the show for now."
            "The sparks and hydraulic fluid spraying all around really get my heart pounding!"
            show cat tired
            "Catherine is less enthusiastic, however."
            n "Pretty amazing what those bots can do, huh?"
            show cat normal_downright
            c "I suppose it qualifies as entertainment."
            $ cat_mood -= 1
    return

label MovieTheatreDate:
    #call .datestart
    #call .ticketbooth
    #call .seating
    #call .movie
    #call .opinions
    #call .onhermind
    #call .dateend
    scene city_street
    call date_arrival 
    $ cat_mood = 0
    call .tickets 
    return
    
# The date start should depend on:
# * Affection Level
# * Trust level (openness)
# * RNG 1: Who arrives first
# * RNG 2: Weather
# * RNG 3: How long is the wait
# * Location
# * Location of last date
# * Previous activity
# * Time since last meeting
# * Catherine's mood at the end of the last meeting
# * Nick's qualities: Runner, Flatterer, Apologist

# Structure:
#date_arrivals
# Dialogue
# Going in

label .tickets:
    $ movie_choices = [("House Alone 12", "MonsterInTheHouse"), ("Immanence", "Immanence"), ("Dr Machine", "DrMachine"),
    ("It Happened on One Road", "ItHappenedOnOneRoad"), ("One Life, One Game", "OneLifeOneGame"), ("Nordic Valley", "NordicValley"),
    ("A Boy and His Glob", "ABoyAndHisGlob"), ("Brother Powa", "BrotherPowa"), ("Card up my...", "CardUpMy"), ("Forest Bump 2", "ForestGuy2")]
    $ choice1 = renpy.random.choice(movie_choices)
    $ movie_choices.remove(choice1)
    $ choice2 = renpy.random.choice(movie_choices)
    $ movie_choices.remove(choice2)
    $ choice3 = renpy.random.choice(movie_choices)
    cashier "Yes? Which movie would you like to see?"
    jump .movie_choices
    
label .movie_choices:
    menu:
        "Two tickets for [choice1[0]]":
            $ target = choice1[1]
        "Two tickets for [choice2[0]]":
            $ target = choice2[1]
        "Two tickets for [choice3[0]]":
            $ target = choice3[1]
        "These choices suck.":
            $ cat_mood -= 1
            show cat frown
            c "Nick!"
            cashier "Well, if you don't like them, just leave."
            menu:
                "Okay, okay.":
                    jump .movie_choices
                "Leave.":
                    n "Let's ditch this place, Catherine."
                    show cat question
                    c "Seriously? Well, all right..."
                    return
    jump .payment
    
label .payment:
    $ pay_both_tried = False
    cashier "That was one student, one adult, right?"
    n "Yes."
    $ price_student = prices['movies_student']
    $ price_movies = prices['movies']
    $ price_both = price_student+price_movies
    cashier "That'll be [price_student] and [price_movies] bits, please."
    call check_wallet 
    jump .payment_menu
    
    
label .payment_menu:
    menu:
        "Pay for both." if not pay_both_tried:
            n "I'll pay for both."
            show cat smile
            c "Nick..."
            "She starts to say something, but holds her tongue."
            cashier "[price_both] bits."
            call pay(price_both) 
            if not pay_successful:
                n "Oh. Not enough bits."
                $ pay_both_tried = True
                jump .payment_menu
            $ cat_mood += 2
        "Pay for yourself.":
            "Sorry, Catherine. I only have cash to pay for myself."
            "I don't think she really minds, though."
            call pay(prices['movies']) 
            if not pay_successful:
                n "Well, this is an embarrassment."
                call .catpays 
        "Ask Catherine to pay for you.":
            call .catpays 
    hide cat
    hide cat_torso
    with moveoutright
    scene movie_theatre
    scene movie_theatre dark with Dissolve(8.00)
    "We go inside the theater, picking our seats, and I slouch back as the movie starts playing."
    $ cat_opinion = 0
    call expression target 
    jump .opinion
    
label .catpays:
    n "Uh, Catherine? Could you pay for me, just this once?"
    # If this happened last time as well, she tries to refuse.
    show cat frown
    c "You invite me on a date and then ask me to pay for you?"
    show cat eyes_closed
    c "Whatever, let's just go in."
    hide cat
    hide cat_torso
    with moveoutright
    "She pays for both our tickets with her wristband."
    $ cat_mood -= 2
    return
    
label .opinion:
    n "So, how did you like it?"
    c "I can't really decide... Did you like it?"
    menu:
        "It was great!":
            if cat_opinion > 0:
                c "Yeah, it was good!"
                # Increase cat_mood
                $ cat_mood += 2
            elif cat_opinion < 0:
                c "Really, you think so?"
                # Decrease cat_mood
                $ cat_mood -= 1
            else:
                c "I guess it was okay..."
        "It wasn't bad.":
            if cat_opinion > 0:
                c "I thought it was pretty good, actually."
            elif cat_opinion == 0:
                c "It wasn't the worst movie I've ever seen."
                # Increase cat_mood
                $ cat_mood += 1
            else:
                c "Could have been a lot better."
        "It was pretty horrible.":
            if cat_opinion < 0:
                c "To be honest, I feel exactly the same."
                # Increase cat_mood
                $ cat_mood += 1
            elif cat_opinion > 0:
                c "What? I thought it was great!"
                # Decrease cat_mood
                $ cat_mood -= 2
            else:
                c "We lost nothing by trying it out, right?"
                n "Except for money..."
                # Decrease cat_mood
                $ cat_mood -= 1
    jump date_end
    
label date_end:
    if cat_mood > 0:
        c "That was pretty fun. Let's do this again sometime."
        $ affection_modify('Catherine', +1)
    elif cat_mood < 0:
        c "I hope next time won't be this bad..."
        n "What was that?"
        c "Nothing!"
        $ affection_modify('Catherine', -1)
    else:
        c "That was okay, I guess. Call me sometime."
    scene black with dissolve
    #n "Okay, see you again!"
    return

label date_arrival:
    $ umbrella = False
    $ catlate = False
    $ nicklate = False
    $ walkingspeed = "walk"
    call .setuplocation 
    call .setupweather 
    call .setupnickcondition 
    $ i = renpy.random.random()
    if i <= 0.45:
        # Nick is hurrying to the scene
        $ walkingspeed = renpy.random.choice(["run", "make my way", "walk"])
        "I [walkingspeed] through the[rainswept]streets[weather_reaction]"
        
        $date_arrival = renpy.random.choice(["Arriving at", "Upon arriving at", "Upondate_arrival at", "As I arrive at", "As I reach", "Upon reaching", "Reaching"])
        
        $ see = renpy.random.choice(["see", "find", "discover"])
        
        $ j = renpy.random.random()
        
        call .setupcatdescription 
        
        if j < 0.5:
            "[date_arrival] the [location],[nickcondition] I [see] that Catherine is not here yet."
            $ k = renpy.random.random()
            if k < 0.25:
                "Did she already go inside?"
            elif k < 0.5:
                "Did she decide to call it off without telling me?"
            elif k < 0.75:
                "She couldn't have just ditched me, right?"
            else:
                "She must be coming shortly."
            call .wait 
        else:
            $ nicklate = True
            show cat frown at right, flip
            show cat_torso orange at right, flip behind cat
            with moveinright
            "[date_arrival] the [location],[nickcondition] I [see] that Catherine is already here[catdescription]."
    elif i <= 0.9:
        # Nick is well on time
        $ ontime = renpy.random.choice(["right on time", "on time", "well on time", "just in time"])
        "I arrive at the [location] [ontime]."
        "It seems that Catherine is not here yet."
        call .wait 
    else:
        # Nick and Cat arrive at the same time
        show cat smile
        show cat_torso orange behind cat
        with moveinright
        "Coincidentally, it seems both Cat and I arrive at the [location] at precisely the same time."
    jump .conversation_start
    
label .wait:
    "I wait for her under the pentice of the [location][weather_reaction]"
    $ waitingtime = renpyrandomnormal(5, 7)
    if waitingtime > 8:
        # long wait
        $ catlate = True
        $ waitingdescription = renpy.random.choice(["After a long wait", "After what seems like an eternity", "After waiting there for a long time"])
    else:
        $ waitingdescription = renpy.random.choice(["After a short while", "In a short while", "Not much later", "Pretty soon", "A bit later"])
    call .setupcatdescription 
    $ j = renpy.random.random()
    show cat tired
    show cat_torso orange behind cat
    with moveinright
    if j < 0.5:
        "[waitingdescription], Catherine appears from behind a corner[catdescription]."
    else:
        "[waitingdescription], Cat arrives, walking toward me at a brisk pace."
        if catdescription != "":
            "Here she is[catdescription]"
    return
    
label .setupcatdescription:
    $ catdescriptors = []
    if raining > 1:
        $ catdescriptors.append("carrying an umbrella")
    elif cloudiness == "sunny":
        $ i = renpy.random.random()
        if i < 0.5:
            $ catdescriptors.append("wearing sunglasses")
        if temperature == "hot":
            $ catdescriptors.append("carrying a sunshade")
    if cat_mood < 0:
        $ catdescriptors.append("looking a bit annoyed")
    if len(catdescriptors) > 0:
        $ catdescription = ", "+andlisting(catdescriptors)
    else:
        $ catdescription = ""
    return
    
label .setupnickcondition:
    if raining > 1:
        if not umbrella:
            $ nickcondition = " soaking wet,"
    else:
        if temperature != "cold" and walkingspeed == "run":
            $ nickcondition = renpy.random.choice([" catching my breath,", " out of breath,", " sweating heavily,"])
        else:
            $ nickcondition = ""
    return
    
label .setuplocation:
    if act == 'movies':
        $ location = "movie theater"
    elif act == 'parlor':
        $ location = "ice cream parlor"
    elif act == 'vrarcade':
        $ location = "VR arcade"
    elif act == 'restaurant':
        $ location = "restaurant"
    elif act == 'bowling':
        $ location = "bowling hall"
    elif act == 'bar':
        $ location = "bar"
    elif act == 'swimminghall':
        $ location = "swimming hall"
    elif act == 'gym':
        $ location = "gym"
    elif act == 'runningtrack':
        $ location = "running track"
    elif act == 'mall':
        $ location = "mall"
    elif act == 'library':
        $ location = "library"
    elif act == 'work':
        $ location = "place I'm working at"
    elif act == 'clean':
        $ location = "house I live in"
    elif act == 'cathouse':
        $ location = "apartment Catherine lives in"
    elif act == 'business':
        $ location = "business school"
    else:
        $ location = "place we were supposed to meet at"
    return
    
label .setupweather:
    $ raining = (renpy.random.random() - 0.5)*4
    $ temperature = renpy.random.choice(["cold", "cool", "warm", "hot"])
    $ cloudiness = renpy.random.choice(["sunny", "cloudy"])
    if raining > 0:
        $ cloudiness = "cloudy"
        if temperature == "hot":
            $ temperature = "warm"
        $ rainswept = " rainswept "
        if raining > 1:
            $ weather_reaction = ", getting soaked in the rain."
        else:
            $ weather_reaction = ", feeling refreshed in the "+temperature+" rain."
    else:
        $ rainswept = " "
        if temperature == "hot":
            $ weather_reaction = ", baking in the heat."
        elif temperature == "cold":
            $ weather_reaction = ", shivering in the surprisingly cold air."
        else:
            $ weather_reaction = ", enjoying the "+temperature+" "+period+" air."
    $ i = renpy.random.random()
    if i > 0.75:
        $ weather_reaction = "." # Just to provide some variety.
    return
    
label .conversation_start:
    # construct a set of appropriate labels, pick at random
    $ conv = "start"
    call run_dialogue_events 
    n "Well, let's go in."
    return
    
#labeldate_arrival:
    # Great, it started raining just in time for our date. Glad it's not an outdoors place.
    # "Why did I have to forget my umbrella!?"
    #"As I arrive at the [location], [out of breath / catching my breath / soaking wet / sweating heavily / ] I can see that [Cat-reference] is already here[, waiting for me impatiently / looking impatient / annoyed][, carrying an umbrella / dayshade]".
    #"I arrive well on time, standing [in front of the [location] / under the pentice of the [location]]"
            
# Catherine arrives first
label CatFirst:
    "As I arrive at the movie theatre, I can see that Cat is already here."
    n "Hi. Did you wait for long?"
    if affection['Catherine'] < -2:
        # Cat is angry
        if trust['Catherine'] < -2:
            c "Yes."
            n "Uh, sorry."
            "She sighs."
            c "It's always the same with you, isn't it?"
        elif trust['Catherine'] > 2:
            c "A while. But I knew you'd come."
            n "Oh?"
            c "You're a jerk, but at least you're dependable."
            "W-was that a compliment?"
        else:
            c "You really shouldn't leave a girl waiting like that."
            c "Where are your manners?"
            n "Hey, I tried to be on time."
            c "You don't have to tell me what you were busy with..."
    elif affection['Catherine'] > 2:
        if trust['Catherine'] < -2:
            c "Yes. But I was expecting to."
            n "Is that the sort of image you have of me?"
            c "You're my little ne'er-do-well. Do you think I don't know what you're like?"
        elif trust['Catherine'] > 2:
            c "No, I just got here."
            n "Good, good."
        else:
            c "Not too long yet, dear."
            n "Well, that's good to hear."
    else:
        if trust['Catherine'] < -2:
            c "Nick, why must you be so undependable sometimes..."
            n "I'm sorry, Cat. Busy again."
        elif trust['Catherine'] > 2:
            c "You're usually more careful than this, Nick."
            n "Yeah, sorry about that."
        else:
            c "It's not that important."
            n "Yeah, these things happen, right?"
            c "Just make sure they don't happen too often."
    return
    
# You arrive first


# Both arrive at the same time


# Coming together from the last activity