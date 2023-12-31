label scene2_script:
    call street_monologue_script
    call rtf_watchwoman_script
    call rtf_classroom_script
    if branch_choice_a_b == 1:
        call gallery_dialogue_script
        call coffee_script
        call english_classroom_script
    else:
        call first_desk_script
        call after_physics_script 
    call back_home_script
    return












screen street_monologue_scene_1:
    add "bg_nine_sk.jpg" fit "fill"
    zorder -10

screen street_monologue_scene_2:
    add "bg_alley_people.jpg" fit "fill"
    zorder -10

screen street_monologue_scene_3:
    add "bg_alley_empty.jpg" fit "fill"
    zorder -10

screen street_monologue_scene_4:
    add "bg_street_traffic.jpg" fit "fill"
    zorder -10

screen street_monologue_scene_5:
    add "bg_street_crosswalk.jpg" fit "fill"
    zorder -10

screen street_monologue_scene_6:
    add "bg_rtf_entrance.jpg" fit "fill"
    zorder -10

define street_monologue_music = "Toby Fox — Ruins.mp3"
define street_monologue_ambient = "City Noise.mp3"

label street_monologue_script:
    show screen street_monologue_scene_1 with usual_transition
    play music street_monologue_music fadein .5
    play ambient street_monologue_ambient loop fadein .5
    speech.thought "Вы же зашли сюда, чтобы узнать что-то про айти?{w} Или про универ...{w} Ну, на крайний случай, про мой успешный путь и все дела..."
    speech.thought "Ну, слушайте.{w} Жили-были... Нет."
    speech.thought "Однажды..."
    hide screen street_monologue_scene_1 with usual_transition
    show screen street_monologue_scene_2 with usual_transition
    speech.thought "Ха-ха! Поверили?{w} Да я обычный первокурсник, вернее сказать, пекус.{w} Живу в центре Екатеринбурга в {a=https://vk.com/urfu9sk}{i}9ск{/i}{/a} и сейчас иду на свой {a=https://vk.com/thefirstdayurfu}{i}первый день в Уральском Федеральном{/i}{/a}."
    hide screen street_monologue_scene_2 with usual_transition
    show screen street_monologue_scene_3 with usual_transition
    speech.thought "Почему  {a=https://urfu.ru/ru/}{i}УрФУ{/i}{/a}?{w} Нуу.. Я долго выбирал универ.{w} Мне важно было близкое расположение общежитий (ребятам из {a=https://www.ural.kp.ru/daily/27555/4823514/}{i}новокольцово{/i}{/a} привет), хорошее образование, крупный город, подъемные проходные баллы."
    speech.thought "Звучит как реклама?{w} Мне за неё не платили.{w} Но я правда не думал, что всё это найду. Да ещё и в российском вузе.{w} Ещё и в УрФУ."
    hide screen street_monologue_scene_3 with usual_transition
    show screen street_monologue_scene_4 with usual_transition
    speech.thought "Кстати... Что сближает многих студентов?{w} Неопределенность! А кем я хочу быть в будущем?{w} Не знаю."
    speech.thought "Прочитал, что в ИРИТ-РТФ есть {a=https://urfu.ru/ru/iot/}{i}индивидуальные траектории{/i}{/a}, или просто “ИОТ”.{w} Это что-то вроде “ты сам выбираешь себе расписание и со временем понимаешь, кем хочешь работать”."
    speech.thought "Ха-ха-ха-ха! Какой бред.{w} Вуз поможет понять? Ха-ха-ха...{w} Тем не менее, я теперь радист."
    hide screen street_monologue_scene_4 with usual_transition
    show screen street_monologue_scene_5 with usual_transition
    speech.thought "Честно говоря, Мне страшно.{w} А вам?{w} Я скорее всего прав насчёт высшего образования в России.{w} И скорее всего захочу забрать документы."
    hide screen street_monologue_scene_5 with usual_transition
    show screen street_monologue_scene_6 with usual_transition
    speech.thought "А вообще, радиофак хорош.{w} Но не с утра, когда ты пробираешься сквозь толпу, за одну минуту до пары."
    hide screen street_monologue_scene_6 with usual_transition
    return












screen rtf_watchwoman_scene_1(how):
    add "bg_rtf_preentrance.jpg" fit "fill" at how
    add "ch_watchwoman.png" fit "fill"
    zorder -10

screen rtf_watchwoman_scene_2:
    add "bg_rtf_staircase.jpg" fit "fill"
    zorder -10

define rtf_watchwoman_music_1 = "Toby Fox — Quiet Water.mp3"
define rtf_watchwoman_music_2 = "Toby Fox — Dating Tense!.mp3"
define rtf_watchwoman_sound_1 = "Negative.mp3"
define rtf_watchwoman_sound_2 = "Positive.mp3"

