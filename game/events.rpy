# Events for the day planner

init:
    $ broken_up = False # Implement this later
    $ call_ignored = False
    
    
    $ event("generic_promise_event", "(act, day) in promises.keys()", event.only(), priority=10)
    
    # Simple events for the actions
    $ event("icecreamparlor", "act == 'parlor'", priority=200)
    $ event("restaurant", "act == 'restaurant'", priority=200)
    $ event("movietheatre", "act == 'movies'", priority=200)
    $ event("vrarcade", "act == 'arcade'", priority=200)
    $ event("bowling", "act == 'bowling'", priority=200)
    $ event("bar", "act == 'bar'", priority=200)
    $ event("swimminghall", "act == 'swimming'", priority=200)
    $ event("gym", "act == 'gym'", priority=200)
    $ event("runningtrack", "act == 'track'", priority=200)
    $ event("mall", "act == 'mall'", priority=200)
    $ event("library", "act == 'library'", priority=200)
    $ event("work", "act == 'work'", priority=200)
    $ event("clean", "act == 'clean'", priority=200)
    $ event("business", "act == 'business'", priority=200)
    
    $ event("icecreamparlorintro", "act == 'parlor'", event.once())
    $ event("restaurantintro", "act == 'restaurant'", event.once())
    $ event("movietheatreintro", "act == 'movies'", event.once())
    $ event("vrarcadeintro", "act == 'arcade'", event.once())
    $ event("bowlingintro", "act == 'bowling'", event.once())
    $ event("barintro", "act == 'bar'", event.once())
    $ event("swimminghallintro", "act == 'swimming'", event.once())
    $ event("gymintro", "act == 'gym'", event.once())
    $ event("runningtrackintro", "act == 'track'", event.once())
    $ event("mallintro", "act == 'mall'", event.once())
    $ event("libraryintro", "act == 'library'", event.once())
    $ event("workintro", "act == 'work'", event.once())
    $ event("cleanintro", "act == 'clean'", event.once())
    $ event("businessintro", "act == 'business'", event.once())
    
    $ event("Catherine_afternoon_call_ignored2", "call_ignored and 'Catherine' not in forgotten_promises and unkept_promises_personal_counter['Catherine'] >=3 1 and period == 'afternoon'", priority=5)
    $ event("Catherine_afternoon_call_ignored", "call_ignored and 'Catherine' not in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 1 and period == 'afternoon'", priority=5)
    $ event("Catherine_morning_call3", "'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] > 2 and period == 'morning'", priority=5)
    $ event("Catherine_evening_call3", "call_ignored and 'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] > 2 and period == 'evening'", priority=210)
    $ event("Catherine_afternoon_call2", "'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 2 and period == 'afternoon'", priority=5)
    $ event("Catherine_morning_call1", "'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 1 and period == 'morning'", priority=5)
    $ event("Catherine_afternoon_call1", "call_ignored and 'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 1 and period == 'afternoon'", priority=5)
    $ event("Catherine_evening_call1", "call_ignored and 'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 1 and period == 'evening'", priority=5)
    
init python:
       class NonUniformRandom(object):
            def __init__(self, list_of_values_and_probabilities):
                """
                expects a list of [ (value, probability), (value, probability),...]
                """
                self.the_list = list_of_values_and_probabilities
                self.the_sum = sum([ v[1] for v in list_of_values_and_probabilities])

            def pick(self):
                """
                return a random value taking into account the probabilities
                """
                import random
                r = random.uniform(0, self.the_sum)
                s = 0.0
                for k, w in self.the_list:
                    s += w
                    if r < s: return k
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
            $ call_ignored = True
            "I wonder how long we can keep this up?"
                
label Catherine_morning_call3:
    "I gulp as I feel the vibrations of my wristband."
    "Catherine must be furious. I really really really don't want to talk with her."
    menu:
        "Answer":
            $ call_ignored = False
            "There's a moment of silence as I pick up. I just can't get the words out of my throat."
            c "Hello? Nicholas? I know you're there."
            n "H-hi, Cat..."
            $ place = "movies" # Supplement later
            c "So, didn't see you at the [place] yesterday."
            n "I-I guess I..."
            c "I don't really care what you're excuse is this time."
            c "I just can't trust you anymore, Nick."
            c "This is as hard on me as it is on you, but... Goodbye, Nick."
            "She hangs up, one last fatal blow to my guts."
            n "C-Catherine..."
            $ broken_up = True
        "Ignore":
            $ call_ignored = True
            "I ignore her call, feeling kind of embarrassed."
    return
    
