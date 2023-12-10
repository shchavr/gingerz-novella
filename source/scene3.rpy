label scene3_script:
    if branch_choice_a_b == 1:
        call canteen_entrance_script
        if branch_choice_1_2 == 1:
            call canteen_valeriya_script
        else:
            call canteen_kseniya_script
        call live_event_script
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
    speech.thought "И правда летит... Вы ещё тут? С первого учебного дня прошло две недели."
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

screen canteen_valeriya_scene_2(how):
    add "bg_kseniya_mch.jpg" fit "fill" at how
    zorder -10

screen canteen_valeriya_scene_3:
    add "bg_room_books.jpg" fit "fill"
    zorder -10

label canteen_valeriya_script:
    show screen canteen_valeriya_scene_1(None) with usual_transition
    speech.thought "Вообще, я так не делаю, но тогда подумал: “Ну а чё нет?”"
    speech.thought "В общем, я взял еду и подсел."
    show screen canteen_valeriya_scene_1(blur_out)
    show screen portrait_valeriya_undressed_normal(motion.move(.7)) with usual_transition
    show screen portrait_main_undressed_normal(motion.move(.3)) with usual_transition
    show screen portrait_main_undressed_normal(motion.focus(.3))
    speech.main "Привет... Тут практически все столики заняты... Можно сяду?"
    show screen portrait_main_undressed_normal(motion.unfocus(.3))
    show screen portrait_valeriya_undressed_normal(motion.focus(.7))
    speech.valeriya "Да, силь ву пле."
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
    speech.thought "Всё. Поговорили. Я больше ничего не сказал, а она просто ела. Вот вам и силь ву пле."
    hide screen portrait_valeriya_undressed_sad with usual_transition
    speech.thought "Потом ушла, поэтому я остался за пустым столом."
    show screen canteen_valeriya_scene_1(blur_in)
    hide screen portrait_main_undressed_sad with usual_transition
    Character("???", kind = speech.kseniya) "Приветствую. Тут свободное место, если мне не изменяет мое зрение."
    hide screen canteen_valeriya_scene_1 with usual_transition
    show screen canteen_valeriya_scene_2(None) with usual_transition
    Character("???", kind = speech.kseniya) "Можно я здесь сяду, если это не доставит неудобств?"
    speech.main "Э-э... Да без б."
    show screen canteen_valeriya_scene_2(blur_out)
    show screen portrait_main_undressed_normal(motion.move(.7)) with usual_transition
    show screen portrait_kseniya_undressed_normal(motion.move(.3)) with usual_transition
    show screen portrait_kseniya_undressed_normal(motion.focus(.3))
    Character("???", kind = speech.kseniya) "Вижу, у тебя тоже бесплатный завтрак. Говорят, каша вкусная сегодня. Это правда?"
    show screen portrait_kseniya_undressed_normal(motion.unfocus(.3))
    show screen portrait_main_undressed_normal(motion.focus(.7))
    speech.main "Каша — бомба!"
    show screen portrait_main_undressed_normal(motion.unfocus(.7))
    show screen portrait_kseniya_undressed_normal(motion.focus(.3))
    Character("???", kind = speech.kseniya) "Ты выглядишь немного испуганным, насколько я могу судить. Мне не доставит сложности уйти, если тебе некомфортно."
    show screen portrait_kseniya_undressed_normal(motion.unfocus(.3))
    show screen portrait_main_undressed_normal(motion.focus(.7))
    speech.main "Да не парься... Меня [player_name] зовут."
    show screen portrait_main_undressed_normal(motion.unfocus(.7))
    show screen portrait_kseniya_undressed_normal(motion.focus(.3))
    speech.kseniya "А я Ксения, очень приятно! Твое лицо мне кажется невероятно знакомым..."
    speech.kseniya "Не могу припомнить, где я тебя видела. Может ты сможешь мне подсказать?"
    show screen portrait_kseniya_undressed_normal(motion.unfocus(.3))
    show screen portrait_main_undressed_normal(motion.focus(.7))
    speech.main "На парах? А так, я всегда дома сижу."
    show screen portrait_main_undressed_normal(motion.unfocus(.7))
    hide screen portrait_kseniya_undressed_normal
    show screen portrait_kseniya_undressed_happy(motion.move(.3))
    show screen portrait_kseniya_undressed_happy(motion.focus(.3))
    speech.kseniya "Конечно! Практики по физике. Как же я сразу не вспомнила."
    show screen portrait_kseniya_undressed_happy(motion.unfocus(.3))
    hide screen portrait_main_undressed_normal with usual_transition
    hide screen portrait_kseniya_undressed_happy with usual_transition
    show screen canteen_valeriya_scene_2(blur_in)
    speech.thought "Ну вот и диало-о-ог! Вы тоже офигели от того, насколько культурно Ксю... Ксения разговаривает? Выяснилось, что она на одном направлении со мной, в свободное время преподает и работает."
    speech.thought "Она знает как-то слишком много рандомных фактов, про которые я даже не слышал. По математике, например."
    speech.thought "А ещё мы информатику на одинаковый балл написали. Вот такие приколы."
    speech.kseniya "... вообще, я к своей знакомой хотела успеть. Мы в одно время эти завтраки забираем."
    speech.main "Не к Лере случайно?"
    menu:
        speech.kseniya "К Валерии, верно! Вы знакомы?"
        "Конечно":
            speech.main "Я много слышал от разных людей... Думаю, можно сказать да."
            speech.kseniya "Невероятно! Вот к ней я и шла. Ну, она, может, решила в другое время забрать."
            speech.thought "Я рассказал всю эту историю с кашей. В мельчайших подробностях и без комочков."
            speech.kseniya "Точно! Я вспомнила. У неё же репетиция дебюта в радике. Вот она и ушла. Кстати о мероприятиях! Можно будет сходить куда-нибудь."
            speech.main "Ну... Не знаю, я не в этой теме, так что без меня."
        "Наверное":
            speech.main "Ну, почти знакомы."
            speech.kseniya "Необычно, расскажешь подробней?"
            speech.thought "Я рассказал всю эту историю с кашей. В мельчайших подробностях и без комочков."
            speech.main "Да, караул."
            speech.kseniya "Какой... диалог... Содержательный."
            speech.kseniya "Я думаю, познакомлю вас как-нибудь. Может на каком-нибудь мероприятии... Ты не хочешь куда-нибудь сходить?"
            speech.main "Не, бред, я не пойду."
            speech.kseniya "Да брось, первокурсником раз в жизни только будешь. А посидеть в комнате всегда успеешь."
            speech.main "Где-то я уже это слышал..."
            speech.kseniya "В общем, я поищу, куда можно сходить. Ты слышал, что там происходит вообще? Один парень {a=https://telesco.pe/rtf_urfu/1711}сбрил бровь{/a} прямо на сцене."
            speech.main "Офигеть! Фу..."
        "Никогда":
            speech.main "Ещё нет. Думаю, вряд ли когда-то будем."
            speech.kseniya "Почему так категорично?"
            speech.thought "Я рассказал всю эту историю с кашей. В мельчайших подробностях и без комочков."
            speech.main "Как-то это было... Высокомерно?"
            speech.kseniya "..."
            speech.main "Ксюш? О чем задумалась?"
            speech.kseniya "Я? Ничего. А можешь дать мне свой ВК?"
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

