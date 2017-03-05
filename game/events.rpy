# Events for the day planner

init:
    $ broken_up = False # Implement this later
    
    # Simple events for the actions
    $ event("icecreamparlor", "act == 'parlor'", event.only(), priority=200)
    $ event("restaurant", "act == 'restaurant'", event.only(), priority=200)
    $ event("movietheatre", "act == 'movies'", event.only(), priority=200)
    $ event("vrarcade", "act == 'arcade'", event.only(), priority=200)
    $ event("bowling", "act == 'bowling'", event.only(), priority=200)
    $ event("bar", "act == 'bar'", event.only(), priority=200)
    $ event("swimminghall", "act == 'swimming'", event.only(), priority=200)
    $ event("gym", "act == 'gym'", event.only(), priority=200)
    $ event("runningtrack", "act == 'track'", event.only(), priority=200)
    $ event("mall", "act == 'mall'", event.only(), priority=200)
    $ event("library", "act == 'library'", event.only(), priority=200)
    $ event("work", "act == 'work'", event.only(), priority=200)
    $ event("clean", "act == 'clean'", event.only(), priority=200)
    $ event("business", "act == 'business'", event.only(), priority=200)
    
    $ event("icecreamparlorintro", "act == 'parlor'", event.only(), event.once())
    $ event("restaurantintro", "act == 'restaurant'", event.only(), event.once())
    $ event("movietheatreintro", "act == 'movies'", event.only(), event.once())
    $ event("vrarcadeintro", "act == 'arcade'", event.only(), event.once())
    $ event("bowlingintro", "act == 'bowling'", event.only(), event.once())
    $ event("barintro", "act == 'bar'", event.only(), event.once())
    $ event("swimminghallintro", "act == 'swimming'", event.only(), event.once())
    $ event("gymintro", "act == 'gym'", event.only(), event.once())
    $ event("runningtrackintro", "act == 'track'", event.only(), event.once())
    $ event("mallintro", "act == 'mall'", event.only(), event.once())
    $ event("libraryintro", "act == 'library'", event.only(), event.once())
    $ event("workintro", "act == 'work'", event.only(), event.once())
    $ event("cleanintro", "act == 'clean'", event.only(), event.once())
    $ event("businessintro", "act == 'business'", event.only(), event.once())
    
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
                
label business:
    "I wander around the hallways for a bit. Why did I even come here in the first place?"
    
    return
               
label work:
    "I clean up at some organization."
    
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
    
    $ game1 = NonUniformRandom([("Ghosts & Goblins", 1), ("BlazBlue",1), ("Metal Slug 2",1)])
    $ game2 = NonUniformRandom([("Mortal Kombat", 1), ("Street Fighter II", 1), ("Space Invaders", 1)])
    
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
    
    
# Intros    
    
    
label icecreamparlorintro:
    jump parlorStart
    
label restaurantintro:
    # Restaurant, choose something to eat.
    "The Wind Horse Tavern is located near the stalls of the local horse racing track."
    "I like it due to its pseudo-medieval atmosphere. Kind of reminds me of Dragonfire Online."
    "Taste is the one sense we still haven't cracked in virtual reality."
    "I guess no-one's really interested at the moment. Most people don't even have haptics."
    "Anyway."
    
    jump restaurant
    
    return
    
label movietheatreintro:
    # Movie theatre, choose a movie to go to
    "Despite virtual reality providing a generally more immersive experience, movie theaters still exist."
    "Basically everything is in 3D on huge IMAX screens."
    "But it still doesn't beat VR."
    "At least it's something you can do together with your friends."
    "Going alone like this doesn't make much sense, but what the heck."
    
    jump movietheatre
    
    return
    
label vrarcadeintro:
    # Arcade, choose a game to play
    "TechnoLazers is an arcade in the upper part of the city. It's not terribly popular anymore."
    "A couple years back, arcades made a huge comeback by providing affordable VR experiences to the general populace."
    "But now that you can get relatively high-quality virtual reality in the consumer price range, these renewed VR arcades are falling in popularity."
    "It's a shame. The place has a cool techno aesthetic."
    "There's also an arena for laser tag and robot wars."
    
    jump vrarcade
    
    return
   
label bowlingintro:
    # Bowling, pay for it
    "The bowling place looks about as you'd expect, dark lighting and music and all."
    jump bowling
    
    return
    
label barintro:
    # Bar, choose a drink
    "It's really more of a techno club than a bar, hidden away in the side streets. I've taken Cat here before, but she's not into the place."
    
    jump bar
    
    return
    
label swimminghallintro:
    # Leisure swimming vs. Exercise
    "This is a secluded, relatively unpopular swimming hall mostly frequented by the elderly."
    "No-one comes here because of the labyrinthine architecture."
    "I swear, I get lost in the hallways every time I decide to visit."
    "Personally, I just come here for the steam sauna."
    
    jump swimminghall
    
    return
    
label gymintro:
    # Choose an exercise
    "This is the gym Catherine frequents. I think she has classes daily here."
    "It's mostly for CrossFit people, so I don't come here that often."
    "Frankly, I find these muscular CrossFit guys a bit intimidating. Even though I'm in good shape myself."
    "Aside from the usual barbells and rowing machines, they have a colossal fighting robot to spar with."
    "I think that's for the Muay Thai practicioners that also come here."
    
    jump gym
            
    return
    
label runningtrackintro:
    # Running
    "The local running track. Not much to see here, though I know Cat comes here every now and then as a part of her workout schedule."
    
    jump runningtrack
    
    return
    
label mallintro:
    # Buy random items
    "The biggest shopping mall in town, right in the center. I've never really liked the crowds."
    
    jump mall
    
    return
    
label libraryintro:
    # Choose a subject to read about
    
    "You'd think libraries would be a thing of the past in an era where every book ever made is easily available on the internet."
    "But you would be wrong. Libraries are still going strong."
    "Aside from providing access to rare antique titles, most libraries have become sorts of community makerspaces, with high-quality
    3D-printers and loads of other tools."
    "If you need a customized item or part on the spot, the library is your place to go."
    
    jump library
    
    return
    
label workintro:
    "I work at a rental cleaning service."
    "Ironically, cleaning is one of the jobs that the robots haven't taken yet."
    "I mean, of course everybody including us is using vacuuming bots and the like."
    "But picking up the litter, cleaning the tables, all these things are still usually done by humans."
    "Well, that's lucky for me. It's the most boring job in the world, but it's not too difficult and the pay is enough to live with."
    
    jump work
    
    return
    
label cleanintro:
    "Considering my line of work, it's ironic that my room is so cluttered."
    "I guess a shoemaker's children really do go barefoot."
    "Normally I'm too exhausted from work to do any cleaning at my own place."
    "But I suppose I should keep it in some shape at least. Wouldn't want to get dust in all those components!"

    jump clean
    
    return
    
label businessintro:
    "This is the business school Catherine goes to. Ridiculously high class."
    "Well, someone with her natural abilities deserves only the best, I guess."
    "It's kinda depressing. I could never make it here."
    "Despite the pressure Cat and my parents put on me."
    
    jump business
    return