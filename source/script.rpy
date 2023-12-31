transform alphaa(a):
    alpha .7 ** a

screen premain_1:
    vbox xpos .7 ypos .5 xanchor .5 yanchor .5:
        spacing -493
        add "gingers.png" xsize 500 ysize 500 at alphaa(9)
        add "gingers.png" xsize 500 ysize 500 at alphaa(8)
        add "gingers.png" xsize 500 ysize 500 at alphaa(7)
        add "gingers.png" xsize 500 ysize 500 at alphaa(6)
        add "gingers.png" xsize 500 ysize 500 at alphaa(5)
        add "gingers.png" xsize 500 ysize 500 at alphaa(4)
        add "gingers.png" xsize 500 ysize 500 at alphaa(3)
        add "gingers.png" xsize 500 ysize 500 at alphaa(2)
        add "gingers.png" xsize 500 ysize 500 at alphaa(1)
        add "gingers.png" xsize 500 ysize 500 at alphaa(0)
    vbox xpos .55 ypos .45 xanchor 1. yanchor .5:
        spacing -91
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Рекурсивные{/i}{/b}{/size}{/color}{/font}" at alphaa(9)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Рекурсивные{/i}{/b}{/size}{/color}{/font}" at alphaa(8)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Рекурсивные{/i}{/b}{/size}{/color}{/font}" at alphaa(7)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Рекурсивные{/i}{/b}{/size}{/color}{/font}" at alphaa(6)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Рекурсивные{/i}{/b}{/size}{/color}{/font}" at alphaa(5)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Рекурсивные{/i}{/b}{/size}{/color}{/font}" at alphaa(4)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Рекурсивные{/i}{/b}{/size}{/color}{/font}" at alphaa(3)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Рекурсивные{/i}{/b}{/size}{/color}{/font}" at alphaa(2)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Рекурсивные{/i}{/b}{/size}{/color}{/font}" at alphaa(1)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Рекурсивные{/i}{/b}{/size}{/color}{/font}" at alphaa(0)
    vbox xpos .55 ypos .55 xanchor 1. yanchor .5:
        spacing -91
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Пряники{/i}{/b}{/size}{/color}{/font}" at alphaa(9)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Пряники{/i}{/b}{/size}{/color}{/font}" at alphaa(8)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Пряники{/i}{/b}{/size}{/color}{/font}" at alphaa(7)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Пряники{/i}{/b}{/size}{/color}{/font}" at alphaa(6)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Пряники{/i}{/b}{/size}{/color}{/font}" at alphaa(5)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Пряники{/i}{/b}{/size}{/color}{/font}" at alphaa(4)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Пряники{/i}{/b}{/size}{/color}{/font}" at alphaa(3)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Пряники{/i}{/b}{/size}{/color}{/font}" at alphaa(2)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Пряники{/i}{/b}{/size}{/color}{/font}" at alphaa(1)
        text "{font=Disket-Mono-Regular.ttf}{color=#FFFFFF}{size=+55}{b}{i}Пряники{/i}{/b}{/size}{/color}{/font}" at alphaa(0)
    text "{font=Disket-Mono-Regular.ttf}{color=#555555}{b}{i}Представляют{/i}{/b}{/color}{/font}" xpos .5 ypos .7 xanchor .5 yanchor .5

screen premain_2:
    text "{color=#FFFFFF}{size=+15}В этой игре для управления Вам понадобится мышь или тачпад{/size}{/color}" xpos .5 ypos .4 xanchor .5
    text "{color=#FFFFFF}{size=+15}Мы также настоятельно рекомендуем проходить игру в наушниках.{/size}{/color}" xpos .5 ypos .45 xanchor .5
    text "{color=#FFFFFF}{size=-15}Нажмите {b}пробел{/b} или {b}левую кнопку мыши{/b}, чтобы пропустить этот экран.{/size}{/color}" xpos .5 ypos .65 xanchor .5

screen premain_3:
    text "{color=#FFFFFF}{size=+15}Игра содержит изображения, сгенерированные искусственным интеллектом.{/size}{/color}" xpos .5 ypos .4 xanchor .5
    text "{color=#FFFFFF}{size=+15}Если Вас пугают увиденные Вами изображения, {b}не продолжайте игру{/b}.{/size}{/color}" xpos .5 ypos .45 xanchor .5
    text "{color=#FFFFFF}{size=-15}Нажмите {b}пробел{/b} или {b}левую кнопку мыши{/b}, чтобы пропустить этот экран.{/size}{/color}" xpos .5 ypos .65 xanchor .5

screen premain_4:
    text "{color=#FFFFFF}{size=+15}Все совпадения с реальностью случайны, все шутки несерьёзны.{/size}{/color}" xpos .5 ypos .4 xanchor .5
    text "{color=#FFFFFF}{size=+15}{b}Приятной игры{/b}.{/size}{/color}" xpos .5 ypos .45 xanchor .5
    text "{color=#FFFFFF}{size=-15}Нажмите {b}пробел{/b} или {b}левую кнопку мыши{/b}, чтобы пропустить этот экран.{/size}{/color}" xpos .5 ypos .65 xanchor .5

define splashscreen_music_1 = "Toby Fox — Snowdin Town.mp3"
define splashscreen_music_2 = "Toby Fox — An Ending.mp3"

