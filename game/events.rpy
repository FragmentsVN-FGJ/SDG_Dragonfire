# Events for the day planner

init:
    $ broken_up = False # Implement this later
    $ call_ignored = False
    
    $ event("Catherine_movie_scene", "act == 'movies'", event.only(), event.once(), priority=5)
    $ event("Catherine_broken_up_mall", "act == 'mall'", event.only(), event.once(), priority=5)
    $ event("DFOServers", "act == 'work'", event.once(), event.only(), priority=5)
    
    $ event("Catherine_study_together", "act == 'cathouse'", event.only(), priority=200)
    $ event("Catherine_gym_together", "act == 'gym'", event.only(), event.once(), priority=50)
    $ event("sauna_accident", "act == 'swimming'", event.only(), event.depends("swimminghallintro"), event.once(), priority=50)
    $ event("Catherine_running_together", "broken_up == False and act == 'track'", event.once(), event.only(), priority=50)
    
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
    
    $ event("Catherine_afternoon_call_ignored2", "call_ignored and 'Catherine' not in forgotten_promises and unkept_promises_personal_counter['Catherine'] >= 3 and period == 'afternoon'", priority=5)
    $ event("Catherine_afternoon_call_ignored", "call_ignored and 'Catherine' not in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 1 and period == 'afternoon'", priority=5)
    $ event("Catherine_morning_call3", "'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] > 2 and period == 'morning'", priority=5)
    $ event("Catherine_evening_call3", "call_ignored and 'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] > 2 and period == 'evening'", priority=210)
    $ event("Catherine_afternoon_call2", "'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 2 and period == 'afternoon'", priority=5)
    $ event("Catherine_morning_call1", "'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 1 and period == 'morning'", priority=5)
    $ event("Catherine_afternoon_call1", "call_ignored and 'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 1 and period == 'afternoon'", priority=5)
    $ event("Catherine_evening_call1", "call_ignored and 'Catherine' in forgotten_promises and unkept_promises_personal_counter['Catherine'] == 1 and period == 'evening'", priority=5)
    
define o = Character("Old guy")
define jackquotes = Character("'Jack'")
define jack = Character("Jack")
define m = DynamicCharacter("serverguy")
    
init python:
       import math
       handkerchief = False
       last_seen = ""
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
                retur
                
       def renpyrandomnormal(mean, sd):
            # Produce a renpy random from the given normal distribution using Box-Muller transform
            i = renpy.random.random()
            j = renpy.random.random()
            Z_0 = math.sqrt(-2*math.log(i))*math.cos(2*math.pi*j); # Random variable from the standard normal distribution
            return sd*Z_0 + mean
            
       hub_seen_labels = []
                
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
    
    
# Special Scenes, Catherine

label sauna_accident:
    "I yawn while navigating the labyrinthine hallways of the swimming hall."
    "I didn't sleep that well, and I'm feeling really tired today."
    "I'm hoping the cold water will refresh me. Wouldn't want to feel tired for the whole day."
    "In a slight daze, I finally arrive at the lockers. Some nagging voice in the back of my voice is saying that something is different today, but I'm too tired to take note of it."
    "I undress and go to the showers."
    "I woke up so early that no-one else is around yet."
    "While standing under the warm pouring water, I'm struck by something strange."
    "The architecture feels really different today. Was that door always on that side?"
    "Aaaah, I should just let go of the tension and forget it."
    "I go sit in the sauna, relaxing even further in the Eucalyptus-tinged vapours."
    "This is the life. I'm so relaxed, I'm practically dozing... off..."
    "Someone comes in and sits beside me, a bit further away."
    "Then, the person seems to recognize me, and I'm jolted awake."
    c "Nick...?"
    "W-wait, what's Catherine doing on the men's side?"
    "Suddenly, I realize why something felt off before."
    "This is not the men's side at all, is it!?"
    menu:
        "Engage!":
            n "I, uh, I am... I..."
            "Damn, I'm so sleepy I can barely put a coherent sentence together!"
            "Catherine seems at a loss for words as well."
            call .Catherine_conversation
        "Take cover!":
            "I stumble to cover up my private parts!"
            "Catherine's looking at me, eyes agape."
            call .Catherine_conversation
        "Run away!":
            "I run away as fast as I can!"
            c "Nick, what the hell are you doing!?"
            "I almost slip on the wet floor, but manage to get away, with no time to close the door behind me."
            "Damn! I can hear Catherine following right behind me. Thankfully, she's walking rather than sprinting."
            "Quick, I need to hide somewhere!"
            $ locker = False
            menu:
                "Inside the locker!":
                    "The locker looks just barely big enough."
                    "I cram myself in, and close the door just in time!"
                    call .Catherine_investigation("through the slits in the door", "to check the lockers")
                    $ locker = True
                "Under the benches!":
                    "I crawl under the bench just in time!"
                    call .Catherine_investigation("up from here,", "and look under the benches")
                "Behind the column!":
                    "It's not much of a hiding place, but I need to be quick!"
                    "I hide behind the column just in time!"
                    call .Catherine_investigation(", in the corner of my vision,", "near the column")
            "After Catherine has left, the absurdity of my sleep-addled reaction hits me."
            if locker:
                "And as I try to leave the locker, I realize it's locked!"
                "This is turning out to be a great day..."
                "Eventually, a cleaner comes in."
                "I try to discreetly catch her attention by tapping on the door."
                "She looks suspicious, and slowly approaches."
                "As she opens the door, I bolt out as quickly as I can."
                "She is left behind, utterly aghast."
                "Well, you don't see naked men running from girl's lockers every day!"
            "I dress up quickly, red with shame, and leave without even trying to go for a swim."
    return

label .Catherine_investigation(visibility, place):
    "Catherine walks in, and [visibility] I can see her investigating the perimeter."
    c "Nick, I know you're in here somewhere!"
    "I'm holding my breath, praying that she won't come [place]."
    "Finally, she appears to lose interest."
    c "Whatever. We'll talk when you're ready to act like an adult."
    "I hold back a sigh of relief until she is no longer visible."
    return
            
label .Catherine_conversation:
    # Funny music here
    menu:
        "This is some anime cliche, isn't it!?":
            n "This is like the oldest cliche ever! Next you're gonna beat me up for seeing you naked!"
        "It was an accident!":
            n "Cat, you have to believe me, it was an accident! I didn't come here to peep on you!"
            n "Please don't hurt me!"
        "I'm sorry!":
            n "I'm so sorry, I'm so sorry, please don't beat me up!"
    "Cat frowns and blinks, as if confused, but then..."
    "... she starts giggling!"
    c "Oh yeah, I'll send you blasting off again!"
    c "Nicky, you really watch too much anime, don't you?"
    c "Why would I beat you? I'm not that scary, am I?"
    "She's teasing me now."
    c "And it's not like you haven't seen me naked before..."
    "I storm out, all red, hoping that I don't meet anyone on the way out."
    return
    
    
label Catherine_gym_broken_up:
    "As I arrive at the gym, I see that Catherine is already here."
    "I don't really want to face her like this, but I did come here to exercise."
    menu:
        "Stay and exercise":
            "I go as far away from Catherine as possible, deciding to lift some weights."
        "Leave":
            "I leave Catherine to her own gym devices."
            return
    "Eventually, Catherine comes over as well."
    "She doesn't even look at me, and starts lifting some weights."
    "Does she think she rules the place or something?"
    "I get some bigger weights and tighten my pace."
    "Seeing that, she does likewise."
    "Pretty soon, we're in a heated competition, trying to see who can lift the most!"
    "Other guys at the gym come around us, cheering for Catherine."
    "Yeesh, is she some sort of celebrity around these parts?"
    if fitness < 45:
        "I'm in pretty poor shape."
        "I grit my teeth as I see her still going fast while my own arms scream with pain!"
        "Damnit! I'm never giving uuuuuuup!"
        "THUMP!"
        "Suddenly, all the strength disappears from my arms and legs, and I collapse to the ground."
        "Everyone is laughing at my misfortune. Darn, how can she be so good?"
    elif fitness < 75:
        "I'm in good shape myself, but she's just amazing."
        "Her T-shirt has turned bright green, and she's huffing and puffing right next to me."
        "But unlike me, she doesn't seem to be slowing down at all!"
        "The crowd breaks into a cheer as I collapse to the ground, giving up."
    elif fitness < 90:
        "She's in great shape, but I'm no pushover myself."
        "I manage to keep up pace with her, and our combat ends in a draw."
        "The crowd seems a bit disappointed, and disperses."
    else:
        "She's in great shape, but she's still no match for me!"
        "I can see her trying as hard as she can, but eventually she must acquiesce."
        "She sits on the ground panting heavily. The crowd boos, though I'm not sure if it's directed at me or at her."
    # Talk with Catherine here. If there's nothing to discuss...
    "I don't talk to her after that."
    "Well, at least I really gave it my all this time."
    "Although my arms sure are going to ache tomorrow..."
    $ fitness += 10
    
label Catherine_gym_together:
    # Fight with the robot
    $ i = renpy.random.random()
    
    "Upon arrival, I see that Catherine is already here, in full exercise mode."
    menu:
        "Talk to her":
            "I walk up to her to say hi."
            n "Already hard at work, I see."
        "No need to disturb her":
            "She's so deeply focused, I'd better not disturb her."
            "I go a bit further off, doing some acrobatic exercises."
            "She eventually comes over."
            # Hi scene
            c "Hi!"
            n "Hello there! I guess you're almost done?"
    c "Yeah, I've been developing a lot of muscle strength. Wanna see?"
    "She grins and holds her fist right below my nose."
    menu:
        "Sure":
            n "Show me what you've got."
        "I'll pass":
            n "No, no, I believe you."
        "Please don't hit me!":
            n "Please don't hurt me, it wasn't me!"
            "Catherine looks surprised, and then blushes and whispers."
            c "Nick, you idiot! Don't embarrass me in front of the whole box!"
            "She glances around, trying to confirm that no-one heard my outburst."
            c "Anyway."
    c "Just come over here, I'll show you."
    "She walks over to the sparring robot, still sporting a wide grin."
    c "I've been learning some martial arts on the side!"
    "She takes a fighting stick and approaches the bot."
    "However, just then, an older gray-haired guy comes over. Despite his age, he manages to boast a six-pack."
    o "Hi, Catherine. Daily workout almost done?"
    "He sizes me up."
    o "Is this your boyfriend?"
    c "Hi, Jack. Jack this is Nicholas, my boyfriend. Nick, this is Jack, my trainer and the leader of this gym."
    n "Does he have an Onyx?"
    "Cat casts a sharp glance at me."
    jackquotes "Well, let's see what he's made of. You two, spar with the robot together."
    c "There's a team mode?"
    jack "Sure there is. Let's crank up the difficulty a bit..."
    "He plays with the settings of the robot, and it sprouts two extra arms and legs!"
    jack "Ready... set... go!"
    "Jack recedes into the background as the robot springs to life!"
    play music "bgm/Battle1.wav"
    "Its red visor turns from target to target, finally locking onto..."
    $ cat_in_air = False
    $ nick_in_air = False
    $ robot_stunned = False
    $ struggle_counter = 0
    $ victorious = False
    if i < 0.5:
        "Catherine!"
        "The robot lunges its elongated arms forward, attempting to grapple her!"
        $ robot_focusing = "Catherine"
        jump .react_phase
    else:
        "Me!"
        "I barely have the time to see the robot's long arms coming straight towards me!"
        $ robot_focusing = "Nick"
        jump .react_phase
    return
                
