image white = Color("#fff")

define girl = Character("Girl", color="#FF1493", ctc="blinking_arrow")

label dream_start:

    scene street_background_01
    play music "bgm/bensound-littleidea.mp3"

    "Nooooo!!"
    with vpunch
    "I run on the streets, chewing on a piece of toast while panting heavily!"
    "I'm late for school again."
    "Why does this happen every damn morning!!?"
    "CRASH!"
    with vpunch
    with hpunch
    "Not looking where I'm going, I accidentally stumble on something in front of me."
    girl "Ouch! Watch where you're going!"
    "The force of our collision crashes us both to the ground."
    "She's actually pretty cute..."
    "That was my first thought. It takes me a while to realize where my hand is."
    girl "What the... get your hands off meee!!"
    "I get up as fast as I can. Then I remember what I was doing."
    "I've got no time for this! I have to run!"
    n "Sorry!"
    "I shout to the girl and run ahead, leaving her far behind."
    
    scene another_school_building_day with dissolve
    
    "Not really gentlemanly behaviour, but I am in a hurry."
    
    scene classroom_01_day with dissolve
    
    "I make it to the class just in time, trying to hide my exhaustion as I fall on my seat."
    with vpunch
    "I wouldn't hurry so much if the punishments in this school weren't so severe."
    "There's all sorts of rumors going around, like they torture kids in the basement or something. It's really quite horrible."
    "I try not to think about it. Instead, my thoughts drift to the girl I saw."
    "I wonder who she was. She looked about my age, but I've never seen her before."
    "If this was a high school anime, she would probably be a mysterious transfer student."
    "She'd come to class and hate me, but in the end she couldn't resist my manly charm. She'd have to join my harem!"
    "Ha ha ha! No need to fight over me, girls! Get in queue and wait for your turns!"
    "......."
    "My thoughts get a bit weird sometimes."
    "Something at the periphery of my consciousness snaps me out of my daze."
    "It's the girl from before. It looks like she just entered."
    girl "Sorry for being late."
    "The teacher introduces her. She's a new transfer student."
    "She walks to an empty seat nearby."
    "Then she notices me."
    "For a few seconds, I can see her eyes widen with surprise."
    "She looks away and walks to her seat, a little behind me."
    "Class goes on, but I can't shake the feeling that she's staring at me."
    "I try to covertly look behind to confirm my suspicions."
    "I freeze. She has noticed me."
    "She shoots me an icy glare that sends shivers down my spine."
    "She really hates me, huh..."
    "......."
    
    scene library with dissolve
    
    "In the evening, I decide to go to the library to do some studying."
    "I've got nothing better to do, and I'm trying to keep my grades up."
    "I find a place to sit, take out my books and begin reading."
    "But my attention quickly starts to wander... Oh!"
    "I glance at the person sitting in a nearby chair."
    "It's this cute girl I often see at the library."
    "She's always so focused on her textbooks. It's really quite inspiring."
    "I don't think I can achieve that level of focus anymore. Social media has changed me."
    "I kind of want to go talk to her, but I can never muster the courage to do it."
    "See, this is why I'll never get a girlfriend... Sigh."
    scene room_night with dissolve
    "......."
    "I crash to bed, exhausted despite doing nothing physical."
    "These pillows are so feathery..."
    "Feathers..."
    stop music
    scene black with Dissolve(3.0)
    "Zzz... Zzz..."
    "It's so hot in here. Why is it so hot in here?"
    play music "bgm/fire.wav"
    "Smoke. Fire."
    
    scene school_corridor with wipeup
    
    "The school is on fire!"
    "I need to get out of here!"
    "I run and run, but the hallways twist and turn in ways I can't understand."
    
    scene classroom_01_evening with dissolve
    
    "Why is our classroom here? I'm pretty sure it's not supposed to be here..."
    "The door is wide open. And inside, I see the transfer student."
    "In contrast to her usually tough persona, she's crying and cowering."
    "She's holding her ankle."
    "She notices me and cries out."
    "Transfer student" "Please! Help! I... I can't walk!"
    "I'm just about to go help her as I hear a loud crash and a scream!"
    with vpunch
    with hpunch
    scene school_corridor with wipeleft
    "It's the girl from the library! A bookcase fell, and she's trapped underneath!"
    "Library girl" "Help..."
    "The flames are already catching up to me. I can't save both of them!"
    menu:
        "Save the transfer student":
            jump transfer_student
        "Save the library girl":
            jump library_girl

