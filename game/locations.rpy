init:
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
    
    $ serverguy = "Man"
    
    $ visited = {"arcade": False, "movies": False}
    $ prices = {'arcade': 7000, 'arcade_both': 14000, 'movies': 15000, 'movies_student': 7500, 'movies_both': 22500, 'gym': 1000, 'swimminghall': 3000, "bar_cheap": 3000, "bar_medium": 6000, "bar_expensive": 12000, "parlor_cheap": 6000, "parlor_medium": 12000, "parlor_expensive": 24000, "mall_cheap": 3000, "mall_medium": 8000, "mall_expensive": 24000, "bowling": 1000, "restaurant_cheap": 12000, "restaurant_medium": 24000, "restaurant_expensive": 48000}
    $ fitness_bonuses = {'swimminghall': 7, 'runningtrack': 5, 'gym': 6}
    $ stress_modifiers = {'movies': -2, 'arcade': -1, 'bar_drink': -1, 'bar_nodrink': 0, 'library': 0, 'work': 2, 'restaurant': -1, 'mall_expensive': -3, 'mall_medium': -2, 'mall_cheap': -1, 'clean': 0, 'bowling': -1, 'swimminghall': 0, 'gym': 0, 'runningtrack': 0, 'business': 0, 'parlor_broken_up': 0, 'parlor': -2}


    
# Location-specific characters
define o = Character("Old guy")
define jackquotes = Character("'Jack'")
define jack = Character("Jack")
define m = DynamicCharacter("serverguy")
define cashier = Character("Cashier")

# Location-specific actions
label business:
    "I wander around the hallways for a bit. Why did I even come here in the first place?"
    
    $ stress += stress_modifiers['business']
    
    return
               
label work:
    "I clean up at some organization."
    
    $ i = renpy.random.random()
    
    $ stress += stress_modifiers['work']
    
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
        
    $ work_counter += 1
    
    return
    
label clean:
    "I clean up the litter that's accumulated on the floor of my apartment."
    
    $ stress += stress_modifiers['clean']
    
    return
    
label icecreamparlor:
    "I eat some ice cream."
    if broken_up:
        "Eating here reminds me of Catherine. The sweetness of the ice cream mixes with the bitterness of my emotions."
        $ stress += stress_modifiers['parlor_broken_up']
    else:
        "Delicious as always."
        $ stress += stress_modifiers['parlor']
    return
    
label restaurant:
    # Restaurant, choose something to eat.
    
    if cash < prices['restaurant']:
        "I walk past the restaurant, feeling grim."
        "I don't have enough bits to eat here right now."
    
    "I pick something cheap from the menu."
    "At least I don't have to stumble making food by myself."
    $ stress += stress_modifiers['restaurant']
    
    return
    
label movietheatre:
    # Movie theatre, choose a movie to go to
    
    $ genre = NonUniformRandom( [("action", 2), ("romantic comedy", 1), ("horror", 1)] ).pick()
    
    if cash >= prices['movies']:
        "I watch a random [genre] flick, all alone."
        $ cash -= prices['movies']
        $ stress += stress_modifiers['movies']
    else:
        "At the movie theater, it dawns on me that I do not have enough cash to buy a ticket."
    
    return
    
label vrarcade:
    # Arcade, choose a game to play
    
    $ game1 = NonUniformRandom([("Ghosts & Goblins", 1), ("BlazBlue",1), ("Metal Slug 2",1)]).pick()
    $ game2 = NonUniformRandom([("Mortal Kombat", 1), ("Street Fighter II", 1), ("Space Invaders", 1)]).pick()
    
    if cash >= prices['arcade']:
        "I boot up some of the old retro arcade games, playing [game1] and [game2]."
        "The virtual reality stuff is cool too, but I have far better equipment at home."
        $ cash -= prices['arcade']
        $ stress += stress_modifiers['arcade']
    else:
        "I suddenly realize that I lack the bits to pay for the entrance fee."
    
    return
   