# States: Nick in air, Cat not; Cat in air, Nick not; Both in air; Neither in air; Robot focusing on Nick, robot focusing on Catherine, robot stunned,
# robot attacking
# Act phase and react phase separate, choices controlled by state flags?
# Winning conditions: Robot focusing on Catherine, robot stunned, Nick hits the button; or with Nick's and Catherine's roles reversed.

label .act_phase:
    menu:
        #Implement
        "Struggle to break free!" if nick_in_air and struggle_counter == 0:
            call .struggle
        "Struggle some more!" if nick_in_air and struggle_counter > 0:
            call .struggle
        "Attack!" if not nick_in_air:
            call .attack
        "Tell Catherine to press the red button!" if robot_focusing == "Nick":
            call .Catherine_press
        "Press the red button" if not nick_in_air and robot_focusing == "Catherine":
            call .press
        "Ask Catherine to distract it!" if robot_focusing == "Nick":
            call .Catherine_distract
        "Try to catch its attention!" if robot_focusing == "Catherine":
            call .distract
    if victorious:
        jump .victory
    if cat_in_air:
        call .Catherine_struggle
    call .robot_act
    jump .act_phase # Loop act phase until victory

    
label .struggle:
    $ struggle_counter += 1
    "I exert all my strength to break free of its grip!"
    $ j = renpy.random.random()
    if j < 0.5:
        "But it's too strong!"
    else:
        "Suddenly, it loosens its grasp, and I fall gracefully to the ground!"
        $ nick_in_air = False
        "It shifts its visor towards me, preparing to attack."
        $ robot_focusing = "Nick"
        $ struggle_counter = 0
    return
    
label .Catherine_struggle:
    # Catherine attempts to break free
    "Catherine struggles heroically in the robot's grasp!"
    $ j = renpy.random.random
    if j < 0.66:
        "However, she can't break free of its iron-grasp!"
    else:
        "The robot is forced to release her, and she lands on the ground, graceful as a cat."
        $ cat_in_air = False
    return

    
label .attack:
    if robot_focusing == "Catherine":
        "I've got to protect Catherine!" # "No way I'm gonna let you hurt Cat!"
    else:
        "I need to keep distracting it!"
    if cat_in_air:
        "I strike at the arm holding Catherine, forcing the robot to release its grip."
        "She rolls in the air and lands beside me."
        c "Thanks!"
        $ cat_in_air = False
        "The robot appears to be stunned by my strike."
    else:
        "I strike at one of the robot's arms, causing it to halt for a few seconds."
    $ robot_stunned = True
    $ stun_counter = 1
    if robot_focusing == "Catherine":
        "Its red visor shifts ominously towards me."
        $ robot_focusing = "Nick"
    return
        
label .Catherine_press:
    n "Catherine, press the button, quick!"
    c "O-okay!" # Y-yes!
    if not robot_stunned:
        "Catherine approaches, but at the last moment, the robot notices her and evades the incursion!"
        if nick_in_air:
            "In the commotion, it accidentally releases me, and I land on the ground."
            $ nick_in_air = False
    else:
        # Victory
        "The robot does not have the time to react, and Cat manages to shut it down!"
        $ victorious = True
    return
    
label .press:
    "While the machine is concentrating on Catherine, I sneak up on it, attempting to press the power down button on its back."
    if not robot_stunned:
        "At the last moment, its head rotates 180 degrees to face me, and it lashes out at me!"
        $ robot_focusing = "Nick"
    else:
        # Victory
        "Without giving the robot time to react, I shut it down!"
        $ victorious = True
    return
    
label .Catherine_distract:
    n "Catherine! Try to draw its attention!"
    c "U-uh, hey you stupid robot, don't forget about me!"
    "Catherine strikes one of the robot's arms, and it turns its head towards her."
    $ robot_focusing = "Catherine"
    return
    
label .distract:
    "I get closer to the robot, hoping to capture its attention."
    n "Hey, you pile of screws! Look here!"
    "It's visor turns to face me, and I feel shudders going down my spine."
    $ robot_focusing = "Nick"
    return
        
label .react_phase:
    menu:
        #Implement
        "Jump out of the way!" if robot_focusing == "Nick":
            call .dodge("jump")
        "Strike!" if robot_focusing == "Nick":
            "I stomp on one of its arms right as it's about to grapple me!"
            "If robots feel pain, I'm sincerely sorry!"
            "The robot retracts its arms, giving me a few seconds to act!"
            $ robot_stunned = True
            $ stun_counter = 0
        "Roll!" if robot_focusing == "Nick":
            call .dodge("roll")
        "Jump to protect her!" if robot_focusing == "Catherine":
            "I jump in front of the robots arms!"
            c "Nick, get out of my way!"
            "Oh right, Cat already had experience in this, didn't she..."
            "And I forgot that the robot's got four arms!"
            "It's arms curl up around us, and it lifts us both into the air."
            c "Niiick, you idiooot!"
            $ cat_in_air = True
            $ nick_in_air = True
        "Let her handle it" if robot_focusing == "Catherine":
            "Cat deftly dodges the robot's arms, delivering a strong blow with her fighting stick!"
            "The robot is completely focused on fighting Catherine now."
            $ robot_stunned = True
            $ stun_counter = 0
        "Sneak up on the robot" if robot_focusing == "Catherine":
            "The red power switch glows on the robot's back. If only I could reach it..."
            "I sneak up towards the robot, but just as I'm about to press the button, it notices me and retreats!"
            "Now it's lunging its arms towards me!"
            $ robot_focusing = "Nick"
            jump .react_phase
    jump .act_phase


        
label .dodge(method):
    $ attempt = NonUniformRandom( [("attempt", 1), ("try", 1)] ).pick()
    $ i = renpy.random.random
    "I [attempt] to [method] out of the way!"
    if i < 0.5:
        "And barely manage to!"
        "The robot is momentarily confused as its claws grasp thin air!"
        $ robot_stunned = True
        $ stun_counter = 0
    else:
        "It's no use! The robot catches my leg and lifts me into the air!"
        $ nick_in_air = True
    return
    
label .robot_act:
if not robot_stunned:
    if robot_focusing == "Catherine":
        if not cat_in_air:
            "The robot lashes out its huge arms, aimed right at Catherine!"
            jump .react_phase
        else:
            "Secure in Cat's captivity, the robot turns its attention to me."
            $ robot_focusing = "Nick"
            jump .act_phase
    else:
        if not nick_in_air:
            "The robot lunges one of its many arms in my direction!"
            jump .react_phase
        else:
            "Having made sure that I'm not going anywhere, the robot shifts its focus to Catherine."
            $ robot_focusing = "Catherine"
            jump .act_phase
elif stun_counter < 1:
    "The bot seems to recover from its daze."
    $ robot_stunned = False
else:
    $ stun_counter -= 1
return
    
label .victory:
    play music "bgm/Hope(Ver1.00).ogg"
    jack "So you did manage to beat it."
    "He sounds genuinely impressed."
    "Hey, wait a minute, weren't you expecting us to win!?"
    n "Is this thing even legal!? What if you need to turn it off?"
    jack "Yeah, I guess these were outlawed a while back."
    n "Then why do you still have one!? I should tell the cops!"
    jack "It's good to see that your boyfriend's got some sass."
    "Seriously, what is it with this guy..."
    return
        
label Catherine_running_together:
    "I go to the running track to run a few laps."
    "As I'm running, Catherine arrives, and I slow down to meet her."
    # Catherine introductions
    c "Hi, how's it going, Nick?"
    "I have to catch my breath for a bit."
    n "Oh, you know, the usual. How are you?"
    c "Great! Especially now that I'm going to beat you at this race!"
    "She darts right ahead of me."
    "Yeesh, this is unfair, I'm already exhausted!"
    if fitness < 45:
        "Not only that, I'm not in as good shape as I used to be!"
        "I'm not giving uuuup!"
        "Except that I have no choice in the matter. My body fails me, and I trip face down into the red sand."
        "She easily beats my times. Well, at least she's happy."
    elif fitness < 75:
        "I can keep up with her with a while, but she's in even better condition than I am."
        "She beats my times with little difficulty."
        "Darnit! A guy losing to his own girlfriend in sports, this is a disgrace!"
        "Even for a nerd like me!"
    elif fitness < 90:
        "Despite my exhaustion, I manage to keep up with her."
        "She purses her lips and frowns, trying her most to run even faster."
        "She barely manages to beat me. I'd chalk that up to unfair advantage, but I'm not saying that to her face."
    else:
        "Even with the advantage, she can only barely keep up with me."
        "It's actually kind of sad to leave her behind like this."
        "But that's life I guess. Sorry Cat! Even you can't always win!"
        "Cat's still pouting once we've finished racing."
        c "Hmph. Don't get any big ideas. I was just tired from the gym today."
    if fitness < 90:
        "Cat approaches, smiling."
        c "Wow, you're sweating."
        n "Well, yeah. I was running as hard as I could back there."
        c "Want a handkerchief?"
        menu:
            "Thanks.":
                n "Thanks."
                c "No problem."
                $ handkerchief = True
            "No need.":
                n "Nah, you keep it."
                c "Okay then."
    "I really gave it my all today. My muscles are really aching."
    $ fitness += 8
    return
    
label Catherine_study_together:
    # For now, assuming this happens at Cat's house, though I'd like the player to
    # be able to choose between that, the library and the parlor.
    
    "I'm standing in front of the door to Catherine's apartment."
    "It's just an ordinary apartment in a small tower block right by the docks."
    "It still manages to be far more fancy than mine, though, with an entrance, two rooms and a kitchen."
    "I guess not spending all your money on VR gaming also has its advantages."
    "Don't get it wrong. I'm perfectly happy with my life choices! When you've got VR, you're apartment can be the size of a mansion!"
    "Virtually, that is."
    "We agreed to meet at 5pm. I don't want to wake her dog up, so I guess I'll just knock."
    "After a time period which feels far longer than a minute, I begin to get worried."
    "She's not answering. That's very unusual. Normally we'd already be down to business by now."
    jump .atthedoor
    
