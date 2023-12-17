label scene3_script:
    if branch_choice_a_b == 1:
        call canteen_entrance_script
        if branch_choice_1_2 == 1:
           call canteen_valeriya_script
        else:
           call canteen_kseniya_script
        call live_event_script
        call after_show_script
    else:
        show screen text_scene(stub)
        ""
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

define canteen_entrance_music = "Toby Fox — Shop.mp3"
define canteen_entrance_ambient = "Lively Noise.mp3"

label canteen_entrance_script:
    show screen canteen_entrance_scene_1 with usual_transition
    stop music fadeout .5
    play music canteen_entrance_music fadein .5
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
    play ambient canteen_entrance_ambient loop fadein .5
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
    add "bg_room_bed.jpg" fit "fill"
    zorder -10

define canteen_valeriya_sound = "Notification.mp3"
define canteen_valeriya_music = "Toby Fox — Undyne.mp3"

label canteen_valeriya_script:
    show screen canteen_valeriya_scene_1(None) with usual_transition
    speech.thought "Вообще, я так не делаю, но тогда подумал: “Ну а чё нет?”"
    speech.thought "В общем, я взял еду и подсел."
    show screen canteen_valeriya_scene_1(blur_out)
    $ portrait.valeriya.appear("undressed", "normal", .7, False)
    $ portrait.main.appear("undressed", "normal", .3, True)
    speech.main "Привет... Тут практически все столики заняты... Можно сяду?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Да, силь ву пле."
    $ portrait.valeriya.morph(None, None, None, False)
    speech.thought "У неё было такое лицо... Ну, она была чем-то занята. Но сидеть в тишине — мега глупо, да же?  Ну я и..."
    $ portrait.main.morph(None, "sad", None, True)
    speech.main "Ты тоже бесплатный завтрак взяла?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Эм... Ну... да."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Здорово... Вкусная каша?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "sad", None, True)
    speech.valeriya "Вкусная..."
    $ portrait.valeriya.morph(None, None, None, False)
    speech.thought "Всё. Поговорили. Я больше ничего не сказал, а она просто ела. Вот вам и силь ву пле."
    $ portrait.valeriya.disappear()
    speech.thought "Потом ушла, поэтому я остался за пустым столом."
    show screen canteen_valeriya_scene_1(blur_in)
    $ portrait.main.disappear()
    Character("???", kind = speech.kseniya) "Приветствую. Тут свободное место, если мне не изменяет моё зрение."
    hide screen canteen_valeriya_scene_1 with usual_transition
    show screen canteen_valeriya_scene_2(None) with usual_transition
    Character("???", kind = speech.kseniya) "Можно я здесь сяду, если это не доставит неудобств?"
    speech.main "Э-э... Да без б."
    show screen canteen_valeriya_scene_2(blur_out)
    $ portrait.main.appear("undressed", "sad", .7, False)
    $ portrait.kseniya.appear("undressed", "normal", .3, True)
    Character("???", kind = speech.kseniya) "Вижу, у тебя тоже бесплатный завтрак. Говорят, каша вкусная сегодня. Это правда?"
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, "normal", None, True)
    speech.main "Каша — бомба!"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, None, None, True)
    Character("???", kind = speech.kseniya) "Ты выглядишь немного испуганным, насколько я могу судить. Мне не доставит труда уйти, если тебе некомфортно."
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Да не парься... Меня [player_name] зовут."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, "happy", None, True)
    speech.kseniya "А я Ксения, очень приятно! Твоё лицо мне кажется невероятно знакомым..."
    $ portrait.kseniya.morph(None, "normal", None, None)
    speech.kseniya "Не могу припомнить, где я тебя видела. Может ты сможешь мне подсказать?"
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "На парах? А так, я всегда дома сижу."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, "happy", None, True)
    speech.kseniya "Конечно! Практики по физике. Как же я сразу не вспомнила."
    $ portrait.main.disappear()
    $ portrait.kseniya.disappear()
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
    stop ambient fadeout .5
    show screen text_scene("Тем же вечером") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen canteen_valeriya_scene_3 with usual_transition
    stop music fadeout .5
    play music canteen_valeriya_music fadein .5
    speech.thought "Мне пришло сообщение с неизвестного номера."
    play sound canteen_valeriya_sound
    speech.polina_hidden "Завтра. Теплофак. 16:00."
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
    add "bg_room_bed.jpg" fit "fill"
    zorder -10

