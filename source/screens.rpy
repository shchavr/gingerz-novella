################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            showif False:
                textbutton _("Back") action Rollback()
            textbutton _("История") action ShowMenu('history')
            showif False:
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            showif False:
                textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Сохранить") action ShowMenu('save')
            textbutton _("Загрузить") action ShowMenu('load')
            textbutton _("Быстрое сохранение") action QuickSave()
            showif False:
                textbutton _("Q.Load") action QuickLoad()
            textbutton _("Настройки") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Начать игру") action Start()

        else:

            textbutton _("История") action ShowMenu("history")

            textbutton _("Сохранить") action ShowMenu("save")

        textbutton _("Загрузить") action ShowMenu("load")

        textbutton _("Настройки") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Главное меню") action MainMenu()

        textbutton _("Информация") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Управление") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Выйти") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

define slides = ["title.jpg",           "bg_alley_empty.jpg",       "bg_guk_sky.jpg",           "bg_cat_pillow.jpg",        "bg_rtf_coffeeshop.jpg",
                "bg_none_1.jpg",        "bg_viktoriya_mch.jpg",     "bg_zephyrka_selfie.jpg",   "bg_street_people.jpg",     "bg_none_2.jpg",
                "bg_cat_floor.jpg",     "bg_none_3.jpg",            "bg_cat_tigra.jpg",         "bg_egor_mch.jpg",          "bg_none_4.jpg",
                "bg_mch_cat.jpg",       "bg_bar.jpg",               "bg_rtf_parking.jpg",       "bg_history_teacher.jpg",   "bg_none_5.jpg"]
define slides_filt = ["filt_1.jpg",     "bg_rtf_entrance.jpg",  "bg_desks_students.jpg",    "bg_nine_sk.jpg",   "bg_street_people.jpg",     "bg_cat_pillow.jpg",    "bg_canteen_inside.jpg",
                            "bg_viktoriya_mch.jpg",     "filt_9.jpg",   "filt_10.jpg",  "bg_stepashka.jpg",     "bg_history_teacher.jpg"]
define slides_orig = ["orig_1.jpg",     "orig_2.jpg",           "orig_3.jpg",               "orig_4.jpg",       "orig_5.jpg",               "orig_6.jpg",           "orig_7.jpg",
                            "orig_8.jpg",               "orig_9.jpg",   "orig_10.jpg",  "orig_11.jpg",          "orig_12.jpg"]
define slides_text = ["{b}Главный учебный корпус УрФУ{/b}\nулица Мира, 19",
                        "{b}Институт радиотехники УрФУ{/b}\nулица Мира, 32",
                        "{b}Пара по истории России в “Радике”{/b}\nулица Мира, 32",
                        "{b}Общежитие №9{/b}\nулица Фонвизина, 8",
                        "{b}“Аллейка”{/b}\nперекрёсток Малышева—Мира",
                        "{b}Милашкинс из котокафе “Мяу”{/b}\nулица Чапаева, 17",
                        "{b}Столовая ГУКа{/b}\nулица Мира, 19",
                        "{b}А вот и главные герои{/b}\nулица Мира, 32",
                        "{b}Кажется, Ваня — не совсем Ваня{/b}\nулица Фонвизина, 8",
                        "{b}Пряники общаются-слипаются{/b}\nулица Мира, 32",
                        "{b}Андрей Викторович, пара физики{/b}\nулица Мира, 32",
                        "{b}Алексей Вячеславович, пара истории{/b}\nулица Мира, 32"]

define hold_slide = 5.
define hold_slide_alt = 7.
define fade_slide = .5
define crop_slide = 1.
define zoom_portion = 1.2

transform slide(index):
    xanchor .5 yanchor .5 xpos .5 ypos .5 subpixel True alpha 0. zoom (zoom_portion if index % 2 == 0 else 1.)
    linear index * hold_slide
    parallel:
        ease fade_slide alpha 1.
        linear hold_slide - fade_slide
    parallel:
        linear hold_slide zoom (1. if index % 2 == 0 else zoom_portion)
    parallel:
        linear hold_slide - fade_slide
        ease fade_slide alpha 0.
    linear (len(slides) - 1 - index) * hold_slide
    repeat

