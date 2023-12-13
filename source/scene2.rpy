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

label street_monologue_script:
    show screen street_monologue_scene_1 with usual_transition
    play music street_monologue_music
    speech.thought "Вы же зашли сюда, чтобы узнать что-то про айти? Или про универ... Ну, на крайний случай, про мой успешный путь и все дела..."
    speech.thought "Ну, слушайте. Жили-были... Нет."
    speech.thought "Однажды..."
    hide screen street_monologue_scene_1 with usual_transition
    show screen street_monologue_scene_2 with usual_transition
    speech.thought "Ха-ха! Поверили? Да я обычный первокурсник, вернее сказать, пекус. Живу в центре Екатеринбурга в {a=https://vk.com/urfu9sk}{i}9ск{/i}{/a} и сейчас иду на свой {a=https://vk.com/thefirstdayurfu}{i}первый день в Уральском Федеральном{/i}{/a}."
    hide screen street_monologue_scene_2 with usual_transition
    show screen street_monologue_scene_3 with usual_transition
    speech.thought "Почему  {a=https://urfu.ru/ru/}{i}УрФУ{/i}{/a}? Нуу.. Я долго выбирал универ. Мне важно было близкое расположение общежитий (ребятам из {a=https://www.ural.kp.ru/daily/27555/4823514/}{i}новокольцово{/i}{/a} привет), хорошее образование, крупный город, подъемные проходные баллы."
    speech.thought "Звучит как реклама? Мне за нее не платили. Но я правда не думал, что все это найду. Да еще и в российском вузе. Еще и в УрФУ."
    hide screen street_monologue_scene_3 with usual_transition
    show screen street_monologue_scene_4 with usual_transition
    speech.thought "Кстати... Что сближает многих студентов? Неопределенность! А кем я хочу быть в будущем? Не знаю."
    speech.thought "Прочитал, что в ИРИТ-РТФ есть {a=https://urfu.ru/ru/iot/}{i}индивидуальные траектории{/i}{/a}. Это что-то вроде “ты сам выбираешь себе расписание и со временем понимаешь, кем хочешь работать”."
    speech.thought "Ха-ха-ха-ха! Какой бред. Вуз поможет понять? Ха-ха-ха... Тем не менее, я теперь радист."
    hide screen street_monologue_scene_4 with usual_transition
    show screen street_monologue_scene_5 with usual_transition
    speech.thought "Честно говоря, Мне страшно. А вам? Я скорее всего прав насчёт высшего образования в России. И скорее всего захочу забрать документы."
    hide screen street_monologue_scene_5 with usual_transition
    show screen street_monologue_scene_6 with usual_transition
    speech.thought "А вообще, радиофак хорош. Но не с утра, когда ты пробираешься сквозь толпу, за одну минуту до пары."
    hide screen street_monologue_scene_6 with usual_transition
    return












screen rtf_watchwoman_scene_1(how):
    add "bg_rtf_preentrance.jpg" fit "fill" at how
    add "ch_watchwoman.png" fit "fill"
    zorder -10

screen rtf_watchwoman_scene_2:
    add "bg_rtf_staircase.jpg" fit "fill"
    zorder -10

define rtf_watchwoman_music = "Toby Fox — Dating Tense!.mp3"