define canteen_kseniya_sound = "Notification.mp3"
define canteen_kseniya_music = "Toby Fox — Undyne.mp3"

label canteen_kseniya_script:
    show screen canteen_kseniya_scene_1 with usual_transition
    speech.thought "Да нет. Вы бы сели? Хотя, если вы выбрали этот вариант, то я знаю ответ. Глупо садиться к человеку, ещё и здесь, поэтому моё место за единственным свободным столиком."
    speech.thought "Хотя, может и не совсем... Там, вроде, чьи-то вещи."
    Character("???", kind = speech.kseniya) "Приветствую, тут занято."
    hide screen canteen_kseniya_scene_1 with usual_transition
    show screen canteen_kseniya_scene_2(None) with usual_transition
    speech.main "Да тут некуда сесть, но я могу ливнуть, если некомфортно."
    show screen canteen_kseniya_scene_2(blur_out)    
    $ portrait.main.appear("undressed", "sad", .7, False)
    $ portrait.kseniya.appear("undressed", "normal", .3, True)
    Character("???", kind = speech.kseniya) "Вижу, у тебя тоже бесплатный завтрак. Говорят, каша вкусная сегодня. Это правда?"
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, "normal", None, True)
    speech.main "Каша — бомба!"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, None, None, True)
    Character("???", kind = speech.kseniya) "Ты выглядишь немного испуганным, насколько я могу судить. Мне не доставит труда уйти, если тебе некомфортно."
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Да не парься... Меня [player_name] зовут."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, "happy", None, True)
    speech.kseniya "А я Ксения, очень приятно! Твоё лицо мне кажется невероятно знакомым..."
    $ portrait.kseniya.morph(None, "normal", None, None)
    speech.kseniya "Не могу припомнить, где я тебя видела. Может ты сможешь мне подсказать?"
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "На парах? А так, я всегда дома сижу."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, "happy", None, True)
    speech.kseniya "Конечно! Практики по физике. Как же я сразу не вспомнила."
    $ portrait.main.disappear()
    $ portrait.kseniya.disappear()
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
    stop ambient fadeout .5
    show screen text_scene("Тем же вечером") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen canteen_kseniya_scene_3 with usual_transition
    stop music fadeout .5
    play music canteen_kseniya_music fadein .5
    play sound canteen_kseniya_sound
    speech.thought "Тогда она меня, видимо, не услышала, потому что вечером на мой телефон пришло сообщение с неизвестного номера."
    speech.polina_hidden "Завтра. Теплофак. 16:00."
    speech.thought "Променять Джокера и чипсики на мероприятие?"
    speech.thought "Ха-ха-ха-ха-ха!"
    hide screen canteen_kseniya_scene_3 with usual_transition
    return













screen live_event_scene_1:
    add "bg_before_event.jpg" fit "fill"
    showif not asking_smth:
        vbox xpos .08 ypos .15 xanchor .5 yanchor .5:
            imagebutton idle "empty.png" hover "question.png" action Call("gotcha_event_script") at fade_in_out
    zorder -10

screen live_event_scene_2(how):
    add "bg_concert_hall.jpg" fit "fill" at how
    zorder -10

define live_event_music = "Toby Fox — Another Medium.mp3"
define live_event_sound = "Short Applause.mp3"
define gotcha_event_sound = "Positive.mp3"
define live_event_ambient_1 = "Park Noise.mp3"
define live_event_ambient_2 = "Lively Noise.mp3"

