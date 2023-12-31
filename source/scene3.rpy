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
        call before_argument_script
        call coffee_argument_script
        if branch_choice_1_2 == 1:
            call cat_cafe_script
        else:
            if branch_choice_x_y == 1:
                call bar_script
                call after_bar_script
                if branch_choice_alpha_beta == 1:
                    call history_class_script
            else:
                call history_alternative_script
                call snow_games_script
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
define canteen_entrance_sound = "Negative.mp3"

label canteen_entrance_script:
    show screen canteen_entrance_scene_1 with usual_transition
    stop music fadeout .5
    play music canteen_entrance_music fadein .5
    speech.main "Время летит..."
    hide screen canteen_entrance_scene_1 with usual_transition
    show screen canteen_entrance_scene_2 with usual_transition
    speech.thought "И правда летит...{w} Вы ещё тут?{w} С первого учебного дня прошло две недели.{w} Что нового?{w} Пары и учеба.{w} Ну и онлайн курсы ещё."
    hide screen canteen_entrance_scene_2 with usual_transition
    show screen canteen_entrance_scene_3 with usual_transition
    speech.thought "Дебют, о котором говорила Вика, совсем скоро пройдет в актовом зале."
    speech.thought "Ввели {a=https://vk.com/wall-52671067_2437}{i}бесплатные завтраки{/i}{/a} для тех, кто в {color=#FF00FF}профсоюзе{/color}.{w} Именно поэтому сейчас я отправляюсь в столовку."
    hide screen canteen_entrance_scene_3 with usual_transition
    show screen canteen_entrance_scene_4 with usual_transition
    play ambient canteen_entrance_ambient loop fadein .5
    speech.thought "Вообще, пока что я мало с кем познакомился.{w} Конечно, я знаю свою группу, других ребят, но близко общаюсь только с Викой и Ваней."
    hide screen canteen_entrance_scene_4 with usual_transition
    show screen canteen_entrance_scene_5 with usual_transition
    speech.thought "Думаю, у меня мало знакомых, потому что я не хожу на все мероприятия, которые проводит универ.{w} В отличие от..."
    hide screen canteen_entrance_scene_5 with usual_transition
    show screen canteen_entrance_scene_6 with usual_transition
    speech.thought "... Леры.{w} Про неё много рассказывала Вика.{w} Можно сказать я знаю её, не зная её."
    label canteen_entrance_again:
    menu:
        speech.thought "А может всё-таки..."
        "{color=#FF3838}[[40]{/color} Сесть к Лере" if player_score < 40:
            play sound canteen_entrance_sound
            $ renpy.notify("У вас недостаточно очков.")
            jump canteen_entrance_again
        "{color=#38FF38}[[40]{/color} Сесть к Лере" if player_score >= 40:
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
    speech.thought "Вообще, я так не делаю, но тогда подумал: “Ну а чё нет?”{w} В общем, я взял еду и подсел."
    show screen canteen_valeriya_scene_1(blur_out)
    $ portrait_valeriya.appear("undressed", "normal", .7, False)
    $ portrait_main.appear("undressed", "normal", .3, True)
    speech.main "Привет...{w} Тут практически все столики заняты...{w} Можно сяду?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Да, силь ву пле."
    $ portrait_valeriya.morph(None, None, None, False)
    speech.thought "У неё было такое лицо...{w} Ну, она была чем-то занята.{w} Но сидеть в тишине — мега глупо, да же? Ну я и..."
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "Ты тоже бесплатный завтрак взяла?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Эм...{w} Ну... да."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Здорово...{w} Вкусная каша?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "Вкусная..."
    $ portrait_valeriya.morph(None, None, None, False)
    speech.thought "Всё.{w} Поговорили.{w} Я больше ничего не сказал, а она просто ела.{w} Вот вам и силь ву пле."
    $ portrait_valeriya.disappear()
    speech.thought "Потом ушла, поэтому я остался за пустым столом."
    show screen canteen_valeriya_scene_1(blur_in)
    $ portrait_main.disappear()
    Character("???", kind = speech.kseniya) "Приветствую.{w} Тут свободное место, если мне не изменяет моё зрение."
    hide screen canteen_valeriya_scene_1 with usual_transition
    show screen canteen_valeriya_scene_2(None) with usual_transition
    Character("???", kind = speech.kseniya) "Можно я здесь сяду, если это не доставит неудобств?"
    speech.main "Э-э...{w} Да без б."
    show screen canteen_valeriya_scene_2(blur_out)
    $ portrait_main.appear("undressed", "sad", .7, False)
    $ portrait_kseniya.appear("undressed", "normal", .3, True)
    Character("???", kind = speech.kseniya) "Вижу, у тебя тоже бесплатный завтрак.{w} Говорят, каша вкусная сегодня. Это правда?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, "normal", None, True)
    speech.main "Каша — бомба!"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    Character("???", kind = speech.kseniya) "Ты выглядишь немного испуганным, насколько я могу судить.{w} Мне не доставит труда уйти, если тебе некомфортно."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Да не парься...{w} Меня [player_name] зовут."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "happy", None, True)
    speech.kseniya "А я Ксения, очень приятно!{w} Твоё лицо мне кажется невероятно знакомым..."
    $ portrait_kseniya.morph(None, "normal", None, None)
    speech.kseniya "Не могу припомнить, где я тебя видела.{w} Может ты сможешь мне подсказать?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "На парах?{w} А так, я всегда дома сижу."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "happy", None, True)
    speech.kseniya "Конечно! Практики по физике.{w} Как же я сразу не вспомнила."
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    show screen canteen_valeriya_scene_2(blur_in)
    speech.thought "Ну вот и диало-о-ог!{w} Вы тоже офигели от того, насколько культурно Ксю...{w} Ксения разговаривает?{w} Выяснилось, что она на одном направлении со мной, в свободное время преподает и работает."
    speech.thought "Она знает как-то слишком много рандомных фактов, про которые я даже не слышал.{w} По математике, например.{w} А ещё мы информатику на одинаковый балл написали.{w} Вот такие приколы."
    speech.kseniya "... вообще, я к своей знакомой хотела успеть.{w} Мы в одно время эти завтраки забираем."
    speech.main "Не к Лере случайно?"
    menu:
        speech.kseniya "К Валерии, верно! Вы знакомы?"
        "Конечно":
            speech.main "Я много слышал от разных людей...{w} Думаю, можно сказать да."
            speech.kseniya "Невероятно!{w} Вот к ней я и шла.{w} Ну, она, может, решила в другое время забрать."
            speech.thought "Я рассказал всю эту историю с кашей.{w} В мельчайших подробностях и без комочков."
            speech.kseniya "Точно! Я вспомнила.{w} У неё же репетиция дебюта в радике. Вот она и ушла.{w} Кстати о мероприятиях! Можно будет сходить куда-нибудь."
            speech.main "Ну...{w} Не знаю, я не в этой теме, так что без меня."
        "Наверное":
            speech.main "Ну, почти знакомы."
            speech.kseniya "Необычно, расскажешь подробней?"
            speech.thought "Я рассказал всю эту историю с кашей.{w} В мельчайших подробностях и без комочков."
            speech.main "Да, караул."
            speech.kseniya "Какой...{w} диалог...{w} Содержательный."
            speech.kseniya "Я думаю, познакомлю вас как-нибудь. Может на каком-нибудь мероприятии...{w} Ты не хочешь куда-нибудь сходить?"
            speech.main "Не, бред, я не пойду."
            speech.kseniya "Да брось, первокурсником раз в жизни только будешь.{w} А посидеть в комнате всегда успеешь."
            speech.main "Где-то я уже это слышал..."
            speech.kseniya "В общем, я поищу, куда можно сходить.{w} Ты слышал, что там происходит вообще?{w} Один парень {a=https://telesco.pe/rtf_urfu/1711}сбрил бровь{/a} прямо на сцене."
            speech.main "Офигеть!{w} Фу..."
        "Никогда":
            speech.main "Ещё нет.{w} Думаю, вряд ли когда-то будем."
            speech.kseniya "Почему так категорично?"
            speech.thought "Я рассказал всю эту историю с кашей.{w} В мельчайших подробностях и без комочков."
            speech.main "Как-то это было...{w} Высокомерно?"
            speech.kseniya "..."
            speech.main "Ксюш?{w} О чем задумалась?"
            speech.kseniya "Я?{w} Ничего.{w} А можешь дать мне свой ВК?"
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
    speech.thought "Видимо, Ксюша всё-таки нашла какое-то мероприятие.{w} Собираюсь ли я в своё свободное время тащиться в теплофак?{w} Ха-ха-ха-ха-ха!"
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
    speech.thought "Да нет.{w} Вы бы сели?{w} Хотя, если вы выбрали этот вариант, то я знаю ответ.{w} Глупо садиться к человеку, ещё и здесь, поэтому моё место за единственным свободным столиком."
    speech.thought "Хотя, может и не совсем...{w} Там, вроде, чьи-то вещи."
    Character("???", kind = speech.kseniya) "Приветствую, тут занято."
    hide screen canteen_kseniya_scene_1 with usual_transition
    show screen canteen_kseniya_scene_2(None) with usual_transition
    speech.main "Да тут некуда сесть, но я могу ливнуть, если некомфортно."
    show screen canteen_kseniya_scene_2(blur_out)    
    $ portrait_main.appear("undressed", "sad", .7, False)
    $ portrait_kseniya.appear("undressed", "normal", .3, True)
    Character("???", kind = speech.kseniya) "Вижу, у тебя тоже бесплатный завтрак.{w} Говорят, каша вкусная сегодня. Это правда?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, "normal", None, True)
    speech.main "Каша — бомба!"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    Character("???", kind = speech.kseniya) "Ты выглядишь немного испуганным, насколько я могу судить.{w} Мне не доставит труда уйти, если тебе некомфортно."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Да не парься... Меня [player_name] зовут."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "happy", None, True)
    speech.kseniya "А я Ксения, очень приятно!{w} Твоё лицо мне кажется невероятно знакомым..."
    $ portrait_kseniya.morph(None, "normal", None, None)
    speech.kseniya "Не могу припомнить, где я тебя видела.{w} Может ты сможешь мне подсказать?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "На парах? А так, я всегда дома сижу."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "happy", None, True)
    speech.kseniya "Конечно! Практики по физике.{w} Как же я сразу не вспомнила."
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    show screen canteen_kseniya_scene_2(blur_in)
    speech.thought "После небольшого диалога я узнал, что это Ксюша.{w} Она на одном направлении со мной, в свободное время преподает и работает."
    speech.thought "Знает как-то слишком много рандомных фактов, про которые я даже не слышал.{w} По математике, например.{w} А ещё мы информатику на одинаковый балл написали.{w} Вот такие приколы."
    speech.kseniya "... вчера я весь вечер учила коллоквиум, представляешь?{w} Позавчера ходила на волонтерство.{w} Ещё чуть позже была на олимпиаде.{w} Завтра идём с одной из моих знакомых на мероприятие."
    speech.main "Я вижу в этом намёк..."
    speech.kseniya "Ни в коем случае, но если у тебя есть желание и возможности..."
    speech.main "Я не любитель подобных мероприятий."
    speech.kseniya "Каждый когда-то должен сделать исключение, по-моему мнению."
    speech.main "Слушай, мне правда всё это не интересно.{w} Пустая трата времени."
    speech.kseniya "Однако, вдруг не пустая?"
    speech.main "Ксюш...{w} Я хочу поесть чипсы и пересмотреть Джокера.{w} Без обид."
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
    speech.thought "Променять Джокера и чипсики на мероприятие?{w} Ха-ха-ха-ха-ха!"
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

