# The Dating Sim Engine was written by PyTom,
# with updates added by Andrea Landaker.
#
# For support, see the Lemma Soft forums thread:
# http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=31571
#
# It is released under the MIT License - see DSE-LICENSE.txt
#
#
# This is the main program. This can be changed quite a bit to
# customize it for your program... But remember what you do, so you
# can integrate with a new version of DSE when it comes out.

# Set up a default schedule.
init python:
    crt = ImageDissolve("images/crt.png", 0.5, 0)
    #register_stat("Strength", "strength", 10, 100)
    #register_stat("Intelligence", "intelligence", 10, 100)
    register_stat("Fitness", "fitness", 50, 100)
    register_stat("Stress", "stress", 3, 10)
    register_stat("Bits", "cash", 24126, 999999)

    #dp_period("Morning", "morning_act")
    #dp_choice("Attend Class", "class")
    #dp_choice("Cut Class", "cut")

    # This is an example of an event that should only show up under special circumstances
    #dp_choice("Fly to the Moon", "fly", show="strength >= 100 and intelligence >= 100")

    dp_period("Morning", "morning_act")
    dp_choice("Swimming hall", "swimming")
    dp_choice("Gym", "gym", show="day == 3")
    dp_choice("Running track", "track")
    dp_choice("Call Catherine", "callcat")

    dp_period("Afternoon", "afternoon_act")
    #dp_choice("Study", "study")
    #dp_choice("Hang Out", "hang")
    dp_choice("Ice Cream Parlor", "parlor")
    dp_choice("Restaurant", "restaurant")
    #dp_choice("Bowling", "bowling")
    dp_choice("Mall", "mall")
    dp_choice("Library", "library")
    dp_choice("Work", "work")
    dp_choice("Business school", "business")

    dp_period("Evening", "evening_act")
    #dp_choice("Exercise", "exercise")
    #dp_choice("Play Games", "play")
    dp_choice("Bar", "bar")
    dp_choice("Movie theatre", "movies")
    dp_choice("VR Arcade", "arcade")
    dp_choice("Clean room", "clean")
    dp_choice("Catherine's apartment", "cathouse")
    
    # PROMISE SYSTEM
    
    promises = {}
    forgotten_promises = set()
    unkept_promises_personal_counter = {}
    # Promises are stored in a dictionary mapping (act, day) -tuples to [person, activity, boolean]-lists indicating 
    # the person the promise was made to, the promise itself, and whether the promise is
    # fulfilled (True), or not (False). The label night checks whether the promises for that day have been fulfilled and
    # gives a warning if they haven't. There're special date events linked to promises.
    
    # CASH SYSTEM
    def paycash(amount):
        if amount > cash:
            return False
        cash -= amount
        return True
        
    # WORK SYSTEM
    work_counter = 6
    work_payment = 1500
    # At the start of each week, you get work_payment bits for each day you've worked during the last week
    
    # AFFECTION AND TRUST
    max_affection = 10
    max_trust = 10
    affection = {'Catherine': 5, 'Silvia': 5}
    trust = {'Catherine': 5, 'Silvia': 5}
    
    def affection_modify(person, amount):
        affection[person] = affection[person] + amount
        if affection[person] > max_affection:
            affection[person] = max_affection
        if affection[person] < 0:
            affection[person] = 0
        return
            
    def trust_modify(person, amount):
        trust[person] = trust[person] + amount
        if trust[person] > max_trust:
            trust[person] = max_trust
        if trust[person] < 0:
            trust[person] = 0
        return
        

# Define characters
define a = Character("Aerith")
define n = Character("Nicholas")
define s = Character("Silvia")
define c = Character("Catherine")
define nvlNarrator = Character(None, kind=nvl)

label pay(amount):
    $ pay_successful = paycash(amount)
    if pay_successful:
        "I validate the transaction with my wristband."
    else:
        "As I'm about to pay, my wristband flashes a red light with the message: 'Transaction rejected. Bitcoin wallet balance exceeded.'"
    return
    
label check_wallet:
    "I covertly check my bitcoin wallet."
    "It seems I've got [cash] bits."
    return