label gotcha_event_script:
    if not asking_smth:
        $ asking_smth = True
        play sound gotcha_event_sound
        $ player_score += 10
        $ renpy.notify("Вы нашли секрет! Баллы: 10/10. Всего баллов: " + str(player_score) + ".")
    return

label live_event_script:
    show screen live_event_scene_1 with usual_transition
    $ asking_smth = False
    stop music fadeout .5
    play music live_event_music fadein .5
    play ambient live_event_ambient_1 fadein .5
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
    show screen live_event_scene_2(blur_out) with usual_transition
    stop ambient fadeout .5
    play ambient live_event_ambient_2 loop fadein .5
    $ portrait.main.appear("dressed", "sad", .3, False)
    $ portrait.kseniya.appear("dressed", "normal", .7, True)
    speech.kseniya "Я по дороге прочитала, что здесь будет что-то про навыки для ИИ. Ты зарегистрировал нашу команду?"
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, "surprised", None, True)
    speech.main "Я? Так это ты меня позвала!"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, "surprised", None, True)
    speech.kseniya "[player_name], с тобой всё хорошо? Я переживаю и нахожу твои вопросы немного неуместными."
    $ portrait.kseniya.morph(None, None, .5, False)
    $ portrait.main.morph(None, None, .2, None)
    $ portrait.valeriya.appear("dressed", "normal", .8, True)
    speech.valeriya "Вика вроде бы зарегала."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "sad", None, None)
    $ portrait.kseniya.morph(None, "sad", None, True)
    speech.kseniya "Отлично, а она..."
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "happy", None, True)
    speech.valeriya "Опоздает минут на пять."
    show screen live_event_scene_2(blur_in)
    $ portrait.main.disappear()
    $ portrait.kseniya.disappear()
    $ portrait.valeriya.disappear()
    Character("Ведущий", kind = speech.generic) "Н-у-у-у что-о-о-о, первокурсники... Всем огромный приве-е-ет! Вы готовы пошуме-е-еть?"
    Character("Ведущий", kind = speech.generic) "Сегодня мы с вами займемся полезными делами! Вы распределились на команды, список у нас есть."
    Character("Ведущий", kind = speech.generic) "Мы ставим вам баллы — вы выполняете задания. Будут победители, будут подарки! Ещё раз... Вы готовы-ы-ы?"
    speech.thought "Зал взорвался. Но я всё ещё не понимал, почему регать команду должен был именно я. И какой ещё номер?"
    speech.thought "И почему за столом Лера не могла сказать ни слова, а тут — силь ву пле."
    Character("Ведущий", kind = speech.generic) "Ваша задача сегодня — угадать, какие навыки придумали для ИИ ваши наставники. Но это не всё: нужно угадать и предложить навыки лучше!"
    Character("Ведущий", kind = speech.generic) "Или смешнее. Или глупее. Это на ваш выбор, ха-ха-ха! Вы присылаете ответы в телеграмм и зарабатываете баллы."
    Character("Ведущий", kind = speech.generic) "Всё понятно, радисты?"
    show screen live_event_scene_2(blur_out)
    $ portrait.viktoriya.appear("dressed", "happy", .5, True)
    speech.viktoriya "Элементарно-о-о-о!"
    $ portrait.viktoriya.morph(None, None, None, False)
    speech.narrator "*Вика пробирается сквозь ряды пекусов к нам*"
    $ portrait.viktoriya.morph(None, None, None, True)
    speech.viktoriya "Мы сейчас всех сделаем. Всем приветики! Двигайтесь."
    show screen live_event_scene_2(blur_in)
    $ portrait.viktoriya.disappear()
    Character("Ведущий", kind = speech.generic) "Внимание на экран!"
    Character("Наставник №1", kind = speech.generic) "Я заваливал НТК три раза подряд. Может быть, я бы не ходил на пересдачи, если бы ИИ умел..."
    Character("Ведущий", kind = speech.generic) "Ваш выход, господа! Телеграм на экране, а ваши баллы у нас. Время пошло!"
    show screen live_event_scene_2(blur_out)
    $ portrait.viktoriya.appear("undressed", "happy", .3, False)
    $ portrait.main.appear("undressed", "sad", .7, True)
    speech.main "Мда... Бредятина."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    speech.viktoriya "Да бро-ось, это ведь интересно. Может, так: “... если бы ИИ умел бы давать ответы на тесты”?"
    speech.viktoriya "“... как только они запускаются в браузере”?"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Нужно что-то пооригинальней."
    $ portrait.main.morph(None, None, .8, False)
    $ portrait.viktoriya.morph(None, None, .2, None)
    $ portrait.kseniya.appear("undressed", "normal", .5, True)
    speech.kseniya "Может быть, стоит рассмотреть такой вариант: “... выставление максимального балла в брс”?"
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    speech.viktoriya "Вот это уже хорошо. Может ещё..."
    speech.viktoriya "“... умел блокировать сайты, на которые нам выкладывают тесты”? Так бы их вообще не было."
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "И мы бы сдавали сессию очно. Не очень хороший план, согласись."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "Бе-бе-бе!"
    show screen live_event_scene_2(blur_in)
    $ portrait.main.disappear()
    $ portrait.viktoriya.disappear()
    $ portrait.kseniya.disappear()
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
    $ portrait.main.appear("undressed", "sad", .3, False)
    $ portrait.valeriya.appear("undressed", "happy", .7, True)
    speech.valeriya "Мы сейчас вернёмся, пошли отойдём..."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Чего тебе?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Слушай, я вижу, ты не любишь всё вот это... Команды, конкурсы."
    speech.valeriya "Но ты ведь уже сюда пришёл. Может постараешься хотя бы?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Я бы с радостью, но задания правда ни о чём."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "normal", None, True)
    speech.valeriya "Зачем тогда позвал нас сюда?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "surprised", None, True)
    speech.main "Слушай, я никого не..."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "sad", None, True)
    speech.valeriya "Ну-ну. Ты вот знаешь... Представь, что ты разработчик."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "sad", None, True)
    speech.main "Чего?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Думай, чего людям не хватает."
    speech.valeriya "Тебе тоже сдавать НТК, что бы ты хотел от ИИ?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "surprised", None, True)
    speech.main "Мы в театре что ли? Не буду я никого играть."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Так что бы хотел?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "sad", None, True)
    speech.main "..."
    speech.main "Не знаю, чтобы он слил мне все вопросы и ответы на них."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Ну? Разве это плохой ответ?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "..."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "normal", None, True)
    speech.valeriya "Давай пойдём, не кисни."
    show screen live_event_scene_2(blur_in)
    $ portrait.main.disappear()
    $ portrait.valeriya.disappear()
    speech.thought "..."
    speech.thought "Удивитесь? Мы ответили на все следующие вопросы."
    speech.thought "Я втянулся. Был разработчиком, как завещала Лера. Лично у меня в голове, мы все сидели в офисе и придумывали продукт, который поможет людям."
    speech.thought "Ну, и принесёт нам миллионы. И нет, это не выглядело как глупая фантазия, рождённая детской эйфорией вовлечённости."
    Character("Ведущий", kind = speech.generic) "Итак, наставник номер четыре!"
    Character("Наставник №4", kind = speech.generic) "Знаете, мне не хватает кое-чего в этом мире. И вряд ли мне это может подарить искусственный интеллект, но может быть..."
    Character("Наставник №4", kind = speech.generic) "Может быть, это станет реальностью? В ближайшем будущем. Есть у вас варианты, воспитанники Попова?"
    
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
    $ portrait.valeriya.morph(None, "happy", None, None)
    speech.thought "Краем глаза я заметил, что Лера смотрела на меня и улыбалась."
    speech.thought "Она... гордилась мной?.."
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
    Character("Наставник №4", kind = speech.generic) "Забавно, но мне бы хотелось верить, что ИИ будет неким товарищем человека."
    Character("Наставник №4", kind = speech.generic) "Знаете, не просто помогать ему в программировании, но ещё и сочувствовать."
    Character("Наставник №4", kind = speech.generic) "А сейчас на смс “мне плохо” он может ответить только “настоятельно рекомендуется обратиться за медицинской помощью”."
    Character("Ведущий", kind = speech.generic) "Вот такой ответ наставника группы РИ-130918... Вроде бы у нас есть команды, которые угадали..."
    play sound live_event_sound
    Character("Ведущий", kind = speech.generic) "“Рекурсивные пряники”, в точку! Ха-ха, смешное название, ребят, двадцать баллов ваши!"
    speech.thought "Нет, не надо вопросов. Вика зарегала нашу команду под именем “Рекурсивные пряники”. Я не знаю, почему."
    hide screen live_event_scene_2 with usual_transition
    return