screen live_event_scene_3:
    add "bg_tutor.jpg" fit "fill"
    zorder -10

screen live_event_scene_4(how):
    add "bg_rtf_staircase.jpg" fit "fill"
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
    play ambient live_event_ambient_1 loop fadein .5
    speech.kseniya "Приветствую!"
    speech.main "Я до сих пор не понимаю, почему я здесь."
    speech.valeriya "“Не любитель движа”?!{w} “Не пойду, не пойду”?{w} Интересный ты конечно!"
    speech.main "И тебе привет.{w} А ты откуда знаешь?.."
    speech.valeriya "Не-е-ет, это ты...{w} ты откуда знаешь номер Ксюши?{w} Нашёл меро раньше неё. Ну ты даёшь."
    speech.main "Э-э, чего?!"
    speech.kseniya "Мы ушли с пар, чтоб сходить сюда.{w} Я до сих пор сомневаюсь, стоило ли это того.{w} Всё-таки пропускать пару по аналитической геометрии..."
    speech.valeriya "Ушли по уважительной причине! Всё окей.{w} Гоу найдем аудиторию, пять минут до начала осталось."
    hide screen live_event_scene_1 with usual_transition
    show screen live_event_scene_2(blur_out) with usual_transition
    stop ambient fadeout .5
    play ambient live_event_ambient_2 loop fadein .5
    $ portrait_main.appear("dressed", "sad", .3, False)
    $ portrait_kseniya.appear("dressed", "normal", .7, True)
    speech.kseniya "Я по дороге прочитала, что здесь будет что-то про навыки для ИИ.{w} Ты зарегистрировал нашу команду?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Я?{w} Так это ты меня позвала!"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "surprised", None, True)
    speech.kseniya "[player_name], с тобой всё хорошо?{w} Я переживаю и нахожу твои вопросы немного неуместными."
    $ portrait_kseniya.morph(None, None, .5, False)
    $ portrait_main.morph(None, None, .2, None)
    $ portrait_valeriya.appear("dressed", "normal", .8, True)
    speech.valeriya "Вика вроде бы зарегала."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, None)
    $ portrait_kseniya.morph(None, "sad", None, True)
    speech.kseniya "Отлично, а она..."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, True)
    speech.valeriya "Опоздает минут на пять."
    show screen live_event_scene_2(blur_in)
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    Character("Ведущий", kind = speech.generic) "Н-у-у-у что-о-о-о, первокурсники...{w} Всем огромный приве-е-ет!{w} Вы готовы пошуме-е-еть?"
    Character("Ведущий", kind = speech.generic) "Сегодня мы с вами займемся полезными делами!{w} Вы распределились на команды, список у нас есть."
    Character("Ведущий", kind = speech.generic) "Мы ставим вам баллы — вы выполняете задания.{w} Будут победители, будут подарки!{w} Ещё раз... Вы готовы-ы-ы?"
    speech.thought "Зал взорвался.{w} Но я всё ещё не понимал, почему регать команду должен был именно я.{w} И какой ещё номер?"
    speech.thought "И почему за столом Лера не могла сказать ни слова, а тут — силь ву пле."
    Character("Ведущий", kind = speech.generic) "Ваша задача сегодня — угадать, какие навыки придумали для ИИ ваши наставники.{w} Но это не всё: нужно угадать и предложить навыки лучше!"
    Character("Ведущий", kind = speech.generic) "Или смешнее. Или глупее.{w} Это на ваш выбор, ха-ха-ха!{w} Вы присылаете ответы в телеграмм и зарабатываете баллы."
    Character("Ведущий", kind = speech.generic) "Всё понятно, радисты?"
    show screen live_event_scene_2(blur_out)
    $ portrait_viktoriya.appear("dressed", "happy", .5, True)
    speech.viktoriya "Элементарно-о-о-о!"
    $ portrait_viktoriya.morph(None, None, None, False)
    speech.narrator "*Вика пробирается сквозь ряды пекусов к нам*"
    $ portrait_viktoriya.morph(None, None, None, True)
    speech.viktoriya "Мы сейчас всех сделаем.{w} Всем приветики! Двигайтесь."
    show screen live_event_scene_2(blur_in)
    $ portrait_viktoriya.disappear()
    Character("Ведущий", kind = speech.generic) "Внимание на экран!"
    hide screen live_event_scene_2 with usual_transition
    show screen live_event_scene_3 with usual_transition
    Character("Наставник №1", kind = speech.generic) "Я заваливал НТК три раза подряд.{w} Может быть, я бы не ходил на пересдачи, если бы ИИ умел..."
    hide screen live_event_scene_3 with usual_transition
    show screen live_event_scene_2(None) with usual_transition
    Character("Ведущий", kind = speech.generic) "Ваш выход, господа!{w} Телеграм на экране, а ваши баллы у нас.{w} Время пошло!"
    show screen live_event_scene_2(blur_out)
    $ portrait_viktoriya.appear("undressed", "happy", .3, False)
    $ portrait_main.appear("undressed", "sad", .7, True)
    speech.main "Мда...{w} Бредятина."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    speech.viktoriya "Да бро-ось, это ведь интересно.{w} Может, так:{w} “... если бы ИИ умел бы давать ответы на тесты”?"
    speech.viktoriya "“... как только они запускаются в браузере”?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Нужно что-то пооригинальней."
    $ portrait_main.morph(None, None, .8, False)
    $ portrait_viktoriya.morph(None, None, .2, None)
    $ portrait_kseniya.appear("undressed", "normal", .5, True)
    speech.kseniya "Может быть, стоит рассмотреть такой вариант:{w} “... выставление максимального балла в брс”?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    speech.viktoriya "Вот это уже хорошо.{w} Может ещё...{w} “... умел блокировать сайты, на которые нам выкладывают тесты”?{w} Так бы их вообще не было."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "И мы бы сдавали сессию очно.{w} Не очень хороший план, согласись."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "Бе-бе-бе!"
    show screen live_event_scene_2(blur_in)
    $ portrait_main.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_kseniya.disappear()
    Character("Ведущий", kind = speech.generic) "Время вышло, готовы к следующему вопросу?{w} Не слышу!{w} Все правильные ответы будут показаны в конце, а сейчас..."
    speech.thought "В общем, зря я пришел.{w} В чем смысл?{w} Навыки для ИИ.{w} Опять этот ИИ. Куда не пойди, везде нейросети.{w} Ещё и баллы потеряли, ничего не успели."
    hide screen live_event_scene_2 with usual_transition
    show screen text_scene("Некоторое время спустя") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen live_event_scene_2(None) with usual_transition
    speech.thought "Мы продули уже в трёх вопросах.{w} Когда я закатил глаза пятый раз подряд, Лера схватила меня за руку и потащила в сторону."
    hide screen live_event_scene_2 with usual_transition
    show screen live_event_scene_4(None) with usual_transition
    
    stop music fadeout .5
    show screen live_event_scene_4(blur_out)
    $ portrait_main.appear("undressed", "sad", .3, False)
    $ portrait_valeriya.appear("undressed", "happy", .7, True)
    speech.valeriya "Мы сейчас вернёмся, пошли отойдём..."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Чего тебе?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Слушай, я вижу, ты не любишь всё вот это...{w} Команды, конкурсы.{w} Но ты ведь уже сюда пришёл.{w} Может постараешься хотя бы?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Я бы с радостью, но задания правда ни о чём."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "Зачем тогда позвал нас сюда?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Слушай, я никого не..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "Ну-ну.{w} Ты вот знаешь...{w} Представь, что ты разработчик."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "Чего?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Думай, чего людям не хватает.{w} Тебе тоже сдавать НТК, что бы ты хотел от ИИ?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Мы в театре что ли?{w} Не буду я никого играть."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Так что бы хотел?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "...{w} Не знаю, чтобы он слил мне все вопросы и ответы на них."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Ну?{w} Разве это плохой ответ?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "Давай пойдём, не кисни."
    $ portrait_main.disappear()
    $ portrait_valeriya.disappear()
    hide screen live_event_scene_4 with usual_transition
    show screen live_event_scene_2(None)
    play music live_event_music fadein .5
    speech.thought "Удивитесь?{w} Мы ответили на все следующие вопросы.{w} Я втянулся. Был разработчиком, как завещала Лера."
    speech.thought "Лично у меня в голове, мы все сидели в офисе и придумывали продукт, который поможет людям."
    speech.thought "Ну, и принесёт нам миллионы.{w} И нет, это не выглядело как глупая фантазия, рождённая детской эйфорией вовлечённости."
    Character("Ведущий", kind = speech.generic) "Итак, наставник номер четыре!"
    
    hide screen live_event_scene_2 with usual_transition
    show screen live_event_scene_3 with usual_transition
    Character("Наставник №4", kind = speech.generic) "Знаете, мне не хватает кое-чего в этом мире.{w} И вряд ли мне это может подарить искусственный интеллект, но может быть..."
    Character("Наставник №4", kind = speech.generic) "Может быть, это станет реальностью?{w} В ближайшем будущем.{w} Есть у вас варианты, воспитанники Попова?"
    hide screen live_event_scene_3 with usual_transition
    show screen live_event_scene_2(None) with usual_transition
    
    show screen live_event_scene_2(blur_out)
    $ portrait_main.appear("undressed", "sad", .2, False)
    $ portrait_valeriya.appear("undressed", "normal", .4, True)
    $ portrait_viktoriya.appear("undressed", "normal", .6, False) 
    $ portrait_kseniya.appear("undressed", "normal", .8, False) 
    speech.valeriya "Возможность путешествовать?{w} Или открыто посещать другие страны..."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    speech.viktoriya "Готовить еду?{w} Тесто, сырок, пиццу в духовку..."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    speech.kseniya "Виктория?{w} Нужно будет сходить в столовую."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Ха-ха-ха, я шучу!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "normal", None, True)
    speech.main "Может собеседника?{w} Ну, я имею в виду, возможность поговорить с ИИ не как с роботом, а как с другом.{w} Сейчас ведь правда многие одиноки."
    $ portrait_main.morph(None, "happy", None, None)
    speech.main "А робот есть робот.{w} Если бы у него было что-то вроде своего мнения и своей души..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, None)
    speech.thought "Краем глаза я заметил, что Лера смотрела на меня и улыбалась.{w} Она...{w} гордилась мной?.."
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Офигенно!"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "Но это бред..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "Кого это волнует, это классно!"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "ИИ не сможет на таком уровне..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, True)
    speech.valeriya "Ну если ты станешь разработчиком, то точно сможет.{w} Я отправила."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_viktoriya.disappear() 
    $ portrait_kseniya.disappear()
    show screen live_event_scene_2(blur_in)
    
    Character("Ведущий", kind = speech.generic) "Мы дождались ответа всех команд, внимание на экран!"
    hide screen live_event_scene_2 with usual_transition
    show screen live_event_scene_3 with usual_transition
    Character("Наставник №4", kind = speech.generic) "Забавно, но мне бы хотелось верить, что ИИ будет неким товарищем человека.{w} Знаете, не просто помогать ему в программировании, но ещё и сочувствовать."
    Character("Наставник №4", kind = speech.generic) "А сейчас на смс “мне плохо” он может ответить только “настоятельно рекомендуется обратиться за медицинской помощью”."
    Character("Ведущий", kind = speech.generic) "Вот такой ответ наставника группы РИ-130918...{w} Вроде бы у нас есть команды, которые угадали..."
    hide screen live_event_scene_3 with usual_transition
    show screen live_event_scene_2(None) with usual_transition
    play sound live_event_sound
    Character("Ведущий", kind = speech.generic) "“Рекурсивные пряники”, в точку!{w} Ха-ха, смешное название, ребят, двадцать баллов ваши!"
    speech.thought "Нет, не надо вопросов.{w} Вика зарегала нашу команду под именем “Рекурсивные пряники”.{w} Я не знаю, почему."
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
    speech.thought "Мы не выиграли тогда.{w} Нам не хватило 15 баллов, которые мы потеряли на первых вопросах."
    speech.thought "Но, мне казалось, мы получили нечто большее, чем мерч от УрФУ и третье место.{w} Хотя что может быть круче толстовок?"
    hide screen after_show_scene_1 with usual_transition
    show screen after_show_scene_2(None) with usual_transition
    stop ambient fadeout .5
    play ambient after_show_ambient_2 loop fadein .5
    speech.thought "Мне вообще не свойственно взаимодействовать с людьми, которых я знаю не так давно, однако я активно участвовал в беседе."
    show screen after_show_scene_2(blur_out)
    $ portrait_viktoriya.appear("dressed", "happy", .5, True)
    speech.thought "Гиперактивность Вики уже не смотрелась так странно."
    $ portrait_viktoriya.morph(None, None, .7, False)
    $ portrait_kseniya.appear("dressed", "happy", .3, True)
    speech.thought "Теперь мне не казалась чуждой заумная манера речи Ксюши."
    $ portrait_viktoriya.morph(None, None, .8, False)
    $ portrait_kseniya.morph(None, None, .2, False)
    $ portrait_valeriya.appear("dressed", "happy", .5, True)
    speech.thought "Лера спустилась с небес и куда-то спрятала былую надменность."
    $ portrait_valeriya.morph(None, None, .6, False)
    $ portrait_main.appear("dressed", "normal", .4, True)
    speech.thought "Мы шли и болтали. Как будто мы знакомы уже год, или пять."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Подождите-е-е!!!{w} А представьте, если сделать так, чтобы по утрам ИИ сам бы выбирал тебе музыку, под которую нужно проснуться."
    speech.valeriya "Например, у тебя сегодня коллоквиум, и он включает тебе {a=https://youtu.be/sXq0qRkghUM?autoplay=1}это{/a}."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    speech.viktoriya "Ха-ха-ха-ха, шикарно-о-о-о!"
    $ portrait_viktoriya.morph(None, "normal", None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Или знаете...{w} Играл бы с тобой в игры?"
    $ portrait_main.morph(None, "sad", None, None)
    speech.main "У меня есть куча таких, которые я хочу пройти, но не с кем."
    $ portrait_main.morph(None, "normal", None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Слушайте, настроение бомба!{w} Анекдот?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    speech.kseniya "Было бы превосходно!"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Валяй!"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Чтобы не искать каждый раз светофоры, Ваня сходил в МФЦ и получил справку с печатью, что он не робот."
    $ portrait_main.morph(None, "happy", None, True)
    $ portrait_valeriya.morph(None, "happy", None, True)
    $ portrait_kseniya.morph(None, "happy", None, True)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.narrator "*Все смеются*"
    $ portrait_main.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_viktoriya.disappear()
    hide screen after_show_scene_2 with usual_transition
    show screen after_show_scene_3 with usual_transition
    speech.thought "После легендарной шутки мы обсуждали, и обсуждали, и обсуждали искусственный интеллект...{w} Мне тогда казалось, что это не просто мысли на ветер."
    speech.thought "Как будто мы думали над нашим будущим проектом.{w} Впервые за долгое время, мне было {b}правда{/b} хорошо."
    speech.thought "Не знаю, куда делся мой гнев.{w} Почему-то сейчас мне хотелось придумать как можно больше идей."
    hide screen after_show_scene_3 with usual_transition
    show screen after_show_scene_4(blur_out) with usual_transition
    stop ambient fadeout .5
    $ portrait_vanya.appear("undressed", "happy", .5, True) 
    speech.vanya "Чува-ак, я сейчас упаду и не встану...{w} Да ты просто сияешь!"
    $ portrait_vanya.morph(None, None, None, False)
    speech.thought "Я только зашёл в комнату и сразу услышал этот вопрос.{w} Потом повернулся к зеркалу и не заметил в себе никаких изменений."
    $ portrait_vanya.morph(None, None, None, True)
    speech.vanya "Глаза горя-ят...{w} Ты втюрился что ли?"
    $ portrait_vanya.morph(None, None, .3, False)
    $ portrait_main.appear("dressed", "sad", .7, True) 
    speech.main "Да ну тебя!"
    $ portrait_main.morph("undressed", None, None, False)
    $ portrait_vanya.morph(None, "normal", None, True)
    speech.vanya "Я не вижу на тебе толстовки, так что тут только один варик, че-е-eл.{w} Я жду опупенную историю и шлёпаю за пепси." 
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_vanya.disappear()
    $ portrait_main.disappear()
    show screen after_show_scene_4(blur_in)
    speech.thought "Я рассказал Ване суть мероприятия и что мы там делали.{w} Он расстроился, потому что, наверное, ждал историю про какую-нибудь первокурсницу, но всё равно был за меня рад."
    show screen after_show_scene_4(blur_out)
    $ portrait_main.appear("undressed", "normal", .3, False)
    $ portrait_vanya.appear("undressed", "normal", .7, True)
    speech.vanya "Ну кайф бро, ка-a-айф, столько идей нашировертил, ёмаё.{w} Откуда в твоей головёшке столько?"
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Да мы как-то вместе шировертили.{w} И ещё наста..."
    $ portrait_main.morph(None, None, None, False)
    stop music fadeout .5
    play music after_show_music_2 fadein .5
    speech.thought "Меня прервал звук уведомления на телефоне."
    play sound after_show_sound
    speech.polina_hidden "Неплохо получилось. Спасибо, что решил пойти."
    $ portrait_main.morph(None, "surprised", None, None)
    speech.thought "Точно, я забыл записать Ксюшу у себя в телефоне.{w} Почему она не пишет мне в вк?"
    $ portrait_vanya.morph(None, None, None, True)
    speech.vanya "Чё там?"
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Ксюша.{w} Пишет, что мы сегодня были хороши."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_vanya.morph(None, None, None, True)
    speech.vanya "Хороши?{w} Да потому что ты набазарил такого.{w} Вы будущие мегамозги, куском пиццы клянусь!"
    $ portrait_main.disappear() 
    $ portrait_vanya.disappear()
    hide screen after_show_scene_4 with usual_transition
    return

















screen before_argument_scene_1:
    add "bg_room_bed.jpg" fit "fill"
    zorder -10

screen before_argument_scene_2:
    add "bg_scooter_street.jpg" fit "fill"
    zorder -10

screen before_argument_scene_3(how):
    add "bg_rtf_preentrance.jpg" fit "fill" at how
    add "ch_watchwoman.png" fit "fill"
    zorder -10

define before_argument_music_1 = "Toby Fox — Premonition.mp3"
define before_argument_music_2 = "Toby Fox — Dating Tense!.mp3"
define before_argument_ambient_1 = "City Noise.mp3"
define before_argument_ambient_2 = "Quiet Noise.mp3"

label before_argument_script:
    show screen before_argument_scene_1 with usual_transition
    stop music fadeout .5
    play music before_argument_music_1 fadein .5
    speech.thought "На следующий день...{w} Вам чего?{w} Никаких историй не будет, на следующий день были пары.{w} А вы думали, что студенческая жизнь — это постоянные тусовки?{w} Пары, пары, и ещё раз пары!"
    hide screen before_argument_scene_1 with usual_transition
    show screen before_argument_scene_2 with usual_transition
    play ambient before_argument_ambient_1 loop fadein .5
    speech.thought "У меня программирование, очное, прикиньте?{w} У всех дистанционно, а я тащусь писать “Hello, world!” в радик."
    speech.thought "Вчера Ксюша нашла меня в ВК.{w} У меня один вопрос — как?{w} Если я даже не говорил ей свою фамилию."
    speech.thought "Ну, в общем, я записал её “Джимми Нейтрон”...{w} Надеюсь, что она оценит."
    hide screen before_argument_scene_2 with usual_transition
    show screen before_argument_scene_3(blur_out) with usual_transition
    stop ambient fadeout .5
    play ambient before_argument_ambient_2 loop fadein .5
    stop music fadeout .5
    play music before_argument_music_2 fadein .5
    menu:
        speech.thought "Ну не-е-ет, опять?"
        "Проигнорировать и молча пройти":
            $ pass
        "Приготовить студик и уверенно его показать":
            $ pass
        "Приготовить студик, но не показывать его":
            $ pass
    Character("Вахтёрша", kind = speech.generic) "Добрый день;{w} день добрый;{w} проходите пожалуйста."
    $ portrait_main.appear("dressed", "surprised", .8, False)
    speech.thought "Это как...{w} как работает?{w} Значит, сегодня у нее хорошее настроение...{w} Удивительно конечно."
    $ portrait_main.morph(None, "sad", None, None)
    speech.thought "А у меня вот улыбка на лицо не лезет без кофе, прикиньте?{w} Просто не могу заста..."
    $ portrait_main.disappear()
    hide screen before_argument_scene_3 with usual_transition
    return












screen coffee_argument_scene_1(how):
    add "bg_rtf_coffeeshop.jpg" fit "fill" at how
    zorder -10

define coffee_argument_music_1 = "Toby Fox — Undyne.mp3"
define coffee_argument_music_2 = "Toby Fox — Death By Glamour.mp3"
define coffee_argument_sound_1 = "Negative.mp3"
define coffee_argument_sound_2 = "Positive.mp3"

label coffee_argument_script:
    show screen coffee_argument_scene_1(blur_out) with usual_transition
    stop music fadeout .5
    play music coffee_argument_music_1 fadein .5
    $ portrait_main.appear("undressed", "surprised", .7, False)
    $ portrait_polina.appear("undressed", "sad", .3, True)
    Character("???", kind = speech.polina) "{sc=7}Ты совсем рихнулся?!{/sc}"
    $ portrait_polina.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Ой... да я..."
    $ portrait_main.morph(None, "sad", None, False)
    $ portrait_polina.morph(None, "sad", None, True)
    Character("???", kind = speech.polina) "{sc=3}Смотри куда идёшь!{/sc}"
    $ portrait_polina.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "А ничё, что ты летела на всех парусах?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_polina.morph(None, "surprised", None, True)
    Character("???", kind = speech.polina) "{sc=7}Ты испортил мне кофту, придурок!{sc}"
    $ portrait_polina.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, None)
    speech.thought "О да, я столкнулся с истеричкой и пролил на неё кофе."
    $ renpy.notify("Цифры на пунктах меню показывают, сколько вам нужно очков, чтобы вы могли сделать этот выбор. Эти очки не списываются!")
    label coffee_argument_again:
    menu:
        speech.thought "Что теперь ответить?"
        "{color=#FF3838}[[35]{/color} Извиниться" if player_score < 35:
            play sound coffee_argument_sound_1
            $ renpy.notify("У вас недостаточно баллов.")
            jump coffee_argument_again
        "{color=#38FF38}[[35]{/color} Извиниться" if player_score >= 35:
            stop music fadeout .5
            play music coffee_argument_music_2 fadein .5
            play sound coffee_argument_sound_2
            $ branch_choice_1_2 = 1
            $ player_score += 10
            $ renpy.notify("За терпение вы получили баллов: 10/10. Всего баллов: " + str(player_score) + ".")
            $ portrait_main.morph(None, None, None, True)
            speech.main "Ладно, извини, я не хотел."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_polina.morph(None, "normal", None, True)
            Character("???", kind = speech.polina) "Ну, я вот тоже не хотела весь день ходить облитая."
            $ portrait_polina.morph(None, None, None, False)
            $ portrait_main.morph(None, "surprised", None, True)
            speech.main "Да я тебя даже не увидел, ты просто из-за поворота выпрыгнула."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_polina.morph(None, "surprised", None, True)
            Character("???", kind = speech.polina) "У тебя со зрением все хорошо?"
            $ portrait_polina.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Нет, но если бы и было хорошо, то я бы всё равно тебя не увидел."
            $ portrait_main.morph(None, None, None, False)
            speech.thought "Она заметно растерялась после того, как узнала, почему я ношу очки.{w} Как будто раньше не замечала их."
            $ portrait_polina.morph(None, "sad", None, True)
            Character("???", kind = speech.polina) "Ладно...{w} Сорян, что так наехала.{w} У меня с самого утра какой-то дурдом. Теперь ещё больший дурдом."
            $ portrait_polina.morph(None, None, None, False)
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "Да и у меня уже второй день.{w} Я завтра не пойду на пары походу, ну нафиг."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_polina.morph(None, "happy", None, True)
            Character("???", kind = speech.polina) "Да, лучше уж дома сидеть, чем кофе на всех проливать."
            $ portrait_polina.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Ну я же уже извинился..."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_polina.morph(None, "normal", None, True)
            Character("???", kind = speech.polina) "Ладно, шучу.{w} Вписывайся в углы в следующий раз."
            $ portrait_polina.disappear()
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "А зовут-то тебя как..?"
            $ portrait_main.disappear()
            show screen coffee_argument_scene_1(blur_in)
            speech.thought "Убежала.{w} А я остался без кофе, с плохим настроением и время кстати...{w} Мда, я ещё и опаздываю на пару."
            show screen coffee_argument_scene_1(blur_out)
            $ portrait_main.appear("undressed", "normal", .3, False)
            $ portrait_viktoriya.appear("undressed", "happy", .7, True)
            Character("???", kind = speech.viktoriya) "Ну вы прям как в анекдоте, реально."
            $ portrait_viktoriya.morph(None, None, None, False)
            speech.thought "..?"
            $ portrait_viktoriya.morph(None, "normal", None, True)
            Character("???", kind = speech.viktoriya) "Ну ты стоял, смотрел на спину бабы Зины, потом поворачиваешься и бу-ум всё кофе к потолку, было эффектно, это можно даже нарисовать..."
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_main.morph(None, "surprised", None, True)
            speech.main "Тебе смешно, да?{w} Иди, куда шла."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, "sad", None, True)
            Character("???", kind = speech.viktoriya) "Да ладно тебе, я хотела сказать, что Полина не всегда такая, с ней надо аккуратней просто."
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_main.morph(None, "surprised", None, True)
            speech.main "Я ничего не сделал, мне уже нельзя ходить по коридорам?"
            $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, "normal", None, True)
            Character("???", kind = speech.viktoriya) "Так, давай: вдох-выдох.{w} Всё олрайт, кофту же не она заставила тебя стирать."
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Ага, а я бы прям согласился."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, "happy", None, True)
            Character("???", kind = speech.viktoriya) "Хочешь анекдот?"
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_main.morph(None, "surprised", None, True)
            speech.main "Я вижу тебя впервые, говорю с тобой 2 минуты и не знаю твоего имени, а ты..."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, None, None, True)
            Character("???", kind = speech.viktoriya) "Самый хороший способ взбодрить человека с утра — кофе в постель."
            $ portrait_viktoriya.morph(None, "normal", None, None)
            Character("???", kind = speech.viktoriya) "Вылил и беги."
            $ portrait_viktoriya.morph(None, None, None, False)
            menu:
                speech.thought "?.."
                "Промолчать":
                    $ pass
                "Смешно":
                    $ portrait_main.morph(None, "normal", None, True)
                    speech.main "Ладно, это правда смешно."
                    $ portrait_main.morph(None, None, None, False)
                "Хватит":
                    $ portrait_main.morph(None, "normal", None, True)
                    speech.main "Это ты {a=https://youtu.be/jOpQuy2i1kk?t=2852&autoplay=1}анекдоты для сталкера{/a} писала?"
                    $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, "happy", None, True)
            Character("???", kind = speech.viktoriya) "Ну после такого обычно спрашивают имя и дружат всю жизнь."
            $ portrait_viktoriya.morph(None, "normal", None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Хорошо.{w} “Как тебя зовут? Давай дружить всю жизнь”."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_viktoriya.morph(None, "happy", None, True)
            speech.viktoriya "Я — Вика.{w} Давай дружить!{w} Жду сегодня по адресу Чапаева семнадцать."
            $ portrait_viktoriya.morph(None, "normal", None, False)
            $ portrait_main.morph(None, "surprised", None, True)
            speech.main "Я пошутил так-то..."
            $ portrait_main.morph(None, "sad", None, False)
            $ portrait_viktoriya.morph(None, "happy", None, True)
            speech.viktoriya "А я нет... Мяу!"
            $ portrait_viktoriya.disappear()
            $ portrait_main.morph(None, "surprised", None, True)
            speech.main "Стой, что?{w} Какое ещё Чапаева..."
            $ portrait_main.morph(None, "sad", None, False)
            speech.thought "Такими темпами, я сойду с ума ещё до сессии."
            $ portrait_main.disappear()

        "Сама виновата":
            $ branch_choice_1_2 = 2
            stop music fadeout .5
            play music coffee_argument_music_2 fadein .5
            $ portrait_main.morph(None, "surprised", None, True)
            speech.main "Ты вообще адекватная?{w} Смотри, куда прёшь!"
            $ portrait_main.morph(None, None, None, False)
            $ portrait_polina.morph(None, "normal", None, True)
            Character("???", kind = speech.polina) "О-о-о, ты бы так не выражался, чувак."
            $ portrait_polina.disappear()
            $ portrait_main.morph(None, "sad", None, None)
            speech.main "Да, кайф.{w} Наорать на меня и убежать с поля боя.{w} Что тут вообще по утрам происходит?"
            $ portrait_egor.appear("undressed", "normal", .3, True)
            speech.egor "Капец чувак, вот она отбитая, да?"
            $ portrait_egor.morph(None, None, None, False)
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "О, Егор, привет."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Просто так наорала, нормальная вообще?{w} Как они бесят все, да?"
            $ portrait_egor.morph(None, None, None, False)
            $ portrait_main.morph(None, "surprised", None, True)
            speech.main "Да я вообще ничё не сделал, просто шёл, она выплыла со своим кофе."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Да не парься, таких чокнутых ещё поискать надо."
            $ portrait_egor.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Чё-то я даже забыл, куда шёл..."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Слушай, может это и к лучшему?{w} Пойдём прогуляемся, у тебя какая пара сейчас?"
            $ portrait_egor.morph(None, None, None, False)
            $ portrait_main.morph(None, None, None, True)
            speech.main "Прога, вроде."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Так а нафиг она тебе сдалась, ты уже знаешь си шарп лучше, чем все преподы вместе взятые!" 
            $ portrait_egor.morph(None, None, None, False)
            $ portrait_main.morph(None, "surprised", None, True)
            speech.main "Пропустить первую пару по проге?"
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Да чел, а что в этом такого? Это всё в твоей голове, все эти правила." 
            $ portrait_egor.morph(None, None, None, False)
            menu:
                speech.thought "Что делать?"
                "Пойти с Егором":
                    $ branch_choice_x_y = 1
                    $ portrait_main.morph(None, "sad", None, True)
                    speech.main "Ладно, пофиг. Факты говоришь, братанчик.{w} А куда пойдем?"
                    $ portrait_main.morph(None, None, None, False)
                    $ portrait_egor.morph(None, None, None, True)
                    speech.egor "Ну во-от, другое дело.{w} Есть у меня одно место..."
                    $ portrait_main.disappear()
                    $ portrait_egor.disappear()
                "Пойти на пары":
                    $ branch_choice_x_y = 2
                    $ portrait_main.morph(None, "sad", None, True)
                    speech.main "Блин, давай как-нибудь в другой раз."
                    $ portrait_main.morph(None, None, None, False)
                    $ portrait_egor.morph(None, None, None, True)
                    speech.egor "Ой, мальчик испугался прогулов?{w} Не ожидал от тебя такого конечно...{w} А может..."
                    $ portrait_main.disappear()
                    speech.egor "Эй, ты куда?"
                    $ portrait_egor.disappear()
    hide screen coffee_argument_scene_1 with usual_transition
    return














screen cat_cafe_scene_1:
    add "bg_car_street.jpg" fit "fill"
    zorder -10

screen cat_cafe_scene_2:
    add "bg_many_cats.jpg" fit "fill"
    zorder -10

screen cat_cafe_scene_3(how):
    add "bg_cat_tigra.jpg" fit "fill" at how
    zorder -10

screen cat_cafe_scene_4(how):
    add "bg_cats_window.jpg" fit "fill" at how
    zorder -10

screen cat_cafe_scene_5(how):
    add "bg_cat_floor.jpg" fit "fill" at how
    zorder -10

screen cat_cafe_scene_6(how):
    add "bg_cat_pillow.jpg" fit "fill" at how
    zorder -10

screen cat_cafe_scene_7(how):
    add "bg_cat_castle.jpg" fit "fill" at how
    zorder -10

screen cat_cafe_scene_8:
    add "bg_mch_cat.jpg" fit "fill"
    zorder -10

screen cat_cafe_scene_9:
    add "bg_zephyrka_selfie.jpg" fit "fill"
    zorder -10

define cat_cafe_music = "K. K. Slider — K. K. Parade (Radio).mp3"
define cat_cafe_ambient_1 = "City Noise.mp3"
define cat_cafe_ambient_2 = "Cat Cafe.mp3"
define cat_cafe_sound = "Notification.mp3"

label cat_cafe_script:
    show screen cat_cafe_scene_1 with usual_transition
    stop ambient fadeout .5
    play ambient cat_cafe_ambient_1 loop fadein .5
    stop music fadeout .5
    play music cat_cafe_music loop fadein .5
    speech.thought "Не надо задавать лишних вопросов, ладно?{w} Да, поехал я на этот адрес.{w} Да, с неизвестной мне девочкой.{w} Кстати говоря, знаете, почему Вика сказала “мяу”?"
    hide screen cat_cafe_scene_1 with usual_transition
    show screen cat_cafe_scene_2 with usual_transition
    stop ambient fadeout .5
    play ambient cat_cafe_ambient_2 loop fadein .5
    speech.viktoriya "О-а-о-а, какие они!{w} Посмотри туда!"
    speech.thought "Потому что мы приехали в {a=https://vk.com/cafe.meow}{i}котокафе{/i}{/a}."
    hide screen cat_cafe_scene_2 with usual_transition
    show screen cat_cafe_scene_3(None) with usual_transition
    Character("Кот", kind = speech.generic) "Мяу-у."
    Character("Работник кафе", kind = speech.generic) "Его зовут Тигра, можете погладить."
    show screen cat_cafe_scene_3(blur_out)
    $ portrait_main.appear("undressed", "normal", .7, False)
    $ portrait_viktoriya.appear("undressed", "happy", .3, True)
    speech.viktoriya "Привет, Тигра!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Смотри, справа от тебя..."
    $ portrait_main.disappear() 
    $ portrait_viktoriya.disappear() 
    hide screen cat_cafe_scene_3 with usual_transition
    show screen cat_cafe_scene_4(None) with usual_transition
    ""
    show screen cat_cafe_scene_4(blur_out)
    $ portrait_main.appear("undressed", "happy", .5, True)
    speech.main "Ха-ха, вижу некое сходство между собой и котом на подоконнике." 
    $ portrait_main.morph(None, "normal", None, False)
    Character("Работник кафе", kind = speech.generic) "Это Тишка.{w} Он...{w} спит. Иногда сидя.{w} Ещё умеет втыкать в стену очень много часов." 
    $ portrait_main.morph(None, "happy", .7, True)
    show screen cat_cafe_scene_4(blur_in)
    speech.main "Ну вот и я о том же."
    $ portrait_main.morph(None, None, .5, False)
    show screen cat_cafe_scene_4(blur_out)
    while (not cats_tried_loved) or (not cats_tried_audience) or (not cats_tried_pet):
        menu:
            speech.thought "Надо как-то поддержать разговор."
            "Любимчики" if not cats_tried_loved:
                $ cats_tried_loved = True
                $ portrait_main.morph(None, "normal", None, True)
                speech.main "А у вас есть любимые котята?"
                $ portrait_main.morph(None, None, None, False)
                Character("Работник кафе", kind = speech.generic) "О-о, да они у нас все разные и замечательные, так что сложно выбрать кого-то одного."
            "Посетители" if not cats_tried_audience:
                $ cats_tried_audience = True
                $ portrait_main.morph(None, "normal", None, True)
                speech.main "Сколько людей приходит к вам за год?"
                $ portrait_main.morph(None, None, None, False)
                Character("Работник кафе", kind = speech.generic) "Много.{w} Ну, знаете, в основном это туристы, которые нашли необычное кафе и решили в него заглянуть.{w} Но у нас есть и постоянные клиенты."
                Character("Работник кафе", kind = speech.generic) "Они любят кошек, но не могут завести себе по определенным причинам.{w} Не хватает средств, много работы, ну и так далее.{w} А животные помогают им расслабиться и снять стресс."
            "Свой питомец" if not cats_tried_pet:
                $ cats_tried_pet = True
                $ portrait_main.morph(None, "normal", None, True)
                speech.main "А у вас есть домашнее животное?"
                $ portrait_main.morph(None, None, None, False)
                Character("Работник кафе", kind = speech.generic) "Я как раз из тех людей, которые не могут позволить себе домашнее животное."
                Character("Работник кафе", kind = speech.generic) "У меня...{w} Да это не важно. Без животных правда тяжко.{w} Так что я рада, что работаю здесь..."
    $ portrait_main.disappear()
    hide screen cat_cafe_scene_4 with usual_transition
    show screen cat_cafe_scene_5(None) with usual_transition
    Character("Работник кафе", kind = speech.generic) "Забавно ведь?"
    $ portrait_main.appear("undressed", "normal", .5, True)
    show screen cat_cafe_scene_5(blur_out)
    speech.main "Вы о чём?"
    $ portrait_main.morph(None, None, None, False)
    Character("Работник кафе", kind = speech.generic) "{b}Что мы ничем не можем заменить домашних животных.{/b}{w} Ну можно глянуть фильм, сходить погулять, но вот...{w} они дарят какие-то эмоции.{w} Иные, что ли."
    $ portrait_main.disappear()
    hide screen cat_cafe_scene_5 with usual_transition
    show screen cat_cafe_scene_6(None) with usual_transition
    speech.viktoriya "О-о-о, ну как он сидит на подушке-е-е.{w} [player_name], посмотри!"
    show screen cat_cafe_scene_6(blur_out)
    $ portrait_viktoriya.appear("undressed", "sad", .5, True)
    speech.viktoriya "[player_name]?"
    $ portrait_viktoriya.disappear()
    show screen cat_cafe_scene_6(blur_in)
    speech.thought "А мы ведь реально не можем заменить животных.{w} Я чё-то никогда об этом не думал.{w} Вот сейчас подумал, и..."
    show screen cat_cafe_scene_6(blur_out)
    $ portrait_viktoriya.appear("undressed", "surprised", .5, True)
    speech.viktoriya "Ты уснул там?!{w} Смотри как он лапки на подушку положил!"
    $ portrait_viktoriya.disappear()
    hide screen cat_cafe_scene_6 with usual_transition
    show screen cat_cafe_scene_7(blur_out) with usual_transition
    $ portrait_viktoriya.appear("undressed", "normal", .3, False)
    $ portrait_main.appear("undressed", "normal", .7, False)
    speech.thought "Теперь эта мысль не могла выйти у меня из головы."
    $ portrait_main.morph(None, None, None, True)
    speech.main "У тебя есть домашнее животное?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Да, собака.{w} А что?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "А если бы ты не могла себе никого завести?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "Ну-у...{w} Это было бы печально. Наверное.{w} Ты это к чему?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Да так..."
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    hide screen cat_cafe_scene_7 with usual_transition
    show screen text_scene("Спустя некоторое время") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen cat_cafe_scene_8 with usual_transition
    speech.main "Я останусь тут поработать, сделаю домашку.{w} Среди котов лучше думается."
    speech.viktoriya "Давай, чао!"
    speech.thought "Вообще, я хотел сделать практики по программированию, но до сих пор думал над словами работника...{w} Домашние животные...{w} Не у всех есть возможность их завести..."
    speech.thought "Они незаменимы...{w} Ну, в общем, появилась у меня кое-какая идейка.{w} Практики подождут."
    hide screen cat_cafe_scene_8 with usual_transition
    show screen cat_cafe_scene_9 with usual_transition
    speech.thought "Пока я работал, ко мне постоянно приставала белая кошка.{w} Оказалось, её зовут Зефирка.{w} Я даже поставил её на аватарку в ВК."
    speech.thought "Не прошло пяти минут, как мне пришло уведомление:{w}{nw}"
    play sound cat_cafe_sound
    speech.thought "Не прошло пяти минут, как мне пришло уведомление:{fast} “Виктория оценила вашу фотографию”."
    hide screen cat_cafe_scene_9 with usual_transition
    return











screen bar_scene_1(how):
    add "bg_rtf_parking.jpg" fit "fill" at how
    zorder -10

screen bar_scene_2(how):
    add "bg_street_people.jpg" fit "fill" at how
    zorder -10

screen bar_scene_3(how):
    add "bg_alley_empty.jpg" fit "fill" at how
    zorder -10

screen bar_scene_4(how):
    add "bg_bar.jpg" fit "fill" at how
    zorder -10

screen bar_scene_5(how):
    add "bg_room_bed.jpg" fit "fill" at how
    zorder -10

define bar_music = "Toby Fox — Heartache.mp3"
define bar_ambient_1 = "City Noise.mp3"
define bar_ambient_2 = "Heartbeat.mp3"

label bar_script:
    show screen bar_scene_1(blur_out) with usual_transition
    stop music fadeout .5
    play music bar_music fadein .5
    stop ambient fadeout .5
    play ambient bar_ambient_1 loop fadein .5
    $ portrait_egor.appear("dressed", "normal", .3, False)
    $ portrait_main.appear("dressed", "sad", .7, True)
    speech.main "Слушай, зря мы ушли...{w} Давай обратно?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Да ладно тебе, это ознакомительная пара, чё будет?{w} Ты мне лучше скажи, ты будущий разработчик?"
    $ portrait_egor.morph(None, None, None, False)
    $ portrait_main.morph(None, "normal", None, True)
    speech.main "Да не знаю... Скорее всего.{w} Только разработчик чего? Ну, у меня пока что мало опыта."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Мало опыта?!{w} Да ты такую игру сделал, ты гонишь?{w} Такое только талантливые люди могут." 
    $ portrait_egor.disappear()
    $ portrait_main.disappear()
    hide screen bar_scene_1 with usual_transition
    show screen bar_scene_2(blur_out) with usual_transition
    $ portrait_egor.appear("dressed", "normal", .3, False)
    $ portrait_main.appear("dressed", "normal", .7, True)
    speech.main "Да ладно тебе..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "А у тебя есть ещё какие-то идеи?{w} Ну, будущие проекты..."
    $ portrait_egor.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Ну... Кое-что есть...{w} Я хочу пойти в {a=https://vk.com/t_kipenia_urfu}Точку Кипения{/a} и им закинуть, может получится сделать стартап."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Точка Кипения?{w} Ты чего, туда пекусам нельзя." 
    $ portrait_egor.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Как нельзя?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Ты не слышал?{w} С этого года для нас туда дорога закрыта."
    $ portrait_egor.disappear()
    $ portrait_main.disappear()
    hide screen bar_scene_2 with usual_transition
    show screen bar_scene_3(blur_out) with usual_transition
    $ portrait_egor.appear("dressed", "normal", .3, False)
    $ portrait_main.appear("dressed", "sad", .7, True)
    speech.main "Я первый раз это слышу...{w} Почему никто нигде про это не писал?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Да не успели наверное ещё.{w} Но ты не грусти, главное не упускать мысль о проекте, на следующий год представишь идею.{w} Она ведь крутая у тебя?"
    $ portrait_egor.morph(None, None, None, False)
    $ portrait_main.morph(None, "normal", None, True)
    speech.main "Да так..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Ну колись уже!" 
    $ portrait_egor.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "Ну... Я хочу сделать...{w} Что-то вроде платформы для создания сюжетов."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Э-э. Это как?"
    $ portrait_egor.morph(None, None, None, False)
    $ portrait_main.morph(None, "normal", None, True)
    speech.main "Ну например, я хочу рассказать людям про свой одиннадцатый класс, но не умею писать книги или рисовать и так далее."
    speech.main "И вот моя платформа позволит выбрать формат изложения: рисунок, или фильм, или книга, например, и создаст какой-нибудь сюжет.{w} И так люди смогут поделиться друг с другом важными мыслями."
    $ portrait_egor.disappear()
    $ portrait_main.disappear()
    hide screen bar_scene_3 with usual_transition
    show screen bar_scene_4(blur_out) with usual_transition
    $ portrait_main.appear("dressed", "normal", .7, False)
    $ portrait_egor.appear("dressed", "normal", .3, True)
    speech.egor "Чува-ак, это бомба!{w} Это же идея на миллион, как раз столько и выигрываешь в стартапе..."
    $ portrait_egor.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "Но она ещё сырая...{w} Я никому до этого не рассказывал про неё. Да на самом деле, деньги не так важны."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "О-о, деньги очень важны, чувак.{w} Блин, скорее бы второй курс."
    show screen bar_scene_4(blur_in)
    $ portrait_egor.disappear()
    $ portrait_main.disappear()
    speech.egor "А мы, кстати, пришли."
    hide screen bar_scene_4 with usual_transition
    speech.thought "..."
    stop music fadeout .5
    stop ambient fadeout .5
    play ambient bar_ambient_2 loop fadein .5
    show screen bar_scene_5(blur_out) with Dissolve(10.)
    $ portrait_vanya.appear("undressed", "normal", .5, True)
    speech.vanya "Чувак, але-е, шары открывай свои!"
    $ portrait_vanya.morph(None, None, None, False)
    speech.main "..."
    $ portrait_vanya.morph(None, "sad", None, True)
    speech.vanya "[player_name], ты где так нахрюкался?{w} Ты же не бухаешь вообще."
    $ portrait_vanya.morph(None, None, .7, False)
    $ portrait_main.appear("undressed", "sad", .3, True)
    speech.main "ъ...{w} ё...{w} м..."
    speech.narrator "*Нечленораздельная пьяная речь*"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_vanya.morph(None, "normal", None, True)
    speech.vanya "Ром?{w} Чего?{w} Ты вообще где это надыбал?"
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Воды..."
    $ portrait_main.disappear()
    speech.narrator "*Теряет равновесие и падает на пол*"
    $ portrait_vanya.morph(None, "sad", None, True)
    speech.vanya "Братан, я в шоке.{w} Ты в курсе, что у тебя стырили всю стипу?"
    $ portrait_vanya.morph(None, "normal", None, False)
    speech.main "..."
    $ portrait_vanya.morph(None, "sad", None, True)
    speech.vanya "Чуваки, он отходить будет сутки, тапком клянусь.{w} Шуруйте на перерыв на...{w} да фиг его знает на сколько, он к вам вернётся, когда хоть чё-то сможет сказать."
    $ portrait_vanya.disappear()
    hide screen bar_scene_5 with usual_transition
    speech.thought "..."
    return














screen after_bar_scene_1(how):
    add "bg_rtf_staircase.jpg" fit "fill" at how
    zorder -10

screen after_bar_scene_2(how):
    add "bg_rtf_parking.jpg" fit "fill" at how
    zorder -10

screen after_bar_scene_3(how):
    add "bg_alley_empty.jpg" fit "fill" at how
    zorder -10

screen after_bar_scene_4(how):
    add "bg_apartment_wallet.jpg" fit "fill" at how
    zorder -10

screen after_bar_scene_5:
    add "bg_wallet_zoomed.jpg" fit "fill"
    zorder -10

define after_bar_music = "Toby Fox — Oh! One True Love.mp3"
define after_bar_ambient_1 = "Quiet Noise.mp3"
define after_bar_ambient_2 = "City Noise.mp3"

label after_bar_script:
    show screen after_bar_scene_1(None) with usual_transition
    stop music fadeout .5
    play music after_bar_music fadein .5
    play ambient after_bar_ambient_1 loop fadein .5
    speech.thought "Я вообще ничего не помню.{w} Я помню вывеску этого бара, дальше — пустота.{w} Кто-то позвонил Ване с моего телефона, и он забрал меня."
    speech.thought "По его словам, я был один.{w} У меня украли деньги, наушники. Мне до сих пор плохо.{w} Я пропустил следующий день и вроде ещё...{w} день...{w} Потом пошел в радик. Я не мог понять одного: где..."
    show screen after_bar_scene_1(blur_out)
    $ portrait_egor.appear("undressed", "normal", .5, True)
    speech.egor "Боже мой, [player_name], я не мог до тебя дозвониться, потому что не взял твой вк.{w} Ты куда пропал вообще?"
    $ portrait_egor.morph(None, None, None, False)
    speech.thought "А вот и он."
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Я оставил тебя в баре на секунду буквально и вышел, потом вернулся, а тебя нет.{w} Ты если уходишь, так предупреждай хотя бы."
    $ portrait_egor.morph(None, None, .3, False)
    $ portrait_main.appear("undressed", "surprised", .7, True)
    speech.main "Эм..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Так не делают, чувак.{w} Ну да ладно, я не в обиде на тебя. Ты вообще в порядке?" 
    $ portrait_egor.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "У меня пропали деньги и наушники.{w} Это буквально единственное, что у меня было, и то забрали."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Серьёзно?!{w} Бро, какие люди свиньи.{w} Могу дать тебе в долг, тут я всегда выручу."
    $ portrait_egor.morph(None, None, None, False)
    speech.thought "..."
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Надо?{w} Только пойдём до квартиры моей сгоняем побырому, а то я не ношу с собой налик."
    $ portrait_egor.morph(None, None, None, False)
    menu:
        speech.thought "Что делать?"
        "Отказаться":
            $ branch_choice_alpha_beta = 1
            $ portrait_main.morph(None, "happy", None, True)
            speech.main "Ха-ха, спасибо, чувак, но одного раза мне хватило."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "О чём ты?" 
            $ portrait_egor.morph(None, None, None, False)
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "Я отходил от этого всего 3 дня."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Бро, я бы пришёл, если бы знал номер твоей комнаты и номер телефона.{w} Я вообще не знаю, кто тебя так напоил."
            $ portrait_egor.morph(None, None, None, False)
            $ portrait_main.morph(None, None, None, True)
            speech.main "Напоил?" 
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Вот и я о том же, сам в шоке."
            $ portrait_egor.morph(None, None, None, False)
            $ portrait_main.morph(None, "happy", None, True)
            speech.main "Ты ведь ушёл, когда я сидел за столом.{w} А потом вернулся, когда меня уже не было."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Ну так...{w} Я это...{w} Предполагаю.{w} Ты ведь не мог сам? Или мог?"
            $ portrait_egor.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Я пойду на пары, удачи."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Бро, ты всё ещё не отошёл походу..."
            $ portrait_main.disappear()
            speech.egor "..."
            speech.egor "Ну ты звони, если что..."
            $ portrait_egor.disappear()
            hide screen after_bar_scene_1 with usual_transition
        "Взять деньги":
            $ branch_choice_alpha_beta = 2
            $ portrait_egor.disappear()
            $ portrait_main.disappear()
            hide screen after_bar_scene_1 with usual_transition
            show screen after_bar_scene_2(blur_out) with usual_transition
            stop ambient fadeout .5
            play ambient after_bar_ambient_2 fadein .5
            $ portrait_egor.appear("dressed", "normal", .3, False)
            $ portrait_main.appear("dressed", "sad", .7, True)
            speech.main "Блин... Егор...{w} Я даже не знаю, как тебя благодарить."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Да ты чё, без проблем вообще.{w} У меня родители дома, так что я даже чаем угощу."
            $ portrait_egor.disappear()
            $ portrait_main.disappear()
            hide screen after_bar_scene_2 with usual_transition
            show screen after_bar_scene_3(blur_out) with usual_transition
            $ portrait_egor.appear("dressed", "normal", .3, False)
            $ portrait_main.appear("dressed", "normal", .7, True)
            speech.main "Я пропустил три дня учёбы и опять прогуливаю пары.{w} Но, с другой стороны, что мне есть?{w} А так хотя бы будут деньги. Ну и чай попью."
            speech.main "Ничего страшного, никуда не убежит эта учеба.{w} У меня все под контролем."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_egor.morph(None, None, None, True)
            speech.egor "Правильно думаешь, братанчик, всё нормально будет.{w} У нас за пропуски не гоняют."
            $ portrait_egor.disappear()
            $ portrait_main.disappear()
            hide screen after_bar_scene_3 with usual_transition
            show screen after_bar_scene_4(blur_out) with usual_transition
            $ portrait_main.appear("dressed", "normal", .7, False)
            $ portrait_egor.appear("dressed", "normal", .3, True)
            stop ambient fadeout .5
            speech.main "Проходи, располагайся, я сейчас приду."
            $ portrait_egor.disappear()
            $ portrait_main.disappear()
            show screen after_bar_scene_4(blur_in)
            speech.thought "А у него уютно!{w} В прихожке даже пуфик стоит.{w} На котором..."
            hide screen after_bar_scene_4 with usual_transition
            show screen after_bar_scene_5 with usual_transition
            stop music fadeout .5
            speech.thought "Мои наушники и мой кошелек." 
            hide screen after_bar_scene_5 with usual_transition
            speech.thought "..."
    return













screen history_class_scene_1:
    add "bg_english_classroom.jpg" fit "fill"
    zorder -10

screen history_class_scene_2(how):
    add "bg_desks_students.jpg" fit "fill" at how
    zorder -10

screen history_class_scene_3(how):
    add "bg_history_teacher.jpg" fit "fill" at how
    zorder -10

screen history_class_scene_4(how):
    add "bg_nine_sk.jpg" fit "fill" at how
    zorder -10

define history_class_music_1 = "Toby Fox — Another Medium.mp3"
define history_class_music_2 = "Toby Fox — Hopes And Dreams.mp3"
define history_class_ambient_1 = "Classroom Noise.mp3"
define history_class_ambient_2 = "City Noise.mp3"

label history_class_script:
    show screen history_class_scene_1 with usual_transition
    stop music fadeout .5
    play music history_class_music_1 fadein .5
    speech.thought "Я бежал от него дальше, чем видел.{w} Об уже сделанном не жалеют, но зачем я пошёл тогда с ним?{w} Как я... Я?{w} Человек, который не любит новые знакомства и постоянно сидит дома с чипсами..."
    speech.thought "Короче говоря, я пришёл на пару по истории.{w} Прикиньте чего? Модеус сошёл с ума.{w} Он поменял мне преподов, причём сам.{w} Просто так.{w} Ну точнее не преподов, а препода."
    speech.thought "Как раз по истории.{w} Я написал куратору, но он пока что не ответил.{w} Ну, а я теперь завязал с пропуском пар, поэтому..."
    hide screen history_class_scene_1 with usual_transition
    show screen history_class_scene_2(blur_out) with usual_transition
    stop ambient fadeout .5
    play ambient history_class_ambient_1 loop fadein .5
    $ portrait_valeriya.appear("undressed", "normal", .7, False)
    $ portrait_kseniya.appear("undressed", "normal", .3, True)
    speech.kseniya "...И я предполагаю, что быть либералами невероятно здорово и обоснованно, ведь если мы обратимся к статистике в начале 20 века... {w}Ты...{w} ты слушаешь?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    Character("???", kind = speech.valeriya) "Да я тут такой вкусный чай купила, подожди, хочу попробовать.{w} Либералами? Да, можно.{w} Можно и социалистами.{w} Про них же много книг написали."
    Character("???", kind = speech.valeriya) "Вон, кстати, точно социалист идёт."
    $ portrait_valeriya.morph(None, None, .8, False)
    $ portrait_kseniya.morph(None, None, .5, None)
    $ portrait_main.appear("undressed", "sad", .2, True)
    speech.main "Ну, в какой-то степени она права...{w} У меня теперь деньги общие, и наушники общие...{w} Неизвестно с кем."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "happy", None, True)
    speech.kseniya "[player_name], здравствуй! Мы и на истории у одного преподавателя?{w} Восхитительно!"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, "normal", None, True)
    speech.main "О, привет, Ксю. Я сяду тут к вам?{w} Какая тема пары?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "normal", None, True)
    speech.kseniya "У нас сейчас будет конференция, мы должны выступать за одно из течений: либерализм, консерватизм или же социализм."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, True)
    Character("???", kind = speech.valeriya) "Может тогда в команду соберёмся?{w} Раз вы знакомы. Щас ещё Вика придёт.{w} О, а вот и..."
    $ portrait_valeriya.morph(None, None, .6, False)
    $ portrait_kseniya.morph(None, None, .4, None)
    $ portrait_viktoriya.appear("undressed", "sad", .8, True)
    speech.viktoriya "Я не-на-ви-жу этого идиота, Лера, что я сделала?{w} Ты вот мне объясни?{w} Просто прекратил общение, он нормальный?"
    $ portrait_viktoriya.morph(None, "happy", None, None)
    speech.viktoriya "Ой...{w} Приветики!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "[player_name], это Вика; Вика, это [player_name].{w} Мы социалисты?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    speech.kseniya "Предполагаю, что да?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "surprised", None, True)
    speech.narrator "*Лера шепчет Вике на ухо*"
    speech.valeriya "О ком речь?.."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "surprised", None, True)
    speech.narrator "*Вика шепчет Лере на ухо*"
    speech.valeriya "Догадайся с трёх раз..."
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    hide screen history_class_scene_2 with usual_transition
    show screen history_class_scene_3(None) with usual_transition
    Character("Преподаватель", kind = speech.generic) "Ну что, готовы к дебатам?{w} Правила такие: выступает одна команда — другие слушают.{w} Потом можете заваливать друг друга вопросами и аргументами, загонять в тупик."
    Character("Преподаватель", kind = speech.generic) "Команде-победителю даю десять баллов в БРС.{w} Даю вам время на подготовку."
    show screen history_class_scene_3(blur_out)
    $ portrait_viktoriya.appear("undressed", "normal", .5, True)
    speech.viktoriya "Так, смотрите.{w} Я принесла усы и бороду. Как тебя там...{w} Э-э-э... [player_name]?{w} Держи, ты Ленин.{w} Лероу, лови пиджак.{w} Ксюша-держи плакат.{w} Вот так выходим и рассказываем лозунги."
    $ portrait_viktoriya.morph(None, "happy", None, None)
    speech.viktoriya "Ну какие вы красивые!"
    $ portrait_viktoriya.morph(None, None, .3, False)
    $ portrait_valeriya.appear("undressed", "normal", .7, True)
    speech.valeriya "Давайте по сценарию: Я говорю лозунг социалистов, потом рассказываем по очереди.{w} Есть одна идейка... Такой, что-то вроде сюжетного поворота.{w} Потом вам объясню."
    $ portrait_valeriya.morph(None, None, .8, False)
    $ portrait_viktoriya.morph(None, None, .2, None)
    $ portrait_kseniya.appear("undressed", "normal", .5, True)
    speech.kseniya "Если опираться на исторические сведения, то у социалистов были все шансы выиграть.{w} Проанализировав их выступления, я пришла к выводу, что нужно упоминать крестьянский вопрос."
    speech.kseniya "Он притягивает внимание публики."
    $ portrait_kseniya.morph(None, None, .6, False)
    $ portrait_main.appear("undressed", "normal", .4, True)
    speech.main "Офигеть вы ребят...{w} У меня есть идея..."
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    hide screen history_class_scene_3 with usual_transition
    show screen text_scene("Некоторое время спустя") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen history_class_scene_3(None) with usual_transition
    speech.thought "Мы выступили просто великолепно, я нигде так не выступал.{w} Костюмы Вики, структура выступления Леры, аналитика Ксюши — бомба."
    speech.thought "Я на коленях сделал сайт социалистов. Ну, каким бы он был в то время...{w} Мне кажется, преподавателю... понравилось?"
    Character("Преподаватель", kind = speech.generic) "Ну, ребята, я получил наслаждение, наблюдая за вами.{w} Посчитаем количество плюсов?"
    Character("Преподаватель", kind = speech.generic) "12 — Консерваторы, 14 — Либералы, и...{w} 17 — социалы.{w} Кажется, у нас есть победитель!"
    hide screen history_class_scene_3 with usual_transition
    show screen history_class_scene_4(blur_out) with usual_transition
    stop music fadeout .5
    play music history_class_music_2 fadein .5
    stop ambient fadeout .5
    play ambient history_class_ambient_2 loop fadein .5
    $ portrait_viktoriya.appear("dressed", "normal", .2, False)
    $ portrait_main.appear("dressed", "normal", .4, False)
    $ portrait_kseniya.appear("dressed", "normal", .6, False)
    $ portrait_valeriya.appear("dressed", "normal", .8, False)
    speech.narrator "*Лера пьёт чай из термоса*"
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "А я сегодня опоздала опять.{w} Прикиньте, захожу в расписание, а там другой препод по истории.{w} Я вообще его не выбирала."
    speech.viktoriya "Чё за бред, так и не поняла.{w} Ну оно и к лучшему, иначе вас бы не встретила."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "О-о, то же самое.{w} Может, сбой?{w} Не должны быть такие перемены преподов."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Да у нас вроде все нормально."
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    show screen history_class_scene_4(blur_in) 
    speech.thought "Потом мы вспоминали наше выступление.{w} Я задумался над словами Вики: может, правда всё к лучшему?{w} Но модеус правда шалит." 
    show screen history_class_scene_4(blur_out) 
    $ portrait_viktoriya.appear("dressed", "happy", .2, True)
    $ portrait_main.appear("dressed", "normal", .4, False)
    $ portrait_kseniya.appear("dressed", "normal", .6, False)
    $ portrait_valeriya.appear("dressed", "normal", .8, False)
    speech.viktoriya "Ну какой же кайф.{w} А они ещё нам: “А как вы собираетесь помогать крестьянам?”, а ты им: “Прочитайте на сайте!”"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "А вот ладно сайт.{w} Но вы прикиньте, сделать историю в виртуале.{w} То есть смоделировать какие-то события...{w} Ну, например, в игре. Было бы прикольно."
    speech.valeriya "Вика, ты бы как Ленина изобразила?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "surprised", None, True)
    speech.viktoriya "Ну усы, борода понятное дело, сзади — плакат социалистов.{w} И в толпе его нарисовала бы."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, True)
    speech.valeriya "... И вот он идёт на площадь и говорит...{w} Нет-нет, он разрабатывает план по восстановлению страны."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Ребят, аккуратно: машина.{w} Откуда у вас столько идей?{w}"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    speech.kseniya "А что, забавно.{w} Такая игра скорее всего была бы популярна, ведь в настоящее время школьники не любят учить материал по учебникам.{w} А игры проходят около 3,7 млрд человек."
    $ portrait_kseniya.morph(None, "sad", None, None)
    speech.kseniya "Ну это уже не актуально, к сожалению."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "Да-а, эта идея уже занята."
    $ portrait_viktoriya.morph(None, None, None, False)
    stop music fadeout .5
    speech.thought "По спине у меня пробежал холодок.{w} Неужели..?"
    $ portrait_main.morph(None, None, None, True)
    speech.main "Какая идея?{w} Вы о чём?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Ты не слышал?{w} Один пекус запатентовал идею в Точке Кипения."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "Платформа для создания любых игр."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Нет...{w} нет-нет-нет!"
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    hide screen history_class_scene_4 with usual_transition
    speech.main "..."
    speech.kseniya "Все нормально?{w} [player_name]?"
    return