label rtf_watchwoman_script:
    show screen rtf_watchwoman_scene_1(blur_out) with usual_transition
    stop music fadeout .5
    stop ambient fadeout .5
    play music rtf_watchwoman_music_2 fadein .5
    speech.thought "Ну, кажется, есть ещё одна проблема..."
    Character("Вахтёрша", kind = speech.generic) "{sc=3}Молодой человек! Пропуск мне кто показывать будет?{/sc}"
    menu:
        speech.thought "Что ответить..?"
        "Нагрубить и сказать, что уже показывал":
            play sound rtf_watchwoman_sound_1
            $ tmp = "провалена"
            $ portrait_main.appear("dressed", "normal", .8, True)
            speech.main "Я это уже сделал, женщина.{w} Внимательней нужно смотреть, или у вас со зрением проблемы?"
            $ portrait_main.morph(None, None, None, False)
            Character("Вахтёрша", kind = speech.generic) "{sc=5}{color=#FFDDDD}Показывать надо нормально, а ещё язык за зубами держать!{/color}{/sc}"
            Character("Вахтёрша", kind = speech.generic) "{sc=10}{color=#FFBBBB}Я тут не первый год работаю, а вы вот что себе позволяете!!!{/color}{/sc}"
            $ portrait_main.morph(None, "surprised", None, None)
            Character("Вахтёрша", kind = speech.generic) "{sc=20}{color=#FF9999}А вы знаете что вообще-то...{/color}{/sc}"
            $ portrait_main.morph(None, "sad", None, None)
            Character("Вахтёрша", kind = speech.generic) "{sc=50}{color=#FF7777}Мы, пОжИлыЕ лЮди, из-За таКиХ хамОв, как Вы, выНУждЕны пО ТРи смЕНы паХаТь...{/color}{/sc}"
            $ renpy.notify("За ссору с вахтершей вы получили баллов: 0/10. Всего баллов: " + str(player_score) + ".")
            speech.thought "Придётся бежать с поля боя."
            $ portrait_main.disappear()
        "Промолчать и показать пропуск ещё раз":
            stop music fadeout .5
            play music rtf_watchwoman_music_1 fadein .5
            play sound rtf_watchwoman_sound_2
            $ tmp = "пройдена.{w} “Вас наполняет решимость”"
            $ player_score += 10
            $ renpy.notify("За терпение вы получили баллов: 10/10. Всего баллов: " + str(player_score) + ".")
            Character("Вахтёрша", kind = speech.generic) "Вот так и в следующий раз будьте добры."
    show screen rtf_watchwoman_scene_1(blur_in)
    hide screen rtf_watchwoman_scene_1 with usual_transition
    show screen rtf_watchwoman_scene_2 with usual_transition
    speech.thought "Битва с боссом [tmp]."
    speech.thought "А теперь найти бы аудиторию...{w} Первая — физика."
    hide screen rtf_watchwoman_scene_2 with usual_transition
    if tmp == "провалена":
        stop music fadeout .5
        play music rtf_watchwoman_music_1 fadein .5
    return















screen rtf_classroom_scene_1:
    add "bg_rtf_classroom.jpg" fit "fill"
    zorder -10

screen rtf_classroom_scene_2:
    add "bg_rtf_auditorium.jpg" fit "fill"
    zorder -10

define rtf_classroom_ambient = "Classroom noise.mp3"
define rtf_classroom_sound = "Positive.mp3"

label rtf_classroom_script:
    speech.thought "..."
    speech.thought "..."
    speech.thought "???"
    show screen rtf_classroom_scene_1 with usual_transition
    speech.thought "Она оказалась на третьем этаже. Сколько времени я искал?{w} Даже не спрашивайте."
    hide screen rtf_classroom_scene_1 with usual_transition
    show screen rtf_classroom_scene_2 with usual_transition
    play ambient rtf_classroom_ambient loop fadein .5
    menu:
        speech.thought "Куда мне сесть?"
        "Галёрка — поближе к обществу!":
            $ branch_choice_a_b = 1
            $ player_score += 5
            $ renpy.notify("Вы получили 5 баллов. Всего баллов: " + str(player_score) + ".")
        "Первая парта — поближе к знаниям!":
            $ branch_choice_a_b = 2
            $ player_score += 10
            $ renpy.notify("Вы получили 10 баллов. Всего баллов: " + str(player_score) + ".")
    play sound rtf_classroom_sound
    hide screen rtf_classroom_scene_2 with usual_transition
    return














screen gallery_dialogue_scene_1:
    add "bg_viktoriya_gallery.jpg" fit "fill"
    zorder -10

screen gallery_dialogue_scene_2(how):
    add "bg_gallery_view.jpg" fit "fill" at how
    zorder -10

screen gallery_dialogue_scene_3:
    add "bg_stepashka.jpg" fit "fill"
    zorder -10

screen gallery_dialogue_scene_4:
    add "bg_viktoriya_mch.jpg" fit "fill"
    zorder -10

define gallery_dialogue_sound = "Negative.mp3"