screen after_show_scene_1:
    add "bg_guk_sky.jpg" fit "fill"
    zorder -10

screen after_show_scene_2(how):
    add "bg_street_people.jpg" fit "fill" at how
    zorder -10

screen after_show_scene_3:
    add "bg_nine_sk.jpg" fit "fill"
    zorder -10

screen after_show_scene_4(how):
    add "bg_room_bed.jpg" fit "fill" at how
    zorder -10

define after_show_music_1 = "Toby Fox — Hopes And Dreams.mp3"
define after_show_music_2 = "Toby Fox — Unnecessary Tension.mp3"
define after_show_ambient_1 = "Park Noise.mp3"
define after_show_ambient_2 = "City Noise.mp3"
define after_show_sound = "Notification.mp3"

label after_show_script:
    show screen after_show_scene_1 with usual_transition
    stop music fadeout .5
    play music after_show_music_1 fadein .5
    stop ambient fadeout .5
    play ambient after_show_ambient_1 loop fadein .5
    speech.thought "Мы не выиграли тогда. Нам не хватило 15 баллов, которые мы потеряли на первых вопросах."
    speech.thought "Но, мне казалось, мы получили нечто большее, чем мерч от УрФУ и третье место."
    speech.thought "Хотя что может быть круче толстовок?"
    hide screen after_show_scene_1 with usual_transition
    show screen after_show_scene_2(None) with usual_transition
    stop ambient fadeout .5
    play ambient after_show_ambient_2 loop fadein .5
    speech.thought "Мне вообще не свойственно взаимодействовать с людьми, которых я знаю не так давно, однако я активно участвовал в беседе."
    show screen after_show_scene_2(blur_out)
    $ portrait.viktoriya.appear("dressed", "happy", .5, True)
    speech.thought "Гиперактивность Вики уже не смотрелась так странно."
    $ portrait.viktoriya.morph(None, None, .7, False)
    $ portrait.kseniya.appear("dressed", "happy", .3, True)
    speech.thought "Теперь мне не казалась чуждой заумная манера речи Ксюши."
    $ portrait.viktoriya.morph(None, None, .8, False)
    $ portrait.kseniya.morph(None, None, .2, False)
    $ portrait.valeriya.appear("dressed", "happy", .5, True)
    speech.thought "Лера спустилась с небес и куда-то спрятала былую надменность."
    $ portrait.valeriya.morph(None, None, .6, False)
    $ portrait.main.appear("dressed", "normal", .4, True)
    speech.thought "Мы шли и болтали. Как будто мы знакомы уже год, или пять."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Подождите-е-е!!! А представьте, если сделать так, чтобы по утрам ИИ сам бы выбирал тебе музыку, под которую нужно проснуться."
    speech.valeriya "Например, у тебя сегодня коллоквиум, и он включает тебе {a=https://youtu.be/sXq0qRkghUM?autoplay=1}это{/a}."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, None, None, True)
    speech.viktoriya "Ха-ха-ха-ха, шикарно-о-о-о!"
    $ portrait.viktoriya.morph(None, "normal", None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Или знаете... Играл бы с тобой в игры?"
    $ portrait.main.morph(None, "sad", None, None)
    speech.main "У меня есть куча таких, которые я хочу пройти, но не с кем."
    $ portrait.main.morph(None, "normal", None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Слушайте, настроение бомба! Анекдот?"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.kseniya.morph(None, None, None, True)
    speech.kseniya "Было бы превосходно!"
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Валяй!"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Чтобы не искать каждый раз светофоры, Ваня сходил в МФЦ и получил справку с печатью, что он не робот."
    $ portrait.main.disappear()
    $ portrait.valeriya.disappear()
    $ portrait.kseniya.disappear()
    $ portrait.viktoriya.disappear()
    hide screen after_show_scene_2 with usual_transition
    show screen after_show_scene_3 with usual_transition
    speech.thought "После легендарной шутки мы обсуждали, и обсуждали, и обсуждали искусственный интеллект... Мне тогда казалось, что это не просто мысли на ветер."
    speech.thought "Как будто мы думали над нашим будущим проектом. Впервые за долгое время, мне было {b}правда{/b} хорошо."
    speech.thought "Не знаю, куда делся мой гнев. Почему-то сейчас мне хотелось придумать как можно больше идей."
    hide screen after_show_scene_3 with usual_transition
    show screen after_show_scene_4(blur_out) with usual_transition
    stop ambient fadeout .5
    $ portrait.vanya.appear("undressed", "happy", .5, True) 
    speech.vanya "Чува-ак, я сейчас упаду и не встану... Да ты просто сияешь!"
    $ portrait.vanya.morph(None, None, None, False)
    speech.thought "Я только зашёл в комнату и сразу услышал этот вопрос."
    speech.thought "Потом повернулся к зеркалу и не заметил в себе никаких изменений."
    $ portrait.vanya.morph(None, None, None, True)
    speech.vanya "Глаза горя-ят... Ты втюрился что ли?"
    $ portrait.vanya.morph(None, None, .3, False)
    $ portrait.main.appear("dressed", "normal", .7, True) 
    speech.main "Да ну тебя!"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.vanya.morph(None, "normal", None, True)
    speech.vanya "Я не вижу на тебе толстовки, так что тут только один варик, че-е-eл. Я жду опупенную историю и шлёпаю за пепси." 
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.vanya.disappear()
    $ portrait.main.disappear()
    show screen after_show_scene_4(blur_in)
    speech.thought "Я рассказал Ване суть мероприятия и что мы там делали. Он расстроился, потому что ждал историю про какую-нибудь первокурсницу, но всё равно был за меня рад."
    $ portrait.main.appear("undressed", "normal", .3, False)
    $ portrait.vanya.appear("undressed", "normal", .7, True)
    speech.vanya "Ну кайф бро, ка-a-айф, столько идей нашировертил, ёмаё."
    speech.vanya "Откуда в твоей головешке столько?"
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Да мы как-то вместе шировертили. И ещё наста..."
    $ portrait.main.morph(None, None, None, False)
    stop music fadeout .5
    play music after_show_music_2 fadein .5
    speech.thought "Меня прервал звук уведомления на телефоне."
    play sound after_show_sound
    speech.polina_hidden "Неплохо получилось. Спасибо, что решил пойти."
    speech.thought "Точно, я забыл записать Ксюшу у себя в телефоне. Почему она не пишет мне в вк?"
    $ portrait.vanya.morph(None, None, None, True)
    speech.vanya "Чё там?"
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Ксюша. Пишет, что мы сегодня были хороши."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.vanya.morph(None, None, None, True)
    speech.vanya "Хороши? Да потому что ты набазарил такого. Вы будущие мегамозги, куском пиццы клянусь!"
    $ portrait.main.disappear() 
    $ portrait.vanya.disappear()
    hide screen after_show_scene_4 with usual_transition
    return