# This is the entry point into the game.
label start:

    # Initialize the default values of some of the variables used in
    # the game.
    $ day = 0

    $ blade_sphere_control = False
    $ Aerith_angry = False
    $ Aerith_hurt = False
    $ Aerith_barrier = False
    $ curing_light = False
    
    # Show a default background.
    scene forest

    # The script here is run before any event.

    # Battle music
    play music "bgm/Battle1.wav"

    n "Damnit!"

    # Sound effect

    "The monster sinks its fangs into my skin, drawing blood!"

    # Screen shake & sound

    "I can feel the warm liquid trickling down my skin... Damnit!"

    "With a huge throwing motion, I manage to shed the weasel, but others are already circling around me."

    "They're huge. But I'm not actually worried. Not yet, anyway."

    "I see Aerith in the corner of my vision."

    "She's surrounded by the creatures as well, trying to keep them away
    with her staff."

    "Um, shouldn't you just cast a spell or something?"

    "Silvia is nowhere to be seen. Hiding somewhere in plain sight, no doubt."

    "The weasels are circling me, staring at my wound with blood-hungry eyes."

    menu:
        "Okay, let's go!"
        "Fight!":
            jump WeaselFight
        "Protect Aerith!":
            # You pull the weasels to Aerith
            jump WeaselPull
        "Time to retreat!":
            jump WeaselRetreat

    # We jump to day to start the first day.
    # jump day

label WeaselPull:
    "Trampling the weasels around me, I run to protect Aerith!"
    "Damn, they're following me! Of course this would happen!"
    "Now all of them are focused on us. Aerith is holding her hands to her mouth, gasping for air."
    jump WeaselProtectAerith

label WeaselFight:
    # Silvia uses hail of daggers

    "I'll just have to beat them off!"

    "I slash at the pack with my sword!"

    "The weasels screech in pain, flying off in a torrent of blood!"

    "But there's too many of them! No matter how many times I attack, more are lashing right at me!"

    s "Protect yourself."

    "I hear Silvia's voice from somewhere nearby, and instantly understand."

    "I raise my shield just in time as a hail of daggers falls all around me, piercing the weasels and spraying
    blood everywhere!"

    "The monsters lie dead on the grass, painted crimson with blood."

    "I turn around to thank Silvia, but then I hear Aerith scream from behind."

    jump WeaselAerithScream

    return

label WeaselAerithScream:
    # You can run to Aerith, tell her to use the barrier spell, or tell Silvia to use her hail of daggers again

    "She's still surrounded by a pack of weasels, desperately pushing them off!"

    "Their gnawing at her health. She won't last at this rate!"

    menu:
        "Run to save her!":
            "I run through the pack to her side, seeking to protect her from harm!"
            jump WeaselProtectAerith
        "Tell her to cast her barrier spell":
            jump WeaselAerithBarrier
        "Tell Silvia to use the hail of daggers":
            jump WeaselSilviaHailOfDaggersAerithAlone

    return

label WeaselSilviaHailOfDaggersAerithAlone:
    n "Silvia! Finish them with a hail of daggers!"
    "Silvia smirks, hesitating a bit."
    s "You sure about that, liege?"
    "Then, her smile turns fiendish, and she shrugs."
    s "Here goes!"
    "She launches into the air and begins her technique."
    "The daggers rain upon the weasels, killing them instantly!"
    "Of course, they hit Aerith as well. I really should have realized that."
    "She falls on her knees, but seems to be alive for the moment."
    "In any case, the weasels are dealt with."
    $ Aerith_angry = True
    $ Aerith_hurt = True
    jump WeaselVictory

label WeaselAerithBarrier:
    n "Aerith! A barrier!"
    "Aerith's eyes flit from foe to foe in terror, but then she begins casting."
    a "Phopassus, protect thy faithful in a time of need. Light Barrier!"
    "I watch as a sphere of searing white light envelops Aerith."
    $ Aerith_barrier = True
    "The weasels can't get to her now. However, they are turning towards me instead!"
    menu:
        "Run to Aerith":
            "I run towards the pack, ready to protect Aerith!"
            jump WeaselProtectAerith
        "Better retreat!":
            # Barrier wears off
            jump WeaselRetreat

label WeaselProtectAerith:
    "The weasels are baring their fangs at us, and Silvia is nowhere to be seen."

    "Aerith is cowering behind me, trying to think of a spell to cast."

    if Aerith_barrier:
        "Her light barrier is still protecting her, but who knows how long it'll last."

    "Well, I'm a guardian, so I should be able to do this, right?"

    menu:
        "Offensive technique: Furious strike!":
            jump WeaselFuriousStrike
        "Protective technique: Blade Sphere Control!":
            jump WeaselBladeSphereControl
        "Aerith Spell: Depths of Slumber!":
            jump AerithDepthsOfSlumber
        "Silvia Technique: Hail of Daggers!":
            jump WeaselSilviaHailOfDaggers

    return