label .atthedoor:
    menu:
        "Knock again":
            # Still no answer
            "I try to knock again, but the only response is silence."
            jump .atthedoor
        "Ring the doorbell":
            # The dog doesn't wake up
            "I attempt to ring the doorbell."
            "Strange, even the dog isn't waking up."
            jump .atthedoor
        "Use the key":
            "I have a copy of the key to her apartment, of course. I'm her boyfriend, right?"
            "It's kind of bad-mannered to just waltz in like this, but I'm sure she won't mind if I explain it to her afterwards."
            "I turn the key in the lock and walk into her apartment."
            play music "bgm/wrong.wav"
            "There's definitely something going on here."
            "Her shoes are still in the cabinet, so she must be inside."
            "But she's nowhere to be seen. There's a quiet racket coming from the door to the right, which is connected to her bedroom."
            "It couldn't be... a robber? A serial killer?"
            "I swallow, hoping that my worst nightmares are not coming into fruition."
            menu:
                "Wait quietly":
                    "I look around the entrance, trying to find something to arm myself with."
                    "The cabinet has some of Catherine's old sports equipment. There's a golf club, two tennis rackets, and... yes, this will do."
                    "I take the baseball bat and ready it for attack."
                    "Eventually, I see someone come out the door, and I swing the bat over my head!"
                    stop music
                    c "Gyaaa! Nick, what the hell are you doing!?"
                    "It's Catherine. In her underwear, no less."
                    c "Just... stay there! And put that bat down!"
                    $ bat_noticed = 1
                    "She goes back to her bedroom and closes the door."
                    jump .gettingclothed
                "Say something":
                    n "Is... is someone in there?"
                    "For a moment, the sound goes quiet."
                    c "N-Nick? Uh, just stay there for a while!"
                    play music "bgm/Hope(Ver1.00).ogg"
                    "She closes the door to her bedroom, and I can hear her going all around the room, as if looking for something."
                    n "Is everything okay in there?"
                    c "Yeah, sure, just let me get dressed. Weren't we supposed to meet at six?"
                    n "No, it was at five."
                    c "Darn, sorry, I forgot."
                    n "Your dog's somewhere?"
                    c "At my parents. It needed some rest."
                    "She opens the door, dressed in clothes with completely unmatching colors. She must have not had time to look for anything
                    better."
                    "She looks into my eyes for a moment, a bit flustered."
                    c "Hi."
                    "Before I have time to respond, she's already disappeared into the kitchen."
                    jump .kitchen
                "Go closer to the door":
                    "I'd better arm myself first."
                    "I look around the entrance. The cabinet has some old sports equipment in it."
                    "I try the weight of the baseball bat, ready it, and approach the door."
                    "I can hear the strange noise right around the corner. Like someone stomping on the floor."
                    "Okay, here goes nothing!"
                    "Shouting a battlecry, I storm into the room!"
                    # silence
                    stop music
                    "And I see Catherine. Playing a dance game. Wearing a T-shirt and nothing else."
                    "There's an awkward silence as we both stand perfectly still, staring at each other with gaping eyes."
                    c "......"
                    c "Gyaaaa! What the hell, Nick!? Get out get out get out!"
                    "She pushes me back to the corridor and closes the door behind her."
                    $ bat_noticed = 2
                    jump .gettingclothed
                    
                    
label .gettingclothed:
    "I can hear her frantically search for clothing."
    c "Why didn't you knock? Eh, what am I gonna wear, no way... Weren't we supposed to meet at six?"
    n "Um... no, it was at five."
    play music "bgm/Hope(Ver1.00).ogg"
    "While she's getting dressed, I quietly leave the bat where I took it."
    if bat_noticed == 2:
        "I hope she didn't have time to register it."
    else:
        "I hope she won't question me about it."
    # interrupt with Nick's questions
    n "Where's that mutt of yours?"
    c "Oh, Snowy is at my parents. It's been a bit sick lately, I thought the vacation would do it some good."
    "For a moment, I just listen to the wooshing coming from her room."
    c "What were you doing with that baseball bat, anyway?"
    "Damn."
    n "Erm... Actually, I thought there was a robber in there."
    "She sounds almost amused."
    c "Whaat, seriously? In this day and age?"
    "Crime rates how gone down a bit in the recent years, what with the increased availability of automated surveillance systems."
    "But criminals have endless ingenuity for bypassing such things."
    "It's not as unlikely as she makes it sound."
    n "Well, you never know."
    "She opens the door again, dressed a bit more amicably. Still, the colors don't match at all."
    "She must be irritated, not getting to spend the whole day choosing."
    c "I didn't know you were that paranoid, Nick. What's gotten into you?"
    "Without giving me time to answer, she slides into the kitchen."
    jump .kitchen
                   
label .kitchen:
    c "Anyway, let's just get this started. Now, what should we drink?"
    "She starts going through the cupboards."
    "Oh dear, this is going to take the whole day, isn't it?"
    $ water_heater_on = False
    $ coffee_machine_on = False
    $ coke_bottle = False
    menu:
        "Tea, please.":
            c "Y-yeah. I guess that's okay."
            "She turns the water heater on."
            $ water_heater_on = True
            c "Sorry, it's kind of slow."
            c "Let's just go to the living room while it heats up."
        "I could use some coffee.":
            c "Oh, you're tired?"
            c "Let me guess, staying awake until 3am again, playing some game..."
            "She sighs and turns on the coffee machine."
            $ coffee_machine_on = True
            c "Let's just go to the living room while it heats up."
        "You got any coke?":
            c "S-sure. I'll bring the bottle to the living room."
            $ coke_bottle = True
    "I sit on the mat by the glass table, while she sits on the couch, looking down on me."
    "Literally that is. Hopefully not metaphorically."
    c "Now then, let us commence. The purpose of this meeting is to help you get into a good school by studying properly."
    n "Why are you making this sound so professional? We're a pair, right?"
    c "Mister Nicholas, if you would please focus."
    "I can see that she's enjoying this."
    "Cat likes to be in a position where she can tell others what to do."
    "Pretty stereotypical with MBA students, I suppose."
    "Although with her inability to actually make decisions, I'm not sure she'd be such a great boss."
    c "But first, we will have to determine what you should actually study in the first place."
    menu:
        "Game design":
            "I'm not sure if Cat will be on board with this idea, but..."
            n "I've been thinking of game design."
            "She presses her mouth into a thin line."
            c "I suppose that is a job. Of sorts."
            n "Shouldn't you do something you're passionate about?"
            c "As long as you can actually make a living that way."
        "Business":
            n "I'm interested in business."
            "She smiles, incredulous."
            c "Yeah, right. You're just saying that to get on my good side."
            n "No, I really am interested."
            "I'm not certain that's actually true, but I have to say something, right?"
        "I don't know":
            n "I dunno."
            c "Of course not. Not when it's something important."
    "She frowns in that cute way of hers again."
    c "Well, regardless of what you're going to apply for, there's some basic subjects that spring up in every entrance exam."
    c "Mathematics, physics and basic chemistry, for instance."
    c "I guess math is the most common, so we might as well start with that."
    c "Okay then, what's your weakest area, probability theory, calculus or geometry?"
    menu:
        "Probability theory.":
            $ math_subject = 0
        "Calculus.":
            $ math_subject = 1
        "Geometry.":
            $ math_subject = 2
    jump .math_question1
    
label .math_question1:
    $ math_genius = False
    "She closes one eye, beckoning me to answer."
    c "Let's start with a simple one."
    if math_subject == 0:
        jump .probability1
    elif math_subject == 1:
        jump .calculus1
    else:
        jump .geometry1
        
label .right_answer1:
    c "Yeah, I guessed that one would be too easy for you."
    return
    
label .wrong_answer1:
    "Cat blinks."
    c "Uh, no. You see..."
    return

label .right_answer2:
    c "Y-yeah, that's correct."
    "She looks a bit flustered."
    "What, you weren't expecting me to get it right?"
    return
    
label .wrong_answer2:
    c "This one's a bit more difficult, huh?"
    return

label .right_answer3:
    c "W-wait a minute, didn't you say this was your weakest area?"
    c "Are you just really good at math or something?"
    $ math_genius = True
    return
    
label .wrong_answer3:
    c "Yeah, um, I think it goes like this..."
    "You're not certain yourself?"
    return
    
label .math_question2:
    "Well then, how about this one?"
    if math_subject == 0:
        jump .probability2
    elif math_subject == 1:
        jump .calculus2
    else:
        jump .geometry2
    
label .math_question3:
    "Okay, here's a tough one."
    if math_subject == 0:
        jump .probability3
    elif math_subject == 1:
        jump .calculus3
    else:
        jump .geometry3
    
label .probability1:
    c "You roll two normal, six-sided dice. What is the probability that the sum of their values is 11?"
    menu:
        "2/36":
            call .right_answer1
            jump .math_question2
        "11/36":
            call .wrong_answer1
            call .probability1_explanation
        "2/11":
            call .wrong_answer1
            call .probability1_explanation
    jump .interrupt
        
label .probability1_explanation:
    c "Your denominator is the total amount of possible dice combinations. For example, both first die and second die are ones, or the second one is a two or a three and so on."
    c "You can draw all the possibilities in a table like this."
    "The table has the numbers 1-6 both as columns and as rows."
    c "So now each cell of the table represents one possibility. Count them."
    n "There's 36. It's a six-by-six table, I can tell without counting."
    c "Right, of course. Now then, the numerator represents the dice combinations which you're interested in."
    c "So the ones which have a sum of 11. We can fill in the table with the sums in each case."
    c "And now you can just count the amount of 11s in the table! Pretty simple, isn't it?"
    n "When you put it that way..."
    "There's two 11s in the table. First die is 5 and second 6 or the other way around."
    "So 2 as the numerator, 36 as the denominator, the answer is..."
    n "So it's 2/36?"
    c "I knew you'd get it!"
    return
    
label .probability2:
    c "You roll three dice. What is the probability that at least one of them is a 6?"
    menu:
        "3/6":
            call .wrong_answer2
            call .probability2_explanation
        "91/216":
            call .right_answer2
            jump .math_question3
        "215/216":
            call .wrong_answer2
            call .probability2_explanation
    jump .interrupt
    
