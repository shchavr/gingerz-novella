label scene2_script:
    call street_monologue_script from _call_street_monologue_script
    call rtf_watchwoman_script from _call_rtf_watchwoman_script
    call rtf_classroom_script from _call_rtf_classroom_script
    if branch_choice_a_b == 1:
        call gallery_dialogue_script from _call_gallery_dialogue_script
        call english_classroom_script from _call_english_classroom_script
        call back_home_script from _call_back_home_script
    else:
        call first_desk_script from _call_first_desk_script
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

label street_monologue_script:
    show screen street_monologue_scene_1 with usual_transition
    speech.thought "Теперь вы знаете моё имя, место, где я учусь, и расписание на понедельник. Что про меня ещё нужно знать?"
    hide screen street_monologue_scene_1 with usual_transition
    show screen street_monologue_scene_2 with usual_transition
    speech.thought "Я обычный первокурсник, вернее сказать, пекус. Живу в центре Екатеринбурга в {a=https://vk.com/urfu9sk}{i}9ск{/i}{/a} и сейчас иду на свой {a=https://vk.com/thefirstdayurfu}{i}первый день в Уральском Федеральном{/i}{/a}."
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
    speech.thought "Честно говоря, Мне страшно. Я скорее всего прав насчёт высшего образования в России. И скорее всего захочу забрать документы."
    hide screen street_monologue_scene_5 with usual_transition
    show screen street_monologue_scene_6 with usual_transition
    speech.thought "А вообще, радиофак хорош. Но не с утра, когда ты пробираешься сквозь толпу, за одну минуту до пары."
    hide screen street_monologue_scene_6 with usual_transition
    return












screen rtf_watchwoman_scene_1:
    add "bg_rtf_preentrance.jpg" fit "fill"
    add "ch_watchwoman.png" fit "fill"
    zorder -10

screen rtf_watchwoman_scene_2:
    add "bg_rtf_staircase.jpg" fit "fill"
    zorder -10

label rtf_watchwoman_script:
    show screen rtf_watchwoman_scene_1 with usual_transition
    speech.thought "Ну, кажется, есть ещё одна проблема..."
    Character("Вахтёрша", kind = speech.generic) "{sc=3}Молодой человек! Пропуск мне кто показывать будет?{/sc}"
    menu:
        speech.thought "Что ответить..?"
        "Нагрубить и сказать, что уже показывал":
            $ tmp = "провалена"
            show screen portrait_main_dressed_normal(how = motion.move(.8)) with usual_transition
            show screen portrait_main_dressed_normal(how = motion.focus(.8))
            speech.main "Я это уже сделал, женщина. Внимательней нужно смотреть, или у вас со зрением проблемы?"
            show screen portrait_main_dressed_normal(how = motion.unfocus(.8))
            Character("Вахтёрша", kind = speech.generic) "{sc=5}{color=#FFDDDD}Показывать надо нормально, а ещё язык за зубами держать!{/color}{/sc}"
            Character("Вахтёрша", kind = speech.generic) "{sc=10}{color=#FFBBBB}Я тут не первый год работаю, а вы вот что себе позволяете!!!{/color}{/sc}"
            hide screen portrait_main_dressed_normal
            show screen portrait_main_dressed_surprised(how = motion.move(.8))
            Character("Вахтёрша", kind = speech.generic) "{sc=20}{color=#FF9999}А вы знаете что вообще-то...{/color}{/sc}"
            Character("Вахтёрша", kind = speech.generic) "{sc=50}{color=#FF7777}Мы, пОжИлыЕ лЮди, из-За таКиХ хамОв, как Вы, выНУждЕны пО ТРи смЕНы паХаТь...{/color}{/sc}"
            $ renpy.notify("За ссору с вахтершей вы получили баллов: 0/10. Всего баллов: " + str(player_score) + ".")
            speech.thought "Придётся бежать с поля боя."
            hide screen portrait_main_dressed_surprised with usual_transition
        "Промолчать и показать пропуск еще раз":
            $ tmp = "пройдена"
            $ player_score += 10
            $ renpy.notify("За терпение вы получили баллов: 10/10. Всего баллов: " + str(player_score) + ".")
            Character("Вахтёрша", kind = speech.generic) "Вот так и в следующий раз будьте добры."
    hide screen rtf_watchwoman_scene_1 with usual_transition
    show screen rtf_watchwoman_scene_2 with usual_transition
    speech.thought "Битва с боссом [tmp]. А теперь найти бы аудиторию... Первая — физика."
    hide screen rtf_watchwoman_scene_2 with usual_transition
    return