label gallery_dialogue_script:
    show screen gallery_dialogue_scene_1 with usual_transition
    speech.thought "Я решил сесть подальше.{w} Первый день всё-таки, много стресса, а нервые клетки мне ещё на сессии будут нужны."
    hide screen gallery_dialogue_scene_1 with usual_transition
    show screen gallery_dialogue_scene_2(blur_out) with usual_transition
    $ portrait_main.appear("dressed", "normal", .3, False)
    $ portrait_viktoriya.appear("undressed", "normal", .7, True)
    Character("???", kind = speech.viktoriya) "Эй-эй-эй!{w} Куртку нужно сдавать в гардеро-о-об!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "У меня {a=https://vk.com/wall-133242721_51289}петельки нет{/a}."
    $ portrait_main.disappear()
    $ portrait_main.appear("undressed", "normal", .3, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Эм... Ладно."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "А ещё хорошего настроения.{w} Там на входе..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    $ renpy.notify("Цифры на пунктах меню показывают, сколько вам нужно очков, чтобы вы могли сделать этот выбор. Эти очки не списываются!")
    label gallery_dialogue_again_1:
    menu:
        Character("???", kind = speech.viktoriya) "Поругался из-за студика?"
        "{color=#FF3838}[[25]{/color} Переборол себя и показал ещё раз" if player_score < 25:
            play sound gallery_dialogue_sound
            $ renpy.notify("У вас недостаточно баллов.")
            jump gallery_dialogue_again_1
        "{color=#38FF38}[[25]{/color} Переборол себя и показал ещё раз" if player_score >=25:
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_main.morph(None, None, None, True)
            speech.main "Пришлось показать дважды."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, None, None, True)
            Character("???", kind = speech.viktoriya) "Так и надо было."
            $ portrait_viktoriya.morph(None, "normal", None, False)
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "Здесь всегда так с утра?{w} Настроения не было, а сейчас ещё хуже.{w} Да и физику я не понимаю."
        "{color=#FF3838}[[25]{/color} Да, только толку мало. Я ей слово, а она мне..." if player_score < 25:
            play sound gallery_dialogue_sound
            $ renpy.notify("У вас недостаточно баллов.")
            jump gallery_dialogue_again_1
        "{color=#38FF38}[[25]{/color} Да, только толку мало. Я ей слово, а она мне..." if player_score >= 25:
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Да...{w} обменялись любезностями, так сказать."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, "happy", None, True)
            Character("???", kind = speech.viktoriya) "Бывает. Привыкнешь."
            $ portrait_viktoriya.morph(None, "normal", None, False)
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "Здесь всегда так с утра?{w} Настроения не было, а сейчас ещё хуже.{w} Да и физику я не понимаю."
        "Промолчать":
            Character("???", kind = speech.viktoriya) "Э-эй! Язык проглотил?"
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Я...{w} да так...{w} Я ничего...{w} Настроения нет.{w} Ещё и физику не понимаю."

    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Да кто её понимает?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "Вдруг у меня специальность будет с ней связана..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Сочувствую.{w} Ты будущий инженер?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Не знаю, будущий бездарь.{w} Меня тянет ко всему по чуть-чуть.{w} Ещё не определился. Знаю, что технарь, и всё."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Ещё есть время! А в ИРИТ-РТФ индивиду..."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Прекрати говорить рекламными лозунгами, пожалуйста."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    Character("???", kind = speech.viktoriya) "Шучу, шучу. Но мне кажется, что здесь правда можно найти себя.{w} По крайней мере, стоит попытаться."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Попытаюсь."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "sad", None, True)
    label gallery_dialogue_again_2:
    menu:
        Character("???", kind = speech.viktoriya) "Ты прям вообще печальный, хочешь анекдот?"
        "{color=#FF3838}[[25]{/color} Давай" if player_score < 25:
            play sound gallery_dialogue_sound
            $ renpy.notify("У вас недостаточно баллов.")
            jump gallery_dialogue_again_2
        "{color=#38FF38}[[25]{/color} Давай" if player_score >= 25:
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_main.morph(None, None, None, True)
            speech.main "Валяй."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, "happy", None, True)
            Character("???", kind = speech.viktoriya) "Когда искусственный интеллект встанет в один ряд с человеческим, можно ли будет называть его “железяка хренова”, или это будет неполиткорректно?"
            $ portrait_viktoriya.morph(None, None, None, False)
            speech.thought "Я предпочёл промолчать."
            $ portrait_viktoriya.morph(None, "normal", None, True) 
            Character("???", kind = speech.viktoriya) "Ладно, забудь."
        "Мы же на паре...":
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_main.morph(None, None, None, True)
            speech.main "Не хватало мне ещё хохотать на всю аудиторию."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, "normal", None, True)
    
    Character("???", kind = speech.viktoriya) "Тогда может хоть кофе выпьем после физики?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Мне нужно будет найти кабинет английского, а это, скорее всего, займет весь перерыв."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Хочешь, помогу?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "normal", None, True)
    speech.main "Я только за."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    Character("???", kind = speech.viktoriya) "Отлично!{w} Осталось пережить пару и не уснуть."
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    show screen gallery_dialogue_scene_2(blur_in)
    hide screen gallery_dialogue_scene_2 with usual_transition
    show screen gallery_dialogue_scene_3 with usual_transition
    Character("Преподаватель", kind = speech.generic) "Галёрка!{w} У нас тут баллистика!{w} Разговоры прекращаем."
    hide screen gallery_dialogue_scene_3 with usual_transition
    show screen gallery_dialogue_scene_4 with usual_transition
    speech.main "Вот блин."
    hide screen gallery_dialogue_scene_4 with usual_transition
    stop music fadeout .5
    return