label Catherine_evening_call3:
    "Catherine is calling again."
    "Should I just answer it and get it over with?"
    "I can already guess what she is going to say."
    "I really blew it this time."
    menu:
        "Answer":
            $ call_ignored = False
            jump Catherine_calls_ignored
        "Ignore":
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
            $ call_ignored = True
            "I ignore the call, hoping that she will do likewise."
    return
    
label answer_Catherine_afternoon_call2:
    n "Nicholas."
    c "Oh, I know very well who I'm calling. An inconsiderate jackass!"
    n "What's the problem?"
    "I know full well what the problem is, but..."
    c "You broke your promise the second time in a row! I'm just so... Argh!"
    menu:
        "Promise to meet her again":
            n "Look, I'm sorry I messed up again. Let's go to the movies tomorrow, what do you say?"
            c "... I guess that would be nice. But if you ditch me again, it's over!"
            "The threat makes the hair of my neck stand up a bit."
            python:
                if ('parlor', day+1) in promises.keys():
                    promises[('movies', day+1)][("Catherine", "meet")] = False
                else:
                    promises[('movies', day+1)] = {("Catherine", "meet"): False}
        "Threaten to break up with her":
            # Should test for affection here
            n "Look, this is the way I am. Stop trying to change me, or I'll break up with you!"
            c "You know, maybe that would be for the best."
            n "Eh, what!?"
            c "No need to call back, Nick. Goodbye."
            $ broken_up = True
        "Apologize":
            n "I'm really sorry, Cat. It won't happen again."
            c "It better not. Or it's over."
    "I'm left listening to the beeping of the ended call."
    
    return
                
label Catherine_morning_call1:
    "I wake up to the vibrations of my wristband."
    "It's Catherine."
    menu:
        "Answer":
            $ call_ignored = False
            jump answer_Catherine_morning_call
        "Ignore":
            $ call_ignored = True
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
            $ call_ignored = True
            "I click the ignore button and hope she doesn't call again."
    return
    
label answer_Catherine_morning_call:
    n "Hi there."
    c "Nick, what the hell? Weren't we supposed to meet yesterday?"
    menu:
        "Claim you forgot":
            n "Oh, we were? I guess I forgot."
        "Claim you were busy":
            n "Sorry, Catherine. Something came up."
        "Say you were tired":
            n "I was just too tired to come."
    c "Just as long as you weren't playing that freaking game again!"
    n "Look, I'll meet you at the parlor tomorrow, okay?"
    c "You'd better come this time!"
    python:
        if ('parlor', day+1) in promises.keys():
            promises[('parlor', day+1)][("Catherine", "meet")] = False
        else:
            promises[('parlor', day+1)] = {("Catherine", "meet"): False}
    "With that, she hangs up."
    return
    
label answer_Catherine_ignored_call:
    n "H-hi."
    c "What's going on? Why didn't you answer me before?"
    menu:
        "Claim you didn't notice her call":
            n "Sorry, I hadn't noticed it until now."
        "Claim you forgot":
            n "Sorry, I was going to, but then I did something else and forgot entirely."
        "Claim you were busy":
            n "Sorry, Catherine. I've been too busy the whole day."
    c "Too busy playing DFO, I venture."
    n "C'mon, that's not fair."
    c "First you break your promise, then you don't even return my calls."
    n "Oh, that? Let's meet tomorrow, at the parlor. Sound good?"
    c "This time, you'd better actually be there!"
    python:
        if ('parlor', day+1) in promises.keys():
            promises[('parlor', day+1)][("Catherine", "meet")] = False
        else:
            promises[('parlor', day+1)] = {("Catherine", "meet"): False}
    "She hangs up."
    return
                
label business:
    "I wander around the hallways for a bit. Why did I even come here in the first place?"
    
    return
               
label work:
    "I clean up at some organization."
    
    $ i = renpy.random.random()
    
    if i < 0.1:
        "I clean up at a big company headquarters. There's an entire team to support me."
    elif i < 0.2:
        "A boring day of cleaning up at some organization I don't care about."
    elif i < 0.3:
        "One of the vacuum cleaning bots goes out of service. Luckily I manage to repair it."
    elif i < 0.4:
        "My boss is a bit tense today. He shouts at me, and I can't help but be reminded of Catherine."
    elif i < 0.5:
        "I get to clean up at one of the server farms for DFO. This is actually really cool, especially with all the access I've got!"
    elif i < 0.6:
        "The building this time is quite small, so I get to clean it all by myself. I don't mind the silence."
    elif i < 0.7:
        "I get lost in my work, and time passes at a surprising pace. I guess it's a matter of mindset."
    elif i < 0.8:
        "I feel a bit tired at work, but my co-workers don't take notice."
    elif i < 0.9:
        "I'm working with that talkative old guy again. His stories are actually pretty interesting."
    else:
        "I'm cleaning up at a school. There's gum under every single chair, I swear!"
    
    return
    