label bowling:
    # Bowling, pay for it
    
    if cash >= prices['bowling']:
        "I do some bowling by myself."
        $ cash -= prices['bowling']
        $ stress += stress_modifiers['bowling']
    else:
        "It seems I don't have enough bits to go bowling."
    
    return
    
label bar:
    # Bar, choose a drink
    
    if cash >= prices['bar_cheap']:
        "I buy a drink and enjoy the beat."
        $ cash -= prices['bar_cheap']
        $ stress += stress_modifiers['bar_drink']
    else:
        "I don't have enough money to buy a drink, but I still enjoy the beat."
        $ stress += stress_modifiers['bar_nodrink']
    
    if broken_up:
        "Now that I've broken up with Catherine, I guess I could try to find a new partner."
        "Somehow I don't really feel interested, though."
    
    return
    
label swimminghall:
    # Leisure swimming vs. Exercise
    
    if cash >= prices['swimminghall']:
        "I go for a bit of a swim, relaxing in the sauna afterwards."
        $ cash -= prices['swimminghall']
        $ fitness += fitness_bonuses['swimminghall']
        $ stress += stress_modifiers['swimminghall']
    else:
        "Drat. I don't have enough bits to go swimming."
        "Wonder if I could sneak in...?"
        "Nah."
        
    
    return
    
label gym:
    # Choose an exercise
    
    $ i = renpy.random.random()
    
    if cash < prices['gym']:
        "It seems my wallet doesn't have enough bits to go to the gym right now."
        return
    
    $ cash -= prices['gym']
    $ stress += stress_modifiers['gym']
    
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
        
    $ fitness += fitness_bonuses['gym']
    
    return
    
label runningtrack:
    # Running
    "I run the lap a few times."
    
    $ fitness += fitness_bonuses['runningtrack']
    $ stress += stress_modifiers['runningtrack']
    
    return
    
label mall:
    # Buy random items
    
    $ price = NonUniformRandom( [ ("mall_expensive", 2), ("mall_medium", 4), ("mall_cheap", 4) ] ).pick()
    
    if prices["mall_cheap"] > cash:
        "I flit around the mall, but I don't have enough money to buy anything."
        return
        
    if prices[price] > cash:
        $ price = "mall_cheap"
        
    if price == "mall_expensive":
        $ item = renpy.random.choice(["new GPUs", "deluxe GoT figures", "really expensive tea"])
    elif price == "mall_medium":
        $ item = renpy.random.choice(["calculators", "headphones", "T-shirts with cool logos"])
    else:
        $ item = renpy.random.choice(["fast food", "Dr. Pepper", "coffee beans"])
    
    $ i = renpy.random.random()
    if i < 0.5:
        "I flit around the mall, buying some [item]."
        call pay(prices[price])
        $ stress += stress_modifiers[price]
    elif i < 0.65:
        "I wander all around the shopping center, but find nothing of interest."
    elif i < 0.75:
        "There's some sort of event in the center of the mall. They're advertising [item]."
    elif i < 0.85:
        "I find some good sales on [item] at the mall."
        call pay(prices[price]/2)
        $ stress += 2*stress_modifiers[price]
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
    
    $ stress += stress_modifiers['library']
    
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
    "Aside from providing access to rare antique titles, most libraries have become sorts of community makerspaces, with high-quality 3D-printers and loads of other tools."
    "If you need a customized item or part on the spot, the library is your place to go."
    
    return
    
label workintro:
    "I work at a rental cleaning service."
    "Ironically, cleaning is one of the jobs that the robots haven't taken yet."
    "I mean, of course everybody including us is using vacuuming bots and the like."
    "But picking up the litter, cleaning the tables, all these things are still usually done by humans."
    "Well, that's lucky for me. It's the most boring job in the world, but it's not too difficult and the pay is enough to live with."
    "It's [work_payment] bits per working day, paid every Monday."
    
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
    
# Other scenes

label DFOServers:
    scene servers
    $ work_counter += 1
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