screen rtf_classroom_scene_1:
    add "bg_rtf_classroom.jpg" fit "fill"
    zorder -10

screen rtf_classroom_scene_2:
    add "bg_rtf_auditorium.jpg" fit "fill"
    zorder -10

label rtf_classroom_script:
    speech.thought "..."
    speech.thought "..."
    speech.thought "???"
    show screen rtf_classroom_scene_1 with usual_transition
    speech.thought "Она оказалась на третьем этаже. Сколько времени я искал? Даже не спрашивайте."
    hide screen rtf_classroom_scene_1 with usual_transition
    show screen rtf_classroom_scene_2 with usual_transition
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

screen gallery_dialogue_scene_2:
    add "bg_gallery_view.jpg" fit "fill"
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
    show screen gallery_dialogue_scene_2 with usual_transition
    show screen portrait_main_dressed_normal(how = motion.move(.3)) with usual_transition
    show screen portrait_viktoriya_undressed_normal(how = motion.move(.7)) with usual_transition
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.7))
    Character("???", kind = speech.viktoriya) "Эй-эй-эй! Куртку нужно сдавать в гардеро-о-об!"
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.7))
    show screen portrait_main_dressed_normal(how = motion.focus(.3))
    speech.main "У меня {a=https://vk.com/wall-133242721_51289}петельки нет{/a}."
    hide screen portrait_main_dressed_normal with usual_transition
    show screen portrait_main_undressed_normal(how = motion.move(.3)) with usual_transition
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.7))
    Character("???", kind = speech.viktoriya) "Эм... Ладно."
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.7))
    show screen portrait_main_undressed_normal(how = motion.focus(.3))
    speech.main "А ещё хорошего настроения. Там на входе..."
    show screen portrait_main_undressed_normal(how = motion.unfocus(.3))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.7))
    Character("???", kind = speech.viktoriya) "Поругался из-за студика?"
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.7))
    show screen portrait_main_undressed_normal(how = motion.focus(.3))
    menu:
        speech.thought "Что ей ответить?"
        "Переборол себя и показал ещё раз":
            show screen portrait_main_undressed_normal(how = motion.unfocus(.3))
            show screen portrait_viktoriya_undressed_normal(how = motion.focus(.7))
            Character("???", kind = speech.viktoriya) "Так и надо было."
        "Да, только толку мало. Я ей слово, а она мне...":
            show screen portrait_main_undressed_normal(how = motion.unfocus(.3))
            show screen portrait_viktoriya_undressed_normal(how = motion.focus(.7))
            Character("???", kind = speech.viktoriya) "Бывает. Привыкнешь."

    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.7))
    show screen portrait_main_undressed_normal(how = motion.focus(.3))
    speech.main "Здесь всегда так с утра? Настроения не было, а сейчас ещё хуже. Да и физику я не понимаю."
    show screen portrait_main_undressed_normal(how = motion.unfocus(.3))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.7))
    Character("???", kind = speech.viktoriya) "Да кто её понимает?"
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.7))
    hide screen portrait_main_undressed_normal
    show screen portrait_main_undressed_sad(how = motion.move(.3))
    show screen portrait_main_undressed_sad(how = motion.focus(.3))
    speech.main "Вдруг у меня специальность будет с ней связана..."
    show screen portrait_main_undressed_sad(how = motion.unfocus(.3))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.7))
    Character("???", kind = speech.viktoriya) "Сочувствую. Ты будущий инженер?"
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.7))
    show screen portrait_main_undressed_sad(how = motion.focus(.3))
    speech.main "Не знаю, будущий бездарь. Меня тянет ко всему по чуть-чуть. Ещё не определился. Знаю, что технарь, и всё."
    show screen portrait_main_undressed_sad(how = motion.unfocus(.3))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.7))
    Character("???", kind = speech.viktoriya) "Ещё есть время! А в ИРИТ-РТФ индивиду..."
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.7))
    show screen portrait_main_undressed_sad(how = motion.focus(.3))
    speech.main "Прекрати говорить рекламными лозунгами, пожалуйста."
    show screen portrait_main_undressed_sad(how = motion.unfocus(.3))
    hide screen portrait_viktoriya_undressed_normal 
    show screen portrait_viktoriya_undressed_happy(how = motion.move(.7)) 
    show screen portrait_viktoriya_undressed_happy(how = motion.focus(.7))
    Character("???", kind = speech.viktoriya) "Шучу, шучу. Но мне кажется, что здесь правда можно найти себя. По крайней мере, стоит попытаться."
    show screen portrait_viktoriya_undressed_happy(how = motion.unfocus(.7))
    show screen portrait_main_undressed_sad(how = motion.focus(.3))
    speech.main "Попытаюсь."
    show screen portrait_main_undressed_sad(how = motion.unfocus(.3))
    show screen portrait_viktoriya_undressed_happy(how = motion.focus(.7))
    Character("???", kind = speech.viktoriya) "Ты прям вообще печальный, может выпьем кофе после пары? Он должен взбодрить."
    show screen portrait_viktoriya_undressed_happy(how = motion.unfocus(.7))
    show screen portrait_main_undressed_sad(how = motion.focus(.3))
    speech.main "Мне нужно будет найти кабинет английского, а это, скорее всего, займет весь перерыв."
    show screen portrait_main_undressed_sad(how = motion.unfocus(.3))
    show screen portrait_viktoriya_undressed_happy(how = motion.focus(.7))
    Character("???", kind = speech.viktoriya) "Хочешь, помогу?"
    show screen portrait_viktoriya_undressed_happy(how = motion.unfocus(.7))
    hide screen portrait_main_undressed_sad 
    show screen portrait_main_undressed_normal(how = motion.move(.3)) 
    show screen portrait_main_undressed_normal(how = motion.focus(.3))
    speech.main "Я только за."
    show screen portrait_main_undressed_normal(how = motion.unfocus(.3))
    show screen portrait_viktoriya_undressed_happy(how = motion.focus(.7))
    Character("???", kind = speech.viktoriya) "Отлично! Осталось пережить пару и не уснуть."
    hide screen portrait_viktoriya_undressed_happy with usual_transition
    hide screen portrait_main_undressed_normal with usual_transition
    hide screen gallery_dialogue_scene_2 with usual_transition
    show screen gallery_dialogue_scene_3 with usual_transition
    Character("Преподаватель", kind = speech.generic) "Галёрка! У нас тут баллистика! Разговоры прекращаем."
    hide screen gallery_dialogue_scene_3 with usual_transition
    show screen gallery_dialogue_scene_4 with usual_transition
    speech.main "Вот блин."
    hide screen gallery_dialogue_scene_4 with usual_transition
    return