screen canteen_kseniya_scene_2(how):
    add "bg_kseniya_mch.jpg" fit "fill" at how
    zorder -10

screen canteen_kseniya_scene_3:
    add "bg_room_books.jpg" fit "fill"
    zorder -10

label canteen_kseniya_script:
    show screen canteen_kseniya_scene_1 with usual_transition
    speech.thought "Да нет. Вы бы сели? Хотя, если вы выбрали этот вариант, то я знаю ответ. Глупо садиться к человеку, ещё и здесь, поэтому мое место за единственным свободным столиком."
    speech.thought "Хотя, может и не совсем... Там, вроде, чьи-то вещи."
    Character("???", kind = speech.kseniya) "Приветствую, тут занято."
    hide screen canteen_kseniya_scene_1 with usual_transition
    show screen canteen_kseniya_scene_2(None) with usual_transition
    speech.main "Да тут некуда сесть, но я могу ливнуть, если некомфортно."
    show screen canteen_kseniya_scene_2(blur_out)
    show screen portrait_main_undressed_normal(motion.move(.7)) with usual_transition
    show screen portrait_kseniya_undressed_normal(motion.move(.3)) with usual_transition
    show screen portrait_kseniya_undressed_normal(motion.focus(.3))
    Character("???", kind = speech.kseniya) "Вижу, у тебя тоже бесплатный завтрак. Говорят, каша вкусная сегодня. Это правда?"
    show screen portrait_kseniya_undressed_normal(motion.unfocus(.3))
    show screen portrait_main_undressed_normal(motion.focus(.7))
    speech.main "Каша — бомба!"
    show screen portrait_main_undressed_normal(motion.unfocus(.7))
    show screen portrait_kseniya_undressed_normal(motion.focus(.3))
    Character("???", kind = speech.kseniya) "Ты выглядишь немного испуганным, насколько я могу судить. Мне не доставит сложности уйти, если тебе некомфортно."
    show screen portrait_kseniya_undressed_normal(motion.unfocus(.3))
    show screen portrait_main_undressed_normal(motion.focus(.7))
    speech.main "Да не парься... Меня [player_name] зовут."
    show screen portrait_main_undressed_normal(motion.unfocus(.7))
    show screen portrait_kseniya_undressed_normal(motion.focus(.3))
    speech.kseniya "А я Ксения, очень приятно! Твое лицо мне кажется невероятно знакомым..."
    speech.kseniya "Не могу припомнить, где я тебя видела. Может ты сможешь мне подсказать?"
    show screen portrait_kseniya_undressed_normal(motion.unfocus(.3))
    show screen portrait_main_undressed_normal(motion.focus(.7))
    speech.main "На парах? А так, я всегда дома сижу."
    show screen portrait_main_undressed_normal(motion.unfocus(.7))
    hide screen portrait_kseniya_undressed_normal
    show screen portrait_kseniya_undressed_happy(motion.move(.3))
    show screen portrait_kseniya_undressed_happy(motion.focus(.3))
    speech.kseniya "Конечно! Практики по физике. Как же я сразу не вспомнила."
    show screen portrait_kseniya_undressed_happy(motion.unfocus(.3))
    hide screen portrait_main_undressed_normal with usual_transition
    hide screen portrait_kseniya_undressed_happy with usual_transition
    show screen canteen_kseniya_scene_2(blur_in)
    speech.thought "После небольшого диалога я узнал, что это Ксюша. Она на одном направлении со мной, в свободное время преподает и работает."
    speech.thought "Знает как-то слишком много рандомных фактов, про которые я даже не слышал. По математике, например."
    speech.thought "А ещё мы информатику на одинаковый балл написали. Вот такие приколы."
    speech.kseniya "... вчера я весь вечер учила коллоквиум, представляешь? Позавчера ходила на волонтерство."
    speech.kseniya "Ещё чуть позже была на олимпиаде. Завтра идём с одной из моих знакомых на мероприятие."
    speech.main "Я вижу в этом намёк..."
    speech.kseniya "Ни в коем случае, но если у тебя есть желание и возможности..."
    speech.main "Я не любитель подобных мероприятий."
    speech.kseniya "Каждый когда-то должен сделать исключение, по-моему мнению."
    speech.main "Слушай, мне правда всё это не интересно. Пустая трата времени."
    speech.kseniya "Однако, вдруг не пустая?"
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