label rtf_watchwoman_script:
    show screen rtf_watchwoman_scene_1(blur_out) with usual_transition
    play music rtf_watchwoman_music
    speech.thought "Ну, кажется, есть ещё одна проблема..."
    Character("Вахтёрша", kind = speech.generic) "{sc=3}Молодой человек! Пропуск мне кто показывать будет?{/sc}"
    menu:
        speech.thought "Что ответить..?"
        "Нагрубить и сказать, что уже показывал":
            $ tmp = "провалена"
            $ portrait.main.appear("dressed", "normal", .8, True)
            speech.main "Я это уже сделал, женщина. Внимательней нужно смотреть, или у вас со зрением проблемы?"
            $ portrait.main.morph(None, None, None, False)
            Character("Вахтёрша", kind = speech.generic) "{sc=5}{color=#FFDDDD}Показывать надо нормально, а ещё язык за зубами держать!{/color}{/sc}"
            Character("Вахтёрша", kind = speech.generic) "{sc=10}{color=#FFBBBB}Я тут не первый год работаю, а вы вот что себе позволяете!!!{/color}{/sc}"
            $ portrait.main.morph(None, "surprised", None, None)
            Character("Вахтёрша", kind = speech.generic) "{sc=20}{color=#FF9999}А вы знаете что вообще-то...{/color}{/sc}"
            $ portrait.main.morph(None, "sad", None, None)
            Character("Вахтёрша", kind = speech.generic) "{sc=50}{color=#FF7777}Мы, пОжИлыЕ лЮди, из-За таКиХ хамОв, как Вы, выНУждЕны пО ТРи смЕНы паХаТь...{/color}{/sc}"
            $ renpy.notify("За ссору с вахтершей вы получили баллов: 0/10. Всего баллов: " + str(player_score) + ".")
            speech.thought "Придётся бежать с поля боя."
            $ portrait.main.disappear()
        "Промолчать и показать пропуск еще раз":
            $ tmp = "пройдена. “Вас наполняет решимость”."
            $ player_score += 10
            $ renpy.notify("За терпение вы получили баллов: 10/10. Всего баллов: " + str(player_score) + ".")
            Character("Вахтёрша", kind = speech.generic) "Вот так и в следующий раз будьте добры."
    show screen rtf_watchwoman_scene_1(blur_in)
    hide screen rtf_watchwoman_scene_1 with usual_transition
    show screen rtf_watchwoman_scene_2 with usual_transition
    speech.thought "Битва с боссом [tmp]."
    speech.thought "А теперь найти бы аудиторию... Первая — физика."
    hide screen rtf_watchwoman_scene_2 with usual_transition
    return















screen rtf_classroom_scene_1:
    add "bg_rtf_classroom.jpg" fit "fill"
    zorder -10

screen rtf_classroom_scene_2:
    add "bg_rtf_auditorium.jpg" fit "fill"
    zorder -10

define rtf_classroom_music = "Toby Fox — Quiet Water.mp3"
define rtf_classroom_ambient = "Quiet noise.mp3"

label rtf_classroom_script:
    speech.thought "..."
    speech.thought "..."
    speech.thought "???"
    show screen rtf_classroom_scene_1 with usual_transition
    speech.thought "Она оказалась на третьем этаже. Сколько времени я искал? Даже не спрашивайте."
    hide screen rtf_classroom_scene_1 with usual_transition
    show screen rtf_classroom_scene_2 with usual_transition
    play music rtf_classroom_music
    play ambient rtf_classroom_ambient loop
    menu:
        speech.thought "Куда мне сесть?"
        "Галёрка — поближе к обществу!":
            $ branch_choice_a_b = 1
        "Первая парта — поближе к знаниям!":
            $ branch_choice_a_b = 2
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

