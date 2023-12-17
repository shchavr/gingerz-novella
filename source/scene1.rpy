label scene1_script:
    call desk_interactive_script
    call desk_flashback_script 
    call room_packing_script
    return









screen desk_interactive_scene:
    add "bg_desk.jpg" fit "fill"
    zorder -10 
    showif not asking_smth:
        showif not asked_ai:
            vbox xpos .72 ypos .56 xanchor .5 yanchor .5:
                imagebutton idle "empty.png" hover "question.png" action Call("ask_ai_script") at fade_in_out
        showif not asked_hf:
            vbox xpos .9 ypos .65 xanchor .5 yanchor .5:
                imagebutton idle "empty.png" hover "question.png" action Call("ask_hf_script") at fade_in_out
        showif not asked_lamp:
            vbox xpos .2 ypos .4 xanchor .5 yanchor .5:
                imagebutton idle "empty.png" hover "question.png" action Call("ask_lamp_script") at fade_in_out
        showif not asked_water:
            vbox xpos .81 ypos .3 xanchor .5 yanchor .5:
                imagebutton idle "empty.png" hover "question.png" action Call("ask_water_script") at fade_in_out
        showif not asked_pc:
            vbox xpos .5 ypos .4 xanchor .5 yanchor .5:
                imagebutton idle "empty.png" hover "question.png" action Call("ask_pc_script") at fade_in_out
        showif asked_ai and asked_hf and asked_lamp and asked_water and asked_pc and (not asked_all):
            vbox xpos .5 ypos .4 xanchor .5 yanchor .5:
                imagebutton idle "empty.png" hover "question.png" action Call("ask_all_script") at fade_in_out

label ask_ai_script:
    if (not asked_ai) and (not asking_smth):
        $ asking_smth = True
        $ asked_ai = True
        speech.main "Слушай, Алиса! Расскажи о себе!"
        speech.alice "Я — голосовой помощник, который может найти ответ на любой вопрос."
        speech.thought "А это {a=https://programs.edu.urfu.ru/ru/10591/}{i}искусственный интеллект{/i}{/a}. Удивительная штука, все так говорят. Меня она почему-то особо не удивляет."
        $ asking_smth = False
    return

label ask_hf_script:
    if (not asked_hf) and (not asking_smth):
        $ asking_smth = True
        $ asked_hf = True
        speech.thought "Это мои наушники, я люблю слушать {a=https://youtu.be/xm3YgoEiEDc?autoplay=1}{i}музыку{/i}{/a}. Чаще рок, иногда рэп... Поп тоже слушаю. Егор Крид, но редко..."
        speech.thought "..."
        speech.thought "Ладно, неважно."
        speech.thought "Папа хочет, чтобы я был радистом. Но пока что от {a=https://priem-rtf.urfu.ru/ru/baccalaureate/electronics-radio-engineering-and-communication-systems/radio-engineering/}{i}радиотехники{/i}{/a} я далек: максимум слушаю радио с утра и знаю, где памятник Попова."
        speech.thought "Проспект Ленина 39, город Екатеринбург. Видите? Знаю."
        $ asking_smth = False
    return

label ask_lamp_script:
    if (not asked_lamp) and (not asking_smth):
        $ asking_smth = True
        $ asked_lamp = True
        speech.thought "Учение свет. Неучение тьма. Грустно, что, зная пословицу наизусть, я не знаю её автора. Надо загуглить."
        $ asking_smth = False
    return

label ask_water_script:
    if (not asked_water) and (not asking_smth):
        $ asking_smth = True
        $ asked_water = True
        speech.thought "Монооксид дигидрогена, гидроксид водорода, гидроксильная кислота, оксидан, дигидрид кислорода."
        speech.thought "Было бы максимально смешно, если бы в названии было аж два о."
        speech.thought "..."
        speech.thought "Мне смешно, а вам... не знаю."
        $ asking_smth = False
    return