label clean:
    "I clean up the litter that's accumulated on the floor of my apartment."
    
    return
    
label icecreamparlor:
    "I eat some ice cream."
    if broken_up:
        "Eating here reminds me of Catherine. The sweetness of the ice cream mixes with the bitterness of my emotions."
    else:
        "Delicious as always."
    return
    
label restaurant:
    # Restaurant, choose something to eat.
    
    "I pick something cheap from the menu."
    "At least I don't have to stumble making food by myself."
    
    return
    
label movietheatre:
    # Movie theatre, choose a movie to go to
    
    $ genre = NonUniformRandom( [("action", 2), ("romantic comedy", 1), ("horror", 1)] ).pick()
    
    "I watch a random [genre] flick, all alone."
    
    return
    
label vrarcade:
    # Arcade, choose a game to play
    
    $ game1 = NonUniformRandom([("Ghosts & Goblins", 1), ("BlazBlue",1), ("Metal Slug 2",1)]).pick()
    $ game2 = NonUniformRandom([("Mortal Kombat", 1), ("Street Fighter II", 1), ("Space Invaders", 1)]).pick()
    
    "I boot up some of the old retro arcade games, playing [game1] and [game2]."
    "The virtual reality stuff is cool too, but I have far better equipment at home."
    
    return
   
label bowling:
    # Bowling, pay for it
    
    "I do some bowling by myself."
    
    return
    
label bar:
    # Bar, choose a drink
    
    "I buy a drink and enjoy the beat."
    
    if broken_up:
        "Now that I've broken up with Catherine, I guess I could try to find a new partner."
        "Somehow I don't really feel interested, though."
    
    return
    
label swimminghall:
    # Leisure swimming vs. Exercise
    
    "I go for a bit of a swim, relaxing in the sauna afterwards."
    
    return
    
label gym:
    # Choose an exercise
    
    $ i = renpy.random.random()
    
    if i <= 0.33:
        "I spar with the robot."
        if fitness > 65:
            "Due to my experience in Dragonfire Online, I do quite well."
        else:
            "Despite all the combat practice in DFO, reality is a different beast altogether."
    elif i <= 0.66:
        "I try lifting some weights."
        if fitness > 75:
            "These are starting to get quite light."
        else:
            "I can't lift that much. DFO builds up my endurance, not my strength."
    else:
        "I row and row, wishing that this gym had a VR-set for showing hiking footage."
        if fitness >= 50:
            "Due to the endurance I've gotten from playing DFO, this is nothing!"
        else:
            "Phew, seems I've gotten out of shape!"
        
    $ fitness += 5
    
    return
    
label runningtrack:
    # Running
    
    "I run the lap a few times."
    
    return
    
label mall:
    # Buy random items
    
    $ i = renpy.random.random()
    $ something = NonUniformRandom( [("fast food", 4), ("new GPUs", 1), ("calculators", 2), ("Dr. Pepper", 4)] ).pick()
    
    if i < 0.5:
        "I flit around the mall, buying some [something]."
    elif i < 0.65:
        "I wander all around the shopping center, but find nothing of interest."
    elif i < 0.75:
        "There's some sort of event in the center of the mall. They're advertising [something]."
    elif i < 0.85:
        "I find some good sales on [something] at the mall."
    else:
        "The mall seems unusually empty. Then again, there's nothing much going on."
    
    return
    
label library:
    # Choose a subject to read about
    
    $ i = renpy.random.random()
    
    if i < 0.1:
        "I read some classics. Tough, but rewarding."
    elif i < 0.2:
        "I find an interesting book on game design. It holds me captivated for hours."
    elif i < 0.3:
        "The newest Edge has an article on gear I've already bought. I read it anyway."
    elif i < 0.4:
        "Wired has an article on the dangers of hacked IOT devices."
    elif i < 0.5:
        "On a whim, I search for the story about the man who died while playing VR with a modded suit. Seems he had some prior coronary problems."
    elif i < 0.6:
        "I find an old article about the AIDA AI director system that was being developed for DFO."
    elif i < 0.7:
        "A research journal has an article on a drug which is shown to improve VR proprioception by modifying neurotransmitters in the temporal lobe."
    elif i < 0.8:
        "I play around with the 3D printer, creating a model of Samus Aran."
    elif i < 0.9:
        "I talk with some of the hackers at the library."
    else:
        "Well, since I'm at the library, I might as well study something."
    
    return
    
# Promises
        