label .probability2_explanation:
    c "The probability of one die coming up 6 is 1/6, and if you sum them together, you get 3/6."
    c "But that's not the correct answer! Look at this Venn diagram."
    "She draws three overlapping circles on the screen of her table."
    "Tapping them with her finger, she names them 'A: Die 1 comes up 6,' 'B: Die 2 comes up 6,' and 'C: Die 3 comes up 6'."
    c "If you just naively sum the probabilities together, you will end up counting certain combinations twice."
    c "For instance, the combination 'Dice 1 and 2 come up 6' is contained in both the probability 'A: Die 1 comes up 6' and the probability 'B: Die 2 comes up 6,' so you will end up counting it twice!"
    c "To correct for this, you have to subtract the probability of them both coming up 6 from the sum."
    c "In mathematical notation, P(A)+P(B)-P(A and B)."
    c "You can also see this visually in this portion of the Venn diagram."
    c "Now when you have three different variables, or circles, you have to subtract each of these intersections: A and B, A and C, B and C."
    c "But then, you will have removed the middle part, or 'A and B and C' entirely! So you have to add that back."
    c "So you're final formula becomes P(A) + P(B) + P(C) - P(A and B) - P(A and C) - P(B and C) + P(A and B and C)."
    n "That's ridiculously complicated! Isn't there a simpler way?"
    "She raises one corner of her mouth a bit."
    c "Yeah, in this case there is."
    c "If you want to know the probability of getting one or more instances of some specific result with probability p in n repetitions..."
    n "Say that in English, will ya?"
    c "I'm getting to that! The total probability is 1 - (1-p)^n. So in this case, the probability of getting a six is p = 1/6, you're throwing
    three identical dice, which is mathematically the same as throwing one die three times..."
    c "If p = 1/6 and there's three repetitions, the total probability is... 1 - (5/6)^3, or 91/216."
    c "Essentially, you're calculating the probability of none of the dice coming up six, which is (5/6)^3, and taking the complement of that by subtracting from 1."
    n "That still sounds pretty complicated..."
    
label .probability3:
    c "In the Sherlock Holmes story 'The Adventure of the Six Napoleons,' there are six busts of Napoleon, one of which may conceal a priceless pearl."
    c "The probability that one of the busts really does contain the pearl is 1/2. Five of the busts have been destroyed. What is the probability that there is a pearl inside the last one?"
    menu:
        "1/2":
            call .wrong_answer3
            call .probability3_explanation
        "1/12":
            call .wrong_answer3
            call .probability3_explanation
        "1/7":
            call .right_answer3
    jump .interrupt
    
label .probability3_explanation:
    c "So, um, the probability that there's a pearl at all is 1/2, and there are six identical busts."
    c "So if the pearl does exist, it's in bust 1 with a probability of 1/6, and the same for all the other busts."
    c "When you multiply by the probability of there being a pearl at all, you get (1/2)*(1/6) = 1/12, which is, hold on, about 0.083."
    "She checked that with the calculator on her wristband."
    c "However, this is just the probability in the beginning, before any busts have been broken!"
    c "You might be thinking, well, there's a fifty percent chance that it's not in any of the busts, but if it is, then, since all the others have been broken, it must be in the last one."
    c "So there's a 0.5 probability that it is in the last one."
    n "But that's not correct?"
    c "Well, it sort of doesn't take into account the information you get from breaking the busts."
    n "How so?"
    c "Whenever you break a bust without finding the pearl, the probability of there being no pearl at all also increases, so in the end it should be way more than fifty percent!"
    n "This is making my head hurt."
    "Catherine doesn't answer, but the way she's frowning, she must secretly agree."
    c "So. The correct way to do this is to use the Bayes formula. Do you know that?"
    menu:
        "Sure.":
            n "It was something like... P(H|O) = P(O|H)*P(H)/P(O)?"
            c "Yes."
        "Not really...":
            c "The Bayes formula is like the pythagorean theorem of geometry. It's the most important formula in all of probability theory!"
            c "It says: 'The probability of a hypothesis based on observations is the probability of the observations if the hypothesis is true, multiplied by the probability of the hypothesis and divided by the probability of the observations.'"
            c "So in mathematical terms, P(H|O) = P(O|H)*P(H)/P(O)"
        "Can we do another question? I'm getting a headache.":
            c "Be serious about this, Nick!"
            return
    c "Now our observation is that none of the first five busts contained the pearl. And our hypothesis is that the last one contains the pearl."
    c "We want to calculate P(H|O), or 'the probability that the last one contains the pearl when the other ones didn't.'"
    "I'm starting to zone out a bit, listening to the tea kettle in the background."
    c "So if bust number six contains the pearl, the probability that the first five don't contain it is equal to 1: P(O|H) = 1."
    c "The starting probability for the pearl being in bust 6 is like we calculated earlier, 1/12. So P(H) = 1/12."
    c "Now the probability of the observation. There's two cases where the first five busts will be empty. Either the last bust contains the pearl, probability 1/12, or none of them do, probability 1/2."
    c "Thus, P(O) = (1/12)+(1/2) = 7/12."
    c "Now we can just plug in the values to the Bayes formula: P(H|O) = P(O|H)*P(H)/P(O) = 1*(1/12)/(7/12) = 1/7."
    c "And that's the correct answer!"
    n "How could I ever have figured that out!?"
    c "Well, that's why we're here, after all."
    return
    
label .calculus1:
    c "What is the derivative of x^2 + ln(x) relative to x?"
    menu:
        "2x + 1/x":
            call .right_answer1
            jump .math_question2
        "2x + e^x":
            call .wrong_answer1
            call .calculus1_explanation
        "x^2*ln(x) + 2":
            call .wrong_answer1
            call .calculus1_explanation
    jump .interrupt
    
label .calculus1_explanation:
    c "This is just basic formulas. In a sum, you can differentiate the terms separately. So the answer is just D(x^2) + D(ln(x))."
    c "The derivative of x^2 is 2x by the formula D(x^n) = n*x^(n-1)."
    c "The derivative of ln(x) is known to be 1/x."
    c "So the answer is just 2x + 1/x."
    n "I really don't know this stuff..."
    return

label .calculus2:
    c "What is the minimum point of the parabola x^2 + x + 1?"
    menu:
        "(3/4, -1/2)":
            call .wrong_answer2
            call .calculus2_explanation
        "(-1/2, 3/4)":
            call .right_answer2
            jump .math_question3
        "(0, 1)":
            call .wrong_answer2
            call .calculus2_explanation
    jump .interrupt
    
label .calculus2_explanation:
    c "To minimum of a continuous differentiable function like this is either at the ends of the interval being studied, or at the zeroes of the derivative."
    c "Because there's no interval in this case, the minimum must be at the zeroes!"
    c "The derivative is easily calculated as 2x + 1."
    c "It is only zero when x = -1/2."
    c "Before that, the derivative is negative. And after that, it's positive, so there's a local minimum right at that spot!"
    n "Uh-huh."
    c "So just plug in x = -1/2 to the original equation, and you get (-1/2)^2 + (-1/2) + 1 = 3/4. So the minimum point is (-1/2, 3/4)."
    return
    
label .calculus3:
    "She smiles fiendishly."
    c "What is the 2nd-degree Maclaurin polynomial for the function sin(x)?"
    menu:
        "1 + x + (x^2)/2":
            call .wrong_answer3
            call .calculus3_explanation
        "x - (x^2)/2 + (x^4)/24":
            call .wrong_answer3
            call .calculus3_explanation
        "x - (x^3)/6 + (x^5)/120":
            "Her expression melts into astonishment."
            c "W-what!?"
            call .right_answer3
    jump .interrupt
    
label .calculus3_explanation:
    c "So as everybody knows, the nth-degree taylor polynomial for sin(x) is the sum of the terms (-1)^k * x^(2k+1) / (2k + 1)! as k goes from 0 to n."
    n "Who would know something like that!?"
    c "*Cough*... *cough*... Right, a very simple question indeed..."
    
label .geometry1:
    c "You have a right-angled triangle with the hypotenuse of length 5 and one leg of length 3. What is the length of the remaining leg?"
    menu:
        "4":
            call .right_answer1
            jump .math_question2
        "34":
            call .wrong_answer1
            call .geometry1_explanation
        "The square root of 34":
            call .wrong_answer1
            call .geometry1_explanation
    jump .interrupt

label .geometry1_explanation:
    c "The pythagorean theorem. Mark the legs with a = 3 and b = ?, hypotenuse with c = 5. Now a^2 + b^2 = c^2"
    c "So b^2 = c^2 - a^2 = 25 - 9 = 16."
    c "Taking the square root, we get b = 4."
    c "Easy, right?"
    n "Maybe for you..."
    return
    
label .geometry2:
    c "In soccer, the circumference of the ball has to be between 68 and 70 cm."
    n "You play soccer?"
    c "Not really..."
    c "Anyway, how many percent is the largest allowable ball larger than the smallest one?"
    n "Never imagined I'd see you talking about balls with a straight face."
    "She blushes."
    c "Focus, Nick!"
    menu:
        "110\%":
            call .wrong_answer2
            call .geometry2_explanation
        "9\%":
            call .right_answer2
            jump .math_question3
        "8\%":
            call .wrong_answer2
            call .geometry2_explanation
    jump .interrupt
    
label .geometry2_explanation:
    c "First think about what you want to calculate."
    c "If you form a fraction of the volumes like so: V_max / V_min, this will tell you how large the larger ball is procentually compared to the other."
    n "And that's the answer?"
    c "Not quite. You want to know how many percent {i}larger{/i} it is, that is to say, how many percent above 100\%. So you actually want to calculate (V_max / V_min) - 1."
    c "Now if you plug in the ball volume formula V = 4/3 * pi * r and simplify the resulting equation, you get just (r_max)^3 / (r_min)^3 - 1!"
    c "The only thing left to do is to calculate the radii for the balls. So 2*pi*r_min = 68cm, r_min ~= 10.82 cm."
    c "And 2*pi*r_max = 70 cm, r_max ~= 11.14 cm."
    c "Here's the result: 11.14/10.82 - 1 ~= 0.09 = 9\%."
    n "Man, that was just amazingly simple."
    c "Wasn't it though?"
    n "No. It was sarcasm."
    return
    
label .geometry3:
    c "Okay, how about this. What is the volume of the solid of revolution which is formed when the line f(x) = x, x goes from 0 to 2, rotates around the x-axis?"
    n "Does this even count as geometry!?"
    c "Heh, I take it you can't answer?"
    menu:
        "4*pi":
            call .wrong_answer3
            call .geometry3_explanation
        "2":
            call .wrong_answer3
            call .geometry3_explanation
        "8*pi/3":
            call .right_answer3
    jump .interrupt
    
label .geometry3_explanation:
    c "So, uh, you're essentially integrating..."
    n "Integration? So this is calculus?"
    c "Well, you said your calculus is stronger than your geometry!"
    c "Whatever, just... you're integrating, not the function f(x) = x, but the area of the circle formed as f(x) rotates around the x-axis."
    c "For each value of x, the area is A(x) = pi*x^2. Integrating gives pi/3 * x^3 plus a constant. Now just evaluate in the interval from 0 to 2 and you'll get 8*pi/3 as the answer."
    n "Yeesh, who is willing to study this sort of stuff?"
    return
    