screen english_classroom_scene_1:
    add "bg_rtf_coffeeshop.jpg" fit "fill"
    zorder -10

screen english_classroom_scene_2:
    add "bg_english_classroom.jpg" fit "fill"
    zorder -10

screen english_classroom_scene_3:
    add "bg_english_entrance.jpg" fit "fill"
    zorder -10

label english_classroom_script:
    speech.thought "Мучительно прошла физика, и мы отправились искать кабинет английского."
    show screen english_classroom_scene_1 with usual_transition
    show screen portrait_viktoriya_undressed_normal(how = motion.move(.3)) with usual_transition
    show screen portrait_main_undressed_normal(how = motion.move(.7)) with usual_transition
    show screen portrait_main_undressed_normal(how = motion.focus(.7))
    speech.main "Так что ты там говорила?"
    show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
    Character("???", kind = speech.viktoriya) "Попробуешь угадать мое имя? Знаешь такую фишку, на некоторых смотришь и думаешь: “Во-о-от, это точно идёт Настя”."
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
    show screen portrait_main_undressed_normal(how = motion.focus(.7))
    speech.main "Ну..."
    show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
    Character("???", kind = speech.viktoriya) "Ты кстати похож на [player_name]."
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
    hide screen portrait_main_undressed_normal
    show screen portrait_main_undressed_surprised(how = motion.move(.7))
    show screen portrait_main_undressed_surprised(how = motion.focus(.7))
    speech.main "Офигеть! Как ты..."
    show screen portrait_main_undressed_surprised(how = motion.unfocus(.7))
    hide screen portrait_viktoriya_undressed_normal
    show screen portrait_viktoriya_undressed_happy(how = motion.move(.3))
    show screen portrait_viktoriya_undressed_happy(how = motion.focus(.3))
    Character("???", kind = speech.viktoriya) "Угадала?! Я же говорю! Теперь давай ты, даю тебе пять попыток."
    show screen portrait_viktoriya_undressed_happy(how = motion.unfocus(.3))
    hide screen portrait_main_undressed_surprised
    show screen portrait_main_undressed_normal(how = motion.move(.7))
    while guess_tries < 5:
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
            "Вика":
                jump guess_yes
            "Аня" if not guess_tried_anya:
                $ guess_tried_anya = True
                $ guess_choice = "Аня"
                jump guess_nope
            "Наташа" if not guess_tried_natasha:
                $ guess_tried_natasha = True
                $ guess_choice = "Наташа"
                jump guess_nope
            "Юля" if not guess_tried_ylya:
                $ guess_tried_ylya = True
                $ guess_choice = "Юля"
                jump guess_nope
            "Ева" if not guess_tried_eva:
                $ guess_tried_eva = True
                $ guess_choice = "Ева"
                jump guess_nope
        label guess_nope:
        if guess_tries == 0:
            hide screen portrait_viktoriya_undressed_happy
            show screen portrait_viktoriya_undressed_normal(how = motion.move(.3))
            show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
            Character("???", kind = speech.viktoriya) "Ну не-е-ет."
            show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
        if guess_tries == 1:
            show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
            Character("???", kind = speech.viktoriya) "Крутите барабан дальше. Нет такой буквы!"
            show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
        if guess_tries == 2:
            hide screen portrait_viktoriya_undressed_normal
            show screen portrait_viktoriya_undressed_sad(how = motion.move(.3))
            show screen portrait_viktoriya_undressed_sad(how = motion.focus(.3))
            Character("???", kind = speech.viktoriya) "Чего?! Да какая же я “[guess_choice]”?."
            show screen portrait_viktoriya_undressed_sad(how = motion.unfocus(.3))
        if guess_tries == 3:
            hide screen portrait_viktoriya_undressed_sad
            show screen portrait_viktoriya_undressed_normal(how = motion.move(.3))
            show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
            Character("???", kind = speech.viktoriya) "Думай, думай, Марк!"
            show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
            show screen portrait_main_undressed_normal(how = motion.focus(.7))
            speech.main "Чего? Какой ещё Марк?"
            show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
            show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
            Character("???", kind = speech.viktoriya) "Ну это отсылка на Непобедимого... Ой, забей. Не [guess_choice] я. Последняя попытка!"
            show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
        if guess_tries == 4:
            show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
            $ renpy.notify("Вы не смогли угадать имя. За игру вы получили баллов: 0/10. Всего баллов: " + str(player_score) + ".")
            speech.viktoriya "Всё было куда проще, я Вика."
            show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
            hide screen portrait_viktoriya_undressed_normal with usual_transition
        $ guess_tries += 1
        if False:
            label guess_yes:
            hide screen portrait_viktoriya_undressed_normal
            hide screen portrait_viktoriya_undressed_sad
            show screen portrait_viktoriya_undressed_happy(how = motion.move(.3))
            show screen portrait_viktoriya_undressed_happy(how = motion.focus(.3))
            $ player_score += 10
            $ renpy.notify("Вы угадали! За игру вы получили баллов: 10/10. Всего баллов: " + str(player_score) + ".")
            speech.viktoriya "Бинго-о-о!"
            show screen portrait_viktoriya_undressed_happy(how = motion.unfocus(.3))
            hide screen portrait_viktoriya_undressed_happy with usual_transition
            $ guess_tries = 5
    hide screen portrait_main_undressed_normal with usual_transition
    hide screen english_classroom_scene_1 with usual_transition
    speech.thought "После этого мы долго болтали о всех мероприятиях, которые приготовил для нас вуз."
    
    show screen english_classroom_scene_2 with usual_transition
    show screen portrait_main_undressed_normal(how = motion.move(.7)) with usual_transition
    show screen portrait_viktoriya_undressed_normal(how = motion.move(.3)) with usual_transition
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
    speech.viktoriya "{a=https://urfu.ru/ru/students/leisure/oso/tvorchestvo/tradicionnye-meroprijatija/debjut-pervokursnikov/}Дебют пекусов{/a}? Он будет, правда, ещё нескоро. Говорят, нужно приготовить номер на заданную тему и выступить на сцене."
    speech.viktoriya "Репетиции каждый день, все дела."
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
    show screen portrait_main_undressed_normal(how = motion.focus(.7))
    speech.main "Не люблю подобные мероприятия."
    show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
    speech.viktoriya "Я тоже не вижу в них смысла. Столько сил и времени уходит."
    speech.viktoriya "А знаешь, кто точно пойдет на дебют?"
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
    show screen portrait_main_undressed_normal(how = motion.focus(.7))
    speech.main "Кто?"
    show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
    hide screen portrait_viktoriya_undressed_normal
    show screen portrait_viktoriya_undressed_happy(how = motion.move(.3))
    show screen portrait_viktoriya_undressed_happy(how = motion.focus(.3))
    speech.viktoriya "Леро-о-у! Она всегда за любой движ."
    show screen portrait_viktoriya_undressed_happy(how = motion.unfocus(.3))
    show screen portrait_main_undressed_normal(how = motion.focus(.7))
    speech.main "Это..?"
    show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
    hide screen portrait_viktoriya_undressed_happy
    show screen portrait_viktoriya_undressed_normal(how = motion.move(.3))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
    speech.viktoriya "Вы не знакомы? Странно, мне казалось, она добавила в друзья уже весь универ."
    speech.viktoriya "Может как-нибудь встретитесь. Смотри! Вроде бы, это кабинет английского."
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
    hide screen portrait_viktoriya_undressed_normal with usual_transition
    hide screen portrait_main_undressed_normal with usual_transition
    hide screen english_classroom_scene_2 with usual_transition
    
    show screen english_classroom_scene_3 with usual_transition
    show screen portrait_main_undressed_normal(how = motion.move(.7)) with usual_transition
    show screen portrait_viktoriya_undressed_normal(how = motion.move(.3)) with usual_transition
    show screen portrait_main_undressed_normal(how = motion.focus(.7))
    speech.main "И правда он. Так быстро нашли. Спасибо..?"
    show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
    hide screen portrait_viktoriya_undressed_normal
    show screen portrait_viktoriya_undressed_happy(how = motion.move(.3))
    show screen portrait_viktoriya_undressed_happy(how = motion.focus(.3))
    speech.viktoriya "Рада помочь!"
    show screen portrait_viktoriya_undressed_happy(how = motion.unfocus(.3))
    show screen portrait_main_undressed_normal(how = motion.focus(.7))
    speech.main "Ты мельком сказала, что рисуешь..."
    show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
    hide screen portrait_viktoriya_undressed_happy
    show screen portrait_viktoriya_undressed_normal(how = motion.move(.3))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
    speech.viktoriya "Чисто любительски, может как-нибудь покажу."
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
    show screen portrait_main_undressed_normal(how = motion.focus(.7))
    speech.main "Не было желания стать дизайнером?"
    show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
    hide screen portrait_viktoriya_undressed_normal
    show screen portrait_viktoriya_undressed_happy(how = motion.move(.3))
    show screen portrait_viktoriya_undressed_happy(how = motion.focus(.3))
    speech.viktoriya "Ха-ха-ха, какой из меня дизайнер! Хотя... Не знаю. Я еще не определилась."
    speech.viktoriya "В любом случае, время есть. Если кто-то оценит мои работы, то почему бы и нет."
    show screen portrait_viktoriya_undressed_happy(how = motion.unfocus(.3))
    show screen portrait_main_undressed_normal(how = motion.focus(.7))
    speech.main "У меня сосед по комнате увлекается всем этим. Как это называется? Живопись?"
    speech.main "В общем, тоже творческий человек. Я думаю, он может что-нибудь посоветовать."
    show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
    hide screen portrait_viktoriya_undressed_happy
    show screen portrait_viktoriya_undressed_normal(how = motion.move(.3))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
    speech.viktoriya "Так ты общажный?"
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
    show screen portrait_main_undressed_normal(how = motion.focus(.7))
    speech.main "Есть такое. В девятом живу. Ты из одиннадцатой?"
    show screen portrait_main_undressed_normal(how = motion.unfocus(.7))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
    speech.viktoriya "Из Еката. Могу показать кучу мест, если захочешь. Очень много приезжих, так любопытно за вами наблюдать."
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
    hide screen portrait_main_undressed_normal
    show screen portrait_main_undressed_happy(how = motion.move(.7))
    show screen portrait_main_undressed_happy(how = motion.focus(.7))
    speech.main "Если переживу английский, то с радостью."
    speech.main "Ну, мне не пора бежать. Опаздывать на вторую пару подряд такое себе... Еще и в первый день."
    show screen portrait_main_undressed_happy(how = motion.unfocus(.7))
    show screen portrait_viktoriya_undressed_normal(how = motion.focus(.3))
    speech.viktoriya "Чао, как-нибудь увидимся!"
    show screen portrait_viktoriya_undressed_normal(how = motion.unfocus(.3))
    hide screen portrait_viktoriya_undressed_normal with usual_transition
    hide screen portrait_main_undressed_happy with usual_transition
    hide screen english_classroom_scene_3 with usual_transition
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

