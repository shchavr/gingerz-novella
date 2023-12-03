label scene3_script:
    if branch_choice_a_b == 1:
        call canteen_entrance_script
        if branch_choice_1_2 == 1:
            call canteen_valeriya_script
        else:
            call canteen_kseniya_script
    else:
        show screen text_scene(stub)
    return











screen canteen_entrance_scene_1:
    add "bg_nine_summer.jpg" fit "fill"
    zorder -10

screen canteen_entrance_scene_2:
    add "bg_nine_autumn.jpg" fit "fill"
    zorder -10

screen canteen_entrance_scene_3:
    add "bg_canteen_entrance.jpg" fit "fill"
    zorder -10

screen canteen_entrance_scene_4:
    add "bg_canteen_inside.jpg" fit "fill"
    zorder -10
    
screen canteen_entrance_scene_5:
    add "bg_people_eating.jpg" fit "fill"
    zorder -10

screen canteen_entrance_scene_6:
    add "bg_valeriya_eating.jpg" fit "fill"
    zorder -10

label canteen_entrance_script:
    show screen canteen_entrance_scene_1 with usual_transition
    speech.thought "И правда летит... С первого учебного дня прошло две недели."
    speech.thought "Что нового? Пары и учеба."
    hide screen canteen_entrance_scene_1 with usual_transition
    show screen canteen_entrance_scene_2 with usual_transition
    speech.thought "Ну и онлайн курсы ещё."
    speech.thought "Дебют, о котором говорила Вика, совсем скоро пройдет в актовом зале."
    hide screen canteen_entrance_scene_2 with usual_transition
    show screen canteen_entrance_scene_3 with usual_transition
    speech.thought "Ввели {a=https://vk.com/wall-52671067_2437}{i}бесплатные завтраки{/i}{/a} для тех, кто в {color=#FF00FF}профсоюзе{/color}."
    speech.thought "Именно поэтому сейчас я отправляюсь в столовку."
    hide screen canteen_entrance_scene_3 with usual_transition
    show screen canteen_entrance_scene_4 with usual_transition
    speech.thought "Вообще, пока что я мало с кем познакомился. Конечно, я знаю свою группу, других ребят, но близко общаюсь только с Викой и Ваней."
    hide screen canteen_entrance_scene_4 with usual_transition
    show screen canteen_entrance_scene_5 with usual_transition
    speech.thought "Думаю, у меня мало знакомых, потому что я не хожу на все мероприятия, которые проводит универ."
    speech.thought "В отличие от..."
    hide screen canteen_entrance_scene_5 with usual_transition
    show screen canteen_entrance_scene_6 with usual_transition
    speech.thought "... Леры. Про неё много рассказывала Вика."
    speech.thought "Можно сказать я знаю её, не зная её."
    menu:
        speech.thought "А может всё-таки..."
        "Сесть к Лере":
            $ branch_choice_1_2 = 1
        "Сесть отдельно":
            $ branch_choice_1_2 = 2
    hide screen canteen_entrance_scene_6 with usual_transition
    return

















screen canteen_valeriya_scene_1(how):
    add "bg_empty_table.jpg" fit "fill" at how
    zorder -10

screen canteen_valeriya_scene_2:
    add "bg_kseniya_mch.jpg" fit "fill"
    zorder -10

screen canteen_valeriya_scene_3:
    add "bg_room_books.jpg" fit "fill"
    zorder -10