label ask_pc_script:
    if (not asked_pc) and (not asking_smth):
        $ asking_smth = True
        $ asked_pc = True
        speech.thought "Это мой компьютер, вы и сами видите. Урвал на популярном маркетплейсе почти задаром. Ничего необычного."
        speech.thought "Хотя даже такая простая вещь может иметь связь с моей будущей профессией. Вдруг я стану {a=https://programs.edu.urfu.ru/ru/10588/}{i}системным инженером{/i}{/a}?"
        speech.thought "Может и не стану."
        $ asking_smth = False
    return

label ask_all_script:
    if (not asked_all) and (not asking_smth):
        $ asked_all = True
    return

define desk_interactive_music = "Toby Fox — Home.mp3"

label desk_interactive_script:
    show screen desk_interactive_scene with usual_transition
    play music desk_interactive_music
    $ renpy.notify("На ссылки в репликах можно и нужно нажимать, они помогут лучше понять историю.")
    speech.thought "Интересно, что практически всё вокруг нас связано с айти."
    speech.thought "Ну, мне интересно... как вам, не знаю."
    while (not asked_ai) or (not asked_hf) or (not asked_lamp) or (not asked_water) or (not asked_pc):
        ""
    speech.thought "Да... Когда я просыпаюсь в 6 утра, то часто болтаю сам с собой."
    speech.thought "Довольно бездельничать, надо собираться. Сперва узнаю расписание, вроде сохранял на компьютере."
    while not asked_all:
        ""
    hide screen desk_interactive_scene with usual_transition
    return









screen desk_flashback_scene_1:
    add "bg_headon.jpg" fit "fill"
    add "schedule_1.png" fit "fill"
    zorder -10

screen desk_flashback_scene_2:
    add "bg_headon.jpg" fit "fill"
    showif not chose_subjects:
        add "schedule_2.png" fit "fill"
    showif chose_subjects:
        add "bsod.png" fit "fill"
    zorder -10

screen desk_flashback_scene_3:
    add "bg_desk_mch.jpg" fit "fill"
    zorder -10

define desk_flashback_sound = "Sad Trombone.mp3"
define desk_flashback_music = "Toby Fox — Home (Music Box).mp3"


label desk_flashback_script:
    show screen desk_flashback_scene_1 with usual_transition
    speech.thought "Ну и выбрал я себе расписание в {color=#FF00FF}модеусе{/color}. Хотя как выбрал..."
    hide screen desk_flashback_scene_1 with usual_transition
    show screen text_scene("Неделю назад...") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen desk_flashback_scene_2 with usual_transition
    speech.vanya "Десять-ноль-ноль, чувак!"
    speech.vanya "Заходим, быстрее!"
    speech.vanya "Бырее, мы ща не успеем нифига!"
    speech.narrator "*Ваня отчаянно клацает мышкой*"
    speech.vanya "Да святая моя пятка, етить твою малину... Не успел. А ты там как, ..."
    while True:
        $ player_name = renpy.input("{i}Придумайте имя нашему герою! {size=-10}(не героине, к сожалению){/size}{/i}")
        $ player_name = player_name.strip()
        if len(player_name) < 2:
            speech.narrator "Хм... Может что-то подлиннее?"
        else:
            jump desk_name_input_scene_break
    label desk_name_input_scene_break:
    speech.vanya "Да святая моя пятка, етить твою малину... Не успел. А ты там как, [player_name]?"
    stop music
    play sound desk_flashback_sound
    $ chose_subjects = True
    speech.main "Всё прекрасно..."
    speech.vanya "Чувак, мы влипли."
    hide screen desk_flashback_scene_2 with usual_transition
    show screen desk_flashback_scene_1 with usual_transition
    speech.thought "Мда."
    hide screen desk_flashback_scene_1 with usual_transition
    show screen desk_flashback_scene_3 with usual_transition
    play music desk_flashback_music
    speech.main "Влипли... Ничего страшного. От четырех пар в понедельник ещё никто не умирал."
    speech.main "Источник информации: живые второкурсники."
    hide screen desk_flashback_scene_3 with usual_transition
    return