screen coffee_script(how):
    add "bg_rtf_coffeeshop.jpg" fit "fill" at how
    zorder -10

define coffee_music = "Toby Fox — Hotel.mp3"
define coffee_ambient = "Quiet Noise.mp3"
define coffee_sound_1 = "Negative.mp3"
define coffee_sound_2 = "Positive.mp3"

label coffee_script:
    show screen coffee_script(None) with usual_transition
    stop ambient fadeout .5
    play ambient coffee_ambient loop fadein .5
    stop music fadeout .5
    play music coffee_music fadein .5
    speech.thought "Мучительно прошла физика, и мы отправились искать кабинет английского."
    show screen coffee_script(blur_out)
    $ portrait_viktoriya.appear("undressed", "normal", .3, False)
    $ portrait_main.appear("undressed", "normal", .7, True)
    speech.main "Так что ты там говорила?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Попробуешь угадать мое имя?{w} Знаешь такую фишку, на некоторых смотришь и думаешь:{w} “Во-о-от, это точно идёт Настя”."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Да ну, бред."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Ты кстати похож на...{w} [player_name]!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Офигеть! Как ты..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    Character("???", kind = speech.viktoriya) "Угадала?!{w} Я же говорю!{w} Теперь давай ты, даю тебе пять попыток."
    $ portrait_main.morph(None, "normal", None, None)
    while guess_tries < 5:
        $ portrait_viktoriya.morph(None, None, None, False)
        menu:
            speech.thought "Как её зовут? Откуда я знаю!"
            "Ксюша" if not guess_tried_ksysha:
                $ guess_tried_ksysha = True
                $ guess_choice = "Ксюша"
                jump guess_nope
            "Катя" if not guess_tried_katya:
                $ guess_tried_katya = True
                $ guess_choice = "Катя"
                jump guess_nope
            "Ира" if not guess_tried_ira:
                $ guess_tried_ira = True
                $ guess_choice = "Ира"
                jump guess_nope
            "Маша" if not guess_tried_masha:
                $ guess_tried_masha = True
                $ guess_choice = "Маша"
                jump guess_nope
            "Аня" if not guess_tried_anya:
                $ guess_tried_anya = True
                $ guess_choice = "Аня"
                jump guess_nope
            "Наташа" if not guess_tried_natasha:
                $ guess_tried_natasha = True
                $ guess_choice = "Наташа"
                jump guess_nope
            "Вика":
                jump guess_yes
            "Юля" if not guess_tried_ylya:
                $ guess_tried_ylya = True
                $ guess_choice = "Юля"
                jump guess_nope
            "Ева" if not guess_tried_eva:
                $ guess_tried_eva = True
                $ guess_choice = "Ева"
                jump guess_nope
        label guess_nope:
        $ portrait_main.morph(None, None, None, True)
        speech.main "[guess_choice]?"
        play sound coffee_sound_1
        $ portrait_main.morph(None, None, None, False)
        if guess_tries == 0:
            $ portrait_viktoriya.morph(None, "normal", None, True)
            Character("???", kind = speech.viktoriya) "Ну не-е-ет."
        if guess_tries == 1:
            $ portrait_viktoriya.morph(None, None, None, True)
            Character("???", kind = speech.viktoriya) "Крутите барабан дальше.{w} Нет такой буквы!"
        if guess_tries == 2:
            $ portrait_viktoriya.morph(None, "sad", None, True)
            Character("???", kind = speech.viktoriya) "Чего?!{w} Да какая же я “[guess_choice]”?."
        if guess_tries == 3:
            $ portrait_viktoriya.morph(None, "normal", None, True)
            Character("???", kind = speech.viktoriya) "Думай, думай, Марк!"
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_main.morph(None, None, None, True)
            speech.main "Чего? Какой ещё Марк?"
            $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, None, None, True)
            Character("???", kind = speech.viktoriya) "Ну это отсылка на Непобедимого...{w} Ой, забей. Не [guess_choice] я.{w} Последняя попытка!"
        if guess_tries == 4:
            $ portrait_viktoriya.morph(None, None, None, True)
            $ renpy.notify("Вы не смогли угадать имя. За игру вы получили баллов: 0/10. Всего баллов: " + str(player_score) + ".")
            speech.viktoriya "Всё было куда проще, я Вика."
        $ guess_tries += 1
        if False:
            label guess_yes:
            play sound coffee_sound_2
            $ player_score += 10
            $ portrait_viktoriya.morph(None, "happy", None, True)
            $ renpy.notify("Вы угадали! За игру вы получили баллов: 10/10. Всего баллов: " + str(player_score) + ".")
            speech.viktoriya "Бинго-о-о!"
            $ guess_tries = 5
    $ portrait_main.disappear()
    $ portrait_viktoriya.disappear()
    show screen coffee_script(blur_in)
    speech.thought "После этого мы долго болтали о всех мероприятиях, которые приготовил для нас вуз."
    hide screen coffee_script with usual_transition
    return
    