label WeaselBladeSphereControl:
    if Aerith_barrier:
        "Aerith's barrier is beginning to fade."
        $ Aerith_barrier = False

    "I close my eyes and focus to find the calm within."

    "Blade Sphere Control!"

    $ blade_sphere_control = True

    "I hold my blade in a protective stance, ready to block any attack, from any direction!"

    "The weasels are still scuttling around us, but they don't dare to approach."

    "It seems we have reached a standstill."

    menu:
        "Special Technique: Taunt":
            jump WeaselTaunt
        "Aerith Spell: Curing Light":
            jump WeaselAerithCuringLight
        "Aerith Spell: Depths of Slumber":
            jump AerithDepthsOfSlumber
        "Silvia Technique: Hail of Daggers":
            jump WeaselSilviaHailOfDaggers

    return

label WeaselSilviaHailOfDaggers:
    n "Silvia! Use your hail of daggers, now!"

    "Silvia doesn't need to be told twice."

    if blade_sphere_control:
        "As the flurry of thrown knifes falls upon us, I block each and every one coming towards me and Aerith!"
    else:
        "The blades fall upon us, a rain of scathing edges!"
        if curing_light:
            "But due to the healing, we manage to survive despite the wounds."
        else:
            "And we're hit! I can almost taste the pain!"
            "Damnit! I don't think I can move anymore!"
            if Aerith_barrier:
                "At least Aerith was saved by her barrier."
            else:
                "Still, it seems both of us remain alive."
                $ Aerith_hurt = True

    "The weasels aren't as lucky, and the blades pierce their hearts and throats."

    "Only a pitiful whimper is left of them now."

    jump WeaselVictory

label WeaselTaunt:
    "I can't help but smirk."

    "I happen to know a technique for situations exactly like this."

    n "What, you afraid or something? Here I thought I was fighting a pack of weasels..."

    n "... but turns out you're just a bunch of chickens!"

    "You'd think they couldn't understand me."

    "But this is a special guardian technique, passed down from ancient times through generations of invincible warriors!"

    "I'm almost laughing as I see the weasels seething with rage."

    "Suddenly, the entire pack pounces on us, claws flashing in the air!"

    "But they can't get through my perfect defense!"

    "My sword strikes each and every one of them, cutting of their heads and piercing their beating hearts!"

    jump WeaselVictory

label WeaselAerithCuringLight:
    n "Aerith! Cast Curing Light on us!"

    "Aerith seems flustered for a moment, then begins chanting the spell."

    a "Thou art the sun which giveth life and light to the creatures of the earth..."

    a "Lord Phopassus, lend us your power. Curing light!"

    "I feel the warm, green glow closing the wounds on my arms."

    "Freshly invigorated, we return our focus to the battle at hand."

    "The weasels are already getting ready to pounce. We have to react fast!"

    $ curing_light = True

    menu:
        "Offensive technique: Furious strike!":
            jump WeaselFuriousStrike
        "Silvia technique: Hail of Daggers!":
            jump WeaselSilviaHailOfDaggers

    return

label WeaselFuriousStrike:
    "Time to go on the offensive!"

    "I raise my blade above my head, preparing to unleash my technique."

    "But I am interrupted as one of the animals jumps right at me!"

    "Its fangs and claws tear into my arm!"

    if curing_light:
        "However, thanks to the healing, I barely feel it."
    else:
        "Aah, I'm not gonna survive for much longer at this rate!"

    "I shake it off my gauntlet, and prepare the technique again."

    n "Furious Strike!"

    "I slam the critter with my sword!"

    "The steel runs right through its torso, hitting the ground with unbelievable power!"

    "The earth trembles as a shockwave emanates from where the weasel was crushed."

    "The rest of the weasels flee in terror."

    jump WeaselVictory

label AerithDepthsOfSlumber:
    n "Aerith! Cast Depths of Slumber!"

    "Aerith blinks, then nods and begins casting the spell."

    "The weasels aren't about to let that happen!"

    "Three of them jump right at us!"

    if blade_sphere_control:
        # Success
        "I smirk. They're never getting through my perfect defense!"
        "A single swing deals with all of them. Meanwhile, Aerith finishes her spell."
        jump AerithDepthsOfSlumberSuccess
    else:
        "I manage to fend off two, but the remaining one catches Aerith by surprise."
        if Aerith_barrier:
            "Still protected by her barrier, she manages to finish the spell!"
            jump AerithDepthsOfSlumberSuccess
        else:
            "Her spell is interrupted as she grapples with the weasel."
            "The rest of the pack is already preparing to pounce. We need to act fast!"
            menu:
                "Offensive technique: Furious strike!":
                    jump WeaselFuriousStrike
                "Silvia technique: Hail of Daggers!":
                    jump WeaselSilviaHailOfDaggers
    return