label .interrupt:
    if water_heater_on:
        "A red light appears on Cat's device to signal that the water has been boiled."
        c "I'll get the tea!"
        "She comes back to the room carrying too mugs of hot tea."
        c "Sorry, I only have Ceylon Black."
        $ drink = 0
    elif coffee_machine_on:
        "A red light on Cat's wristband indicates that the coffee is ready for drinking."
        c "I'll go fetch the coffee!"
        "She comes back to the room carrying two mugs of the blackest coffee I've ever seen."
        "Cat, just how much powder did you use?"
        c "Here's some tofu milk in case you don't want to drink it black."
        $ drink = 1
    else:
        "Deciding that I'm in need of some refreshment, I open the coke bottle."
        "And of course, it bursts all around the room, spilling on the carpet!"
        c "I'll go get some paper!"
        "We clean up the mess. Thankfully, the bottle is still over half-full."
        $ drink = 2
    jump .timeskip
    
label .timeskip:
    python:
        if math_subject == 0:
            subject = "probability theory"
        elif math_subject == 1:
            subject = "calculus"
        else:
            subject = "geometry"
    if math_genius:
        c "Since you're so good with [subject], I guess we should just move onto physics or something..."
    else:
        c "Well, let's continue with the [subject]. Try doing this one..."
    "We spend the rest of the evening like this, Cat attempting to teach me while I do my best to avoid learning anything."
    if drink == 1:
        "Not even the power of the coffee is enough to keep us alert anymore."
    else:
        "We consume loads of caffeine, but eventually we must acquiesce to the exhaustion."
    jump .DFO
    
label .DFO:
    "As I'm getting ready to leave, Catherine asks me the question that must have been on her mind for a while now."
    c "Nick, are you still playing that game? DFO?"
    menu:
        "Yes.":
            n "Y-yes. I am."
            # check for promise here
            c "Even though you promised?"
            n "It's a great game, Cat. You should try it sometime."
        "No.":
            n "No."
            n "I mean, I promised, right?"
            c "I see..."
        "Not your business.":
            n "What do you care, Cat? Just let me do what I want."
    "Cat looks disheartened."
    c "Nick, why don't you let me help you..."
    menu:
        "I don't need any help.":
            n "Help? You're not helping me, Catherine. I don't need any help."
        "I came here, didn't I?":
            n "Hey, you already did. I learned loads of math and stuff today."
            c "Yeah, right. After I forced you to listen."
        "Cat, it's not as bad as you think.":
            n "Look, Cat, gaming is just a hobby. It's not magically going to destroy my life."
    c "Damnit, Nick! You need to think about your future!"
    n "The future! It's not like there's going to be any jobs anyway. The robots are going to take them all, right?"
    c "That's bullshit!"
    c "Whatever, just..."
    "She hands me my hat and pushes me towards the door."
    c "Just go."
    "As the door closes behind me, I silently go outside, walking through the streets of the night-lit city, letting no-one see the raindrops on my cheeks."
    

# Structure for the movie scene:
# I wasted so much time... Genius (when procedurally generated)!
# Introduction scene
# Handkerchief
# Buying tickets
# Promise to pay for the tickets
# Finding seats
# Movie
# Girlishness
# Looking at the girl
# Comments on the movie
# Silence
# Timeskip
# Touching hands
# Crying
# Talking about the movie
# Childhood memories (Always crying in middle school)
# Thanks for holding my hand
# Kiss
# Credits roll, leave the cinema

label Catherine_movie_scene:
    $ price_asked = False
    $ seen_before_asked = False
    call .date_intro
    n "Anyway, let's go."
    "We arrive at the ticket booth."
    cashier "Yes? Which movie would you like to see?"
    call .cashier

label .cashier:
    menu:
        "Two tickets for Lover's Abandon.":
            cashier "Any students?"
            c "I am."
            menu:
                "Me too.":
                    cashier "Very well, could you press here for authentication?"
                    "Crap."
                    "We press our fingers on the device. The cashier looks through the results."
                    cashier "Says here you don't have a student status, sir. You're fine, madam."
                    jump .payment
                "One student, one adult.":
                    jump .payment
        "How much do they cost?" if not price_asked:
            n "How much do the tickets cost?"
            cashier "Around 15 000 bits per person. Student discount at half price."
            $ price_asked = True
            jump .cashier
        "Have I seen you before?" if not seen_before_asked:
            n "Aren't you the same guy from the ice cream parlor?"
            $ i = renpy.random.random()
            if i < 0.33:
                cashier "I have no idea what you're talking about."
            elif i < 0.66:
                cashier "Must have been my twin brother."
                "Okay, I guess that... makes sense?"
            else:
                cashier "I am many things, Nicholas. But you will not remember that."
                "Hmm... Strange, I can't remember what he just said."
            $ seen_before_asked = True
            jump .cashier
            
label .payment:
    cashier "That will be 15 000 and 7 500 bits."
    # Check money status
    menu:
        "Pay for both.":
            n "I'll pay for both."
            c "Nick, you don't need to..."
            n "It's fine, Catherine. Let me treat you to something for a change."
        "Pay for yourself.":
            "We both pay for the tickets ourselves."
            "It would have been more chivalrous to pay for Cat's ticket, but I need to think of my wallet as well."
        "Ask Catherine to pay for you.":
            "This is kind of embarrassing, but..."
            n "Uh, Cat, could you pay for me just this once?"
            n "I'm kind of in a poor financial situation."
            c "Wasting it all on games, I'm sure."
            "She sighs and pays for the ticket."
    "After the transaction has been authenticated, we continue into the theatre."
    jump .findseats

label .findseats:
    n "Quite dark in here..."
    c "Seems there's quite many seats free. I wonder where we should sit...?"
    menu:
        "In the front":
            n "Well, the front has the best view, I guess."
            $ seating = "front"
        "In the middle":
            n "Somewhere in the middle should be best."
            $ seating = "middle"
        "In the back":
            n "It's more peaceful in the back, I reckon."
            $ seating = "back"
    "We walk over to the [seating] of the theatre and take our seats."
    
    if seating == "back":
        "You can view the whole theatre pretty easily from here. There's some teenagers to the right..."
        "A couple like us on the middle seats..."
        "And a parent with children that are probably a bit too young to understand this movie, sitting right in front."
    elif seating == "middle":
        "These seats have a pretty nice balance of being close to the screen without having our ears blasted off by the loudspeakers."
        "I can hear the commotion of some teenagers sitting in the back."
        "Next to us is another couple, and in the front is a parent with kids who look slightly too young to be watching this film."
    else:
        "With my VR-numbed senses, these seats are the only ones that can provide any immersion."
        "I can faintly hear teenagers talking and a couple of lovebirds whispering behind us."
        "I'm sure their voices will be drowned out by the loudspeakers."
        "There's a parent with some twerps who look too young for this movie, sitting a bit further away to the side."
    
    jump .moviestart
    
label .moviestart:
    "I sit back to relax as the movie begins."
    "Lover's Abandon. As I had heard, it seems to be a chick flick."
    "Catherine can be unexpectedly girly at times."
    "I steal a glance at her."
    "The movie seems to captivate her."
    "I don't really see the appeal of these sappy romance stories myself, but..."
    "Seeing her like this makes me feel pretty good."
    "The movie is a romance drama about a guy and a girl who, predictably, fall in love at first sight."
    "But they don't really fit together. They're from different social classes and they're interests are not compatible at all."
    "So the guy starts avoiding the girl in the second act, and she's heartbroken."
    "In the cheesy scenes that follow, the girl gets the guy to realize how much he loves her."
    "In the end, he promises to change for her sake, and they get married."
    "Pretty ridiculous if you ask me. She should just dump him."
    "Catherine seems touched, though. I wonder if it's appropriate to make a move?"
    "Normally, it would be fine, but I've been making her pretty angry lately..."
    menu:
        "Hold her hand.":
            "I softly press my hand on hers."
            "She tears up."
            "Did I hurt her feelings somehow?"
            menu:
                "Take your hand away.":
                    "As I try to take my hand away, she holds it tight, mot letting me go."
                "Keep holding her hand.":
                    "I keep my hand where it is, and she responds by holding my hand as well."
        "Pretend to yawn.":
            "I pretend to yawn and curl my arm around her shoulder."
            "She begins to tear up."
            "Did I get too close?"
            menu:
                "Keep holding her.":
                    "I keep my arm around her, and she whispers to the air."
                    c "So beatiful..."
                    "So it was the scene after all..."
                "Better stop.":
                    "She takes hold of my hand before I have the chance to move."
                    c "It's fine, Nicky..."
        "Do nothing.":
            "Tears fall on her cheeks."
            "Was she expecting me to do something?"
            c "How beatiful..."
            "I siqh silently out of relief. So it was only the scene she was crying at."
    if handkerchief:
        "As I place my other hand in my pocket, I feel the handkerchief that Cat gave me earlier, tucked in there."
        menu:
            "Should I give her the handkerchief?"
            "Sure.":
                n "Here."
                "As I hand it back to her, she tilts her head, quizzical."
                c "Is that the one I gave you."
                n "Yes, actually. I didn't even remember to give it back..."
                "She smiles."
                c "That's so like you... Well, thanks anyway."
                "She sniffs the handkerchief."
                n "Hey, I did keep it clean!"
                "She responds with a burst of quiet laughter, saying nothing."
                "Then, she wipes her tears into the handkerchief."
                c "Nicky... Thanks."
            "No, let's save it for later.":
                "I take my hand out of my pocket. You never know when it might turn out useful."
    jump .middleschooltalk
    return
    
label .middleschooltalk:
    n "It's not like you to cry so openly. Was it really that touching?"
    c "What do you mean, it's not like me? I cried all the time in middle school, didn't I?"
    c "Yeah, now that you mention it..."
    jump .flashback
    
label .flashback:
    "I sift through a current of hazy memories coming back to me, thinking back to the first time we met."
    "It was in middle school, wasn't it?"
    "We hadn't really talked to each other or anything. It was recess, and my usual group of friends was away from somewhere."
    "That's when I saw Catherine."
    "I'd like to say something cliched, like she was amazingly beautiful and I fell in love with her at first sight."
    "But that's not really the case. She wasn't a very good-looking kid back then." 
    "She wore thick glasses and obviously didn't do much sports."
    "Anyway, it wasn't her appearance which drew my attention. It was the girls bullying her."
    "I think they were teasing her about her glasses, or something equally stupid."
    "Well, you know how kids are. But that doesn't mean I thought the situation was acceptable!"
    menu:
        "So I went to help her.":
            "Being the strongheaded fool I was, I went to tell those idiots to lay off."
            "They started spreading some bad rumours about me, but it's not like I cared."
            call .friends
        "So I cheered her up afterwards.":
            "Well, I was actually too timid to do anything about it at that specific moment."
            "But later that day, I saw her crying by a tree, so I went to cheer her up, telling her to ignore those idiots."
            call .friends
        "So I went to join the bullies":
            "So being the total jerkass I used to be, I went to join in on the fun."
            "But I felt really sorry after she started crying, and secretly went to her to apologize, begging for her forgiveness."
            call .friends
    jump .opinion
    