screen history_alternative_scene_1:
    add "bg_english_classroom.jpg" fit "fill"
    zorder -10

screen history_alternative_scene_2(how):
    add "bg_desks_students.jpg" fit "fill" at how
    zorder -10

screen history_alternative_scene_3(how):
    add "bg_history_teacher.jpg" fit "fill" at how
    zorder -10

screen history_alternative_scene_4(how):
    add "bg_nine_sk.jpg" fit "fill" at how
    zorder -10

screen history_alternative_scene_5(how):
    add "bg_car_street.jpg" fit "fill" at how
    zorder -10

screen history_alternative_scene_6(how):
    add "bg_alley_empty.jpg" fit "fill" at how
    zorder -10

define history_alternative_music_1 = "Toby Fox — Another Medium.mp3"
define history_alternative_music_2 = "Toby Fox — Hopes And Dreams.mp3"
define history_alternative_ambient_1 = "Classroom Noise.mp3"
define history_alternative_ambient_2 = "City Noise.mp3"

label history_alternative_script:
    show screen history_alternative_scene_1 with usual_transition
    stop music fadeout .5
    play music history_alternative_music_1 fadein .5
    speech.thought "Я бежал от него дальше, чем видел.{w} Он меня пугает.{w} Слишком... добрый?{w} Короче я пас. Если вы выбрали этот вариант, то вы либо зубрилкин..."
    speech.thought "...  либо тоже не доверяете Егору.{w} Короче говоря, пойдёмте со мной на пару по истории.{w} Прикиньте чего? Модеус сошел с ума. Он поменял мне преподов, причем сам."
    speech.thought "Просто так. Ну точнее не преподов, а препода.{w} Как раз по истории. Я написал куратору, но он пока что не ответил.{w} Ну, а я теперь завязал с пропуском пар, поэтому..."
    hide screen history_alternative_scene_1 with usual_transition
    show screen history_alternative_scene_2(blur_out) with usual_transition
    stop ambient fadeout .5
    play ambient history_alternative_ambient_1 loop fadein .5
    $ portrait_valeriya.appear("undressed", "normal", .7, False)
    $ portrait_kseniya.appear("undressed", "normal", .3, True)
    speech.kseniya "...И я предполагаю, что быть либералами невероятно здорово и обоснованно, ведь если мы обратимся к статистике в начале 20 века... {w}Ты...{w} ты слушаешь?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    Character("???", kind = speech.valeriya) "Да я тут такой вкусный чай купила, подожди, хочу попробовать.{w} Либералами? Да, можно.{w} Можно и социалистами.{w} Про них же много книг написали."
    Character("???", kind = speech.valeriya) "Вон, кстати, точно социалист идёт."
    $ portrait_valeriya.morph(None, None, .8, False)
    $ portrait_kseniya.morph(None, None, .5, None)
    $ portrait_main.appear("undressed", "sad", .2, True)
    speech.main "Ну, в какой-то степени она права.{w} У меня комната общая, кухня общая...{w} Да и еда с Ваней тоже...{w} общая."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "happy", None, True)
    speech.kseniya "[player_name], здравствуй! Мы и на истории у одного преподавателя?{w} Восхитительно!"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, "normal", None, True)
    speech.main "О, привет, Ксю. Я сяду тут к вам?{w} Какая тема пары?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "normal", None, True)
    speech.kseniya "У нас сейчас будет конференция, мы должны выступать за одно из течений: либерализм, консерватизм или же социализм."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, True)
    Character("???", kind = speech.valeriya) "Может тогда в команду соберёмся?{w} Раз вы знакомы. Щас ещё Вика придёт.{w} О, а вот и..."
    $ portrait_valeriya.morph(None, None, .6, False)
    $ portrait_kseniya.morph(None, None, .4, None)
    $ portrait_viktoriya.appear("undressed", "sad", .8, True)
    speech.viktoriya "Я не-на-ви-жу этого идиота, Лера, что я сделала?{w} Ты вот мне объясни?{w} Просто прекратил общение, он нормальный?"
    $ portrait_viktoriya.morph(None, "happy", None, None)
    speech.viktoriya "Ой...{w} Приветики!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "[player_name], это Вика; Вика, это [player_name].{w} Мы социалисты?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    speech.kseniya "Предполагаю, что да?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "surprised", None, True)
    speech.narrator "*Лера шепчет Вике на ухо*"
    speech.valeriya "О ком речь?.."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "surprised", None, True)
    speech.narrator "*Вика шепчет Лере на ухо*"
    speech.valeriya "Догадайся с трёх раз..."
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    hide screen history_alternative_scene_2 with usual_transition
    show screen history_alternative_scene_3(None) with usual_transition
    Character("Преподаватель", kind = speech.generic) "Ну что, готовы к дебатам?{w} Правила такие: выступает одна команда — другие слушают.{w} Потом можете заваливать друг друга вопросами и аргументами, загонять в тупик."
    Character("Преподаватель", kind = speech.generic) "Команде-победителю даю десять баллов в БРС.{w} Даю вам время на подготовку."
    show screen history_alternative_scene_3(blur_out)
    $ portrait_viktoriya.appear("undressed", "normal", .5, True)
    speech.viktoriya "Так, смотрите.{w} Я принесла усы и бороду. Как тебя там...{w} Э-э-э... [player_name]?{w} Держи, ты Ленин.{w} Лероу, лови пиджак.{w} Ксюша-держи плакат.{w} Вот так выходим и рассказываем лозунги."
    $ portrait_viktoriya.morph(None, "happy", None, None)
    speech.viktoriya "Ну какие вы красивые!"
    $ portrait_viktoriya.morph(None, None, .3, False)
    $ portrait_valeriya.appear("undressed", "normal", .7, True)
    speech.valeriya "Давайте по сценарию: Я говорю лозунг социалистов, потом рассказываем по очереди.{w} Есть одна идейка... Такой, что-то вроде сюжетного поворота.{w} Потом вам объясню."
    $ portrait_valeriya.morph(None, None, .8, False)
    $ portrait_viktoriya.morph(None, None, .2, None)
    $ portrait_kseniya.appear("undressed", "normal", .5, True)
    speech.kseniya "Если опираться на исторические сведения, то у социалистов были все шансы выиграть.{w} Проанализировав их выступления, я пришла к выводу, что нужно упоминать крестьянский вопрос."
    speech.kseniya "Он притягивает внимание публики."
    $ portrait_kseniya.morph(None, None, .6, False)
    $ portrait_main.appear("undressed", "normal", .4, True)
    speech.main "Офигеть вы ребят...{w} У меня есть идея..."
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    hide screen history_alternative_scene_3 with usual_transition
    show screen text_scene("Некоторое время спустя") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen history_alternative_scene_3(None) with usual_transition
    speech.thought "Мы выступили просто великолепно, я нигде так не выступал.{w} Костюмы Вики, структура выступления Леры, аналитика Ксюши — бомба."
    speech.thought "Я на коленях сделал сайт социалистов. Ну, каким бы он был в то время...{w} Мне кажется, преподавателю... понравилось?"
    Character("Преподаватель", kind = speech.generic) "Ну, ребята, я получил наслаждение, наблюдая за вами.{w} Посчитаем количество плюсов?"
    Character("Преподаватель", kind = speech.generic) "12 — Консерваторы, 14 — Либералы, и...{w} 17 — социалы.{w} Кажется, у нас есть победитель!"
    hide screen history_alternative_scene_3 with usual_transition
    show screen history_alternative_scene_4(blur_out) with usual_transition
    stop music fadeout .5
    play music history_alternative_music_2 fadein .5
    stop ambient fadeout .5
    play ambient history_alternative_ambient_2 loop fadein .5
    $ portrait_viktoriya.appear("dressed", "normal", .2, False)
    $ portrait_main.appear("dressed", "normal", .4, False)
    $ portrait_kseniya.appear("dressed", "normal", .6, False)
    $ portrait_valeriya.appear("dressed", "normal", .8, False)
    speech.narrator "*Лера пьёт чай из термоса*"
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "А я сегодня опоздала опять.{w} Прикиньте, захожу в расписание, а там другой препод по истории.{w} Я вообще его не выбирала."
    speech.viktoriya "Чё за бред, так и не поняла.{w} Ну оно и к лучшему, иначе вас бы не встретила."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "О-о, то же самое.{w} Может, сбой?{w} Не должны быть такие перемены преподов."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Да у нас вроде все нормально."
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    show screen history_alternative_scene_4(blur_in) 
    speech.thought "Потом мы вспоминали наше выступление.{w} Я задумался над словами Вики: может, правда всё к лучшему?{w} Но модеус правда шалит." 
    show screen history_alternative_scene_4(blur_out) 
    $ portrait_viktoriya.appear("dressed", "happy", .2, True)
    $ portrait_main.appear("dressed", "normal", .4, False)
    $ portrait_kseniya.appear("dressed", "normal", .6, False)
    $ portrait_valeriya.appear("dressed", "normal", .8, False)
    speech.viktoriya "Ну какой же кайф.{w} А они ещё нам: “А как вы собираетесь помогать крестьянам?”, а ты им: “Прочитайте на сайте!”"
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    hide screen history_alternative_scene_4 with usual_transition
    show screen history_alternative_scene_5(blur_out) with usual_transition
    $ portrait_viktoriya.appear("dressed", "happy", .2, False)
    $ portrait_main.appear("dressed", "normal", .4, False)
    $ portrait_kseniya.appear("dressed", "normal", .6, False)
    $ portrait_valeriya.appear("dressed", "normal", .8, True)
    speech.valeriya "А вот ладно сайт.{w} Но вы прикиньте, сделать историю в виртуале.{w} То есть смоделировать какие-то события...{w} Ну, например, в игре. Было бы прикольно."
    speech.valeriya "Вика, ты бы как Ленина изобразила?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "surprised", None, True)
    speech.viktoriya "Ну усы, борода понятное дело, сзади — плакат социалистов.{w} И в толпе его нарисовала бы."
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    hide screen history_alternative_scene_5 with usual_transition
    show screen history_alternative_scene_6(blur_out) with usual_transition
    $ portrait_viktoriya.appear("dressed", "happy", .2, False)
    $ portrait_main.appear("dressed", "normal", .4, False)
    $ portrait_kseniya.appear("dressed", "normal", .6, False)
    $ portrait_valeriya.appear("dressed", "normal", .8, True)
    speech.valeriya "... И вот он идёт на площадь и говорит...{w} Нет-нет, он разрабатывает план по восстановлению страны."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Ребят, аккуратно: машина.{w} Откуда у вас столько идей?{w}"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    speech.kseniya "А что, забавно.{w} Такая игра скорее всего была бы популярна, ведь в настоящее время школьники не любят учить материал по учебникам.{w} А игры проходят около 3,7 млрд человек."
    $ portrait_kseniya.morph(None, "sad", None, None)
    $ portrait_main.morph(None, "happy", None, True)
    speech.main "Слушайте...{w} Да была у меня одна такая мысля..."
    show screen history_alternative_scene_6(blur_in)
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    ""
    hide screen history_alternative_scene_6 with usual_transition
    return