screen english_classroom_scene_1(how):
    add "bg_english_classroom.jpg" fit "fill" at how
    zorder -10

screen english_classroom_scene_2(how):
    add "bg_english_entrance.jpg" fit "fill" at how
    zorder -10

label english_classroom_script:
    show screen english_classroom_scene_1(blur_out) with usual_transition
    $ portrait_main.appear("undressed", "normal", .7, False)
    $ portrait_viktoriya.appear("undressed", "normal", .3, True)
    speech.viktoriya "{a=https://urfu.ru/ru/students/leisure/oso/tvorchestvo/tradicionnye-meroprijatija/debjut-pervokursnikov/}Дебют пекусов{/a}? Он будет, правда, ещё нескоро.{w} Говорят, нужно приготовить номер на заданную тему и выступить на сцене."
    speech.viktoriya "Репетиции каждый день, все дела."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Какой же бред."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    speech.viktoriya "Я тоже не вижу в них смысла. Столько сил и времени уходит.{w} А знаешь, кто точно пойдет на дебют?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Кто?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Леро-о-у!{w} Она всегда за любой движ."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Это..?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "normal", None, True)
    speech.viktoriya "Вы не знакомы?{w} Странно, мне казалось, она добавила в друзья уже весь универ. Может как-нибудь встретитесь.{w} Смотри!{w} Вроде бы, это кабинет английского."
    $ portrait_main.disappear()
    $ portrait_viktoriya.disappear()
    hide screen english_classroom_scene_1 with usual_transition
    
    show screen english_classroom_scene_2(blur_out) with usual_transition
    $ portrait_main.appear("undressed", "normal", .7, True)
    $ portrait_viktoriya.appear("undressed", "normal", .3, False)
    speech.main "И правда он. Так быстро нашли. Спасибо..?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Рада помочь!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Ты мельком сказала, что рисуешь..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "normal", None, True)
    speech.viktoriya "Чисто любительски, может как-нибудь покажу."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Не было желания стать дизайнером?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Ха-ха-ха, какой из меня дизайнер!{w} Хотя...{w} Не знаю. Я ещё не определилась."
    $ portrait_viktoriya.morph(None, "normal", None, None)
    speech.viktoriya "В любом случае, время есть.{w} Если кто-то оценит мои работы, то почему бы и нет."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "У меня сосед по комнате увлекается всем этим.{w} Как это называется?{w} Живопись?{w} В общем, тоже творческий человек. Я думаю, он может что-нибудь посоветовать."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    speech.viktoriya "Так ты общажный?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Есть такое.{w} В девятом живу. Ты из одиннадцатой?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Я местная. Могу показать кучу мест, если захочешь.{w} Очень много приезжих, так любопытно за вами наблюдать."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "happy", None, True)
    speech.main "Если переживу английский, то с радостью.{w} Ну, мне пора бежать. Опаздывать на вторую пару подряд такое себе...{w} Ещё и в первый день."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    speech.viktoriya "Чао, как-нибудь увидимся!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    show screen english_classroom_scene_2(blur_in)
    $ portrait_main.disappear()
    $ portrait_viktoriya.disappear()
    speech.thought "Так, теперь английский...{w} Easy does it."
    hide screen english_classroom_scene_2 with usual_transition
    stop ambient fadeout .5
    return


















screen first_desk_scene_1:
    add "bg_first_desk.jpg" fit "fill"
    zorder -10

screen first_desk_scene_2:
    add "bg_egor_mch.jpg" fit "fill"
    zorder -10

screen first_desk_scene_3:
    add "bg_stepashka.jpg" fit "fill"
    zorder -10