label canteen_valeriya_script:
    show screen canteen_valeriya_scene_1(None) with usual_transition
    speech.thought "Вообще, я так не делаю, но тогда подумал: “Ну а почему бы и нет?”"
    speech.thought "В общем, я взял еду и подсел."
    show screen canteen_valeriya_scene_1(blur_out)
    show screen portrait_valeriya_undressed_normal(motion.move(.7)) with usual_transition
    show screen portrait_main_undressed_normal(motion.move(.3)) with usual_transition
    show screen portrait_main_undressed_normal(motion.focus(.3))
    speech.main "Привет... Тут практически все столики заняты... Можно сяду?"
    show screen portrait_main_undressed_normal(motion.unfocus(.3))
    show screen portrait_valeriya_undressed_normal(motion.focus(.7))
    speech.valeriya "Да, без проблем."
    show screen portrait_valeriya_undressed_normal(motion.unfocus(.7))
    speech.thought "У нее было такое лицо... Ну, она была чем-то занята. Но сидеть в тишине — мега глупо, да же?  Ну я и..."
    hide screen portrait_main_undressed_normal
    show screen portrait_main_undressed_sad(motion.move(.3))
    show screen portrait_main_undressed_sad(motion.focus(.3))
    speech.main "Ты тоже бесплатный завтрак взяла?"
    show screen portrait_main_undressed_sad(motion.unfocus(.3))
    show screen portrait_valeriya_undressed_normal(motion.focus(.7))
    speech.valeriya "Эм... Ну... да."
    show screen portrait_valeriya_undressed_normal(motion.unfocus(.7))
    show screen portrait_main_undressed_sad(motion.focus(.3))
    speech.main "Здорово... Вкусная каша?"
    show screen portrait_main_undressed_sad(motion.unfocus(.3))
    hide screen portrait_valeriya_undressed_normal
    show screen portrait_valeriya_undressed_sad(motion.move(.7))
    show screen portrait_valeriya_undressed_sad(motion.focus(.7))
    speech.valeriya "Вкусная..."
    show screen portrait_valeriya_undressed_sad(motion.unfocus(.7))
    speech.thought "Всё. Поговорили. Я больше ничего не сказал, а она просто ела."
    hide screen portrait_valeriya_undressed_sad with usual_transition
    speech.thought "Потом ушла, поэтому я остался за пустым столом."
    show screen canteen_valeriya_scene_1(blur_in)
    hide screen portrait_main_undressed_sad with usual_transition
    Character("???", kind = speech.kseniya) "Привет... Эмм... Тут практически все столики заняты... Можно сяду?"
    hide screen canteen_valeriya_scene_1 with usual_transition
    show screen canteen_valeriya_scene_2 with usual_transition
    speech.main "Да, без проблем, получается."
    Character("???", kind = speech.kseniya) "У тебя тоже бесплатный завтрак? Говорят, каша вкусная сегодня."
    speech.thought "Мы в матрице?.."
    speech.main "Вкусная. Правда вкусная."
    Character("???", kind = speech.kseniya) "Ты выглядишь каким-то удивлённым."
    speech.main "Не бери в голову. Я [player_name]."
    speech.kseniya "А я Ксюша. Мне кажется, я тебя уже где-то видела... Может..."
    speech.main "На практике по физике?"
    speech.kseniya "Точно, на физике!"
    speech.thought "Ну вот и диалог! Выяснилось, что Ксюша на одном направлении со мной, в свободное время преподает и работает."
    speech.thought "Она знает как-то слишком много рандомных фактов, про которые я даже не слышал. По математике, например."
    speech.thought "А ещё мы информатику на одинаковый балл написали. Вот такие приколы."
    speech.kseniya "... вообще, я к своей знакомой хотела успеть. Мы в одно время эти завтраки забираем."
    speech.main "Не к Лере случайно?"
    menu:
        speech.kseniya "К ней! Вы знакомы?"
        "Конечно":
            speech.main "Я много слышал от разных людей... Думаю, можно сказать да."
            speech.kseniya "Супер! Вот к ней я и шла. Ну, она, может, решила в другое время забрать."
            speech.thought "Я рассказал всю эту историю с кашей. В мельчайших подробностях и без комочков."
            speech.kseniya "Точно! Я вспомнила. У неё же репетиция дебюта в радике. Вот она и ушла. Кстати о мероприятиях! Можно будет сходить куда-нибудь."
            speech.main "Ну... Не знаю, я не в этой теме, так что без меня."
        "Наверное":
            speech.main "Ну, почти знакомы."
            speech.kseniya "Это как?"
            speech.thought "Я рассказал всю эту историю с кашей. В мельчайших подробностях и без комочков."
            speech.kseniya "Ха-ха-ха... Беда."
            speech.kseniya "Я думаю, познакомлю вас как-нибудь. Может на каком-нибудь мероприятии... Ты не хочешь куда-нибудь сходить?"
            speech.main "Я не любитель."
            speech.kseniya "Да брось, первокурсником раз в жизни только будешь. А посидеть в комнате всегда успеешь."
            speech.main "Где-то я уже это слышал..."
            speech.kseniya "В общем, я поищу, куда можно сходить. Ты слышал, что там происходит вообще? Один парень {a=https://telesco.pe/rtf_urfu/1711}сбрил бровь{/a} прямо на сцене."
            speech.main "Фу-у. Именно поэтому не хожу."
        "Никогда":
            speech.main "Ещё нет. Думаю, вряд ли когда-то будем."
            speech.kseniya "О-о-у, почему так категорично?"
            speech.thought "Я рассказал всю эту историю с кашей. В мельчайших подробностях и без комочков."
            speech.main "Как-то это было... Высокомерно?"
            speech.kseniya "..."
            speech.main "Ксюш? О чем задумалась?"
            speech.kseniya "Ничего. А можешь дать мне свой ВК?"
    hide screen canteen_valeriya_scene_2 with usual_transition
    show screen text_scene("Тем же вечером") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen canteen_valeriya_scene_3 with usual_transition
    speech.thought "Мне пришло сообщение с неизвестного номера."
    Character("8-922-xxx-xx-00", kind = speech.egor) "Завтра. Теплофак. 16:00."
    speech.thought "Видимо, Ксюша всё-таки нашла какое-то мероприятие. Собираюсь ли я в своё свободное время тащиться в теплофак?"
    speech.thought "Ха-ха-ха-ха-ха!"
    hide screen canteen_valeriya_scene_3 with usual_transition
    return











