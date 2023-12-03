define speech.narrator = Character(" ", what_prefix = "{bt=3}{i}", what_suffix = "{/i}{/bt}")
define speech.thought = Character("   ", what_prefix = "{i}", what_suffix = "{/i}")
define speech.main = Character("[player_name]", who_prefix = "{color=#719AE8}", who_suffix = "{/color}")
define speech.alice = Character("{glitch=3}{color=#FF00FF}А{/color}{/glitch}{glitch=6}{color=#FF00FF}л{/color}{/glitch}{glitch=4}{color=#FF00FF}и{/color}{/glitch}{glitch=2}{color=#FF00FF}с{/color}{/glitch}{glitch=5}{color=#FF00FF}а{/color}{/glitch}")
define speech.vanya = Character("Сосед Ваня", who_prefix = "{color=#938260}", who_suffix = "{/color}")
define speech.egor = Character("Егор", who_prefix = "{color=#CF1000}", who_suffix = "{/color}")
define speech.kseniya = Character("Ксюша", who_prefix = "{color=#E7943E}", who_suffix = "{/color}")
define speech.valeriya = Character("Лера", who_prefix = "{color=#F0C641}", who_suffix = "{/color}")
define speech.viktoriya = Character("Вика", who_prefix = "{color=#F0C641}", who_suffix = "{/color}")
define speech.polina = Character("Полина", who_prefix = "{color=#CF1000}", who_suffix = "{/color}")
define speech.generic = Character("", who_prefix = "{color=#999999}", who_suffix = "{/color}")










screen portrait_main_undressed_normal(how):
    add "ch_main_undressed_normal.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_main_undressed_happy(how):
    add "ch_main_undressed_happy.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_main_undressed_surprised(how):
    add "ch_main_undressed_surprised.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_main_undressed_sad(how):
    add "ch_main_undressed_sad.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_main_dressed_normal(how):
    add "ch_main_dressed_normal.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_main_dressed_happy(how):
    add "ch_main_dressed_happy.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_main_dressed_surprised(how):
    add "ch_main_dressed_surprised.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_main_dressed_sad(how):
    add "ch_main_dressed_sad.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5



screen portrait_viktoriya_undressed_normal(how):
    add "ch_viktoriya_undressed_normal.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_viktoriya_undressed_happy(how):
    add "ch_viktoriya_undressed_happy.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_viktoriya_undressed_surprised(how):
    add "ch_viktoriya_undressed_surprised.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_viktoriya_undressed_sad(how):
    add "ch_viktoriya_undressed_sad.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_viktoriya_dressed_normal(how):
    add "ch_viktoriya_dressed_normal.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_viktoriya_dressed_happy(how):
    add "ch_viktoriya_dressed_happy.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_viktoriya_dressed_surprised(how):
    add "ch_viktoriya_dressed_surprised.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_viktoriya_dressed_sad(how):
    add "ch_viktoriya_dressed_sad.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5



screen portrait_kseniya_undressed_normal(how):
    add "ch_kseniya_undressed_normal.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_kseniya_undressed_happy(how):
    add "ch_kseniya_undressed_happy.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_kseniya_undressed_surprised(how):
    add "ch_kseniya_undressed_surprised.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_kseniya_undressed_sad(how):
    add "ch_kseniya_undressed_sad.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_kseniya_dressed_normal(how):
    add "ch_kseniya_dressed_normal.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_kseniya_dressed_happy(how):
    add "ch_kseniya_dressed_happy.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_kseniya_dressed_surprised(how):
    add "ch_kseniya_dressed_surprised.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_kseniya_dressed_sad(how):
    add "ch_kseniya_dressed_sad.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5



screen portrait_valeriya_undressed_normal(how):
    add "ch_valeriya_undressed_normal.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_valeriya_undressed_happy(how):
    add "ch_valeriya_undressed_happy.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_valeriya_undressed_surprised(how):
    add "ch_valeriya_undressed_surprised.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_valeriya_undressed_sad(how):
    add "ch_valeriya_undressed_sad.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_valeriya_dressed_normal(how):
    add "ch_valeriya_dressed_normal.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_valeriya_dressed_happy(how):
    add "ch_valeriya_dressed_happy.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_valeriya_dressed_surprised(how):
    add "ch_valeriya_dressed_surprised.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5
screen portrait_valeriya_dressed_sad(how):
    add "ch_valeriya_dressed_sad.png" xanchor .5 yanchor 1. ypos 1.05 at how
    zorder -5

















transform fade_in_out:
    on idle:
        ease .2 alpha 0.
    on hover:
        ease .2 alpha 1.

transform blur_out:
    blur 0.
    ease .3 blur 15.

transform blur_in:
    blur 15.
    ease .3 blur 0.

transform motion.move(start, delta = 0., period = 0.):
    xpos start
    ease period xpos (start + delta)

transform motion.shake(start, amplitude, period):
    linear period xpos start
    linear period xpos (start + amplitude)
    linear period xpos start
    linear period xpos (start - amplitude)
    repeat

transform motion.focus(start):
    ypos 1.05 xpos start
    linear .2 ypos 1.    

transform motion.unfocus(start):
    ypos 1. xpos start
    linear .2 ypos 1.05    