init:
    transform say_in:
        yanchor 0.0
        ypos 1.0
        ease 0.5 yalign 1.0

    transform hp_us_in(index):
        xanchor 1.0
        xpos 0.0
        pause 0.05*index
        ease 0.5 xalign 0.0
        
    transform hp_us_out:
        xanchor 0.0
        xpos 1.0
        pause 0.05
        ease 0.5 xalign 0.0

    transform hp_em_in:
        xanchor 0.0
        xpos 1.0
        ease 0.5 xalign 1.0