label gallery_dialogue_script:
    show screen gallery_dialogue_scene_1 with usual_transition
    speech.thought "Я решил сесть подальше. Первый день всё-таки, много стресса, а нервые клетки мне ещё на сессии будут нужны."
    hide screen gallery_dialogue_scene_1 with usual_transition
    show screen gallery_dialogue_scene_2(blur_out) with usual_transition
    $ portrait.main.appear("dressed", "normal", .3, False)
    $ portrait.viktoriya.appear("undressed", "normal", .7, True)
    Character("???", kind = speech.viktoriya) "Эй-эй-эй! Куртку нужно сдавать в гардеро-о-об!"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "У меня {a=https://vk.com/wall-133242721_51289}петельки нет{/a}."
    $ portrait.main.disappear()
    $ portrait.main.appear("undressed", "normal", .3, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Эм... Ладно."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "А ещё хорошего настроения. Там на входе..."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    menu:
        Character("???", kind = speech.viktoriya) "Поругался из-за студика?"
        "Переборол себя и показал ещё раз":
            $ portrait.viktoriya.morph(None, None, None, False)
            $ portrait.main.morph(None, None, None, True)
            speech.main "Пришлось показать дважды."
            $ portrait.main.morph(None, None, None, False)
            $ portrait.viktoriya.morph(None, None, None, True)
            Character("???", kind = speech.viktoriya) "Так и надо было."
        "Да, только толку мало. Я ей слово, а она мне...":
            $ portrait.viktoriya.morph(None, None, None, False)
            $ portrait.main.morph(None, "sad", None, True)
            speech.main "Да... обменялись любезностями, так сказать."
            $ portrait.main.morph(None, None, None, False)
            $ portrait.viktoriya.morph(None, "happy", None, True)
            Character("???", kind = speech.viktoriya) "Бывает. Привыкнешь."

    $ portrait.viktoriya.morph(None, "normal", None, False)
    $ portrait.main.morph(None, "normal", None, True)
    speech.main "Здесь всегда так с утра? Настроения не было, а сейчас ещё хуже. Да и физику я не понимаю."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Да кто её понимает?"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "sad", None, True)
    speech.main "Вдруг у меня специальность будет с ней связана..."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Сочувствую. Ты будущий инженер?"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Не знаю, будущий бездарь. Меня тянет ко всему по чуть-чуть. Ещё не определился. Знаю, что технарь, и всё."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Ещё есть время! А в ИРИТ-РТФ индивиду..."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Прекрати говорить рекламными лозунгами, пожалуйста."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    Character("???", kind = speech.viktoriya) "Шучу, шучу. Но мне кажется, что здесь правда можно найти себя. По крайней мере, стоит попытаться."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Попытаюсь."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "sad", None, True)
    menu:
        Character("???", kind = speech.viktoriya) "Ты прям вообще печальный, хочешь анекдот?"
        "Давай":
            $ portrait.viktoriya.morph(None, None, None, False)
            $ portrait.main.morph(None, None, None, True)
            speech.main "Валяй."
            $ portrait.main.morph(None, None, None, False)
            $ portrait.viktoriya.morph(None, "happy", None, True)
            Character("???", kind = speech.viktoriya) "Когда искусственный интеллект встанет в один ряд с человеческим, можно ли будет называть его “железяка хренова”, или это будет неполиткорректно?"
            $ portrait.viktoriya.morph(None, None, None, False)
            speech.thought "Я предпочёл промолчать."
            $ portrait.viktoriya.morph(None, "normal", None, True) 
            Character("???", kind = speech.viktoriya) "Ладно, забудь."
        "Мы же на паре...":
            $ portrait.viktoriya.morph(None, None, None, False)
            $ portrait.main.morph(None, None, None, True)
            speech.main "Не хватало мне ещё хохотать на всю аудиторию."
            $ portrait.main.morph(None, None, None, False)
            $ portrait.viktoriya.morph(None, "normal", None, True)
    
    Character("???", kind = speech.viktoriya) "Тогда может хоть кофе выпьем после физики?"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Мне нужно будет найти кабинет английского, а это, скорее всего, займет весь перерыв."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Хочешь, помогу?"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "normal", None, True)
    speech.main "Я только за."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    Character("???", kind = speech.viktoriya) "Отлично! Осталось пережить пару и не уснуть."
    $ portrait.viktoriya.disappear()
    $ portrait.main.disappear()
    show screen gallery_dialogue_scene_2(blur_in)
    hide screen gallery_dialogue_scene_2 with usual_transition
    show screen gallery_dialogue_scene_3 with usual_transition
    Character("Преподаватель", kind = speech.generic) "Галёрка! У нас тут баллистика! Разговоры прекращаем."
    hide screen gallery_dialogue_scene_3 with usual_transition
    show screen gallery_dialogue_scene_4 with usual_transition
    speech.main "Вот блин."
    hide screen gallery_dialogue_scene_4 with usual_transition
    stop music
    return














screen coffee_script(how):
    add "bg_rtf_coffeeshop.jpg" fit "fill" at how
    zorder -10

define coffee_music = "Toby Fox — Hotel.mp3"
define coffee_sound = "Short Applause.mp3"