label AerithDepthsOfSlumberSuccess:
    a "Gift them with a peaceful sleep!"
    a "Depths of Slumber!"
    "All around us, a glowing powder descends on the weasels, and they fall asleep one by one."
    "We retreat, and Silvia finishes them off with a flurry of daggers."
    "They shall trouble us no more."
    jump WeaselVictory

label WeaselRetreat:
    # Silvia appears in front of you: "Good thinking!"
    "I turn around to run!"
    "Out of nowhere, Silvia appears beside me with a teasing smile."
    s "Good thinking, liege! You're pulling all of them towards you."
    "Glancing behind, I see the whole pack on my tail!"
    "Heheh, this wasn't really my intention, but no way I'm admitting that..."
    "Silvia slips back into the shadows. From the corner of my eye, I see Aerith
    running from the pack behind me!"
    $ Aerith_angry = True
    if Aerith_barrier:
        "Damn! Her barrier must have worn off!"
        $ Aerith_barrier = False
    "I stop in my tracks, and she runs behind me."
    jump WeaselProtectAerith

label WeaselVictory:

    play music "bgm/fanfare.mp3"

    "Silvia emerges from her hiding place, and I walk to her."

    s "Whew! Nice workout, eh?"

    "She flashes a wide grin."

    s "Seeing all that blood really makes my stomach tickle!"

    if Aerith_hurt:
        "Aerith comes towards us, visibly hurt."
    else:
        "Aerith approaches as well."

    if Aerith_angry:
        a "What the hell were you doing!? I could have died!"
        "I touch the back of my neck, slightly embarrassed."
        n "I'm sorry, don't know what I was thinking, really."
        n "Don't take it too seriously. It's just a game, right?"
        n "You would just have revived at the cathedral's teleporter."
        "Aerith pouts, folding her arms."
        a "Don't you think I know that?"
    else:
        "Her earlier terror has been replaced by disgust."
        a "Aah, there's blood everywhere, even my robes are all red... Eek!"
        "She is startled by a weasel head, rolling on the ground."
        a "Why is this game so gory!?"
        n "Uh, you know you can turn it down in the settings, right?"
        a "Y-yes, of course I do. Which is why I'll do that now."
        s "Come on, the gore is the best part!"
        "Aerith gives her a mean look, but doesn't retort."
        n "Well, I just think it's good for realism."

    n "Anyway, thanks for grinding with me. I guess I'll call it a day."
    "We say our farewells, and I log off."
    scene black with crt
    "Taking off my headset, it takes a while for my eyes to adjust to the dim lighting of my room."
    jump RoomDescription
    return