label splashscreen:
    if persistent.endings == None:
        $ persistent.endings = [False, False, False, False, False, False, False]
    $ config.main_menu_music = splashscreen_music_2 if all(persistent.endings) else splashscreen_music_1
    play music config.main_menu_music
    if True: # Поменять на False, чтобы не показывать (при разработке мешает)
        show screen premain_1 with usual_transition
        pause 2.
        hide screen premain_1 with usual_transition
        show screen premain_2 with usual_transition
        pause 4.
        hide screen premain_2 with usual_transition
        show screen premain_3 with usual_transition
        pause 4.
        hide screen premain_3 with usual_transition
        show screen premain_4 with usual_transition
        pause 4.
        hide screen premain_4
    #$ preferences.set_mixer("music", .5) # Для балансировки звука (убрать на релизе!!!)
    #$ preferences.set_mixer("sfx", .5)
    return









init python:
    if persistent.endings == None:
        persistent.endings = [False, False, False, False, False, False, False]
init -1 python:
    if persistent.endings == None:
        persistent.endings = [False, False, False, False, False, False, False]
         








screen text_scene(what):
    text "{bt=3}{size=+15}[what]{/size}{/bt}" text_align .5 xpos .5 ypos .5 xanchor .5 yanchor .5
    zorder -10

define stub = "К сожалению, эта ветка еще не реализована :("

label start:
    stop music fadeout .5
    call scene1_script
    call scene2_script
    call scene3_script
    call scene4_script
    $ persistent.endings[ending_index] = True
    $ tmp = "{b}Поздравляем, вы прошли игру!{/b}\nВы получили " + str(player_score) + " баллов и {color=" + ("#FF3838" if ending_index in [3, 4] else "#38FF38") + "}" + ending_names_alternative[ending_index] + "{/color}.\nНо это ещё не всё..."
    show screen text_scene(tmp) with usual_transition
    ""
    hide screen text_scene with usual_transition
    if all(persistent.endings):
        show screen text_scene("Ну что ж, вы прошли все концовки.\nВы прошли игру!.. Вы ждали сюрприз, но где он?") with usual_transition
        ""
        hide screen text_scene with usual_transition
        show screen text_scene("Главный герой прошёл свой жизненный путь, где лишь одной\nостановкой был Уральский Федеральный; а вы прошли игру. Главный\nгерой, в прошлом обычный пекус, {b}начал понимать жизнь{/b}.") with usual_transition
        ""
        hide screen text_scene with usual_transition
        show screen text_scene("Он перестал видеть реальность через мультяшные нейро-фильтры,\nон перестал воспринимать мир под шутливую, игривую музыку.\nСпасибо {b}вам{/b} за игру. Пора бы и вам увидеть {b}реальность{/b}...") with usual_transition
        ""
        hide screen text_scene with usual_transition
        $ config.main_menu_music = splashscreen_music_2
    else:
        $ tmp = "Попробуйте пройти игру ещё раз, получите {b}другое количество баллов{/b},\nи найдите все оставшиеся концовки:\n{color=" + str(gui.accent_color)+ "}"
        $ tmp += ("" if (persistent.endings[0]) else (ending_names[0] + "\n"))
        $ tmp += ("" if (persistent.endings[1]) else (ending_names[1] + "\n"))
        $ tmp += ("" if (persistent.endings[2]) else (ending_names[2] + "\n"))
        $ tmp += ("" if (persistent.endings[3]) else (ending_names[3] + "\n"))
        $ tmp += ("" if (persistent.endings[4]) else (ending_names[4] + "\n"))
        $ tmp += ("" if (persistent.endings[5]) else (ending_names[5] + "\n"))
        $ tmp += ("" if (persistent.endings[6]) else (ending_names[6] + "\n"))
        $ tmp += "{/color}(Если возникают трудности, напишите нам — мы поможем)"
        show screen text_scene(tmp) with usual_transition
        ""
        hide screen text_scene with usual_transition
        show screen text_scene("Загляните в папку игры, там много интересного! В крайнем случае,\nпотупите в главное меню, там красивая анимация :D") with usual_transition
        ""
        hide screen text_scene with usual_transition
        show screen text_scene("Постойте... у вас появились вопросы? Что-то не сходится?\nЧто ж, мы должны упомянуть: многие секреты раскрываются\nне в тех концовках, где возникают.") with usual_transition
        ""
        hide screen text_scene with usual_transition
        show screen text_scene("Другими словами, нашу игру нужно воспринимать как\nединое целое — после прохождения всех концовок.") with usual_transition
        ""
        hide screen text_scene with usual_transition
        show screen text_scene("Кроме того, если сумеете пройти все концовки, то в конце\nвас ждёт сюрприз в главном меню.\n{b}С нетерпением ждём вас снова!!!{/b}") with usual_transition
        ""
        hide screen text_scene with usual_transition
    return









default ending_names = ["концовка “Гений, миллиардер, плейбой, филантроп”",
                        "концовка “Слово не воробей”",
                        "“Котоконцовка ◕ω◕”",
                        "концовка “Доверчивый бомж”",
                        "концовка “Не пейте пиво”",
                        "концовка “Кто-то гений, кто-то ищет студик”",
                        "концовка “А месть бывает сладкой”"]
default ending_names_alternative = ["концовку “Гений, миллиардер, плейбой, филантроп”",
                                    "концовку “Слово не воробей”",
                                    "“Котоконцовку ◕ω◕”",
                                    "концовку “Доверчивый бомж”",
                                    "концовку “Не пейте пиво”",
                                    "концовку “Кто-то гений, кто-то ищет студик”",
                                    "концовку “А месть бывает сладкой”"]