transform slide_zoom_n_fade(index):
    xanchor .5 yanchor .5 xpos .5 ypos .5 subpixel True alpha 0. zoom (zoom_portion if index % 2 == 0 else 1.)
    linear index * hold_slide_alt
    parallel:
        ease fade_slide alpha 1.
        linear hold_slide_alt - fade_slide
    parallel:
        linear hold_slide_alt zoom (1. if index % 2 == 0 else zoom_portion)
    parallel:
        linear hold_slide_alt - fade_slide
        ease fade_slide alpha 0.
    linear (len(slides_filt) - 1 - index) * hold_slide_alt
    repeat

transform slide_fade(index):
    alpha 0.
    linear index * hold_slide_alt
    parallel:
        ease fade_slide alpha 1.
        linear hold_slide_alt - fade_slide
    parallel:
        linear hold_slide_alt - fade_slide
        ease fade_slide alpha 0.
    linear (len(slides_filt) - 1 - index) * hold_slide_alt
    repeat

transform slide_orig(index):
    xanchor .5 yanchor .5 xpos .5 ypos .5 subpixel True alpha 0.
    linear index * hold_slide_alt
    linear fade_slide
    alpha 1.
    linear hold_slide_alt - fade_slide
    linear (len(slides_filt) - 1 - index) * hold_slide_alt
    repeat

transform slide_filt(index):
    xanchor 1. yanchor .5 xpos 1. ypos .5 subpixel True alpha 1. crop (0., 0., 1., 1.)
    linear index * hold_slide_alt
    parallel:
        linear hold_slide_alt - fade_slide
        alpha 0.
        linear fade_slide
    parallel:
        linear (hold_slide_alt - crop_slide) * .5
        ease crop_slide crop (1., 0., 0., 1.)
        linear (hold_slide_alt - crop_slide) * .5
    linear (len(slides_filt) - 1 - index) * hold_slide_alt
    repeat