label .friends:
    "Cat and I started to spend a lot of time together after that. I had quite a lot of friends, and she joined our group as an equal."
    "Despite not really being into the sort of nerdy stuff we liked, she seemed a lot happier after that."
    return
    
label .opinion:
    "Cat looks into my eyes."
    c "Wasn't it great?"
    menu:
        "Yes.":
            n "Yeah."
            jump .kiss
        "If you say so.":
            n "If you liked it, then so do I."
            jump .kiss
        "It was terrible.":
            n "No, it sucked."
            "Cat frowns."
            c "Well thank you very much for ruining the mood, Nicholas."
            "We move out of the theatre, Cat's berating still ringing in my ears."
            "Still, she looks happy enough."
            c "Thanks, Nick. We should do things together more often."
            "With one last hug, we go our separate ways."
    return
    
label .kiss:
    "She closes her eyes expectantly."
    menu:
        "Kiss her.":
            "In the darkness of the movie theatre, I press my mouth on her soft, slightly open lips."
        "Hesitate.":
            "Since I won't make the first move, she does, pressing her rosy lips upon mine."
    
    if seating == "front":
        "The parent sitting next to us probably doesn't appreciate our wanton display of carnal desires."
        "But it's really their own fault for bringing kids to a movie like this in the first place."
    elif seating == "middle":
        "The couple next to us is kissing as well, and I can hear the teenagers variously cheering and booing in the background."
    else:
        "The teens next to us are giggling and whispering to each other, but I do my best to ignore them."
        
    "After a long kiss, we move out of the theatre."
    c "Thanks, Nick. Let's do this again some time."
    "We say our farewells and go our separate ways."
    return
    
label .date_intro:
    "As I arrive at the movie theatre, I see that Catherine is already here."
    n "Sorry, have you been waiting for long?"
    c "N-no, just a short while."
    return
 
label Catherine_broken_up_mall:
    "While walking at the mall, I spot Catherine inspecting some clothes."
    menu:
        "Should I go talk to her?"
        "Go talk to her.":
            "I gather my courage and approach her."
            "I'm so close that I can smell the floral notes of her shampoo, but her mind seems to be wandering in some other world."
            "I tap her on the shoulder, and she jolts."
            c "N-nick? Hi."
            n "Hi."
        "Better leave it be.":
            "I go to a store and wait for her to leave. She probably doesn't want to see me, anyway."
            return
    c "Could you just... I really don't feel like talking to you right now."
    "She's avoiding eye contact."
    menu:
        "Apologize":
            jump .sorry
        "Blame her":
            n "I just want to say one thing to you, Catherine."
            n "It was all your fault. And you're not guilt tripping me on this one."
            "Her expression turns blank, her face white, and she turns to leave without saying anything."
        "Stay silent":
            "I stand behind her, both of us stammering for words."
            "Finally, she breaks the silence."
            c "Do you hate me?"
            menu:
                "Yes":
                    n "Kind of."
                    c "... I thought so."
                "No":
                    n "Of course not."
                    c "... That's good to hear."
    return
        
label .sorry:
    n "Catherine, I'm sorry. I didn't mean to hurt you."
    n "Please forgive me."
    "She looks hesitant, her eyes glimmering with sorrow."
    c "Nicky......"
    "The silence is interrupted by the sound of her swallowing."
    c "Nicholas, I already have someone else."
    n "What? It's only been three days!"
    "Cat frowns."
    c "Well, he asked me out."
    menu:
        "T-that's great!":
            n "Well, that's just great."
            c "It, uh, it is?"
            n "Yeah, I'm so happy for you."
            n "I'm sure you've finally found someone you deserve."
            n "You know, someone who doesn't waste all his time online."
            c "Nick, stop acting like a fricking kid!"
            n "I'm serious! I'm sure this guy is way better for you. What's he like, anyway?"
            jump .guydescription
        "Come on, who is it?":
            n "Who is it?"
            "Cat folds her arms in defense."
            c "None of your business."
            n "Come on, tell me."
            c "I-it's no one you know..."
            n "Well, what's he like?"
            jump .guydescription
        "Well, I've got a new girlfriend too!":
            jump .newgirlfriend
            
label .newgirlfriend:
    n "W-well, you know what? I've found a new girlfriend too!"
    "Now it's her turn to be astonished."
    c "W-WHAT!? Who?"
    n "Oh, you haven't met her..."
    c "... Oh yeah? What's she like?"
    "Uh-oh. She doesn't seem to be buying my story!"
    menu:
        "She plays DFO.":
            c "Really? What sort of character?"
            n "What do you care? It's not like you'd even understand."
            "My comment doesn't seem to satisfy her."
            c "Nevermind that. Just tell me."
            menu:
                "She's a priestess named Aerith.":
                    "Catherine blinks."
                    c "O-oh? Is that so?"
                    n "Yes. She had obviously taken a liking to me, so we hooked up right after you and I broke up."
                    c "Excuse me, 'obviously liked you'? Cut it with the arrogance, Nick."
                "She's an assassin named Silvia.":
                    "Catherine's expression turns sour."
                    c "Really. Have you even met this person in real life?"
                    menu:
                        "Yes.":
                            n "Sure. Many times."
                            c "You're such a bad liar, Nick."
                            "The wavering of her voice betrays her uncertainty."
                        "No.":
                            n "Well, not yet..."
                            "Catherine responds to that with a hurt laugh."
                            c "And you think you're together. Get your feet back on the ground."
                        "We have a date coming up.":
                            n "We've already set up a date."
                            "Catherine raises her eyebrows in disbelief."
                            c "No way! You're just, you're just saying that to boost your ego..."
                "She's a demopyre mage named Lucia666.":
                    "Catherine seems confused."
                    c "What? A demopyre?"
                    n "Demon vampire, duh."
                    "She shakes her head, frowning in disbelief."
                    c "That doesn't even make sense."
                    n "Hey, I didn't design the game."
                    c "That's not what I... whatever."
        "Okay, I made her up.":
            n "You caught me. I made it up."
            c "Figured as much."
        "She's hot.":
            n "Well, you know, a real blonde bombshell!"
            n "Short, wavy hair, curvy body, ample breasts..."
            n "... always wears white ..."
            c "Uh, Nick?"
            c "Are you describing Marilyn Monroe?"
            n "What? Nooo. No, she's real. I mean, Marilyn Monroe is real too, and so's this girl!"
            n "Yeah, and she's really into me. She says I'm the most handsome man she's ever laid her eyes upon!"
            n "And then she said: 'You'd have to be a real idiot to let go of a guy like me!' Yeah!"
            "Catherine is giggling now."
            c "Whatever. I never did get your sense of humor, Nick."
    return

label .guydescription:
    $ height = renpyrandomnormal(178, 7)
    $ haircolor = renpy.random.choice(["auburn", "fiery", "blonde", "chestnut", "black"])
    $ eyecolor = renpy.random.choice(["baby blue", "cerulean", "gray", "hazel", "amber", "deep blue", "indigo"])
    $ positiveattribute1 = renpy.random.choice(["smart", "intelligent", "hunky", "confident"])
    $ positiveattribute2 = renpy.random.choice(["funny", "humorous", "good-looking", "attractive"])
    c "Well, he's [height] cm tall, he has [haircolor] hair and [eyecolor] eyes, he's [positiveattribute1] and [positiveattribute2]..."
    n "... And he lives in Canada."
    c "This is serious, Nick!"
    return
    
label .interrupt:
    "Catherine puts down the shirt she was inspecting and turns to leave."
    menu:
        "Stop her.":
            # Silence
            "I place my hand on her shoulder, and she turns around, looking defiantly into my eyes."
            c "What?"
            menu:
                "Kiss her.":
                    # Response should depend on affection
                    "Without giving her time to react, I press my mouth upon her rosy lips."
                    "At first she resists, but then her arms curl around my back, embracing me."
                    # If she's angry, expect a slap instead
                    "After a moment's eternity, we let go, still gazing deeply into each other's eyes."
                    jump .loveyou
                "Profess your love for her.":
                    n "Cat, I love you. Please come back to me."
                    # Response should depend on affection
                    c "Nick, I..."
                    c "I can't. It won't work."
                    "She breaks free from my grasp and walks away as I reach my hand toward her back, receding into the distance."
                "Slap her.":
                    "I slap her on her cheek. I try to be gentle, but hey..."
                    "She holds her cheek with reddened eyes."
                    "Then, she regains her fervor."
                    c "What did you do that for!?"
                    menu:
                        "Because I love you.":
                            n "I love you, Cat. And I can't take these games any longer."
                            jump .loveyou
                        "Because you deserve it.":
                            n "You're always playing games with me. I can't stand it anymore!"
                            c "Games!? I'm the one playing games with {i}you{/i}?"
                            c "You're a hypocritical bastard, you know that, Nick?"
                            "She breaks free from my grasp and storms off."
                        "I just felt like it.":
                            n "I don't know where it came from. Sorry, I guess."
                            c "You're always guessing, aren't you?"
                            n "W-what's that supposed to mean?"
                            "She sighs, breaks free and leaves me hanging."
                "Say nothing.":
                    "We stay silent, still looking at each other."
                    "Then, she whispers."
                    c "Nick, please just let it go."
                    "She turns around, and, breaking free from my grasp, walks away.."
        "Let her go.":
            "With a heavy heart, I watch her back disappear into the crowd."
    return
        
label .loveyou:
    c "Nick, I..."
    # If she really likes you, she'll be willing to try again
    "She closes her eyes, then runs away."
    
# Other scenes

label DFOServers:
    scene servers
    "I'm pretty elated."
    "I get to clean at one of the server farms at DFO today!"
    "In one of the rooms I'm supposed to clean, I see a guy wearing cheap VR gear at one of the desks."
    "He's probably an employee. Usually there isn't anyone here while I'm working, though."
    "Should I disturb him?"
    menu:
        "Is there any real choice?":
            jump .conversation_start
        "Eh, I'll go clean somewhere else.":
            "I go clean the other parts of the building, but when I return, the guy is still there."
            menu:
                "Talk to him.":
                    jump .conversation_start
                "Just ignore the room":
                    "As I turn to leave, one last thought enters my mind."
                    "My boss has been a bit stressed lately. No way he's going to appreciate it if someone finds out I didn't clean the room."
                    menu:
                        "Leave anyway.":
                            "He seems really busy. Maybe this is the best option in the end."
                            return
                        "Okay, okay, go talk to the guy. Yeesh.":
                            jump .conversation_start
    return
    
