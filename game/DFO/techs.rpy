label CuringLight(caster, target):
    $ gamestate.players[target].mp -= mp_costs['Curing Light']
    $ gamestate.players[target].hp += heal_amount['Curing Light']
    if gamestate.players[target].hp > gamestate.players[target].max_hp:
        $ gamestate.players[target].hp = gamestate.players[target].max_hp

    if target == "Nick":
        "The green light fills me with strength."
    else:
        $ i = renpy.random.randint(1, 3)
        if i == 1:
            "Green light closes [target]'s wounds."
        elif i == 2:
            "Green light flows over [target], closing her wounds."
        else:
            "In a flash of green light, [target]'s wounds are healed."
    return

label LightBarrier(caster, target = "Aerith"):
    $ gamestate.players[target].mp -= mp_costs["Light Barrier"]
    a "Luxphoros, protect thy faithful in a time of need. Light Barrier!"
    $ duration = renpy.random.randint(2, 4)
    $ light_barrier_active[target] = duration

    $ description1 = renpy.random.choice(["I'm momentarily blinded as", "I watch as"])
    $ light_descriptor = renpy.random.choice(["blinding ", "searing ", "bright ", ""])
    $ envelops = renpy.random.choice(["envelops", "closes around"])
    if target == "Nick":
        $ target = "me"
    show white with dissolve
    hide white with dissolve
    "[description1] a sphere of [light_descriptor]white light [envelops] [target]!"
    # Aerith is enveloped by bright white light as she finishes her spell.
    return

label usetechnique(caster, technique_name, target = "Nick"):
    $ tech_fail = False
    if mp_costs[technique_name] > gamestate.players[target].mp:
        $ tech_fail = True
    # Potential interrupt here.
    if tech_fail:
        call expression idtolabel[technique_name]+".start("+caster+", "+target+")"
        call expression idtolabel[technique_name]+".fail("+caster+", "+target+")"
        return
    $ gamestate.players[target].mp -= mp_costs[technique_name]
    $ i = renpy.random.random()
    if i <= 0.5:
        call expression idtolabel[technique_name]+".start("+caster+", "+target+")"
        call expression idtolabel[technique_name]+".fail("+caster+", "+target+")"
    else:
        call expression idtolabel[technique_name]+".start_and_finish("+caster+", "+target+")"
    call expression idtolabel[technique_name]+".effect("+target+")"
    return