label first_desk_script:
    show screen first_desk_scene_1 with usual_transition
    speech.thought "Сяду за первую парту.{w} Препод запомнит, {a=https://memepedia.ru/wp-content/uploads/2023/09/mem-sharikov.jpg}{i}зачёт поставит автоматом{/i}{/a}."
    hide screen first_desk_scene_1 with usual_transition
    show screen first_desk_scene_2 with usual_transition
    speech.main "Я немного задержался, искал кабинет.{w} Не подскажешь, какая тема?"
    Character("???", kind = speech.egor) "Понимаю, я тоже чуть не опоздал.{w} Зашел в {a=https://soc.urfu.ru/ru/upravlenie-razvitija-studencheskogo-potenciala/kovorkingi/#:~:text=Радиоточка}коворкинг{/a} вместо третьего этажа.{w} Тема — Баллистика."
    speech.main "Ха-ха, спасибо!{w} А как зовут преподавателя?"
    Character("???", kind = speech.egor) "Вроде, Антон Валерьевич."
    hide screen first_desk_scene_2 with usual_transition
    show screen first_desk_scene_3 with usual_transition
    speech.main "Антон Валерьевич, можете перелистнуть слайд?"
    Character("???", kind = speech.kseniya) "Удивительные вещи, однако."
    hide screen first_desk_scene_3 with usual_transition
    show screen first_desk_scene_2 with usual_transition
    speech.main "Я бы не назвал физику удивительной вещью."
    Character("???", kind = speech.kseniya) "Простите, я не про это.{w} По статистике примерно 65 процентов учеников забывают имя преподавателя через секунду после того, как он его назвал."
    "В общем, его не так зовут.{w} Я Ксения, приятно познакомиться!"
    Character("???", kind = speech.egor) "Ой. Перепутал.{w} Первый день всё-таки, никого ещё не запомнил.{w} У тебя, кстати, какое-то знакомое лицо..."
    speech.kseniya "Он создал игру про свою школу.{w} [player_name] вроде, да ведь?{w} Классно получилось! Читала об этом на сайте лицея."
    speech.egor "Точно-о-о, [player_name]!{w} Меня Егор звать.{w} Видел геймплей, всё на высшем уровне.{w} Завидую твоей будущей команде по {color=#FF00FF}Основам проектной деятельности{/color}.{w} Увлекаешься созданием игр?"
    speech.main "Есть такое. Просто иногда хочу рассказать миру какую-то мысль.{w} Выступать на публике не моё, писать книги тоже. Вот и нашел способ."
    speech.thought "Так странно, что меня узнают..."
    hide screen first_desk_scene_2 with usual_transition
    show screen first_desk_scene_3 with usual_transition
    Character("Преподаватель", kind = speech.generic) "Первый ряд!{w} По нулям поставить в {color=#FF00FF}БРС{/color} или будете слушать меня?"
    hide screen first_desk_scene_3 with usual_transition
    show screen first_desk_scene_2 with usual_transition
    speech.kseniya "Мне было бы интересно узнать Вас поближе, может..."
    speech.main "У меня английский после этой пары.{w} Боюсь, не успею найти кабинет, на разговоры уж точно нет времени."
    speech.kseniya "У меня тоже, вот так совпадение.{w} А такие совпадения по статистике случаются редко. Удивительно, быть может, мы в одной группе?"
    speech.main "Хм, у меня уровень B2, Болтенкова..."
    speech.kseniya "Да, в одной группе.{w} Превосходно!{w} Тогда вместе и найдем аудиторию.{w} Если доверять теории вероятности, то так будет быстрее."
    speech.narrator "*Егор шепчет на ухо*"
    speech.egor "Она чокнутая какая-то...{w} Может всё-таки гоу со мной?"
    speech.thought "Я ничего не ответил, хотя мне тоже она показалась странной."
    hide screen first_desk_scene_2 with usual_transition
    return












screen after_physics_scene_1(how):
    add "bg_english_classroom.jpg" fit "fill" at how
    zorder -10

screen after_physics_scene_2(how):
    add "bg_english_entrance.jpg" fit "fill" at how
    zorder -10

define after_physics_music = "Toby Fox — Confession.mp3"
define after_physics_ambient = "Quiet Noise.mp3"
define after_physics_sound = "Negative.mp3"