screen canteen_kseniya_scene_1:
    add "bg_empty_table.jpg" fit "fill"
    zorder -10

screen canteen_kseniya_scene_2:
    add "bg_kseniya_mch.jpg" fit "fill"
    zorder -10

screen canteen_kseniya_scene_3:
    add "bg_room_books.jpg" fit "fill"
    zorder -10

label canteen_kseniya_script:
    show screen canteen_kseniya_scene_1 with usual_transition
    speech.thought "Да нет. Глупо садиться к человеку, ещё и здесь, поэтому мое место за единственным свободным столиком."
    speech.thought "Хотя, может и не совсем... Там, вроде, чьи-то вещи."
    Character("???", kind = speech.kseniya) "Ой."
    hide screen canteen_kseniya_scene_1 with usual_transition
    show screen canteen_kseniya_scene_2 with usual_transition
    speech.main "Тут просто вроде было свободно. Ну я и сел."
    Character("???", kind = speech.kseniya) "Я отходила взять вилку."
    speech.main "Могу отсесть, если тебе некомфортно..."
    Character("???", kind = speech.kseniya) "Да ничего страшного, сиди. У тебя тоже бесплатный завтрак? Говорят, каша вкусная сегодня. Или врут?"
    speech.main "Да не знаю, ещё не успел попробовать."
    Character("???", kind = speech.kseniya) "Мне кажется, я тебя уже где-то видела. Может..."
    speech.main "На практике по физике? Мне твоё лицо тоже знакомым кажется."
    Character("???", kind = speech.kseniya) "Точно!" 
    speech.thought "После небольшого диалога я узнал, что это Ксюша. Она на одном направлении со мной, в свободное время преподает и работает."
    speech.thought "Знает как-то слишком много рандомных фактов, про которые я даже не слышал. По математике, например."
    speech.thought "А ещё мы информатику на одинаковый балл написали. Вот такие приколы."
    speech.kseniya "... а вчера я весь вечер учила коллоквиум, пять часов убила."
    speech.main "А как же оставить всё на последний момент? Завтра же день есть."
    speech.kseniya "Хотели сходить с Лерой на одно мероприятие... Но команда из двух человек и не команда совсем."
    speech.main "Я вижу в этом намёк..."
    speech.kseniya "... нам так хотелось бы поучаствовать! Может ты хочешь..."
    speech.main "Я не любитель подобных мероприятий."
    speech.kseniya "А если один раз сделать исключение?"
    speech.main "Слушай, мне правда всё это не интересно. Пустая трата времени."
    speech.kseniya "А вдруг не пустая?"
    speech.main "Ксюш... Я хочу поесть чипсы и пересмотреть Джокера."
    speech.main "Без обид."
    hide screen canteen_kseniya_scene_2 with usual_transition
    show screen text_scene("Тем же вечером") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen canteen_kseniya_scene_3 with usual_transition
    speech.thought "Тогда она меня, видимо, не услышала, потому что вечером на мой телефон пришло сообщение с неизвестного номера."
    Character("8-922-xxx-xx-00", kind = speech.egor) "Завтра. Теплофак. 16:00."
    speech.thought "Променять Джокера и чипсики на мероприятие?"
    speech.thought "Ха-ха-ха-ха-ха!"
    hide screen canteen_kseniya_scene_3 with usual_transition
    return