label coffee_script:
    show screen coffee_script(None) with usual_transition
    play music coffee_music
    speech.thought "Мучительно прошла физика, и мы отправились искать кабинет английского."
    show screen coffee_script(blur_out)
    $ portrait.viktoriya.appear("undressed", "normal", .3, False)
    $ portrait.main.appear("undressed", "normal", .7, True)
    speech.main "Так что ты там говорила?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Попробуешь угадать мое имя? Знаешь такую фишку, на некоторых смотришь и думаешь: “Во-о-от, это точно идёт Настя”."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Да ну, бред."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    Character("???", kind = speech.viktoriya) "Ты кстати похож на [player_name]."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "surprised", None, True)
    speech.main "Офигеть! Как ты..."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    Character("???", kind = speech.viktoriya) "Угадала?! Я же говорю! Теперь давай ты, даю тебе пять попыток."
    $ portrait.main.morph(None, "normal", None, None)
    while guess_tries < 5:
        $ portrait.viktoriya.morph(None, None, None, False)
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
        $ portrait.main.morph(None, None, None, True)
        speech.main "[guess_choice]?"
        $ portrait.main.morph(None, None, None, False)
        if guess_tries == 0:
            $ portrait.viktoriya.morph(None, "normal", None, True)
            Character("???", kind = speech.viktoriya) "Ну не-е-ет."
        if guess_tries == 1:
            $ portrait.viktoriya.morph(None, None, None, True)
            Character("???", kind = speech.viktoriya) "Крутите барабан дальше. Нет такой буквы!"
        if guess_tries == 2:
            $ portrait.viktoriya.morph(None, "sad", None, True)
            Character("???", kind = speech.viktoriya) "Чего?! Да какая же я “[guess_choice]”?."
        if guess_tries == 3:
            $ portrait.viktoriya.morph(None, "normal", None, True)
            Character("???", kind = speech.viktoriya) "Думай, думай, Марк!"
            $ portrait.viktoriya.morph(None, None, None, False)
            $ portrait.main.morph(None, None, None, True)
            speech.main "Чего? Какой ещё Марк?"
            $ portrait.main.morph(None, None, None, False)
            $ portrait.viktoriya.morph(None, None, None, True)
            Character("???", kind = speech.viktoriya) "Ну это отсылка на Непобедимого... Ой, забей. Не [guess_choice] я. Последняя попытка!"
        if guess_tries == 4:
            $ portrait.viktoriya.morph(None, None, None, True)
            $ renpy.notify("Вы не смогли угадать имя. За игру вы получили баллов: 0/10. Всего баллов: " + str(player_score) + ".")
            speech.viktoriya "Всё было куда проще, я Вика."
        $ guess_tries += 1
        if False:
            label guess_yes:
            $ player_score += 10
            $ portrait.viktoriya.morph(None, "happy", None, True)
            $ renpy.notify("Вы угадали! За игру вы получили баллов: 10/10. Всего баллов: " + str(player_score) + ".")
            play sound coffee_sound
            speech.viktoriya "Бинго-о-о!"
            $ guess_tries = 5
    $ portrait.main.disappear()
    $ portrait.viktoriya.disappear()
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
    $ portrait.main.appear("undressed", "normal", .7, False)
    $ portrait.viktoriya.appear("undressed", "normal", .3, True)
    speech.viktoriya "{a=https://urfu.ru/ru/students/leisure/oso/tvorchestvo/tradicionnye-meroprijatija/debjut-pervokursnikov/}Дебют пекусов{/a}? Он будет, правда, ещё нескоро. Говорят, нужно приготовить номер на заданную тему и выступить на сцене."
    speech.viktoriya "Репетиции каждый день, все дела."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Какой же бред."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    speech.viktoriya "Я тоже не вижу в них смысла. Столько сил и времени уходит."
    speech.viktoriya "А знаешь, кто точно пойдет на дебют?"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Кто?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Леро-о-у! Она всегда за любой движ."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Это..?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "normal", None, True)
    speech.viktoriya "Вы не знакомы? Странно, мне казалось, она добавила в друзья уже весь универ."
    speech.viktoriya "Может как-нибудь встретитесь. Смотри! Вроде бы, это кабинет английского."
    $ portrait.main.disappear()
    $ portrait.viktoriya.disappear()
    hide screen english_classroom_scene_1 with usual_transition
    
    show screen english_classroom_scene_2(blur_out) with usual_transition
    $ portrait.main.appear("undressed", "normal", .7, True)
    $ portrait.viktoriya.appear("undressed", "normal", .3, False)
    speech.main "И правда он. Так быстро нашли. Спасибо..?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Рада помочь!"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Ты мельком сказала, что рисуешь..."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "normal", None, True)
    speech.viktoriya "Чисто любительски, может как-нибудь покажу."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Не было желания стать дизайнером?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Ха-ха-ха, какой из меня дизайнер! Хотя... Не знаю. Я еще не определилась."
    $ portrait.viktoriya.morph(None, "normal", None, None)
    speech.viktoriya "В любом случае, время есть. Если кто-то оценит мои работы, то почему бы и нет."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "У меня сосед по комнате увлекается всем этим. Как это называется? Живопись?"
    speech.main "В общем, тоже творческий человек. Я думаю, он может что-нибудь посоветовать."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    speech.viktoriya "Так ты общажный?"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Есть такое. В девятом живу. Ты из одиннадцатой?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Я местная. Могу показать кучу мест, если захочешь. Очень много приезжих, так любопытно за вами наблюдать."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "happy", None, True)
    speech.main "Если переживу английский, то с радостью."
    speech.main "Ну, мне не пора бежать. Опаздывать на вторую пару подряд такое себе... Ещё и в первый день."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    speech.viktoriya "Чао, как-нибудь увидимся!"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    show screen english_classroom_scene_2(blur_in)
    $ portrait.main.disappear()
    $ portrait.viktoriya.disappear()
    speech.thought "Так, теперь английский... Easy does it."
    hide screen english_classroom_scene_2 with usual_transition
    stop ambient
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
    speech.thought "Сяду за первую парту. Препод запомнит, {a=https://memepedia.ru/wp-content/uploads/2023/09/mem-sharikov.jpg}{i}зачёт поставит автоматом{/i}{/a}."
    hide screen first_desk_scene_1 with usual_transition
    show screen first_desk_scene_2 with usual_transition
    speech.main "Я немного задержался, искал кабинет. Не подскажешь, какая тема?"
    Character("???", kind = speech.egor) "Понимаю, я тоже чуть не опоздал. Зашел в {a=https://soc.urfu.ru/ru/upravlenie-razvitija-studencheskogo-potenciala/kovorkingi/#:~:text=Радиоточка}коворкинг{/a} вместо третьего этажа."
    Character("???", kind = speech.egor) "Тема — Баллистика."
    speech.main "Ха-ха, спасибо! А как зовут преподавателя?"
    Character("???", kind = speech.egor) "Вроде, Антон Валерьевич."
    hide screen first_desk_scene_2 with usual_transition
    show screen first_desk_scene_3 with usual_transition
    speech.main "Антон Валерьевич, можете перелистнуть слайд?"
    Character("???", kind = speech.kseniya) "Ха-ха-ха!"
    hide screen first_desk_scene_3 with usual_transition
    show screen first_desk_scene_2 with usual_transition
    speech.main "Что смешного?"
    speech.kseniya "Андрей Викторович его зовут. А меня, кстати, Ксюша."
    Character("???", kind = speech.egor) "Ой. Перепутал. Первый день всё-таки, никого ещё не запомнил."
    Character("???", kind = speech.egor) "У тебя, кстати, какое-то знакомое лицо..."
    speech.kseniya "Он создал игру про свою школу. [player_name] вроде, да ведь? Классно получилось! Читала об этом на сайте лицея."
    speech.egor "Точно-о-о, [player_name]! Меня Егор звать. Видел геймплей, всё на высшем уровне."
    speech.egor "Завидую твоей будущей команде по {color=#FF00FF}Основам проектной деятельности{/color}. Увлекаешься созданием игр?"
    speech.main "Есть такое. Просто иногда хочу рассказать миру какую-то мысль. Выступать на публике не моё, писать книги тоже. Вот и нашел способ."
    speech.thought "Так странно, что меня узнают..."
    hide screen first_desk_scene_2 with usual_transition
    show screen first_desk_scene_3 with usual_transition
    Character("Преподаватель", kind = speech.generic) "Первый ряд! По нулям поставить в {color=#FF00FF}БРС{/color} или будете слушать меня?"
    hide screen first_desk_scene_3 with usual_transition
    show screen first_desk_scene_2 with usual_transition
    speech.kseniya "Поболтаем после пары?"
    speech.main "У меня английский. Боюсь, не успею найти кабинет."
    speech.kseniya "У меня тоже! Мы, может, в одной группе?"
    speech.main "Хм, у меня уровень B2, Болтенкова..."
    speech.kseniya "Да, в одной группе. Тогда вместе и найдем аудиторию."
    speech.egor "Везёт вам. А мне на математику идти."
    hide screen first_desk_scene_2 with usual_transition
    return