label next_morning:
        
    "Luckily she seems to be mostly alright. But I don't think she's in any condition to walk right now."
    "I carry her on my back and crawl out of the school."
    "The sun is really bright..."
    
    scene white with dissolve
    
    "So bright... Huh?"
    scene room_night with dissolve
    "I blink awake as the sunlight reaches my eyes."
    "What was I even dreaming about? Can't remember..."
    "More importantly, why is it so warm in here?"
    "I'm sweating all over!"
    "Did mom forget to turn on the air conditioning again?"
    "I get up, put on my clothes, and walk downstairs to make some breakfast."
    "It's not even that late. I won't have to run to school today."
    "Dad walks into the room."
    "Dad" "Good morning, Nick!"
    "He glances at the clock, then at his phone."
    "Dad" "Oh, the clock's about a half an hour late. Better fix that."
    "Wait, what?"
    "Crap."
    
    scene street_background_01 with dissolve
    
    "Why does this happen every single dayyy!!?"
    "At least I didn't crash into the transfer student this time..."

    return

label library_girl:

    "I walk over to the books and help the girl emerge from underneath."

    call next_morning
    
    scene library with dissolve
    
    "......."
    "At the library again."
    "This time, I decide to gather my courage."
    "She dropped her pen. Now's my chance!" # Darn you're awkward, Nick...
    n "Here!"
    "She blinks and blushes. Aaah, just the reaction I was waiting for!"
    girl "T-thanks."
    n "What are you reading, by the way?"
    girl "O-oh. This is just my economics homework."
    n "Wow, I didn't know you study economics."
    "Her eyes flash with determination."
    girl "I'm going to get an MBA."
    "I can hear a hint of passion in her voice."
    "I had no idea she was this determined!"
    "Her expression wavers."
    girl "Although I really can't understand this part about cryptocurrencies."
    n "Can you explain it to me?"
    girl "Not very well..."
    n "Often teaching is the best way to learn. Try!"
    girl "Um, okay, but this is going to take a while."
    n "That's okay, I'll just move my stuff over here."
    n "What's your name, by the way?"
    "She blushes."
    girl "Catherine."
    "I wake up in a state of torpor."
    "It's not morning yet, is it?"
    "The memories of my first proper meeting with Catherine linger in my head, sparking associations."
    
    scene black with Dissolve(2.0)
    
    "After that time we began to meet more often."
    "At first it was just to study. Catherine didn't like to come out of her shell very much."
    "But gradually she softened up to me, and started smiling more often."
    "We went to prom together and started dating."
    "Life was pretty sweet for me."
    "Turns out her parents were really rich too. I convinced her to buy an Oculus Rift even though she wasn't into gaming or anything."
    "I think she bought it just so I would come over more often."
    "Lots of things happened after that."
    "We graduated from high school. She got into a prestigious business school, while I tried to find work."
    "We didn't move together, since she didn't want to argue with her parents about me being her boyfriend."
    "Although I'm pretty sure they suspected it anyway."
    "We did move into the same city though, just a few blocks apart."
    "Her personality began to change. I guess that happens in five years."
    "She became a lot more assertive and business-minded."
    "And she started thinking a lot more about her appearance."
    "The glasses had to go, replaced by contact lenses."
    "And all that fitness stuff... she should just play some games in VR instead!"
    "Slowly, I drift back... to... sleep..."
    return
    
label transfer_student:
    
    "I decide to walk over to the transfer student."

    call next_morning
    
    scene street_background_01 with dissolve
    
    "I'm walking home after an uneventful day at school."
    
    "While walking, I notice that a new cafe has opened down the road."
    
    "Amazing! It's one of those maid cafes I've been hearing about!"

    "Should I? It's a bit embarrassing, to be honest..."
    
    "No! For the sake of cuteness, I must go!"
    
    "I go in and get a table. The girls here are all wearing cute maid outfits."
    
    "Transfer student" "Welcome, sir... Eeehh?"
    
    n "Wait, what? You're a maid here!?"
    "Our school is pretty small, and I'm probably the only one who would think of going to a cafe like this."
    "I see, so you thought you wouldn't be found out..."

    # Something about finding out where she works and extorting her over it
    girl "I only work here because my parents own the chain."
    n "Wow, your parents must be really rich!"
    girl "Kind of."
    girl "Hey! What's my family life to you anyway!?"
    
    girl "Don't you dare tell anyone that I work here!"
    girl "It would ruin my reputation!"
    "... What reputation is she referring to?"
    "Although if she wants to keep this a secret between the two of us, all the better for me!"
    
    n "Oh, don't worry, you're secret is safe with me..."
    "She looks relieved."
    girl "It's good that you know what's best for you."
    "I close one eye and smirk."
    n "Of course, it's going to cost ya."
    girl "WHAT!?"
    n "First, no more icy glares. That was ages ago, so just forget about it."
    "Her expression turns to a more controlled annoyance."
    girl "Done."
    n "Second, ever heard of the Oculus Rift?"
    girl "N-no?"
    n "What's your name, by the way?"
    girl "Don't tell me you don't know? Catherine."
    "I flash her my most devilish grin."
    n "Well, Catherine, I think this is the beginning of a beautiful friendship."
    return