label RoomDescription:
    play music "bgm/buzz.wav"
    nvlNarrator "Not that there's much to see, in any case."
    nvlNarrator "It's a small, dirty one-room apartment overlooked by a single, large window with eternally closed curtains."
    nvlNarrator "Not like there’s anything meaningful behind them anyway. Just the gray exterior of another apartment building."
    nvlNarrator "Why they even bothered making a window so large for such a dreadful view is beyond me."
    nvlNarrator "My eyes linger on the shadows of empty coke bottles and assorted trash littering the small, barely sun-lit floor space."
    nvlNarrator "I really should throw that pizza slice away."
    nvl clear
    nvlNarrator "The only thing of note here is the VR equipment, which has eaten all of my wages to date."
    nvlNarrator "I've got the full setup. Head-mounted display, omnidirectional treadmill, haptic feedback suit, everything I could buy."
    nvlNarrator "This project already started in middle school, when I got the Oculus Rift as a gift from my parents."
    nvlNarrator "Since then, I've been obsessively buying more and more amazing gadgets in search of ever-deepening immersion."
    nvlNarrator "And to top it all of, due to the weight of the HMD and the suit, and the exercise provided by the omnidirectional treadmill, I'm actually in great shape!"
    nvl clear
    nvlNarrator "Well, I have to be, to be able to use this for longer than an hour at a time."
    nvlNarrator "Most other people don't care about immersion as much as I do, so they just have a basic setup that they can use seated."
    nvlNarrator "Plebs."
    nvlNarrator "I detach the treadmill's harnest from my waist, proceeding to hop off."
    nvl clear
    play music "bgm/hope(Ver1.00).ogg"
    nvlNarrator "After the natural disorientation and nausea of entering the bleaker tonalities of reality has passed away, I place the HMD on the floor."
    nvlNarrator "The headset's brand new, with fresnel lens and dual 8k-screens providing a 210-degree field of view at 120 frames per second."
    nvlNarrator "In other words, virtually indistinguishable from reality. Though just try to run photorealistic graphics at those speeds!"
    nvlNarrator "Only the new line of GPUs Nvidia released last year is anywhere near capable of outputting those resolutions. I need eight of them just to run Dragonfire Online."
    nvl clear
    nvlNarrator "I start to take off the haptic feedback suit."
    nvlNarrator "This is the most annoying part of the process. It takes forever to set up and disassemble all the equipment."
    nvlNarrator "I've gotten rather skilled at it, though, getting down from about half an hour to just around ten minutes."
    nvlNarrator "At least the suit looks cool. Kind of like Batman in the 8k remaster of the Dark Knight."
    nvlNarrator "It uses electric feedback to generate haptic impressions all around your body. There's also a sort of reverse
    exoskeleton with electric motors to simulate the feeling of weight and pressure."
    nvl clear
    nvlNarrator "There's still some things I've been thinking of trying. It's possible to modify the suit to produce actually painful
    shocks."
    nvlNarrator "It's a bit dangerous, though. I saw a news story about a man who was found dead in his home. He had botched the modding,
    and his rig gave him a jolt of over 80 milliamperes. Instant cardiac arrest."
    nvlNarrator "I already have everything set up to try it out. I just need to gather the courage to do so."
    nvlNarrator "One of these days, for certain..."
    "Suddenly, my wristband vibrates to signal a call."
    "I read the name projected on my forearm."
    "Catherine." # Can this be colored red?
    "My heart skips a beat, and I hover my finger over the ignore button."
    "Then, I manage to get a hold of myself. Lifting my index finger to my ear, I pick up the call."
    n "Hi."
    "A cold, smooth voice responds from the other side. A woman I know all too well."
    c "Hello there, Nicky."
    n "It's been a while, huh."
    c "Indeed." # Change font?
    "Could this atmosphere get any more tense? Just get to the point already!"
    c "Have you had fun? With that little game of yours?"
    "She sounds more hurt than angry now."
    n "Listen, Cat, I've just been busy with work and..."
    c "That's a lie!" # Furious sprite
    "In my mind's eye, I see her face contort with rage."
    c "Just, please Nick, just don't lie to me."
    "There's an awkward silence as I stumble for words."
    c "Nick, we... we need to talk."
    n "Cat, I... I'm sorry. Look, let's go out sometime. We can go to that ice cream parlor you like."
    c "I... yes. That... let's do that."
    n "Let's meet there tomorrow afternoon, 2pm. It's on me."
    c "Thanks, Nicky. You're sweet... sometimes."
    "She hangs up, and I immediately begin to regret the recklessness of my promise."
    "I'm not getting pay until Monday, and my wallet's practically empty. If she wants something expensive..."
    "I sigh. What won't a man do for love?"
    $ promises[('parlor', 1)] = {("Catherine", "meet"): False}

    window hide
    pause 2
    nvl clear
    window show

    play music "bgm/wrong.wav"

    nvlNarrator "My dreams are uneasy that night."
    nvlNarrator "I am lying on the floor of my apartment."
    nvlNarrator "Catherine comes to me, laughing."
    nvlNarrator "She hates me. Hates me."
    nvlNarrator "There’s a knife in her hands now."
    nvlNarrator "I don’t love her enough."
    nvlNarrator "That’s Silvia’s dagger! Why do you have that?"
    nvlNarrator "Silvia appears from the shadows. She’s enraged."
    nvlNarrator "Cat stole her knife."
    nvlNarrator "Only she has the right to use it."
    nvlNarrator "It was her gift to me."
    nvlNarrator "She grabs the knife, and there’s a hail of daggers, and everything is red and Sil laughs and laughs and laughs and I wake up."

    nvl clear

    play music "bgm/hope(Ver1.00).ogg"

    nvlNarrator "My eyes blink open as the timed lights in my room reach their brightest setting."
    nvlNarrator "For a moment, I just lie in bed, doing my most to calm down."
    nvlNarrator "It was just a dream. Just a dream."
    nvlNarrator "I can’t even remember what happened in it. Can’t remember."
    nvlNarrator "Something about Cat or Dragonfire Online or something. I’d better just forget it."
    nvl clear
    nvlNarrator "Rising from the bed, I feel the pangs of oncoming headache as my earlier promise re-emerges into my consciousness."
    nvlNarrator "I sigh yet again. I’m not sure I’m ready to face Cat in this state."
    nvlNarrator "I’m tempted to just boot up Dragonfire Online and play ‘til evening."
    nvlNarrator "But I can’t do that. I’m a man of my word."
    nvlNarrator "At least, I hope to be."
    nvlNarrator "I wouldn’t break a promise if it got me killed!"
    nvl clear
    nvlNarrator "My stomach growls as I stretch my arms far towards the ceiling, careful not to hit the lamp."
    nvlNarrator "Time to make some breakfast, I guess. And then, a plan for the day."
    jump day