label generic_promise_event:
    python:
        kept_promises = set()
        for promise in promises[(act, day)].keys():
            if promise[1] == "meet":
                promises[(act,day)][promise] = True
                kept_promises.add(promise[0])
                unkept_promises_personal_counter[promise[0]] = 0 # Reset the unkept promises counter for the given person
        if len(kept_promises) == 1:
            kept_people = kept_promises.pop()
            promise_pluralized = "promise"
        else:
            list_kept = list(kept_promises)
            kept_people = ", ".join(list_kept[0:len(list_kept)-1]) + " and " + list_kept[-1]
            promise_pluralized = "promises"
    if act == "parlor" and day == 1:
        $ events_executed["icecreamparlorintro"] = True
        jump parlorStart
    else:
        "I keep my [promise_pluralized] to [kept_people]."

    return
    
# Intros    
    
    
label icecreamparlorintro:
    "Queens Gelateria is a mixed Italian-American -style ice cream parlor close to the center."
    
    return
    
label restaurantintro:
    # Restaurant, choose something to eat.
    "The Wind Horse Tavern is located near the stalls of the local horse racing track."
    "I like it due to its pseudo-medieval atmosphere. Kind of reminds me of Dragonfire Online."
    "Taste is the one sense we still haven't cracked in virtual reality."
    "I guess no-one's really interested at the moment. Most people don't even have haptics."
    "Anyway."
    
    return
    
label movietheatreintro:
    # Movie theatre, choose a movie to go to
    "Despite virtual reality providing a generally more immersive experience, movie theaters still exist."
    "Basically everything is in 3D on huge IMAX screens."
    "But it still doesn't beat VR."
    "At least it's something you can do together with your friends."
    "Going alone like this doesn't make much sense, but what the heck."
    return
    
label vrarcadeintro:
    # Arcade, choose a game to play
    "TechnoLazers is an arcade in the upper part of the city. It's not terribly popular anymore."
    "A couple years back, arcades made a huge comeback by providing affordable VR experiences to the general populace."
    "But now that you can get relatively high-quality virtual reality in the consumer price range, these renewed VR arcades are falling in popularity."
    "It's a shame. The place has a cool techno aesthetic."
    "There's also an arena for laser tag and robot wars."
    
    return
   
label bowlingintro:
    # Bowling, pay for it
    "The bowling place looks about as you'd expect, dark lighting and music and all."
    return
    
label barintro:
    # Bar, choose a drink
    "It's really more of a techno club than a bar, hidden away in the side streets. I've taken Cat here before, but she's not into the place."
    
    return
    
label swimminghallintro:
    # Leisure swimming vs. Exercise
    "This is a secluded, relatively unpopular swimming hall mostly frequented by the elderly."
    "No-one comes here because of the labyrinthine architecture."
    "I swear, I get lost in the hallways every time I decide to visit."
    "Personally, I just come here for the steam sauna."
    return
    
label gymintro:
    # Choose an exercise
    "This is the gym Catherine frequents. I think she has classes daily here."
    "It's mostly for CrossFit people, so I don't come here that often."
    "Frankly, I find these muscular CrossFit guys a bit intimidating. Even though I'm in good shape myself."
    "Aside from the usual barbells and rowing machines, they have a colossal fighting robot to spar with."
    "I think that's for the Muay Thai practicioners that also come here."
    return
    
label runningtrackintro:
    # Running
    "The local running track. Not much to see here, though I know Cat comes here every now and then as a part of her workout schedule."
    
    return
    
label mallintro:
    # Buy random items
    "The biggest shopping mall in town, right in the center. I've never really liked the crowds."
    
    return
    
label libraryintro:
    # Choose a subject to read about
    
    "You'd think libraries would be a thing of the past in an era where every book ever made is easily available on the internet."
    "But you would be wrong. Libraries are still going strong."
    "Aside from providing access to rare antique titles, most libraries have become sorts of community makerspaces, with high-quality
    3D-printers and loads of other tools."
    "If you need a customized item or part on the spot, the library is your place to go."
    
    return
    
label workintro:
    "I work at a rental cleaning service."
    "Ironically, cleaning is one of the jobs that the robots haven't taken yet."
    "I mean, of course everybody including us is using vacuuming bots and the like."
    "But picking up the litter, cleaning the tables, all these things are still usually done by humans."
    "Well, that's lucky for me. It's the most boring job in the world, but it's not too difficult and the pay is enough to live with."
    
    return
    
label cleanintro:
    "Considering my line of work, it's ironic that my room is so cluttered."
    "I guess a shoemaker's children really do go barefoot."
    "Normally I'm too exhausted from work to do any cleaning at my own place."
    "But I suppose I should keep it in some shape at least. Wouldn't want to get dust in all those components!"

    
    return
    
label businessintro:
    "This is the business school Catherine goes to. Ridiculously high class."
    "Well, someone with her natural abilities deserves only the best, I guess."
    "It's kinda depressing. I could never make it here."
    "Despite the pressure Cat and my parents put on me."
    
    return