transform spn:
    subpixel True rotate_pad True
    rotate 0.
    linear 1. rotate 360.
    repeat

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    showif not all(persistent.endings):
        add slides[0] at slide(0)
        add slides[1] at slide(1)
        add slides[2] at slide(2)
        add slides[3] at slide(3)
        add slides[4] at slide(4)
        add slides[5] at slide(5)
        add slides[6] at slide(6)
        add slides[7] at slide(7)
        add slides[8] at slide(8)
        add slides[9] at slide(9)
        add slides[10] at slide(10)
        add slides[11] at slide(11)
        add slides[12] at slide(12)
        add slides[13] at slide(13)
        add slides[14] at slide(14)
        add slides[15] at slide(15)
        add slides[16] at slide(16)
        add slides[17] at slide(17)
        add slides[18] at slide(18)
        add slides[19] at slide(19)
    showif all(persistent.endings):
        fixed at slide_zoom_n_fade(0):
            add slides_orig[0] at slide_orig(0)
            add slides_filt[0] at slide_filt(0)
        fixed at slide_zoom_n_fade(1):
            add slides_orig[1] at slide_orig(1)
            add slides_filt[1] at slide_filt(1)
        fixed at slide_zoom_n_fade(2):
            add slides_orig[2] at slide_orig(2)
            add slides_filt[2] at slide_filt(2)
        fixed at slide_zoom_n_fade(3):
            add slides_orig[3] at slide_orig(3)
            add slides_filt[3] at slide_filt(3)
        fixed at slide_zoom_n_fade(4):
            add slides_orig[4] at slide_orig(4)
            add slides_filt[4] at slide_filt(4)
        fixed at slide_zoom_n_fade(5):
            add slides_orig[5] at slide_orig(5)
            add slides_filt[5] at slide_filt(5)
        fixed at slide_zoom_n_fade(6):
            add slides_orig[6] at slide_orig(6)
            add slides_filt[6] at slide_filt(6)
        fixed at slide_zoom_n_fade(7):
            add slides_orig[7] at slide_orig(7)
            add slides_filt[7] at slide_filt(7)
        fixed at slide_zoom_n_fade(8):
            add slides_orig[8] at slide_orig(8)
            add slides_filt[8] at slide_filt(8)
        fixed at slide_zoom_n_fade(9):
            add slides_orig[9] at slide_orig(9)
            add slides_filt[9] at slide_filt(9)
        fixed at slide_zoom_n_fade(10):
            add slides_orig[10] at slide_orig(10)
            add slides_filt[10] at slide_filt(10)
        fixed at slide_zoom_n_fade(11):
            add slides_orig[11] at slide_orig(11)
            add slides_filt[11] at slide_filt(11)
        add "address.png"
        text "{color=[gui.accent_color]}{size=+10}[slides_text[0]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(0)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[1]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(1)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[2]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(2)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[3]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(3)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[4]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(4)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[5]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(5)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[6]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(6)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[7]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(7)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[8]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(8)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[9]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(9)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[10]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(10)
        text "{color=[gui.accent_color]}{size=+10}[slides_text[11]]{/color}{/size}" text_align 1. xanchor 1. yanchor 1. xpos .92 ypos .88 at slide_fade(11)
    add "title.png"

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    showif False:
        if gui.show_name:

            vbox:
                style "main_menu_vbox"

                text "[config.name!t]":
                    style "main_menu_title"

                text "[config.version]":
                    style "main_menu_version"

    vbox xpos .58 ypos .13 yanchor 0. xanchor 0.:
        spacing -54
        text "{color=[gui.accent_color]}{size=-4}                        от команды “Рекурсивные Пряники”{/size}{/color} "
        text "{color=[gui.accent_color]}{size=+120}{b}Gingers{/b}{/size}{/color}"
        showif any(persistent.endings):
            hbox yanchor -.65:
                text "{color=[gui.accent_color]}{size=-4} Открытые концовки:{/size}{/color}"
                spacing 115
                showif not all(persistent.endings):
                    hbox xfill True xsize .175:
                        spacing -50
                        showif persistent.endings[0]:
                            text "{color=[gui.accent_color]}★{/color}"
                        showif not persistent.endings[0]:
                            text "{color=[gui.accent_color]}☆{/color}"

                        showif persistent.endings[1]:
                            text "{color=[gui.accent_color]}★{/color}"
                        showif not persistent.endings[1]:
                            text "{color=[gui.accent_color]}☆{/color}"

                        showif persistent.endings[2]:
                            text "{color=[gui.accent_color]}★{/color}"
                        showif not persistent.endings[2]:
                            text "{color=[gui.accent_color]}☆{/color}"

                        showif persistent.endings[3]:
                            text "{color=[gui.accent_color]}★{/color}"
                        showif not persistent.endings[3]:
                            text "{color=[gui.accent_color]}☆{/color}"

                        showif persistent.endings[4]:
                            text "{color=[gui.accent_color]}★{/color}"
                        showif not persistent.endings[4]:
                            text "{color=[gui.accent_color]}☆{/color}"

                        showif persistent.endings[5]:
                            text "{color=[gui.accent_color]}★{/color}"
                        showif not persistent.endings[5]:
                            text "{color=[gui.accent_color]}☆{/color}"

                        showif persistent.endings[6]:
                            text "{color=[gui.accent_color]}★{/color}"
                        showif not persistent.endings[6]:
                            text "{color=[gui.accent_color]}☆{/color}"

                showif all(persistent.endings):
                    hbox xfill True xsize .175 xanchor .01 yanchor .15:
                        spacing -50
                        text "{color=[gui.accent_color]}★{/color}" at spn
                        text "{color=[gui.accent_color]}★{/color}" at spn
                        text "{color=[gui.accent_color]}★{/color}" at spn
                        text "{color=[gui.accent_color]}★{/color}" at spn
                        text "{color=[gui.accent_color]}★{/color}" at spn
                        text "{color=[gui.accent_color]}★{/color}" at spn
                        text "{color=[gui.accent_color]}★{/color}" at spn


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Назад"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Информация"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "{size=+10}[config.name!t] v1.0{/size}\n"

            text "{i}[gui.about!t]{/i}\n\n{size=-13}Игра сделана при помощи {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]. Программа распространяется по лицензии {a=https://ru.wikipedia.org/wiki/Лицензия_MIT}MIT{/a} как свободное программное обеспечение в целях обучения. Все права на изображения, звуковой и другой медиа-контент, принадлежат их настоящим правообладателям, не нарушаются и не присваиваются разработчиками. Совпадения с действительностью намерены, но так или иначе не подразумевают полное соответствие; иначе случайны. Руководствуйтесь здравым смыслом.{/size}" justify True
            
            text "\n“Рекурсивные Пряники”, УрФУ, Екатеринбург, Россия, 2023."


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Сохранить игру"))