screen room_packing_scene:
    add "bg_room_books.jpg" fit "fill"
    zorder -10
    showif not asking_smth:
        vbox xpos .68 ypos .58 xanchor .5 yanchor .5:
            imagebutton idle "empty.png" hover "question.png" action Call("ask_phys_script") at fade_in_out
        vbox xpos .6 ypos .5 xanchor .5 yanchor .5:
            imagebutton idle "empty.png" hover "question.png" action Call("ask_math_script") at fade_in_out
        vbox xpos .8 ypos .55 xanchor .5 yanchor .5:
            imagebutton idle "empty.png" hover "question.png" action Call("ask_stud_script") at fade_in_out
        vbox xpos .81 ypos .7 xanchor .5 yanchor .5:
            imagebutton idle "empty.png" hover "question.png" action Call("ask_org_script") at fade_in_out
        vbox xpos .58 ypos .75 xanchor .5 yanchor .5:
            imagebutton idle "empty.png" hover "question.png" action Call("ask_pe_script") at fade_in_out
        vbox xpos .92 ypos .65 xanchor .5 yanchor .5:
            imagebutton idle "empty.png" hover "question.png" action Call("ask_eng_script") at fade_in_out
        vbox xpos .48 ypos .38 xanchor .5 yanchor .5:
            imagebutton idle "empty.png" hover "question.png" action Call("ask_shelf_script") at fade_in_out
        vbox xpos .19 ypos .65 xanchor .5 yanchor .5:
            imagebutton idle "empty.png" hover "question.png" action Call("ask_bag_script") at fade_in_out
        vbox xpos .3 ypos .3 xanchor .5 yanchor .5:
            imagebutton idle "empty.png" hover "question.png" action Call("ask_door_script") at fade_in_out
    
define room_packing_sound_1 = "Negative.mp3"
define room_packing_sound_2 = "Positive.mp3"

label ask_phys_script:
    if not asking_smth:
        $ asking_smth = True
        if packed_phys:
            menu:
                speech.thought "Учебник по физике. Я уже положил его с собой. Оставить тут?"
                "Оставить тут":
                    $ packed_phys = False
                "Взять с собой":
                    $ packed_phys = True
        else:
            menu:
                speech.thought "Учебник по физике. Я ещё не взял его с собой. Положить в рюкзак?"
                "Оставить тут":
                    $ packed_phys = False
                "Взять с собой":
                    $ packed_phys = True
        $ asking_smth = False
    return

label ask_math_script:
    if not asking_smth:
        $ asking_smth = True
        if packed_math:
            menu:
                speech.thought "Учебник по математике. Я уже положил его с собой. Оставить тут?"
                "Оставить тут":
                    $ packed_math = False
                "Взять с собой":
                    $ packed_math = True
        else:
            menu:
                speech.thought "Учебник по математике. Я ещё не взял его с собой. Положить в рюкзак?"
                "Оставить тут":
                    $ packed_math = False
                "Взять с собой":
                    $ packed_math = True
        $ asking_smth = False
    return

label ask_stud_script:
    if not asking_smth:
        $ asking_smth = True
        if packed_stud:
            menu:
                speech.thought "Мой студенческий билет. Я уже положил его с собой. Оставить тут?"
                "Оставить тут":
                    $ packed_stud = False
                "Взять с собой":
                    $ packed_stud = True
        else:
            menu:
                speech.thought "Мой студенческий билет. Я ещё не взял его с собой. Положить в рюкзак?"
                "Оставить тут":
                    $ packed_stud = False
                "Взять с собой":
                    $ packed_stud = True
        $ asking_smth = False
    return

label ask_org_script:
    if not asking_smth:
        $ asking_smth = True
        if packed_org:
            menu:
                charspeechacter.thought "Тетрадь по основам российской государственности. Я уже положил её с собой. Оставить тут?"
                "Оставить тут":
                    $ packed_org = False
                "Взять с собой":
                    $ packed_org = True
        else:
            menu:
                speech.thought "Тетрадь по основам российской государственности. Я ещё не взял её с собой. Положить в рюкзак?"
                "Оставить тут":
                    $ packed_org = False
                "Взять с собой":
                    $ packed_org = True
        $ asking_smth = False
    return