screen after_physics_scene_1(how):
    add "bg_english_classroom.jpg" fit "fill" at how
    zorder -10

screen after_physics_scene_2(how):
    add "bg_english_entrance.jpg" fit "fill" at how
    zorder -10

define after_physics_music = "Toby Fox — Confession.mp3"

label after_physics_script:
    show screen after_physics_scene_1(None) with usual_transition
    play music after_physics_music
    speech.thought "Физика прошла, на удивление, быстро."
    show screen after_physics_scene_1(blur_out)
    $ portrait.main.appear("undressed", "normal", .3, True)
    $ portrait.kseniya.appear("undressed", "normal", .7, False)
    speech.main "Я ничего не успел записать. Баллистика — это наука о... брошенных в пространстве, основанная на... Вся тетрадь в корявых определениях."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, None, None, True)
    speech.kseniya "Это не школа. Понятное дело, что преподаватели диктуют быстрее. Да и не думаю, что прям все нужно записывать."
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Просто сложно понять, что будет на {color=#FF00FF}НТК{/color}. Возможно одна из формул, которые я не успел записать."
    speech.main "Кстати, будет экзамен по английскому?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, "happy", None, True)
    speech.kseniya "Будет."
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Хе-хе-хе, ну конечно же. Надо было идти на уровень ниже. Говорят, на B2 и C1 куча домашки и разговорного."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, "normal", None, True)
    speech.kseniya "Вот сейчас и посмотрим. Программистам же нужен английский. Не думаю, что мы ошиблись с выбором."
    $ portrait.kseniya.disappear()
    $ portrait.main.disappear()
    show screen after_physics_scene_1(blur_in)
    hide screen after_physics_scene_1 with usual_transition

    show screen after_physics_scene_2(blur_out) with usual_transition
    $ portrait.main.appear("undressed", "normal", .3, True)
    $ portrait.kseniya.appear("undressed", "normal", .7, False)
    speech.main "А вот и он. Я про кабинет. Даже не опоздали, время еще есть..."
    speech.main "Может расскажешь что-нибудь о себе?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, None, None, True)
    speech.kseniya "Да ничего интересного. Живу в девятой общаге, учусь. В свободное время преподаю и подрабатываю."
    $ portrait.kseniya.morph(None, "sad", None, None)
    speech.kseniya "На днях увидела все онлайн курсы, которые нам поставили, теперь свободного времени у меня нет."
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, "sad", None, True)
    speech.main "Ох, как я тебя понимаю. Десять штук... Сказали, что ещё добавят по физике и ОРГ. Ставим ставки, когда мы сойдём с ума."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, "normal", None, True)
    speech.kseniya "Мне кажется, я уже..."
    $ portrait.kseniya.disappear()
    $ portrait.main.disappear()
    show screen after_physics_scene_2(blur_in)
    hide screen after_physics_scene_2 with usual_transition
    stop ambient
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