screen snow_games_scene_1(how):
    add "bg_alley_snow.jpg" fit "fill" at how
    zorder -10

screen snow_games_scene_2(how):
    add "bg_none_1.jpg" fit "fill" at how
    zorder -10

screen snow_games_scene_3(how):
    add "bg_snow_ring.jpg" fit "fill" at how 
    zorder -10

define snow_games_music_1 = "Toby Fox — Asgore.mp3"

label snow_games_script:
    show screen snow_games_scene_1(None) with usual_transition
    ""
    stop music fadeout .5
    play music snow_games_music_1 fadein .5
    show screen snow_games_scene_1(blur_out)
    $ portrait_valeriya.appear("dressed", "happy", .7, False)
    $ portrait_viktoriya.appear("dressed", "happy", .3, True)
    speech.viktoriya "Я бросаю!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "surprised", None, True)
    speech.valeriya "Не-е-е-ет!"
    $ portrait_valeriya.morph(None, None, None, False)
    speech.thought "Я лишь краем глаза успел увидеть, как в Леру летит снежок размером с {a=https://fizteh.urfu.ru/ru/about/istorija-fiztekha/}{i}корпус физтеха{/i}{/a}."
    $ portrait_viktoriya.morph(None, None, .5, None)
    $ portrait_valeriya.morph(None, None, .8, None)
    $ portrait_kseniya.appear("dressed", "sad", .2, True)
    speech.kseniya "Мы не сможем выступать в таком виде...{w} Вы меня слышите?"
    $ portrait_kseniya.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_valeriya.disappear()
    hide screen snow_games_scene_1 with usual_transition
    show screen snow_games_scene_2(blur_out) with usual_transition
    $ portrait_kseniya.appear("dressed", "sad", .2, False)
    $ portrait_viktoriya.appear("dressed", "happy", .5, False)
    $ portrait_valeriya.appear("dressed", "sad", .8, True)
    speech.valeriya "Вика, я вся в снегу..."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    speech.viktoriya "Ха-ха-ха-ха-ха-ха!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    speech.valeriya "Ну вы же взрослые люди..."
    $ portrait_kseniya.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_valeriya.disappear()
    hide screen snow_games_scene_2 with usual_transition
    show screen snow_games_scene_3(blur_out) with usual_transition
    $ portrait_viktoriya.appear("dressed", "happy", .2, False)
    $ portrait_valeriya.appear("dressed", "sad", .8, False)
    $ portrait_main.appear("dressed", "happy", .5, True)
    speech.main "Берегись!"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "Не-е-е-ет!"
    $ portrait_viktoriya.morph(None, None, None, False)
    speech.thought "Я запустил в Вику снежок размером с {a=https://www.dk.ru/wiki/bc-vysockiy}{i}Высоцкого{/i}{/a}."
    $ portrait_valeriya.morph(None, "happy", None, True)
    speech.valeriya "Ме-е-есть!"
    $ portrait_valeriya.morph(None, None, .8, False)
    $ portrait_viktoriya.morph(None, None, .2, None)
    $ portrait_main.morph(None, "normal", .4, None)
    $ portrait_vanya.appear("undressed", "normal", .6, True)
    speech.vanya "Чуваки, да вы вообще не боитесь, я смотрю."
    $ portrait_vanya.morph(None, None, None, False)
    speech.thought "Я очень волновался, но, как и всегда, не хотел показывать это команде...{w} Команде?{w} Ну да...{w} Я кое-что забыл вам рассказать... Эм...{w} Ну..."
    $ portrait_vanya.morph(None, "happy", None, True)
    speech.vanya "Вам так-то выступать сейчас перед всем УрФУ со своим проектом, прикол, да?"
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "Тебе вообще не холодно в одной рубашке на улице?"
    $ portrait_viktoriya.morph(None, None, None, False)
    menu:
        speech.thought "Что сделать с ваней?"
        "Кинуть снежок":
            speech.narrator "*Замахивается и кидает снежок*"
            $ portrait_main.morph(None, "happy", None, True)
            speech.main "А теперь холодно?"
            $ portrait_main.morph(None, None, None, False)
            $ portrait_vanya.morph(None, "sad", None, True)
            speech.vanya "{sc=3}Чувак, за такое на районе чушпаном называют!{/sc}"
            $ portrait_vanya.morph(None, None, None, False)
        "Предложить куртку":
            $ portrait_main.morph(None, None, None, True)
            speech.main "Держи мою куртку, ещё не хватало, чтоб ты заболел."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_vanya.morph(None, "sad", None, True)
            speech.vanya "Мы снимает мелодраму? Убери куртку свою, братанчик, ничё не случится со мной."
            $ portrait_vanya.morph(None, None, None, False)
        "Кое-что спросить":
            $ portrait_main.morph(None, None, None, True)
            speech.main "Слушай... Чувак...{w} Я давно хотел тебя спросить."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_vanya.morph(None, "normal", None, True)
            speech.vanya "Чё спросить?"
            $ portrait_vanya.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Я не знаю, как ты к этому отнесёшься..." 
            $ portrait_main.morph(None, None, None, False)
            $ portrait_vanya.morph(None, "normal", None, True)
            speech.vanya "К чему?"
            $ portrait_vanya.morph(None, None, None, False)
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "Слушай, если это убьёт нашу дружбу, то я..."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_vanya.morph(None, "sad", None, True)
            speech.vanya "Ты перепил что ли? Чё ты несёшь? Давай спрашивай."
            $ portrait_vanya.morph(None, None, None, False)
            $ portrait_main.morph(None, "happy", None, True)
            speech.main "Почему спустя четыре года после первого курса ты всё ещё ходишь в этой рубашке и никогда её не менял?" 
            $ portrait_main.morph(None, None, None, False)
            $ portrait_vanya.morph(None, "happy", None, True)
            speech.vanya "Почему спустя четыре года ты всё так же выглядишь на тринадцать?"
            $ portrait_vanya.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Ладно, один-один" 
            $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "surprised", None, True)
    speech.viktoriya "Стойте...{w} Смотрите туда!"
    $ portrait_viktoriya.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_vanya.disappear()
    $ portrait_main.disappear()
    hide screen snow_games_scene_3 with usual_transition
    return