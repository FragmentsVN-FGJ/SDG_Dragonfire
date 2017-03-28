# This contains code for the day planner. You probably
# don't want to change this file.
#
# If you want to change the appearance of the day planner,
# look for the dp_ styles in styles.rpy


init -100 python:

    # The title of the done button.
    dp_done_title = "Done Planning"

    # A map from period name to the information we know about that
    # period.
    __periods = { }

    # The period we're updating.
    __period = None

    class __Period(object):

        def __init__(self, name, var):
            self.name = name
            self.var = var
            self.acts = [ ]

    def dp_period(name, var):
        __periods[name] = store.__period = __Period(name, var)

    __None = object()

    def dp_choice(name, value=__None, tooltip=__None, x=__None, y=__None, enable="True", show="True"):

        if not __period:
            raise Exception("Choices must be part of a defined period.")

        if value is __None:
            value = name

        if tooltip is __None:
            tooltip = name

        if x is __None:
            x = 0.15 + renpy.random.random() * 0.7

        if y is __None:
            y = 0.05 + renpy.random.random() * 0.9

        __period.acts.append((name, value, tooltip, x, y, enable, show))

    def __set_noncurried(var, value):
        setattr(store, var, value)
        return True

    __set = renpy.curry(__set_noncurried)


screen image_planner(period):
    $ this_period = __periods[period]
    $ renpy.choice_for_skipping()
    window:
        style "dayplanner_window"
        #background "images/fullmap.png"
        use display_stats(True, True, True, True)
        style_group "dp_choice"
        for name, curr_val, tooltip, x, y, enable, should_show in this_period.acts:
            $ show_this = eval(should_show)
            $ enable = eval(enable)

            #$ selected = (selected_choice == curr_val)

            if show_this:
                if enable:
                    #imagebutton auto "gui/main_start_%s.png" xpos 773 ypos y focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="images/tooltip"+var+".png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
                    if (curr_val, day) in promises.keys():
                        $ txtcolor = Color("#DC143C")
                        if promises[(curr_val, day)] == {('Catherine', 'meet'): False}:
                            $ tooltip = "I promised to meet Catherine here now."
                    else:
                        $ txtcolor = gui.text_color
                    textbutton name xpos x ypos y text_color txtcolor action [Hide("gui_tooltip"), SetField(store, this_period.var, curr_val), Return(curr_val)] hovered [ Show("gui_tooltip", my_tt_text=tooltip, my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
                    #textbutton name action SetField(store, this_period.var, curr_val)
                else:
                    textbutton name

screen gui_tooltip:
    frame:
        xpos my_tt_xpos ypos my_tt_ypos
        text my_tt_text
# Our Day Planner displays the stats, and buttons for the user to choose what to do
# during each period of time defined in "periods".
screen day_planner(periods):
    # indicate to Ren'Py engine that this is a choice point
    $ renpy.choice_for_skipping()
    window:
        style "dayplanner_window"
        use display_stats(True, True, True, True)
        use display_planner(periods)

screen display_planner(periods):
    frame:
        style_group "dp"
        vbox:
            text "Day Planner" yalign 0.0 xalign 0.5
            hbox:
                $ can_continue = True
                for p in periods:
                    vbox:
                        label p
                        if p not in __periods:
                            $ raise Exception("Period %r was never defined." % p)
                        $ this_period = __periods[p]
                        $ selected_choice = getattr(store, this_period.var)

                        $ valid_choice = False
                        vbox:
                            style_group "dp_choice"
                            for name, curr_val, enable, should_show in this_period.acts:
                                $ show_this = eval(should_show)
                                $ enable = eval(enable)

                                $ selected = (selected_choice == curr_val)

                                if show_this:
                                    if enable:
                                        textbutton name action SetField(store, this_period.var, curr_val)
                                    else:
                                        textbutton name

                                if show_this and enable and selected:
                                    $ valid_choice = True

                            if not valid_choice:
                                $ can_continue = False

            if (can_continue):
                textbutton dp_done_title style "dp_done_button" action Return()
            else:
                textbutton dp_done_title style "dp_done_button"