label parlorStart:
    show parlor with dissolve
    $ cat_mood = 0
    $ ice_cream = None
    "Queens Gelateria is a mixed Italian-American -style ice cream parlor close to the center."
    "The place is surprisingly full even though it's already February."
    "I mean, summer's basically over, right?"
    "It's only 21 degrees Celsius outside. You almost need a jacket."
    "We used to come to this place often with Catherine."
    "She can't get enough of the ice cream here."
    "It is good, I'll admit. But also ridiculously expensive."
    "I suppose being right across from the stock exchange guarantees rich customers."
    "Today she's not as elated as usual. Something's on her mind."
    "Well, I guess it's obvious what."
    c "Which one should I choose...?"
    "How about the cheapest one on the menu?"
    "No way I'm saying that out loud though."
    c "I can't decide..."
    "I make a small smirk."
    n "Just close your eyes and I'll decide for you."
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
    "The numbers are projected on my wrist. I've got 24 000 bits, just barely enough for the most expensive one, should I decide to go with that."
    "Well, which should I take?"
    menu:
        "The expensive one":
            "Well, at least I won't go hungry with this choice."
            $ ice_cream = "expensive"
            $ paycash(24000)
        "The cheap one":
            "Sorry, Cat. I just don't have the money."
            $ ice_cream = "cheap"
            $ paycash(6000)
        "Her favorite":
            "She might not admit it, but I'm sure she'll be happy."
            $ ice_cream = "favorite"
            $ paycash(12000)
    n "I'll have this one."
    cashier "Excellent choice, sir. Will you be eating here?"
    n "Yes."
    cashier "I'll bring it to your table."
    "I press my finger on the reader to validate the transaction, and we go sit at a fancy table in the corner. No sense going outside when it's so cold."
    jump parlorConversation

label parlorConversation:
    "There's a bit of an awkward silence as we sit down. Cat is staring at the table, avoiding eye contact."
    "She's fiddling with a napkin, deliberating something, but can't get the words out."
    $ parlorwait = False
    $ parlorapology = False
    $ parloridle = False
    menu:
        "Wait for her to say something":
            jump parlorWait
        "Try to make conversation":
            jump parlorIdle
        "Apologize":
            jump parlorApology

label parlorApology:
    $ parlorapology = True
    n "Look, Cat, I'm sorry for not calling you for a while. I've been really busy."
    "She squeezes the napkin with her hands."
    c "Busy with Dragonfire Online, that is."
    "I'm surprised she remembered the name. She's not much of a gamer."
    n "T-that too. I mean, you know me, right?"
    c "Sometimes, Nicholas, I think I know you too well."
    "I swallow. She's not going to..."
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
    $ cat_mood += 1
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

    if cat_mood < 0:
        "She doesn't take that too kindly."
        c "Yeah, just like last time!"
        "She gets up and storms out, leaving her half-eaten ice cream behind."
        $ affection_modify('Catherine', -2)
    else:
        "She seems a bit sad."
        c "I guess I just have to believe you. Again."
    return

label promiseMovies:
    n "I'll take you to the movies."

    if cat_mood < 0:
        "She purses her lips."
    else:
        "She flashes a sad smile."

    c "Which one?"
    n "Erm, whatever you'd like?"
    c "Lover's Abandon."
    "Darn, that's some boring chick flick."
    n "Ahaha, sounds great!"
    $ affection_modify('Catherine', +2)
    return

label offerDFO:
    n "Cat, I'm a gamer. If you really want to spend time with me..."
    "She raises an eyebrow."
    n "... Let's play some DFO together! What do you say?"

    if cat_mood < 0:
        "Her expression alternates between anger and frustration."
        c "What makes you think I'd be interested in that stupid game?"
    else:
        "She looks away from me. I guess that's a no."
        c "I'm willing to accept that you like the game. But..."

    c "You really need to return to reality, Nicholas. You get too easily obsessed with these things."
    n "Come on, just try it out. I never expected to actually like your dance lessons when you dragged me there!"
    c "... You just don't get it."
    return