screen load():

    tag menu

    use file_slots(_("Загрузить игру"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Пользовательские сохранения"), auto=_("Автоматические сохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("пусто")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    #textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}Авто") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Быстрые") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    #for page in range(1, 10):
                    textbutton "Пользовательские" action FilePage(1)

                    #textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

init -1 python:
    def dltprsstnt():
        for i in range(len(persistent.endings)):
            persistent.endings[i] = False
        for i in renpy.list_saved_games(regexp = '.', fast = True):
            renpy.unlink_save(i)
        config.main_menu_music = splashscreen_music_1
        renpy.play(config.main_menu_music, channel = "music")

screen preferences():

    tag menu

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        textbutton _("Стандартный") action Preference("display", "window")
                        textbutton _("Полноэкранный") action Preference("display", "fullscreen")

                showif False:
                    vbox:
                        style_prefix "check"
                        label _("Skip")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость печати текста")

                    bar value Preference("text speed")

                    showif False:
                        label _("Auto-Forward Time")

                        bar value Preference("auto-forward time")
                    
                    textbutton "\nУдалить прогресс" action Confirm("Вы потеряете сохранения, и пройденные концовки\n придётся проходить снова. Вы уверены?", dltprsstnt, Return())
                    
                    

                vbox:

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                                #if config.sample_sound:
                                #    textbutton _("Test") action Play("sound", config.sample_sound)


                    showif False:
                        if config.has_voice:
                            label _("Voice Volume")

                            hbox:
                                bar value Preference("voice volume")

                                if config.sample_voice:
                                    textbutton _("Test") action Play("voice", config.sample_voice)

                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing

                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("История диалогов пустая. Давайте напишем её!")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Управление"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                textbutton _("Мышь") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Следующий диалог и взаимодействие")

    hbox:
        label _("Пробел")
        text _("Следующий диалог без взаимодействия")

    hbox:
        label _("Стрелки")
        text _("Навигация по интерфейсу")

    hbox:
        label _("Escape")
        text _("Открыть меню игры")

    #hbox:
    #    label _("Ctrl")
    #    text _("Skips dialogue while held down.")

    #hbox:
    #    label _("Tab")
    #    text _("Toggles dialogue skipping.")

    #hbox:
    #    label _("Page Up")
    #    text _("Rolls back to earlier dialogue.")

    #hbox:
    #    label _("Page Down")
    #    text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Спрятать интерйфейс")

    hbox:
        label "S"
        text _("Сделать скриншот")

    #hbox:
    #    label "V"
    #    text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    #hbox:
    #    label "Shift+A"
    #    text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Левая кнопка")
        text _("Следующий диалог и взаимодействие")

    hbox:
        label _("Средняя кнопка")
        text _("Спрятать интерфейс")

    hbox:
        label _("Правая кнопка")
        text _("Открыть меню игры")

    #hbox:
    #    label _("Mouse Wheel Up\nClick Rollback Side")
    #    text _("Rolls back to earlier dialogue.")

    #hbox:
    #    label _("Mouse Wheel Down")
    #    text _("Rolls forward to later dialogue.")'''


screen gamepad_help():

    hbox:
        label _("Правый курок\nA\nНижняя кнопка")
        text _("Advances dialogue and activates the interface.")

    #hbox:
    #    label _("Left Trigger\nLeft Shoulder")
    #    text _("Rolls back to earlier dialogue.")

    #hbox:
    #    label _("Right Shoulder")
    #    text _("Rolls forward to later dialogue.")


    hbox:
        label _("Крестовина\nСтики")
        text _("Навигация по интерфейсу")

    hbox:
        label _("Start")
        text _("Открыть меню игры")

    hbox:
        label _("Y\nВерхняя кнопка")
        text _("Спрятать интерфейс")

    #textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