label ask_pe_script:
    if not asking_smth:
        $ asking_smth = True
        if packed_pe:
            menu:
                speech.thought "Спортивная форма. Я уже положил её с собой. Оставить тут?"
                "Оставить тут":
                    $ packed_pe = False
                "Взять с собой":
                    $ packed_pe = True
        else:
            menu:
                speech.thought "Спортивная форма. Я ещё не взял её с собой. Положить в рюкзак?"
                "Оставить тут":
                    $ packed_pe = False
                "Взять с собой":
                    $ packed_pe = True
        $ asking_smth = False
    return

label ask_eng_script:
    if not asking_smth:
        $ asking_smth = True
        if packed_eng:
            menu:
                speech.thought "Тетрадь по англискому. Я уже положил её с собой. Оставить тут?"
                "Оставить тут":
                    $ packed_eng = False
                "Взять с собой":
                    $ packed_eng = True
        else:
            menu:
                speech.thought "Тетрадь по англискому. Я ещё не взял её с собой. Положить в рюкзак?"
                "Оставить тут":
                    $ packed_eng = False
                "Взять с собой":
                    $ packed_eng = True
        $ asking_smth = False
    return

label ask_shelf_script:
    if not asking_smth:
        $ asking_smth = True
        speech.thought "Шкаф с одеждой. Я уже оделся, мне в нём ничего не нужно."
        $ asking_smth = False
    return

label ask_bag_script:
    if not asking_smth:
        $ asking_smth = True
        speech.thought "Сумка моего соседа Вани. Я не страдаю клептоманией и не буду в неё лезть."
        $ asking_smth = False
    return

label ask_door_script:
    if not asking_smth:
        $ asking_smth = True
        if (not packed_phys) and (not packed_math) and (not packed_stud) and (not packed_org) and (not packed_pe) and (not packed_eng):
            speech.thought "Я ещё ничего не взял с собой, я не могу пойти на пары с пустым рюкзаком."
        else:
            $ tmp = []
            $ if packed_phys: tmp += ["учебник по физике"]
            $ if packed_math: tmp += ["учебник по математике"]
            $ if packed_stud: tmp += ["студенческий билет"]
            $ if packed_org: tmp += ["тетрадь по ОРГ"]
            $ if packed_pe: tmp += ["спортивную форму"]
            $ if packed_eng: tmp += ["тетрадь по английский"]
            $ tmp = ", ".join(tmp)
            menu:
                speech.thought "Я взял с собой [tmp]. Можно идти или нужно взять что-то ещё?"
                "В путь!":
                    $ ready_to_go = True
                "Рюкзак ещё не собран":
                    $ pass
        $ asking_smth = False
    return

label room_packing_script:
    $ asking_smth = True
    show screen room_packing_scene with usual_transition
    speech.main "Есть пять минут на сборы, иначе опоздаю в {a=https://rtf.urfu.ru/ru/}радик{/a}. У меня сегодня..."
    speech.alice "Тяжелый день. Приготовьтесь к лекции и практике по физике, английскому, физкультуре. Не забудьте {a=https://vk.com/wall-22301031_205712}студенческий{/a}."
    speech.thought "Так, надо ничего не забыть: {b}две физики, английский, физкультура, студик...{/b}"
    $ renpy.notify("Подсказка: посмотреть историю диалогов можно, нажав на \"История\" внизу экрана.")
    $ asking_smth = False
    while not ready_to_go:
        ""
    $ asking_smth = True    
    $ tmp = max(packed_phys + packed_pe + packed_eng + 2 * packed_stud - 2 * (packed_org + packed_math), 0) * 2
    $ player_score += tmp
    if tmp == 10:
        play sound room_packing_sound_2
        $ renpy.notify("Ура! Рюкзак собран правильно. Баллы: 10/10. Всего баллов: " + str(player_score) + ".")
        speech.thought "Успел и даже ничего не забыл! Пятнадцать минут и я в радике."
    else:
        play sound room_packing_sound_1
        $ renpy.notify("Ой... Где-то допущена ошибка. Баллы: " + str(tmp) + "/10. Всего баллов: " + str(player_score) + ".")
        speech.thought "Кажется здесь что-то не так..."
    hide screen room_packing_scene with usual_transition
    $ renpy.notify("С этого момента за каждое Ваше действие начисляются баллы. Их количество может повлиять на исход игры.")
    $ asking_smth = False
    return