label .conversation_start:
    $ main_hub_visits = 0
    "I go over to him and tap him lightly on the shoulder."
    "He jolts and takes the VR gear away."
    "His expression relaxes as he sees me, though."
    m "Hi. I guess you're the cleaner?"
    menu:
        "Yes.":
            m "Yeah, I guessed as much."
            jump .main_hub_transition
        "No.":
            m "I haven't seen you before. A new employee?"
            menu:
                "Yes.":
                    m "Excuse me, can I see your ID? Just need to be on the lookout for any suspicious activity, you see."
                    n "Uh, I don't have one."
                    n "Sorry, I was only joking. I'm actually a cleaner."
                    "He doesn't seem to trust me that much."
                    m "Yeah, I hope so."
                    jump .main_hub_transition
                "No, I'm a spy.":
                    n "No, I'm a spy."
                    m "Pretty forthright for a spy. Then again..."
                    m "... you can never be sure."
                    n "It was just a joke. I'm a cleaner, like you thought."
                    jump .main_hub_transition
                "I was just joking. I'm a cleaner.":
                    m "I thought so."
                    jump .main_hub_transition
        "Who are you?":
            m "I'll ask the questions here, if you don't mind."
            m "For reasons of security, you know. Who are you?"
            n "I'm from the cleaning service."
            m "Just as I thought."
            jump .main_hub_transition
        
label .main_hub_transition:
    if main_hub_visits == 0:
        m "What do you want?"
    elif main_hub_visits == 1:
        n "I have some more questions."
        m "Ask away."
    elif main_hub_visits == 2:
        n "I'd still like to ask some questions..."
        m "Okay, but I need to get back to work soon."
    else:
        n "A few more questions..."
        m "{i}One{/i} more question. I really need to get back to work."
    $ main_hub_visits += 1
    jump .main_hub
    
label .main_hub:
    call HubMenu("DFOServers", True, [("Who are you?", "who_transition"),
    ("Could you refresh my memory a bit? Who were you?", "who_transition2"),
    ("What are you doing?", "what_transition"),
    ("Could you remind me what you were doing here?", "what_transition2"),
    ("Why are you still here?", "why_transition"),
    ("You were working late for some reason?", "why_transition2"),
    ("Could you move? I need to clean this room.", "move_transition"),
    ("Why did you say you couldn't move, again?", "move_transition2"),
    ("Do you happen to own a master key?", "key_transition"),
    ("Couldn't you let me see some places, just this once?", "key_transition2")], ("On second thought, I'll just leave you to your work.", "leave"))
    return
            
label .leave:
    n "I think I'll just leave you to do your work."
    m "Well, thanks for the company. It gets a bit lonely here, some nights."
    return
    
label .forced_leave(label):
    if main_hub_visits > 3:
        m "Anyway, I really need to get back to work now. It was nice talking to ya."
        "He puts the VR glasses back on and refuses to respond anymore."
        return
    else:
        jump expression "DFOServers"+label
        
label .who_transition:
    m "Oh, how impolite of me. I'm Andy Vrable, an employee here, at least for now. My friends call me Data."
    $ serverguy = "Andy"
    call .forced_leave(".who")
    return
    
label .who_transition2:
    n "Who were you again?"
    "He looks at me, a bit non-plussed."
    m "Andy 'Data' Vrable, data scientist at Klein Hyperbolic. I didn't catch your name, mister..."
    n "Nicholas."
    m "Yes, well, Nicholas, consider yourself lucky."
    m "I don't remember other people's names and I don't expect them to remember mine."
    call .forced_leave(".who")
    return
    
label .who:
    call HubMenu("DFOServers", True, [("Why do they call you that?", "who_why"),
    ("Why did they call you Data again?", "who_why_recap"),
    ("So you designed DFO?", "who_designed"),
    ("What did you say your job was?", "who_designed_recap"),
    ("'For now'? Are you thinking of quitting?", "who_work"),
    ("What was that AI system you mentioned?", "who_work_recap"),
    ("What's it like to work at a cool company like Klein Hyperbolic?", "who_Klein"),
    ("You said you didn't like to work here?", "who_Klein_recap")], ("I had some more general questions...", "main_hub_transition"))
    return
    
    # $ who_why = False
    # $ who_designed = False
    # $ who_Klein = False
    # $ last_asked = ""
    #menu:
    #    "Why do they call you that?" if not who_why and last_asked != "who_why":
    #        $ who_why = True
    #        $ last_asked = "who_why"
    #        jump .who_why
    #    "Why did they call you Data again?" if who_why and last_asked != "who_why":
    #        $ last_asked = "who_why"
    #        m "Apparently they think I'm like an android. Or it's a twisted compliment, I don't know."
    #    "So you designed DFO?" if not who_designed and last_asked != "who_designed":
    #        $ who_designed = True
    #        $ last_asked = "who_designed"
    #        jump .who_designed
    #    "What did you say your job was?" if who_designed and last_asked != "who_designed" and last_asked != "datascience":
    #        $ last_asked = "datascience"
    #        m "I'm a data scientist. I go through user data logs and try to find patterns in it."
    #    "What was that AI system you mentioned?" if who_designed and last_asked != "who_designed" and last_asked != "AIDA":
    #        $ last_asked = "AIDA"
    #        m "I think it was called AIDA according to the leaks. Artificially Intelligent Directing Assistant."
    #        m "I feel like I've seen the term somewhere else, though..."
    #    "What's it like to work at a cool company like Klein Hyperbolic?" if not who_Klein and last_asked != "who_Klein":
    #        $ who_Klein = True
    #        $ last_asked != "who_Klein"
    #        jump .who_Klein
    #    "You said you didn't like to work here?" if who_Klein and last_asked != "who_Klein":
    #        $ last_asked = "who_Klein"
    #        m "Well, not as long as they're treating their employees like dirt."
    #    "I had some more general questions...":
    #        jump .main_hub_transition
            
label .who_why:
    m "I think it's supposed to be a Star Trek reference. Makes sense, considering my line of work."
    jump .who

label .who_why_recap:
    m "Apparently they think I'm like an android. Or it's a twisted compliment, I don't know."
    jump .who
    
label .who_designed:
    m "Not really. I'm a data scientist. I analyze all the user data we're collecting and try to find sensible patterns within it."
    m "It's my job to figure out what people enjoy so the marketers and game designers can capitalize on that."
    jump .who

label .who_designed_recap:
    m "I'm a data scientist. I go through user data logs and try to find patterns in it."
    jump .who
    
label .who_work:
    m "I guess you know about the AI director?"
    menu:
        "Of course":
            n "Yeah, I, uh, know all about it."
            m "Really? Well, my analyses are used to subtly modify its algorithms. You know, to produce an improved player experience."
        "I've heard of it, but don't know the details.":
            n "I don't really know the details."
            m "Yeah, well, you'd have to be a programmer, I guess. It's not like we want our competitors like ClicheQuest, Alfheim Online and Elder Tale to figure out our secret sauce."
            call .aidescription
        "Never heard.":
            n "Never heard of it?"
            m "Oh? I thought you were a player?"
            n "I've been on hiatus for a while."
            m "Hmm. All right, then."
            call .aidescription
    m "Recently, some guys at the company have been spreading rumors about a next-gen AI director that would completely replace data scientists like me."
    m "Rumor goes Klein Hyperbolic is developing it in collaboration with some big names like MIT and DeepMind Technologies."
    m "It's a secret even within the company, but some articles about it were leaked on the internet a while back."
    m "The architecture they describe is really freaking cool, way beyond any conventional game AI I've ever seen."
    jump .who
    
label .who_work_recap:
    m "I think it was called AIDA according to the leaks. Artificially Intelligent Directing Assistant."
    m "I feel like I've seen the term somewhere else, though..."
    jump .who
            
label .aidescription:
    m "Well, the purpose of the AI director is to improve the player experience by spawning monsters, redesigning dungeons and generating new quests."
    m "It's not actually as complicated as it sounds. Games have been using AI directors since 2008."
    return
    
label .who_Klein:
    n "So, isn't it amazing to work at a company like this?"
    "He doesn't seem to agree with my remark."
    m "Well, you know, it's a job. The pay's good, at least."
    n "But you don't like it?"
    m "I'm working overtime right now, aren't I?"
    jump .who
    
label .who_Klein_recap:
    m "Well, not as long as they're treating their employees like dirt."
    jump .who
    
label .what_transition:
    m "I'm running late on some analyses on the user data generated by the new expansion they released a while back."
    m "So it's crunch time as usual."
    call .forced_leave(".what")
    return
    
label .what_transition2:
    n "What were you doing, again?"
    m "I'm trying to do these analyses."
    "He notices my fidgeting."
    m "It's all right. A small break does no harm."
    call .forced_leave(".what")
    return
    
label .what:
    call HubMenu("DFOServers", True, [("How do you actually analyze the data?", "what_analysis"),
    ("Can you show me that VR thing again?", "what_analysis_recap"),
    ("Any interesting patterns?", "what_interesting"),
    ("You sure you can't tell me any of your findings?", "what_interesting_recap"),
    ("Wasn't that expansion released like a month ago?", "what_expansion"),
    ("Sorry, I forgot why you're still working on this?", "what_expansion_recap")], ("I had some more general questions...", "main_hub_transition"))
    return
            
label .what_analysis:
    n "How do you actually do the analysis? With that headset, I would have mistaken you for a play-tester."
    m "Heh. It's a bit hard to explain. But I can show you."
    "He beckons me to place the headset over my eyes."
    "As I do so, I'm first struck by the primitive graphics."
    "But this initial impression quickly turns into confusion."
    "I am watching small shapes of sundry shapes and colors fly around a pitch-black space, like falling stars or colorful dust motes floating in all directions around me."
    "I return the headset, feeling a bit disoriented."
    n "What was that?"
    m "Well, if you want the technical explanation, it was a projection of a higher-dimensional data space into a 7-dimensional space."
    m "Seven dimensions, that is, three spatial, one temporal, color, size and shape."
    n "That didn't really help."
    m "Haha, just think of it like a really complicated scatter plot."
    m "Exploratory data analysis really took off after the VR revolution."
    m "It takes years to build up the experience you need, but eventually you can read deep patterns in that cloud of information."
    m "I've been dreaming of tech like this ever since I read Gibson as an adolescent. I was one of the first to jump on the bandwagon when the cyberspace became reality."
    jump .what
    