label back_home_script:
    show screen text_scene("Вечером этого же дня") with usual_transition
    ""
    hide screen text_scene with usual_transition 
    show screen back_home_scene_1 with usual_transition
    speech.main "...вот, а потом было ещё три пары. Это просто так... странно? Что всё не так плохо."
    speech.main "Я думал, знакомства заводить сложнее. А она ещё и помогла мне найти кабинет."
    speech.vanya "Бро-о, я говорил, всё норм будет и чтоб ты не кис. Клянусь тапком, говорил."
    speech.main "Кстати, я ведь уже сказал, что она рисует. Я думаю, ты бы нашел с ней общий язык. Тоже этим увлекаешься. Могу дать ее контакты."
    speech.vanya "Эээ... Да я ж не рисую, ты чё... Так, калякаю на листке. Фигня это всё, я любитель. Лучше расскажи, как англ прошел."
    speech.main "Да в целом... неплохо?"
    hide screen back_home_scene_1 with usual_transition
    show screen back_home_scene_2 with usual_transition
    speech.main "Я привык всё критиковать, но тут мне правда зашло."
    speech.main "Я думал, что, возможно, стоило выбрать уровень ниже. Теперь так не считаю. Хотя все равно сложно: у меня разговорный не очень сильный."
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
    speech.vanya "Ого, а мы грэммар решали. Презент симпл и вся ерундень эта."
    speech.vanya "А матеша как? Я так офигел от темпа, ничё толком не записал."
    speech.vanya "Эй! Уснул что ли?"
    hide screen back_home_scene_2 with usual_transition
    show screen back_home_scene_3 with usual_transition
    speech.main "Математика? Да там... Ну... Да ничего интересного..."
    speech.main "Сам понимаешь, прилег на парту, а уже конец пары. Время летит..."
    hide screen back_home_scene_3 with usual_transition
    return

















screen first_desk_scene_1:
    zorder -10

label first_desk_script:
    show screen first_desk_scene_1 with usual_transition

    hide screen first_desk_scene_1 with usual_transition
    show screen text_scene(stub)
    ""
    return