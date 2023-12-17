define speech.narrator = Character(" ", what_prefix = "{bt=3}{i}", what_suffix = "{/i}{/bt}")
define speech.thought = Character("   ", what_prefix = "{i}", what_suffix = "{/i}")
define speech.main = Character("[player_name]", who_prefix = "{color=#719AE8}", who_suffix = "{/color}")
define speech.alice = Character("{glitch=3}{color=#FF00FF}А{/color}{/glitch}{glitch=6}{color=#FF00FF}л{/color}{/glitch}{glitch=4}{color=#FF00FF}и{/color}{/glitch}{glitch=2}{color=#FF00FF}с{/color}{/glitch}{glitch=5}{color=#FF00FF}а{/color}{/glitch}")
define speech.vanya = Character("Сосед Ваня", who_prefix = "{color=#938260}", who_suffix = "{/color}")
define speech.egor = Character("Егор", who_prefix = "{color=#CF1000}", who_suffix = "{/color}")
define speech.kseniya = Character("Ксюша", who_prefix = "{color=#E7943E}", who_suffix = "{/color}")
define speech.valeriya = Character("Лера", who_prefix = "{color=#9178C1}", who_suffix = "{/color}")
define speech.viktoriya = Character("Вика", who_prefix = "{color=#F0C641}", who_suffix = "{/color}")
define speech.polina = Character("Полина", who_prefix = "{color=#C57A9E}", who_suffix = "{/color}")
define speech.polina_hidden = Character("8-922-xxx-xx-00", who_prefix = "{color=#CF1000}", who_suffix = "{/color}")
define speech.generic = Character("", who_prefix = "{color=#999999}", who_suffix = "{/color}")










transform motion.robust(position, focused, appear):
    ease (0. if appear else .2) ypos (1. if focused else 1.05) zoom (1.05 if focused else 1.) xpos position

screen portrait_main(clothing, emotion, position, focused, appear):
    add "ch_main_[clothing]_[emotion].png" xanchor .5 yanchor 1. at motion.robust(position, focused, appear)
    zorder -5

screen portrait_valeriya(clothing, emotion, position, focused, appear):
    add "ch_valeriya_[clothing]_[emotion].png" xanchor .5 yanchor 1. at motion.robust(position, focused, appear)
    zorder -5

screen portrait_viktoriya(clothing, emotion, position, focused, appear):
    add "ch_viktoriya_[clothing]_[emotion].png" xanchor .5 yanchor 1. at motion.robust(position, focused, appear)
    zorder -5

screen portrait_kseniya(clothing, emotion, position, focused, appear):
    add "ch_kseniya_[clothing]_[emotion].png" xanchor .5 yanchor 1. at motion.robust(position, focused, appear)
    zorder -5

screen portrait_polina(clothing, emotion, position, focused, appear):
    add "ch_polina_[clothing]_[emotion].png" xanchor .5 yanchor 1. at motion.robust(position, focused, appear)
    zorder -5

screen portrait_vanya(clothing, emotion, position, focused, appear):
    add "ch_vanya_[clothing]_[emotion].png" xanchor .5 yanchor 1. at motion.robust(position, focused, appear)
    zorder -5

init python:
    class portrait:
        def __init__(self, name):
            self.name = name
        def appear(self, clothing, emotion, position, focused): # можно добавить delay перед выполнением в transform
            self.clothing, self.emotion, self.position, self.focused = clothing, emotion, position, focused
            renpy.transition(usual_transition)
            renpy.show_screen(self.name, self.clothing, self.emotion, self.position, self.focused, True)
        def morph(self, clothing, emotion, position, focused):
            if clothing != None: self.clothing = clothing
            if emotion != None: self.emotion = emotion
            if position != None: self.position = position
            if focused != None: self.focused = focused
            renpy.show_screen(self.name, self.clothing, self.emotion, self.position, self.focused, False)
        def disappear(self):
            renpy.transition(usual_transition)
            renpy.hide_screen(self.name)

        main = valeriya = viktoriya = kseniya = polina = vanya = None
    portrait.main = portrait("portrait_main")
    portrait.valeriya = portrait("portrait_valeriya")
    portrait.viktoriya = portrait("portrait_viktoriya")
    portrait.kseniya = portrait("portrait_kseniya")
    portrait.polina = portrait("portrait_polina")
    portrait.vanya = portrait("portrait_vanya")











transform fade_in_out:
    on idle:
        ease .2 alpha 0.
    on hover:
        ease .2 alpha 1.

transform blur_out:
    xanchor .5 yanchor .5 xpos .5 ypos .5
    ease .3 blur 15. zoom 1.05

transform blur_in:
    xanchor .5 yanchor .5 xpos .5 ypos .5
    ease .3 blur 0. zoom 1.