label back_home_script:
    show screen text_scene("Вечером этого же дня") with usual_transition
    play music back_home_music
    ""
    hide screen text_scene with usual_transition 
    show screen back_home_scene_1 with usual_transition
    if branch_choice_a_b == 1:
        speech.main "...вот, а потом было ещё три пары. Это просто так... странно? Что всё не так плохо."
        speech.main "Я думал, знакомства заводить сложнее. А она ещё и помогла мне найти кабинет."
        speech.vanya "Бро-о, я говорил, всё норм будет и чтоб ты не кис. Клянусь тапком, говорил."
        speech.main "Кстати, я ведь уже сказал, что она рисует. Я думаю, ты бы нашел с ней общий язык. Тоже этим увлекаешься. Могу дать ее контакты."
        speech.vanya "Эээ... Да я ж не рисую, ты чё... Так, калякаю на листке. Фигня это всё, я любитель. Лучше расскажи, как англ прошел."
        speech.main "Да в целом... неплохо?"
    else:
        speech.main "...вот, а потом было ещё три пары. Знаешь, я познакомился с новыми людьми. Это просто так... странно?"
        speech.main "Что всё не так плохо. Я думал, знакомства заводить сложнее."
        speech.vanya "Я говорил, что все будет пучком. Ты, по-моему, накручиваешь себя."
        speech.main "Возможно. Кстати, я подсел сегодня к чуваку... Вроде, его звали Егор. Он неправильно сказал мне имя преподавателя, когда я его спросил."
        speech.main "Я мало того опоздал, так ещё и на всю аудиторию назвал физика левым именем. Понимаю, можно было перепутать фамилию и отчество..."
        speech.main "Но он сам {b}правильно{/b} обращался к нему на протяжении всей пары."
        speech.vanya "Ё-маё, вот опять ты накручиваешь."
        speech.main "Мне почему-то кажется, что он сделал это специально."
        speech.vanya "Все путают имена преподавателей вначале учебы. Тем более, зачем бы ему это нужно было, a?"
        speech.vanya "Давай лучше расскажи, как прошел английский."
        speech.main "Лучше, чем я думал!"
    hide screen back_home_scene_1 with usual_transition
    show screen back_home_scene_2 with usual_transition
    if branch_choice_a_b == 1:
        speech.main "Я привык всё критиковать, но тут мне правда зашло."
        speech.main "Я думал, что, возможно, стоило выбрать уровень ниже. Теперь так не считаю. Хотя все равно сложно: у меня разговорный не очень сильный."
    else:
        speech.main "Сказал Ксюше до пары, что надо было выбирать уровень ниже. Теперь так не считаю."
        speech.main "Хотя ей, вроде, не особо понравилось."
    menu:
        speech.vanya "О чём базарили-то?"
        "Животные":
            $ player_score += 5
            $ renpy.notify("Почти правильно! Вы получили баллов: 5/12. Всего баллов: " + str(player_score) + ".")
            speech.main "Про животных, ничего необычного."
        "Программирование":
            $ player_score += 10
            $ renpy.notify("Очень близко! Вы получили баллов: 10/12. Всего баллов: " + str(player_score) + ".")
            speech.main "Программирование обсуждали. Мне понравилось, я же типа “шарю”, ха-ха-ха."
        "Злорадство":
            $ player_score += 12
            $ renpy.notify("Правильно! Вы получили баллов: 12/12. Всего баллов: " + str(player_score) + ".")
            speech.main "Шаде... Ше... Schadenfreude. Scha-den-freu-de. Язык сломаешь."
    if branch_choice_a_b == 1:
        speech.vanya "Ого, а мы грэммар решали. Презент симпл и вся ерундень эта."
        speech.vanya "А матеша как? Я так офигел от темпа, ничё толком не записал."
    else:
        speech.vanya "Ого, мы вот просто решали тест."
        speech.vanya "А математика как? Я практически ничего не успел записать."
    speech.vanya "Эй! Уснул что ли?"
    hide screen back_home_scene_2 with usual_transition
    show screen back_home_scene_3 with usual_transition
    if branch_choice_a_b == 1:
        speech.main "Математика? Да там... Ну... Да ничего интересного..."
        speech.main "Сам понимаешь, прилег на парту, а уже конец пары. Время летит..."
    else:
        speech.main "Математика? Да там... Ну... Да ничего интересного..."
        speech.main "Просто.. Сам понимаешь."
    hide screen back_home_scene_3 with usual_transition
    return