screen live_event_scene_1:
    add "bg_before_event.jpg" fit "fill"
    zorder -10

screen live_event_scene_2(how):
    add "bg_concert_hall.jpg" fit "fill" at how
    zorder -10

label live_event_script:
    show screen live_event_scene_1 with usual_transition
    speech.kseniya "Приветствую!"
    speech.main "Я до сих пор не понимаю, почему я здесь."
    speech.valeriya "“Не любитель движа”?! “Не пойду, не пойду”? Интересный ты конечно!"
    speech.main "И тебе привет. А ты откуда знаешь?.."
    speech.valeriya "Не-е-ет, это ты... ты откуда знаешь номер Ксюши? Нашёл меро раньше неё. Ну ты даёшь."
    speech.main "Э-э, чего?!"
    speech.kseniya "Мы ушли с пар, чтоб сходить сюда. Я до сих пор сомневаюсь, стоило ли это того."
    speech.kseniya "Всё-таки пропускать пару по аналитической геометрии..."
    speech.valeriya "Ушли по уважительной причине! Всё окей."
    speech.valeriya "Гоу найдем аудиторию, пять минут до начала осталось."
    hide screen live_event_scene_1 with usual_transition
    show screen live_event_scene_2(None) with usual_transition
    show screen live_event_scene_2(blur_out)
    show screen portrait_main_dressed_sad(motion.move(.3)) with usual_transition
    show screen portrait_kseniya_dressed_normal(motion.move(.7)) with usual_transition
    show screen portrait_kseniya_dressed_normal(motion.focus(.7))
    speech.kseniya "Я по дороге прочитала, что здесь будет что-то про навыки для ИИ. Ты зарегистрировал нашу команду?"
    show screen portrait_kseniya_dressed_normal(motion.unfocus(.7))
    hide screen portrait_main_dressed_sad
    show screen portrait_main_dressed_surprised(motion.move(.3))
    show screen portrait_main_dressed_surprised(motion.focus(.3))
    speech.main "Я? Так это ты меня позвала!"
    show screen portrait_main_dressed_surprised(motion.unfocus(.3))
    hide screen portrait_kseniya_dressed_normal
    show screen portrait_kseniya_dressed_surprised(motion.move(.7))
    show screen portrait_kseniya_dressed_surprised(motion.focus(.7))
    speech.kseniya "[player_name], с тобой всё хорошо? Я переживаю и нахожу твои вопросы немного неуместными."
    show screen portrait_kseniya_dressed_surprised(motion.unfocus(.7))
    show screen portrait_kseniya_dressed_surprised(motion.move(.7, -.2, .2))
    show screen portrait_main_dressed_surprised(motion.move(.3, -.1, .2))
    show screen portrait_valeriya_dressed_normal(motion.move(.8)) with usual_transition
    show screen portrait_valeriya_dressed_normal(motion.focus(.8))
    speech.valeriya "Вика вроде бы зарегала."
    show screen portrait_valeriya_dressed_normal(motion.unfocus(.8))
    hide screen portrait_main_dressed_surprised
    show screen portrait_main_dressed_sad(motion.move(.2))
    hide screen portrait_kseniya_dressed_surprised
    show screen portrait_kseniya_dressed_sad(motion.move(.5))
    show screen portrait_kseniya_dressed_sad(motion.focus(.5))
    speech.kseniya "Отлично, а она..."
    show screen portrait_kseniya_dressed_sad(motion.unfocus(.5))
    hide screen portrait_valeriya_dressed_normal
    show screen portrait_valeriya_dressed_happy(motion.move(.5))
    show screen portrait_valeriya_dressed_happy(motion.focus(.8))
    speech.valeriya "Опоздает минут на пять."
    show screen portrait_valeriya_dressed_happy(motion.unfocus(.8))
    show screen live_event_scene_2(blur_in)
    hide screen portrait_main_dressed_sad with usual_transition
    hide screen portrait_valeriya_dressed_happy with usual_transition
    hide screen portrait_kseniya_dressed_sad with usual_transition
    Character("Ведущий", kind = speech.generic) "Н-у-у-у что-о-о-о, первокурсники... Всем огромный приве-е-ет! Вы готовы пошуме-е-еть?"
    Character("Ведущий", kind = speech.generic) "Сегодня мы с вами займемся полезными делами! Вы распределились на команды, список у нас есть."
    Character("Ведущий", kind = speech.generic) "Мы ставим вам баллы — вы выполняете задания. Будут победители, будут подарки! Еще раз... Вы готовы-ы-ы?"
    speech.thought "Зал взорвался. Но я всё ещё не понимал, почему регать команду должен был именно я. И какой ещё номер?"
    speech.thought "И почему за столом Лера не могла сказать ни слова, а тут — силь ву пле."
    Character("Ведущий", kind = speech.generic) "Ваша задача сегодня — угадать, какие навыки придумали для ИИ ваши наставники. Но это не все: нужно угадать и предложить навыки лучше!"
    Character("Ведущий", kind = speech.generic) "Или смешнее. Или глупее. Это на ваш выбор, ха-ха-ха! Вы присылаете ответы в телеграмм и зарабатываете баллы."
    Character("Ведущий", kind = speech.generic) "Все понятно, радисты?"
    speech.viktoriya "Элементарно-о-о-о!"
    speech.narrator "*Вика пробирается сквозь ряды пекусов к нам*"
    speech.viktoriya "Мы сейчас всех сделаем. Всем приветики! Двигайтесь."
    Character("Ведущий", kind = speech.generic) "Внимание на экран!"
    Character("Ведущий", kind = speech.generic) "Наставник номер один: “Я заваливал НТК три раза подряд. Может быть, я бы не ходил на пересдачи, если бы ИИ умел...”"
    Character("Ведущий", kind = speech.generic) "Ваш выход, господа! Телеграм на экране, а ваши баллы у нас. Время пошло!"
    show screen live_event_scene_2(blur_out)
    show screen portrait_viktoriya_undressed_happy(motion.move(.3)) with usual_transition
    show screen portrait_main_undressed_sad(motion.move(.7)) with usual_transition
    show screen portrait_main_undressed_sad(motion.focus(.7))
    speech.main "Мда... Бред."
    show screen portrait_main_undressed_sad(motion.unfocus(.7))
    show screen portrait_viktoriya_undressed_happy(motion.focus(.3))
    speech.viktoriya "Да бро-ось, это ведь интересно. Может, так: “... если бы ИИ умел бы давать ответы на тесты”?"
    speech.viktoriya "“... как только они запускаются в браузере”?"
    show screen portrait_viktoriya_undressed_happy(motion.unfocus(.3))
    show screen portrait_main_undressed_sad(motion.focus(.7))
    speech.main "Нужно что-то пооригинальней."
    show screen portrait_main_undressed_sad(motion.unfocus(.7))
    show screen portrait_viktoriya_undressed_happy(motion.move(.3, -.1, .2))
    show screen portrait_main_undressed_sad(motion.move(.7, .1, .2))
    show screen portrait_kseniya_undressed_normal(motion.move(.5)) with usual_transition
    show screen portrait_kseniya_undressed_normal(motion.focus(.5))
    speech.kseniya "Может быть, стоит рассмотреть такой вариант: “... выставление максимального балла в брс”?"
    show screen portrait_kseniya_undressed_normal(motion.unfocus(.5))
    show screen portrait_viktoriya_undressed_happy(motion.focus(.2))
    speech.viktoriya "Вот это уже хорошо. Может ещё..."
    speech.viktoriya "“... умел блокировать сайты, на которые нам выкладывают тесты”? Так бы их вообще не было."
    show screen portrait_viktoriya_undressed_happy(motion.unfocus(.2))
    show screen portrait_main_undressed_sad(motion.focus(.8))
    speech.main "И мы бы сдавали сессию очно. Не очень хороший план, согласись."
    show screen portrait_main_undressed_sad(motion.unfocus(.8))
    hide screen portrait_viktoriya_undressed_happy with usual_transition
    hide screen portrait_main_undressed_sad with usual_transition
    hide screen portrait_kseniya_undressed_normal with usual_transition
    show screen live_event_scene_2(blur_in)
    Character("Ведущий", kind = speech.generic) "Время вышло, готовы к следующему вопросу? Не слышу!"
    Character("Ведущий", kind = speech.generic) "Все правильные ответы будут показаны в конце, а сейчас..."
    speech.thought "В общем, зря я пришел. В чем смысл? Навыки для ИИ. Опять этот ИИ."
    speech.thought "Куда не пойди, везде нейросети. Ещё и баллы потеряли, ничего не успели."
    hide screen live_event_scene_2 with usual_transition
    show screen text_scene("Некоторое время спустя") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen live_event_scene_2(None) with usual_transition
    speech.thought "Мы продули уже в трёх вопросах. Когда я закатил глаза пятый раз подряд, Лера схватила меня за руку и потащила в сторону."
    show screen live_event_scene_2(blur_out)
    show screen portrait_main_undressed_sad(motion.move(.3)) with usual_transition
    show screen portrait_valeriya_undressed_happy(motion.move(.7)) with usual_transition
    show screen portrait_valeriya_undressed_happy(motion.focus(.7))
    speech.valeriya "Мы сейчас вернёмся, пошли отойдём..."
    show screen portrait_valeriya_undressed_happy(motion.unfocus(.7))
    show screen portrait_main_undressed_sad(motion.focus(.3))
    speech.main "Чего тебе?"
    show screen portrait_main_undressed_sad(motion.unfocus(.3))
    show screen portrait_valeriya_undressed_happy(motion.focus(.7))
    speech.valeriya "Слушай, я вижу, ты не любишь всё вот это... Команды, конкурсы."
    speech.valeriya "Но ты ведь уже сюда пришёл. Может постараешься хотя бы?"
    show screen portrait_valeriya_undressed_happy(motion.unfocus(.7))
    show screen portrait_main_undressed_sad(motion.focus(.3))
    speech.main "Я бы с радостью, но задания правда ни о чём."
    show screen portrait_main_undressed_sad(motion.unfocus(.3))
    hide screen portrait_valeriya_undressed_happy
    show screen portrait_valeriya_undressed_normal(motion.move(.7))
    show screen portrait_valeriya_undressed_normal(motion.focus(.7))
    speech.valeriya "Зачем тогда позвал нас сюда?"
    show screen portrait_valeriya_undressed_normal(motion.unfocus(.7))
    hide screen portrait_main_undressed_sad
    show screen portrait_main_undressed_surprised(motion.move(.7))
    show screen portrait_main_undressed_surprised(motion.focus(.3))
    speech.main "Слушай, я никого не..."
    show screen portrait_main_undressed_surprised(motion.unfocus(.3))
    hide screen portrait_valeriya_undressed_normal
    show screen portrait_valeriya_undressed_sad(motion.move(.7))
    show screen portrait_valeriya_undressed_sad(motion.focus(.7))
    speech.valeriya "Ну-ну. Ты вот знаешь... Представь, что ты разработчик."
    show screen portrait_valeriya_undressed_sad(motion.unfocus(.7))
    hide screen portrait_main_undressed_surprised
    show screen portrait_main_undressed_sad(motion.move(.3))
    show screen portrait_main_undressed_sad(motion.focus(.3))
    speech.main "Чего?"
    show screen portrait_main_undressed_sad(motion.unfocus(.3))
    show screen portrait_valeriya_undressed_sad(motion.focus(.7))
    speech.valeriya "Думай, чего людям не хватает."
    speech.valeriya "Тебе тоже сдавать НТК, что бы ты хотел от ИИ?"
    show screen portrait_valeriya_undressed_sad(motion.unfocus(.7))
    hide screen portrait_main_undressed_sad
    show screen portrait_main_undressed_surprised(motion.move(.3))
    show screen portrait_main_undressed_surprised(motion.focus(.3))
    speech.main "Мы в театре что ли? Не буду я никого играть."
    show screen portrait_main_undressed_surprised(motion.unfocus(.3))
    show screen portrait_valeriya_undressed_sad(motion.focus(.7))
    speech.valeriya "Так что бы хотел?"
    show screen portrait_valeriya_undressed_sad(motion.unfocus(.7))
    hide screen portrait_main_undressed_surprised
    show screen portrait_main_undressed_sad(motion.move(.3))
    show screen portrait_main_undressed_sad(motion.focus(.3))
    speech.main "..."
    speech.main "Не знаю, чтобы он слил мне все вопросы и ответы на них."
    show screen portrait_main_undressed_sad(motion.unfocus(.3))
    show screen portrait_valeriya_undressed_sad(motion.focus(.7))
    speech.valeriya "Ну? Разве это плохой ответ?"
    show screen portrait_valeriya_undressed_sad(motion.unfocus(.7))
    show screen portrait_main_undressed_sad(motion.focus(.3))
    speech.main "..."
    show screen portrait_main_undressed_sad(motion.unfocus(.3))
    hide screen portrait_valeriya_undressed_sad
    show screen portrait_valeriya_undressed_normal(motion.move(.3))
    show screen portrait_valeriya_undressed_normal(motion.focus(.7))
    speech.valeriya "Давай пойдём, не кисни."
    show screen portrait_valeriya_undressed_normal(motion.unfocus(.7))
    hide screen portrait_valeriya_undressed_normal with usual_transition
    hide screen portrait_main_undressed_sad with usual_transition
    show screen live_event_scene_2(blur_in)
    speech.thought "..."
    speech.thought "Удивитесь? Мы ответили на все следующие вопросы."
    speech.thought "Я втянулся. Был разработчиком, как завещала Лера. Лично у меня в голове, мы все сидели в офисе и придумывали продукт, который поможет людям."
    speech.thought "Ну, и принесёт нам миллионы. И нет, это не выглядело как глупая фантазия, рождённая детской эйфорией вовлечённости."
    Character("Ведущий", kind = speech.generic) "Наставник номер четыре: “Знаете, мне не хватает кое-чего в этом мире”."
    Character("Ведущий", kind = speech.generic) "“И вряд ли мне это может подарить искусственный интеллект, но может быть...”"
    Character("Ведущий", kind = speech.generic) "“Может быть, это станет реальностью? В ближайшем будущем.” Есть у вас варианты, воспитанники Попова?"
    

    #newmodelhere


    show screen live_event_scene_2(blur_out)
    $ portrait.main.appear("undressed", "sad", .2, False)
    $ portrait.valeriya.appear("undressed", "normal", .4, True)
    $ portrait.viktoriya.appear("undressed", "normal", .6, False) 
    $ portrait.kseniya.appear("undressed", "normal", .8, False) 
    speech.valeriya "Возможность путешествовать? Или открыто посещать другие страны..."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    speech.viktoriya "Готовить еду? Тесто, сырок, пиццу в духовку..."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, None, None, True)
    speech.kseniya "Виктория? Нужно будет сходить в столовую."
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Ха-ха-ха, я шучу!"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "normal", None, True)
    speech.main "Может собеседника? Ну, я имею в виду, возможность поговорить с ИИ не как с роботом, а как с другом. Сейчас ведь правда многие одиноки."
    $ portrait.main.morph(None, "happy", None, None)
    speech.main "А робот есть робот. Если бы у него было что-то вроде своего мнения и своей души..."
    $ portrait.main.morph(None, None, None, False)
    speech.thought "Краем глаза я заметил, что Лера смотрела на меня и улыбалась."
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Офигенно!"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "sad", None, True)
    speech.main "Но это бред..."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "sad", None, True)
    speech.valeriya "Кого это волнует, это классно!"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "ИИ не сможет на таком уровне..."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "happy", None, True)
    speech.valeriya "Ну если ты станешь разработчиком, то точно сможет. Я отправила."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.disappear()
    $ portrait.valeriya.disappear()
    $ portrait.viktoriya.disappear() 
    $ portrait.kseniya.disappear()
    show screen live_event_scene_2(blur_in)
    
    Character("Ведущий", kind = speech.generic) "Мы дождались ответа всех команд, внимание на экран!"
    Character("Ведущий", kind = speech.generic) "Наставник четыре: “Забавно, но мне бы хотелось верить, что ИИ будет неким товарищем человека”."
    Character("Ведущий", kind = speech.generic) "“Знаете, не просто помогать ему в программировании, но ещё и сочувствовать”."
    Character("Ведущий", kind = speech.generic) "“А сейчас на смс 'мне плохо' он может ответить только 'настоятельно рекомендуется обратиться за медицинской помощью'”."
    Character("Ведущий", kind = speech.generic) "Вот такой ответ наставника группы РИ-130918... Вроде бы у нас есть команды, которые угадали..."
    Character("Ведущий", kind = speech.generic) "“Рекурсивные пряники”, в точку! Ха-ха, смешное название, ребят, двадцать баллов ваши!"
    speech.thought "Нет, не надо вопросов. Вика зарегала нашу команду под именем “Рекурсивные пряники”. Я не знаю, почему."
    return