label .what_analysis_recap:
    n "Could you show me that VR thing again? It was cool."
    m "The 7-dimensional scatter plot? Sure."
    "I place the headset over my eyes again. This time, I can almost make out patterns in the way the technicolor points and crosses move across the vast expanses of the black background."
    n "Yup, still cool, still confusing."
    m "It takes a while to really spot the patterns. It's rewarding work, in and of itself."
    jump .what
    
label .what_interesting:
    n "So, uh, found anything interesting so far?"
    m "Plenty. But they're company secrets."
    menu:
        "Come on, I probably won't even get it.":
            "He looks at me suspiciously."
            m "Yeah. Either you're naive or a spy."
            m "Let me give you a piece of advice, kid."
            m "Don't trust anyone. Everything's broken, nothing is secure."
        "Ah, okay then.":
            n "Okay, no pressure."
            m "Sorry about that. But I really can't tell you."
    jump .what
    
label .what_interesting_recap:
    n "Could you please tell me something you've figured out?"
    m "No. And I'd advise you to stop asking."
    jump .what
    
label .what_expansion:
    n "I thought that expansion was released over a month ago. You're still analysing it?"
    m "Well, of course we've been analysing data from players and beta testers since before it was released."
    m "But now we've acquired enough to start searching for some truly stable patterns."
    jump .what
    
label .what_expansion_recap:
    n "Why were you still analyzing that expansion?"
    m "The more data you have, the more certain will be the inferences you can draw from it."
    m "We've finally collected enough to figure out and confirm stable patterns."
    jump .what
    
label .why_transition:
    m "I'm running late on these analyses I'm supposed to be making. And Klein Hyperbolic really doesn't appreciate late reports."
    m "But they're not against over-time work."
    call .forced_leave(".why")
    return

label .why_transition2:
    n "What was the reason you were working so late?"
    m "Draconic employment policies."
    n "Ah."
    call .forced_leave(".why")
    return
    
label .why:
    call HubMenu("DFOServers", True, [("You still get extra pay, right?", "why_extra"),
    ("They really don't pay you for over-time work?", "why_extra_recap"),
    ("That sorta sucks.", "why_sucks"),
    ("What was that piece of advice you gave me about games development?", "why_sucks_recap"),
    ("Is this really legal?", "why_legal"),
    ("Can't you sue them or something?", "why_legal_recap")], ("I had some more general questions...", "main_hub_transition"))
    return

label .why_extra:
    n "But they still pay you for over-time, right?"
    m "I wish. For me, this is just a way to keep my job."
    jump .why
    
label .why_extra_recap:
    n "They really don't pay you for working over-time?"
    m "What are you expecting me to say? 'Haha, it was just a joke'?"
    "He sighs."
    m "When you get older, you find out that jokes aren't as funny when you're the butt of them..."
    jump .why
    
label .why_sucks:
    n "That kinda sucks."
    "He responds in a dry tone."
    m "Gee, thanks for the empathy."
    m "Anyway, if you ever get into games development, make sure to pick the right company."
    m "In case you're so amazing that you {i}have{/i} choice."
    jump .why
    
label .why_sucks_recap:
    n "What was that tip you gave me about games development?"
    m "Unless you're really passionate about it, just don't."
    m "But hey, you're young. You've no business listening to a cynical old man like me."
    jump .why
    
label .why_legal:
    n "This can't be legal. You can't just make people work like slaves."
    m "Apparently you can, if you're too big to care."
    jump .why

label .why_legal_recap:
    n "You really should just sue them."
    m "And lose my livelihood fighting a losing battle for the sake of justice in an unjust world."
    m "Must be nice to have eyes so clear and blue."
    jump .why

label .key_transition:
    n "So, um, I guess you have the keys to all the top-secret areas?"
    "He furrows his eyebrows, suspicious."
    m "And what if I do?"
    menu:
        "I'd like to see some of the server halls.":
            n "I'd just like to see some of the server halls. You know, out of curiosity."
            m "Is that so? Well, I'm sorry to disappoint, but I can't let you there."
        "Nothing, just asking.":
            n "Oh, it's nothing. I was just curious."
            m "Oh, you were, weren't you?"
    call .forced_leave(".main_hub_transition")
    return
    
label .key_transition2:
    n "You really can't show me around?"
    m "Nope. Sorry, that's just the way it is."
    call .forced_leave(".main_hub_transition")
    return
    
label .move_transition:
    n "Could you maybe move somewhere? I need to clean this room."
    m "Sorry, pal. The data is contained locally on this computer for security reasons. I mean, I could transfer it, but that would take like an hour."
    call .forced_leave(".move")
    return
    
label .move_transition2:
    n "Why did you say you couldn't move from here?"
    m "The data is contained locally, and there's loads of it. And, in addition to that, I simply lack the time."
    call .forced_leave(".move")
    return
    
label .move:
    call HubMenu("DFOServers", True, [("You're storing the data locally?", "move_locally"),
    ("Why did you have to store the data locally, again?", "move_locally_recap"),
    ("An hour? How much data do you have there?", "move_how_much"),
    ("How much data did you say you had stored?", "move_how_much_recap"),
    ("It won't take long. You can just come back afterwards.", "move_quick"),
    ("I'd really like to clean this room.", "move_quick_recap")], ("I had some other questions...", "main_hub_transition"))
    return
    
label .move_locally:
    n "You're storing it locally? As in 'not connected to the Net?'"
    m "That's what the word means, yes."
    n "Why?"
    m "I told you. Security. Course, it means I have to commute here whenever I want to take a look at the whole dataset."
    jump .move
    
label .move_locally_recap:
    n "Why did the data have to be local, again?"
    m "If the storage servers are not connected to the net, there's no danger of them being hacked. In principle, at least."
    jump .move

label .move_how_much:
    n "It takes an hour? Just how much data have you collected?"
    m "I reckon it's somewhere around 1.6 petabytes."
    n "Wow."
    m "Yeah, it's pretty cool."
    jump .move

label .move_how_much_recap:
    n "How much data did you have here?"
    m "It was around 1.6 petabytes."
    n "You know, that number never ceases to amaze me."
    jump .move

label .move_quick:
    n "I'll be quick, I promise."
    n "I really need to clean this place. Command from above, you understand."
    m "Hey, don't worry about it. I'll just tell the bosses I saw you and didn't let you clean up cuz I was so paranoid."
    m "You're not going to get into any trouble for it."
    jump .move
    
label .move_quick_recap:
    n "Could I please clean this place?"
    m "Why do you want it that bad? I said I'm not gonna let anyone pressure you about it."
    n "Um, I guess I'm just addicted to cleanliness."
    m "You'll make a great housewife some day."
    jump .move
    
# Code for handling Bioware-style Hub-and-Spokes conversation in an elegant (or "elegant") way

label HubMenu(calling_label, hide_if_last_asked, list_of_choices, exit_choice = False):
    # list_of_choices is a python list of (string, string)-tuples representing the choice text and the name of the label.
    # The handler *doesn't* allow repeating choices. Instead, for each choice you need to provide a "repeat-alternative" which
    # will be shown after the player has tried the choice once. The rep-alt should provide a short recap of the earlier discussion.
    # Check the examples above, it'll probably be clearer.
    # Supports up to 6 choices, but it's easy to extend.
    
    menu:

        "[list_of_choices[0][0]]" if len(list_of_choices) >= 1 and (not hide_if_last_asked or last_seen != list_of_choices[0][1] ) and not list_of_choices[0][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[0][1]
            $ last_seen = list_of_choices[0][1]
            $ hub_seen_labels.append(list_of_choices[0][1])
        "[list_of_choices[1][0]]" if len(list_of_choices) >= 2 and (not hide_if_last_asked or last_seen != list_of_choices[0][1] ) and list_of_choices[0][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[1][1]
            $ last_seen = list_of_choices[0][1]
            
        "[list_of_choices[2][0]]" if len(list_of_choices) >= 3 and (not hide_if_last_asked or last_seen != list_of_choices[2][1] ) and not list_of_choices[2][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[2][1]
            $ last_seen = list_of_choices[2][1]
            $ hub_seen_labels.append(list_of_choices[2][1])
        "[list_of_choices[3][0]]" if len(list_of_choices) >= 4 and (not hide_if_last_asked or last_seen != list_of_choices[2][1] ) and list_of_choices[2][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[3][1]
            $ last_seen = list_of_choices[2][1]
            
        "[list_of_choices[4][0]]" if len(list_of_choices) >= 5 and (not hide_if_last_asked or last_seen != list_of_choices[4][1] ) and not list_of_choices[4][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[4][1]
            $ last_seen = list_of_choices[4][1]
            $ hub_seen_labels.append(list_of_choices[4][1])
        "[list_of_choices[5][0]]" if len(list_of_choices) >= 6 and (not hide_if_last_asked or last_seen != list_of_choices[4][1] ) and list_of_choices[4][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[5][1]
            $ last_seen = list_of_choices[4][1]
            
        "[list_of_choices[6][0]]" if len(list_of_choices) >= 7 and (not hide_if_last_asked or last_seen != list_of_choices[6][1] ) and not list_of_choices[6][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[6][1]
            $ last_seen = list_of_choices[6][1]
            $ hub_seen_labels.append(list_of_choices[6][1])
        "[list_of_choices[7][0]]" if len(list_of_choices) >= 8 and (not hide_if_last_asked or last_seen != list_of_choices[6][1] ) and list_of_choices[6][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[7][1]
            $ last_seen = list_of_choices[6][1]
            
        "[list_of_choices[8][0]]" if len(list_of_choices) >= 9 and (not hide_if_last_asked or last_seen != list_of_choices[8][1] ) and not list_of_choices[8][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[8][1]
            $ last_seen = list_of_choices[8][1]
            $ hub_seen_labels.append(list_of_choices[8][1])
        "[list_of_choices[9][0]]" if len(list_of_choices) >= 10 and (not hide_if_last_asked or last_seen != list_of_choices[8][1] ) and list_of_choices[8][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[9][1]
            $ last_seen = list_of_choices[8][1]
            
        "[list_of_choices[10][0]]" if len(list_of_choices) >= 11 and (not hide_if_last_asked or last_seen != list_of_choices[10][1] ) and not list_of_choices[10][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[10][1]
            $ last_seen = list_of_choices[10][1]
            $ hub_seen_labels.append(list_of_choices[10][1])
        "[list_of_choices[11][0]]" if len(list_of_choices) >= 12 and (not hide_if_last_asked or last_seen != list_of_choices[10][1] ) and list_of_choices[10][1] in hub_seen_labels:
            $ target = calling_label + "." + list_of_choices[11][1]
            $ last_seen = list_of_choices[10][1]
         
        # Exit choice 
        "[exit_choice[0]]" if exit_choice:
            $ target = calling_label + "." + exit_choice[1]
            
    jump expression target