label after_physics_script:
    show screen after_physics_scene_1(None) with usual_transition
    stop ambient fadeout .5
    play ambient after_physics_ambient loop fadein .5
    stop music fadeout .5
    play music after_physics_music fadein .5
    speech.thought "Физика прошла, на удивление, быстро."
    show screen after_physics_scene_1(blur_out)
    $ portrait_main.appear("undressed", "normal", .3, True)
    $ portrait_kseniya.appear("undressed", "normal", .7, False)
    speech.main "Я ничего не успел записать.{w} Баллистика — это наука о...{w} брошенных в пространстве, основанная на...{w} Вся тетрадь в корявых определениях."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    speech.kseniya "Это не школа.{w} Понятное дело, что преподаватели диктуют быстрее...{w} Ничего, привыкнете."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Да почему ты обращаешься ко мне на “Вы”?{w} Я, блин, выгляжу на тринадцать."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "sad", None, True)
    speech.kseniya "Извините...{w} э-э...{w} извини.{w} Не знаю, привыкла так."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "Отвыкай, я чувствую себя на шестьдесят семь. А это кстати мой психологический возраст.{w} Вот тебе первый факт обо мне, теперь твоя очередь."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "normal", None, True)
    speech.kseniya "Моя очередь...{w} что?"
    $ portrait_kseniya.disappear()
    $ portrait_main.disappear()
    show screen after_physics_scene_1(blur_in)
    hide screen after_physics_scene_1 with usual_transition

    show screen after_physics_scene_2(blur_out) with usual_transition
    $ portrait_main.appear("undressed", "normal", .3, True)
    $ portrait_kseniya.appear("undressed", "normal", .7, False)
    speech.main "Рассказывать 5 фактов о себе."
    $ portrait_main.morph(None, None, None, False)
    while (not knowing_tried_teaching) or (not knowing_tried_payment) or (not knowing_tried_cuisine) or (not knowing_tried_appartment) or (not knowing_tried_insult):
        $ portrait_kseniya.morph(None, None, None, True)
        menu:
            speech.kseniya "{i}Про что мне стоило бы рассказать, исходя из логических рассуждений?{/i}"
            "О преподавании" if not knowing_tried_teaching:
                $ knowing_tried_teaching = True
                $ knowing_tried_insult = True
                speech.kseniya "Эм...{w} Ну...{w} Я преподаю...{w} Не имею никакого понятия, удивительно это или нет.{w}" 
                speech.kseniya "Так получилось, что я объясняю определённые разделы математики, переводя их на максимально доступный язык."
                $ portrait_kseniya.morph(None, None, None, False)
                $ portrait_main.morph(None, "sad", None, True)
                speech.main "Ого...{w} но я уже ничего не понял...{w} Ладно, давай дальше."
                $ portrait_main.morph(None, "normal", None, False)
            "О жизни в общежитии" if not knowing_tried_appartment:
                $ knowing_tried_appartment = True
                $ knowing_tried_insult = True
                speech.kseniya "Я на данный момент обитаю в девятом студенческом корпусе, или просто общежитии."
                speech.kseniya "Мне повезло попасть в это место, хотя у меня за экзамены четыреста пятьдесят шесть баллов за три предмета, поэтому не могло быть иначе."
                $ portrait_kseniya.morph(None, None, None, False)
                $ portrait_main.morph(None, "happy", None, True)
                speech.main "Да-а, прикольно. А у меня четыреста пятьдесят шесть рублей на карте.{w} Ну, неважно."
                $ portrait_main.morph(None, "normal", None, False)
            "О стипендии" if not knowing_tried_payment:
                $ knowing_tried_payment = True
                $ knowing_tried_insult = True
                speech.kseniya "У меня четыреста пятьдесят шесть баллов за экзамены...{w} Я это уже говорила?{w} Поэтому могу похвастаться своей стипендией...{w} Очень неприличная сумма..."
                $ portrait_kseniya.morph(None, None, None, False)
                $ portrait_main.morph(None, "happy", None, True)
                speech.main "Сто-о-ой.{w} О деньгах не говорят при первом знакомстве!{w} Скажешь потом, когда я буду готов услышать пятизначное число."
                $ portrait_main.morph(None, "normal", None, False)
            "О любимом блюде" if not knowing_tried_cuisine:
                $ knowing_tried_cuisine = True
                $ knowing_tried_insult = True
                speech.kseniya "Интереснейший факт, я очень люблю брокколи, потому что они улучшают пищеварение, снижают уровень холестерина..."
                speech.kseniya "...выводят токсины из организма максимизируют усвоение витаминов и минералов."
                $ portrait_kseniya.morph(None, None, None, False)
                $ portrait_main.morph(None, "sad", None, True)
                speech.main "Э-эм, окей..."
                $ portrait_main.morph(None, "normal", None, False)
                $ portrait_kseniya.morph(None, "happy", None, True)
                speech.main "Ладно, шучу, это лейс с крабом."
                $ portrait_kseniya.morph(None, None, None, False)
                $ portrait_main.morph(None, "happy", None, True)
                speech.main "Во-о-т!{w} Наш человек!"
                $ portrait_main.morph(None, "normal", None, False)
            "Не твоё дело!" if not knowing_tried_insult:
                $ knowing_tried_insult = True
                play sound after_physics_sound
                
    $ portrait_kseniya.morph(None, None, None, False)
    menu:
        speech.thought "Что ещё у неё спросить?"
        "Почему так говоришь?":
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "А почему ты так...{w} странно говоришь?" 
            $ portrait_main.morph(None, None, None, False)
            $ portrait_kseniya.morph(None, "normal", None, True)
            speech.kseniya "Говорю...{w} как?"
            $ portrait_kseniya.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Да неважно, забей, у меня просто сосед Ваня и он...{w} ну."
        "Много читаешь?":
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "Сколько книг ты вообще прочитала?"
            $ portrait_main.morph(None, None, None, False)
            $ portrait_kseniya.morph(None, "normal", None, True)
            speech.kseniya "Весьма сложно сказать, но если посчитать количество книг на моей полке и вычесть те, которые..."
            $ portrait_kseniya.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Всё, всё, я понял, могла бы просто сказать:{w} “Мне столько и не снилось”."
    $ portrait_kseniya.disappear()
    $ portrait_main.disappear()
    show screen after_physics_scene_2(blur_in)
    hide screen after_physics_scene_2 with usual_transition
    stop ambient fadeout .5
    return

















screen back_home_scene_1:
    add "bg_vanya_mch.jpg" fit "fill"
    zorder -10

screen back_home_scene_2:
    add "bg_full_classroom.jpg" fit "fill"
    zorder -10

screen back_home_scene_3:
    add "bg_sleepy_classroom.jpg" fit "fill"
    zorder -10

define back_home_music = "Toby Fox — Uwa!! So Temperate.mp3"
define back_home_sound_1 = "Positive.mp3"
define back_home_sound_2 = "Snoring.mp3"
define back_home_ambient = "Classroom Noise.mp3"