label parlorIdle:
    "I try to force a smile."
    n "You curious about the ice cream I ordered?"
    "She clenches her teeth."
    c "Not particularly."
    "Darn, she's really upset, isn't she?"
    jump parlorConsole

label parlorConsole:
    $ parloridle = True
    n "Kittie..."
    $ cat_mood -= 1
    "She slams her fist on the table."
    c "Don't call me that! First you disappear for two weeks, then I call you and you act as if nothing has happened!"

    menu:
        "Get angry":
            n "It's because you're such a psycho!"
            "Catherine's eyes widen in shock, and I immediately regret saying that."
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
    c "Nick, I'm only trying to help you! Can't you see you're hurting yourself!?"
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

    if cat_mood < 0:
        "She blinks, her eyes wet with tears."
        "Without showing me any, she gets up and leaves."
    else:
        "She licks on her spoon, but says nothing."
        "For what feels like an eternity, we just sit there, together yet separate."

    $ broken_up = True
    $ affection_modify('Catherine', -2)
        
    return

label parlorArgue:
    n "What you said about me not studying."
    n "I am going to study. I just need to decide what."
    n "I feel like most of the choices available are just pointless."
    n "If only reality was more like a game..."

    if cat_mood < 0:
        c "You're a fucking addict, you know that?"
        n "Gaming keeps me together! Why can't you get that!?"
        c "Whatever. Just keep playing your games. No need to call."
        "With that, she storms out."
        $ broken_up = True
        $ affection_modify('Catherine', -2)
    else:
        "She looks down at her ice cream."
        c "It wouldn't be any better."
        

        
    return

label parlorHypocrisy:
    n "You're critisizing me for not studying. But you're the one who's always complaining how stressful it is to not have time for anything else!"

    if cat_mood < 0:
        c "It's stressful now! But at least I won't be dying alone in some godforsaken apartment playing a stupid video game because I have no life!"
        c "Whatever. Just keep playing your games. No need to call."
        "With that, she storms out."
        $ broken_up = True
        $ affection_modify('Catherine', -2)
    else:
        c "It's stressful now. But at least I'll get a proper job."
        c "Nick, please just let me help you..."
        "She tries to look endearingly into my eyes, but I avoid her gaze."
        $ affection_modify('Catherine', 1)

    return

label parlorWait:
    $ parlorwait = True
    "After a little bit of silence, she speaks up."
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
    c "I wish I could believe that."
    $ cat_mood += 1
    "I blink so as to hide the tears. I want to just go under the table and cry."
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

    if cat_mood < 0:
        "Cat frowns."
        c "That's not the real problem. Even if you stop playing, you won't change."
        c "Just... Goodbye, Nick."
        "She gets up and leaves."
        $ broken_up = True
        $ affection_modify('Catherine', -2)
    else:
        "Catherine doesn't say anything."
        "Then, she closes her eyes."
        c "Fine, if you promise. Nicholas, this is for your own good."
        $ affection_modify('Catherine', 1)

    return

label parlorAccept:
    n "If you really want to leave me, I guess I just have to... accept it."
    "Cat sighs."

    if cat_mood < 0:
        c "Yes. Well then, goodbye, Nicholas."
        "With that, she gets up and goes out the door."
        $ broken_up = True
        $ affection_modify('Catherine', -2)
    else:
        c "I don't want to leave you. But things can't go on like this anymore."
        n "Can we try? Just a little bit longer?"
        c "One more time. Don't blow it."
    return

label parlorPlead:
    n "Please don't give up on me yet. We'll figure this out."
    "At first, just for a moment, she hesitates."

    if cat_mood < 0:
        c "I don't think so. This is it, Nicholas."
        "Before I have a chance to respond, she gets up and leaves."
        $ broken_up = True
        $ affection_modify('Catherine', -2)
    else:
        c "Fine. Let's try one last time."
        n "You don't realize how happy that makes me."
        "Contrary to my intentions, my comment just makes her sulk."
    return