label back_home_script:
    show screen text_scene("Вечером этого же дня") with usual_transition
    stop music fadeout .5
    play music back_home_music fadein .5
    ""
    hide screen text_scene with usual_transition 
    show screen back_home_scene_1 with usual_transition
    if branch_choice_a_b == 1:
        speech.main "...вот, а потом было ещё три пары.{w} Это просто так...{w} странно?{w} Что всё не так плохо. Я думал, знакомства заводить сложнее.{w} А она ещё и помогла мне найти кабинет."
        speech.vanya "Бро-о, я говорил, всё норм будет и чтоб ты не кис.{w} Клянусь тапком, говорил."
        speech.main "Кстати, я ведь уже сказал, что она рисует.{w} Я думаю, ты бы нашел с ней общий язык.{w} Тоже этим увлекаешься. Могу дать её контакты."
        speech.vanya "Эээ...{w} Да я ж не рисую, ты чё...{w} Так, калякаю на листке. Фигня это всё, я любитель.{w} Лучше расскажи, как англ прошел."
        speech.main "Да в целом...{w} неплохо?"
    else:
        speech.vanya "... бро-о, это реал опупительно, ты сразу с кем-то познакомился.{w} Чел, да ты — Ален Делон, етить налево!"
        speech.main "Возможно.{w} Кстати, я подсел сегодня к чуваку...{w} Вроде, его звали Егор.{w} Он неправильно сказал мне имя преподавателя, когда я его спросил."
        speech.main "Я мало того опоздал, так ещё и на всю аудиторию назвал физика левым именем.{w} Понимаю, можно было перепутать фамилию и отчество...{w} Но он сам {b}правильно{/b} обращался к нему на протяжении всей пары."
        speech.vanya "Ё-маё, вот опять ты накручиваешь, жи ес.{w} Чё за тёрки, чувак."
        speech.main "Мне почему-то кажется, что он сделал это специально."
        speech.vanya "Братанчик, все путают клички в первые дни.{w} Андрей он, Витёк, там шиш поймешь, отвечаю.{w} Я сёдня училку по англу назвал Тамарой, а она Ольга, ты приколись, чувак."
        speech.vanya "Её вот чёт не прикольнуло.{w} Как инглиш, бай зе вей?"
        speech.main "Лучше, чем я думал!"
    hide screen back_home_scene_1 with usual_transition
    show screen back_home_scene_2 with usual_transition
    play ambient back_home_ambient loop fadein .5
    if branch_choice_a_b == 1:
        speech.main "Я привык всё критиковать, но тут мне правда зашло."
        speech.main "Я думал, что, возможно, стоило выбрать уровень ниже.{w} Теперь так не считаю.{w} Хотя всё равно сложно: у меня разговорный не очень сильный."
    else:
        speech.main "Сказал Ксюше до пары, что надо было выбирать уровень ниже.{w} Теперь так не считаю."
        speech.main "Хотя ей, вроде, не особо понравилось."
    menu:
        speech.vanya "О чём базарили-то?"
        "Животные":
            play sound back_home_sound_1
            $ player_score += 5
            $ renpy.notify("Почти правильно! Вы получили баллов: 5/12. Всего баллов: " + str(player_score) + ".")
            speech.main "Про животных, ничего необычного."
        "Программирование":
            play sound back_home_sound_1
            $ player_score += 10
            $ renpy.notify("Очень близко! Вы получили баллов: 10/12. Всего баллов: " + str(player_score) + ".")
            speech.main "Программирование обсуждали.{w} Мне понравилось, я же типа “шарю”, ха-ха-ха."
        "Злорадство":
            play sound back_home_sound_1
            $ player_score += 12
            $ renpy.notify("Правильно! Вы получили баллов: 12/12. Всего баллов: " + str(player_score) + ".")
            speech.main "Шаде...{w} Ше...{w} Schadenfreude.{w} Scha-den-freu-de.{w} Язык сломаешь."
    if branch_choice_a_b == 1:
        speech.vanya "Ого, а мы грэммар решали.{w} Презент симпл и вся ерундень эта.{w} А матеша как?{w} Я так офигел от темпа, ничё толком не записал."
    else:
        speech.vanya "Етить-колотить...{w} Слава Посейдону я на A0, на седьмом небе просто.{w} А матеша... Братан, я просто вылетел.{w} Ничё не успевал с доски переписывать, ты прикинь!"
        speech.vanya "Я старался вникать, отвечаю, долго сидел, разбирался.{w} Ну, через 15 минут забил и влип в мобилу.{w} Матрицы-фигатрицы, не понимаю я их ёмаё.{w} А вы чё?"
    speech.vanya "Эй!{w} Уснул что ли?"
    hide screen back_home_scene_2 with usual_transition
    show screen back_home_scene_3 with usual_transition
    play sound back_home_sound_2
    speech.main "Математика?{w} Да там...{w} Ну...{w} Да ничего интересного..."
    if branch_choice_a_b == 1:
        speech.main "Сам понимаешь, прилег на парту, а уже конец пары."
    else:
        speech.main "Просто...{w} Сам понимаешь."
    stop ambient fadeout .5
    hide screen back_home_scene_3 with usual_transition
    return