label parlorInterrupt:
    "We're interrupted as the cashier comes to our table."

    if ice_cream == "cheap":
        # Strawberry-Chocolate mix
        cashier "One Strawberry-Chocolate mix."
        n "Thank you."

        if cat_mood < 0:
            c "That's what you got me? The cheapest one on the menu?"
            c "Is this some kind of joke?"
        else:
            "Catherine doesn't seem too impressed with the ice cream I got her."
            "Still, she sticks a spoon in it and begins eating."

        $ cat_mood -= 1

    elif ice_cream == "expensive":
        # Rockefeller parfait
        cashier "One Rockefeller parfait. Careful so it doesn't tip over."
        n "Thank you."

        if cat_mood < 0:
            "Catherine looks a bit surprised."
            c "Why'd you get such a big one? I can't eat that much!"
        else:
            "Catherine gasps."
            c "Nicholas, isn't that the most expensive thing on the menu? Why did you..."

        n "I thought we could eat it together."
        "Catherine says nothing, but seems placated, and we start eating."

        $ cat_mood += 1

    else:
        # Chocolate-Peanut butter sundae

        cashier "One Chocolate-Peanut butter sundae."
        n "Thank you."

        if cat_mood < 0:
            "Catherine doesn't look as happy as I had hoped."
            c "Oh, I get it. You saw that I hadn't exercised today..."
            c "... and bought that just to tease me!"
            c "Well, thanks a lot, Nick."
            "If more sarcasm was dripping from her voice, we would have a flood."
            $ cat_mood -= 1
        else:
            "Catherine seems to slightly cheer up as she sees what I bought her."
            c "Oh, thanks, Nick. That was thoughtful of you."
            $ cat_mood += 1

    n "A-anyway."
    return

# This is the label that is jumped to at the start of a day.
label day:

    # Increment the day it is.
    $ day += 1

    # We may also want to compute the name for the day here, but
    # right now we don't bother.

    "It's day %(day)d."
    
    if (day-1)%7 == 1:
        "I get paid [work_counter*work_payment] bits for last week's work."
        $ cash += work_counter*work_payment
        $ work_counter = 0

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available.

    $ morning_act = None
    $ afternoon_act = None
    $ evening_act = None
    $ narrator("What should I do today?", interact=False)

    # Now, we jump the day planner, which may set the act variables
    # to new values. We jump it with a list of periods that we want
    # to compute the values for.
    call screen image_planner("Morning")
    #(["Morning", "Afternoon", "Evening"])


    # We process each of the three periods of the day, in turn.
label morning:

    # Tell the user what period it is.
    centered "{size=+10}{color=#fff}Morning{/color}{/size}{w=1.0}{nw}"

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below.
    $ period = "morning"
    $ act = morning_act

    # Execute the events for the morning.
    call events_run_period
    call screen image_planner("Afternoon")

    # That's it for the morning, so we fall through to the
    # afternoon.

label afternoon:

    # It's possible that we will be skipping the afternoon, if one
    # of the events in the morning jumped to skip_next_period. If
    # so, we should skip the afternoon.
    if check_skip_period():
        jump evening

    # The rest of this is the same as for the morning.

    centered "{size=+10}{color=#fff}Afternoon{/color}{/size}{w=1.0}{nw}"

    $ period = "afternoon"
    $ act = afternoon_act

    call events_run_period
    call screen image_planner("Evening")


label evening:

    # The evening is the same as the afternoon.
    if check_skip_period():
        jump night

    centered "{size=+10}{color=#fff}Evening{/color}{/size}{w=1.0}{nw}"

    $ period = "evening"
    $ act = evening_act

    call events_run_period


label night:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    centered "{size=+10}{color=#fff}Night{/color}{/size}{w=1.0}{nw}"

    "It's getting late, so I decide to go to sleep."
    
    $ fitness -= 2
    
    python:
        forgotten_promises = set()
        for promise_event in promises.keys():
            if promise_event[1] == day:
                if not all(promises[promise_event].values()):
                    for promise in promises[promise_event].keys():
                        if not promises[promise_event][promise]:
                            # An unfulfilled promise today
                            forgotten_promises.add(promise[0])
                            if promise[0] in unkept_promises_personal_counter:
                                unkept_promises_personal_counter[promise[0]] += 1
                            else:
                                unkept_promises_personal_counter[promise[0]] = 1
                    
    if len(forgotten_promises) != 0:
        python:
            if len(forgotten_promises) == 1:
                forgotten_people = next(iter(forgotten_promises))
                promise_pluralized = "promise"
            else:
                list_forgotten = list(forgotten_promises)
                forgotten_people = ", ".join(list_forgotten[0:len(list_forgotten)-1]) + " and " + list_forgotten[-1]
                promise_pluralized = "promises"
        
        "Just as I'm going to sleep, I realize I forgot my [promise_pluralized] to [forgotten_people]."

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day


# This is a callback that is called by the day planner.
label dp_callback:

    # Add in a line of dialogue asking the question that's on
    # everybody's mind.
    $ narrator("What should I do today?", interact=False)

    return
