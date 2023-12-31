label scene4_script:
    if branch_choice_a_b == 1:
        call kitchen_room_script
        call coworking_reveal_script
        call finale_grande_script
    else:
        if branch_choice_1_2 == 1:
            call finale_cats_script
        else:
            if branch_choice_x_y == 1:
                if branch_choice_alpha_beta == 1:
                    if player_score < 30:
                        call finale_beer_script
                    else:
                        call before_vengeance_script
                        if double_ending:
                            call finale_beer_script
                        else:
                            call preparations_script
                            call finale_revenge_script
                else:
                    call finale_homeless_script
            else:
                call finale_alternative_script
    return













screen kitchen_room_scene_1(how):
    add "bg_room_bed.jpg" fit "fill" at how
    zorder -10

screen kitchen_room_scene_2(how):
    add "bg_kitchen_room.jpg" fit "fill" at how
    zorder -10

define kitchen_room_music_1 = "Toby Fox — It's Showtime!.mp3"
define kitchen_room_music_2 = "Toby Fox — Enemy Approaching.mp3"
define kitchen_room_sound = "Notification.mp3"

label kitchen_room_script:
    show screen kitchen_room_scene_1(None) with usual_transition
    stop music fadeout .5
    play music kitchen_room_music_1 fadein .5
    speech.thought "Теперь я хожу на все мероприятия, которые проводит вуз.{w} Теперь мы банда-команда."
    show screen kitchen_room_scene_1(blur_out)
    $ portrait_viktoriya.appear("undressed", "happy", .3, False)
    $ portrait_valeriya.appear("undressed", "happy", .7, False)
    speech.thought "Я не могу представить свой день без Леры и ее термоса с чаем, без Вики, которая стабильно опаздывает на 5 минут и рассказывает анекдоты."
    $ portrait_viktoriya.morph(None, None, .2, None)
    $ portrait_valeriya.morph(None, None, .8, None)
    $ portrait_kseniya.appear("undressed", "happy", .5, False)
    speech.thought "Без культурных бесед с Ксюшей.{w} И без ее странных сообщений.{w} Она продолжала анонимно писать мне после каждого мероприятия."
    speech.thought "“Ты молодец, успех сегодня был на твоей стороне”, “Сегодня Рекурсивные Пряники блистали”..."
    $ portrait_viktoriya.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_kseniya.disappear()
    show screen kitchen_room_scene_1(blur_in)

    speech.thought "Я молчал, но знаете, мне это надое..."
    show screen kitchen_room_scene_1(blur_out)
    $ portrait_valeriya.appear("dressed", "happy", .5, True)
    speech.valeriya "Доставку заказывали?"
    $ portrait_valeriya.morph(None, None, .7, False)
    $ portrait_vanya.appear("undressed", "normal", .3, True)
    speech.vanya "Опа, хоби-дохоби приехали. Коничева, курьерка."
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "Сайонара, Ивантус, суши возьми, пожалуйста."
    $ portrait_vanya.disappear()
    $ portrait_valeriya.disappear()
    hide screen kitchen_room_scene_1 with usual_transition

    show screen kitchen_room_scene_2(blur_out) with usual_transition
    $ portrait_vanya.appear("undressed", "normal", .3, True)
    $ portrait_valeriya.appear("undressed", "normal", .7, False)
    speech.vanya "Чай, вино, медленные танцы?"
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, True)
    speech.valeriya "Благопочтенный господин, желаю чаю, пожалуйста."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_vanya.morph(None, "happy", None, True)
    speech.vanya "Базару ноль, муадмуазель. Ван секонд сильвупле.{w} А где Ксюша?"
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "Чуть задерживается, только не съешь все онигири."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_vanya.morph(None, "normal", None, True)
    speech.vanya "Окей.{w} Чувак, ёмаё, оторвись от мобилы. Чё за дела, хавать пойдём."
    $ portrait_vanya.morph(None, None, .2, False)
    $ portrait_valeriya.morph(None, None, .8, None)
    $ portrait_main.appear("undressed", "normal", .5, True)
    speech.main "Я тут, простите.{w} Мы же идём сегодня в коворкинг?{w} Ты звонила Ксюше?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Коворкинг? Зачем?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Она написала, что встреча в 16 в радике."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_vanya.morph(None, "happy", None, True)
    speech.narrator "*Ваня чавкает*"
    speech.vanya "Чуваки, вы видите друг друга чаще, чем я свою маму, клянусь.{w} Хоть один день посидите в комнате."
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "Она мне ничего не писала..."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "Да зачем ты смотришь в ВК?{w} В СМС зайди."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "В СМС?{w} У меня даже нет её номера."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "normal", None, True)
    speech.main "Очень смешно, дай телефон."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_vanya.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_main.disappear()
    show screen kitchen_room_scene_2(blur_in)
    speech.thought "Но у неё правда не было её номера.{w} Последнее сообщение непонятно от кого.{w} Смайл кота и сердечка."
    show screen kitchen_room_scene_2(blur_out)
    stop music fadeout .5
    play music kitchen_room_music_2 fadein .5
    $ portrait_main.appear("undressed", "normal", .3, False)
    $ portrait_valeriya.appear("undressed", "normal", .7, True)
    speech.valeriya "О чем речь?{w} Кто тебе написал?"
    $ portrait_valeriya.morph(None, None, None, False)
    speech.thought "Я показал ей историю сообщений."
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "Подожди..."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Я просто не понимаю, почему бы не писать в ВК, что за скрытность?"
    $ portrait_main.morph(None, None, None, False)
    play sound kitchen_room_sound
    Character("8-946-xxx-xx-42", kind = speech.polina_hidden) "Лера, коворкинг, 16:00. Важный разговор."
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "..."
    speech.main "Это другой номер..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "Писал не ты?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "При чём тут вообще я?"
    $ portrait_main.morph(None, "normal", None, False)
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "В смысле при чём?{w} А кто позвал нас на первое меро по искусственному интеллекту, ещё в сентябре?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Я что ли?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "Слушай, чувак, ты меня пугаешь..."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "Нет, это ты меня пугаешь."
    $ portrait_main.morph(None, None, None, False)
    speech.narrator "*Ваня удивлённо чавкает*"
    $ portrait_main.morph(None, "surprised", None, True)
    $ portrait_valeriya.morph(None, "surprised", None, True)
    Character("Вместе", kind = speech.generic) "Это Ксюша?!"
    $ portrait_main.morph(None, None, .2, False)
    $ portrait_valeriya.morph(None, None, .8, False)
    $ portrait_vanya.appear("undressed", "normal", .5, True)
    speech.narrator "*Ваня чавкает*"
    speech.vanya "Обалдеть просто..."
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    $ portrait_valeriya.morph(None, "surprised", None, True)
    Character("Вместе", kind = speech.generic) "Это Ксюша!!!"
    $ portrait_main.morph(None, None, .2, False)
    $ portrait_valeriya.morph(None, None, .8, False)
    $ portrait_vanya.morph(None, "happy", None, True)
    speech.narrator "*Ваня чавкает*"
    speech.vanya "Опупеть просто..."
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "В радике в 16?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "Ну, походу."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_vanya.morph(None, None, None, True)
    speech.vanya "Если вы сейчас ливнёте, то я всё сожру, отвечаю!"
    $ portrait_main.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_vanya.morph(None, "normal", None, None)
    speech.vanya "Э-э-й! Чуваки!"
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_vanya.morph(None, "sad", None, True)
    speech.vanya "Офигеть блин.{w} Хоть еду оставили."
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_vanya.disappear()
    hide screen kitchen_room_scene_2 with usual_transition
    return














screen coworking_reveal_scene_1(how):
    add "bg_coworking.jpg" fit "fill" at how
    zorder -10

screen coworking_reveal_scene_2(how):
    add "bg_coworking_dark.jpg" fit "fill" at how
    zorder -10

define coworking_reveal_music_1 = "Toby Fox — Danger Mystery.mp3"
define coworking_reveal_music_2 = "Toby Fox — Dummy!.mp3"
define coworking_reveal_ambient = "Quiet Noise.mp3"
define coworking_reveal_music_3 = "Horn.mp3"
define coworking_reveal_music_4 = "Tention.mp3"
define coworking_reveal_music_5 = "Tention2.mp3"

label coworking_reveal_script:
    show screen coworking_reveal_scene_1(blur_out) with usual_transition
    play ambient coworking_reveal_ambient loop fadein .5
    stop music fadeout .5
    play music coworking_reveal_music_3 fadein .5
    $ portrait_main.appear("undressed", "sad", .7, False)
    $ portrait_valeriya.appear("undressed", "sad", .3, True)
    speech.valeriya "То есть, всё это время она просто завела несколько симок и писала нам?{w} Но зачем?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Я вообще думал, что она просто таким образом сообщает инфу, у меня отключены все уведомления в ВК, а в СМС нет."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Просто, зачем писать мне, если и так практически везде ходим вместе?"
    $ portrait_valeriya.disappear()
    $ portrait_main.disappear()
    hide screen coworking_reveal_scene_1 with usual_transition
    stop music fadeout .5
    play music coworking_reveal_music_4 fadein .5
    speech.thought "Пока я думал, что ответить Лере, мои глаза закрыли чьи-то руки."
    Character("???", kind = speech.polina_hidden) "Приветствую! Угадай, пожалуйста, кто это."
    speech.main "Ксюша, это уже вообще не смешно.{w} Давай мы в игры ещё поиграем, конечно."
    speech.kseniya "Что-то случилось?"
    speech.main "Что случилось? Писать мне с неизвестного номера, ещё и Лере, звать нас сюда..."
    speech.kseniya "Подождите, давайте внесём ясность.{w} Это ведь вы меня позвали, я вообще учила историю."
    stop music fadeout .5
    play music coworking_reveal_music_1 fadein .5
    stop music fadeout .5
    speech.narrator "*Свет в коворкинге гаснет*"
    play music coworking_reveal_music_5 fadein .5
    show screen coworking_reveal_scene_2(None) with usual_transition
    Character("???", kind = speech.polina_hidden) "Ха-ха-ха!"
    speech.thought "..."
    Character("???", kind = speech.polina_hidden) "Ты писал, нет ты писала..."
    speech.thought "..."
    Character("???", kind = speech.polina_hidden) "Забавно, ребята."
    speech.thought "Мы не видели лица человека, силуэт стоял в тени."
    Character("???", kind = speech.polina_hidden) "Ну чего затихли?{w} Нечего сказать?"
    speech.thought "..."
    Character("???", kind = speech.polina_hidden) "Я думала вы быстрее всё поймёте."
    speech.viktoriya "Йоу, всем приветики, я тут задержалась немно...{w} Эм...{w} А что тут происходит? Вы чего в потемках..."
    speech.viktoriya "О-о, Полина-а-а!"
    show screen coworking_reveal_scene_2(blur_out)
    $ portrait_polina.appear("undressed", "normal", .5, False)
    $ portrait_main.appear("undressed", "sad", .16, False)
    $ portrait_viktoriya.appear("undressed", "surprised", .68, False)
    $ portrait_valeriya.appear("undressed", "sad", .32, False)
    $ portrait_kseniya.appear("undressed", "surprised", .84, True)
    stop music fadeout .5
    play music coworking_reveal_music_2 fadein .5
    speech.kseniya "Извини, кто?.."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Что за бред, кто это?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Силь ву пле, кто?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_polina.morph(None, "sad", None, True)
    speech.polina "Вика, ну ты вот нормальная вообще?"
    $ portrait_polina.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Да представляешь, я захотела кофе, а в итоге меня на 20 минут задержали."
    $ portrait_viktoriya.morph(None, "sad", None, None)
    speech.viktoriya "Я что-то испортила?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Я, если честно, чуть не умер.{w} Ты, ёптель, кто вообще?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_polina.morph(None, "happy", None, True)
    speech.polina "Ха-ха-ха, я тот самый неизвестный номер, всем рекурсивным пряникам привет!"
    $ portrait_polina.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Ты... Чего?!"
    $ portrait_main.morph(None, None, None, False)
    speech.thought "..."
    $ portrait_viktoriya.morph(None, "sad", None, None)
    speech.viktoriya "Может анекдот?..."
    $ portrait_viktoriya.disappear()
    $ portrait_polina.disappear()
    $ portrait_main.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_kseniya.disappear()
    hide screen coworking_reveal_scene_2 with usual_transition
    return











screen finale_grande_scene_1(how):
    add "bg_prologue.jpg" fit "fill" at how
    zorder -10

screen finale_grande_scene_2(how):
    add "bg_finale.jpg" fit "fill" at how
    zorder -10

screen finale_grande_scene_3:
    add "bg_audience.jpg" fit "fill"
    zorder -10

screen finale_grande_scene_4:
    add "bg_mch_spotlight.jpg" fit "fill"
    zorder -10

define finale_grande_music_1 = "Siren.mp3"
define finale_grande_music_2 = "Lorn — MSDOS.mp3"
define finale_grande_ambient = "Lively Noise.mp3"
define finale_grande_sound = "Short Applause.mp3"

label finale_grande_script:
    stop ambient fadeout .5
    play ambient finale_grande_ambient loop fadein .5
    stop music fadeout .5
    play music finale_grande_music_1 fadein .5
    speech.thought "..."
    show screen finale_grande_scene_1(None) with usual_transition
    ""
    show screen finale_grande_scene_1(blur_out)
    speech.thought "Я сидел на первом ряду в этом концертном зале и смотрел на пустую сцену."
    speech.thought "..."
    speech.main "Вся слава должна быть мне?{w} Или всё идет так, как и должно."
    speech.main "Я поступил неправильно, доверившись.{w} Или же наоборот, правильно?"
    speech.thought "..."
    play sound finale_grande_sound
    speech.thought "Я отдалённо слышал аплодисменты."
    speech.main "Мне выходить на сцену?"
    speech.thought "Я должен заполнить это пустое место?"
    speech.thought "..."
    speech.main "Почему вы не отвечаете на мои вопросы?"
    speech.thought "..."
    speech.main "{sc=5}Почему вы молчите?!{/sc}"

    if player_score >= 40:
        stop music fadeout .5
        $ portrait_viktoriya.appear("undressed", "normal", .5, True)
        speech.viktoriya "Мы не молчим, всё хорошо, свет настроен.{w} [player_name], мы заслужили это..."
        $ portrait_viktoriya.morph(None, "happy", None, None)
        speech.viktoriya "Ты заслужил.{w} Выходи на сцену."
        $ portrait_viktoriya.morph(None, "normal", None, False)
        speech.main "Всё хорошо?{w} Мы правда это сделали?{w} Мы?"
        $ portrait_viktoriya.disappear()
        hide screen finale_grande_scene_1 with usual_transition
        play music finale_grande_music_2 fadein .5
        show screen finale_grande_scene_4 with usual_transition
        speech.main "Это было настолько давно, друзья мои...{w} Мы тогда даже не могли представить, что нас ждет.{w} Вам, наверное, интересно, кто такая Полина. И как она нас нашла." 
        hide screen finale_grande_scene_4 with usual_transition
        show screen finale_grande_scene_2(None) with usual_transition
        speech.narrator "*В зале взмывает лес рук*"
        speech.main "Да, пожалуйста...{w} Наверное, пришло время вопросов."
        while not meeting_tried_game or not meeting_tried_start or not meeting_tried_polina or not meeting_tried_who:
            menu: 
                "Про что игра?" if not meeting_tried_game:
                    $ meeting_tried_game = True
                    Character("Слушатель", kind = speech.generic) "Эмм... Так мы не очень поняли...{w} Вы сделали игру про свой путь в ИИ?"
                    hide screen finale_grande_scene_2 with usual_transition
                    show screen finale_grande_scene_4 with usual_transition
                    speech.main "Не совсем, мы...{w} {b}Мы сделали ИИ, который сделал игру{/b}...{w} Мы сделали ИИ, который не только выполняет команды, он...{w} Он чувствует."
                    speech.main "Ну, это вам судить, на самом деле.{w} Если игра получилась душевной, то моя работа выполнена качественно...{w} Наша работа."
                    speech.main "Основной посыл игры в том (по крайней мере, так решил ИИ), что {b}выбрав УрФУ, я смог достичь таких высот{/b}.{w} И, насколько я могу судить по себе, искусственный интелект нисколько не ошибся."
                    hide screen finale_grande_scene_4 with usual_transition
                    show screen finale_grande_scene_2(None) with usual_transition
                "С чего всё началось?" if not meeting_tried_start:
                    $ meeting_tried_start = True
                    Character("Слушатель", kind = speech.generic) "То есть, вы хотите сказать, что именно первый курс в УрФУ положил начало в вашей профессии?"
                    hide screen finale_grande_scene_2 with usual_transition
                    show screen finale_grande_scene_4 with usual_transition
                    speech.main "Ха-ха, вы удивлены?{w} А я то как! Да, представляете.{w} Образование в России не отбило у меня желание учиться.{w} На самом деле структура ИОТ помогла. Как и мероприятия, как вы уже поняли, олимпиады."
                    speech.main "Моя команда.{w} Ваня тоже. Чё бы я, блин, делал без него!"
                    hide screen finale_grande_scene_4 with usual_transition
                    show screen finale_grande_scene_2(None) with usual_transition
                    $ portrait_vanya.appear("undressed", "happy", .5, True)
                    speech.narrator "*Ваня кричит из зала*"
                    speech.vanya "Загнулся бы без меня, ха-ха-ха-ха!"
                    $ portrait_vanya.disappear()
                "Кто такая Полина?" if not meeting_tried_polina:
                    $ meeting_tried_polina = True
                    Character("Слушатель", kind = speech.generic) "Так кто такая Полина?{w} Как она нашла ваши номера?"
                    hide screen finale_grande_scene_2 with usual_transition
                    show screen finale_grande_scene_4 with usual_transition
                    speech.main "Наш тимлид.{w} Она залезла в ведомость и посмотрела наши номера, представляете.{w} Писала нам, на какие мероприятия приходить."
                    speech.main "Она собрала команду.{w} С Викой они были в одной группе. Вика рассказала про меня, потом про Леру и Ксюшу."
                    speech.main "А Полина решила сделать нас командой. У неё талант.{w} После того разговора в коворкинге мы отправились есть пиццу."
                    speech.main "А потом, через две недели, мы подали заявку на наш первый стартап.{w} И теперь, я стою перед вами с нашим уже финальным проектом."
                    hide screen finale_grande_scene_4 with usual_transition
                    show screen finale_grande_scene_2(None) with usual_transition
                "Кем вы стали?" if not meeting_tried_who:
                    $ meeting_tried_who = True
                    Character("Слушатель", kind = speech.generic) "Так кем вы стали после обучения в вузе?"
                    hide screen finale_grande_scene_2 with usual_transition
                    show screen finale_grande_scene_4 with usual_transition
                    speech.main "Я — разработчик искусственного интеллекта, Лера — гейм-дизайнер. Она придумывает идеи для наших стартапов.{w} Вика — дизайнер. Ей помогает Ваня с некоторыми проектами. Они хорошо работают вместе."
                    speech.main "Ксюша — аналитик. Её любовь к математике позволяет нам обходить конкурентов.{w} Ну, а Полина — чокнутый человек, который сплотил нас и подарил нам возможность быть не просто командой...{w} А друзьями."
                    speech.main "ИИ очень хорошо передал {b}важность тимбилдинга в процессе обучения{/b}."
                    hide screen finale_grande_scene_4 with usual_transition
                    show screen finale_grande_scene_2(None) with usual_transition
        speech.main "Вижу кучу рук...{w} Понимаю вас! Но это не конец игры.{w} ИИ дописал её до конца, поэтому вы можете поиграть в неё и узнать, как мы выживали на втором курсе..."
        speech.main "... прогуливали пары, чтобы закончить проекты, и выиграли первый миллион.{w} Тот ИИ, который написал эту игру, есть с этой секунды в свободном доступе."
        speech.main "Если вам хочется рассказать миру историю из своей жизни и сделать это душевно, то силь ву пле!{w} Для этого мы и делали этот проект." 
        hide screen finale_grande_scene_2 with usual_transition
        show screen finale_grande_scene_3 with usual_transition
        ""
        hide screen finale_grande_scene_3 with usual_transition
        $ ending_index = 0

    else:
        stop music fadeout .5
        $ portrait_valeriya.appear("undressed", "normal", .5, True)
        speech.valeriya "Эй!!!{w} Ты слышишь меня?{w} Чего завис?{w} Всё нормально будет."
        $ portrait_valeriya.morph(None, None, None, False)
        speech.main "Я не хочу выходить на сцену."
        $ portrait_valeriya.morph(None, "sad", None, True)
        speech.valeriya "Мы столько всего прошли вместе, и ты отступаешь назад?"
        $ portrait_valeriya.morph(None, "normal", None, None)
        speech.valeriya "Посмотри на этих людей: они пришли посмотреть на такого гения, как ты."
        $ portrait_valeriya.morph(None, None, None, False)
        speech.main "Ты думаешь, у меня получится?"
        $ portrait_valeriya.morph(None, "happy", None, True)
        speech.valeriya "Я {b}знаю{/b}, что у тебя получится."
        $ portrait_valeriya.disappear()
        hide screen finale_grande_scene_1 with usual_transition
        show screen finale_grande_scene_2(None) with usual_transition
        play music finale_grande_music_2 fadein .5
        speech.main "Эм...{w} Что ж, всем...{w} всем при...{w} всем привет.{w} Эм...{w} Только что вы видели...{w} игру.{w} Да, вы наверное, заметили, что это игра."
        show screen finale_grande_scene_2(blur_out)
        $ portrait_egor.appear("undressed", "normal", .5, True)
        menu:
            speech.main "Ну мы в общем, эм..."
            "Чего ты мямлишь, можно нормально говорить?":
                Character("???", kind = speech.egor) "Чего ты мямлишь, можно нормально говорить?"
            "Ничего не слышно, эй, ты, на сцене!":
                Character("???", kind = speech.egor) "Ничего не слышно, эй, ты, на сцене!"
            "Кто пустил этого придурка выступать?":
                Character("???", kind = speech.egor) "Кто пустил этого придурка выступать?"
        $ portrait_egor.morph(None, None, None, False)
        speech.main "Эм...{w} Я..."
        $ portrait_egor.morph(None, None, .3, None)
        $ portrait_viktoriya.appear("undressed", "normal", .7, True)
        speech.viktoriya "Спасибо за вопрос, товарищ!{w} Как я могу к вам обратиться?"
        $ portrait_viktoriya.morph(None, None, None, False)
        $ portrait_egor.morph(None, None, None, True)
        Character("???", kind = speech.egor) "Мармеладная моя, а ещё те чё сказать?{w} Куколка, моё имя ты на всю жизнь запомнишь, если я его сейчас назову."
        $ portrait_egor.morph(None, None, None, False)
        $ portrait_viktoriya.morph(None, "happy", None, True)
        speech.viktoriya "Прекрасно, как раз такого персонажа вы можете увидеть во второй ветке нашей игры.{w} А... Вы не поняли? Этот..."
        speech.viktoriya "Эм, как ты его назвал?{w} Придурок?{w} Так вот, этот придурок — гениальный человек, который разработал ИИ, умеющий создавать игры, и..."
        $ portrait_viktoriya.morph(None, None, .8, False)
        $ portrait_egor.morph(None, None, .2, None)
        $ portrait_valeriya.appear("undressed", "happy", .5, True)
        speech.valeriya "...и обрел команду, которая ему в этом помогала."
        $ portrait_valeriya.morph(None, "normal", None, None)
        speech.valeriya "Теперь, если вы захотите рассказать миру про свой творческий путь, интересный поступок или ещё что-то, вы можете скачать приложение “Gingers” и написать игру самостоятельно. С помощью ИИ."
        $ portrait_valeriya.morph(None, "happy", None, None)
        speech.valeriya "То, что вы видели на экране — презентация игры про наш первый курс в Уральском федеральном.{w} Это была лишь одна из множества веток.{w} Игра есть в открытом доступе, можете пройти её сами. Ну, и..."
        $ portrait_valeriya.morph(None, None, .4, False)
        $ portrait_vanya.appear("undressed", "happy", .6, True)
        speech.vanya "...и, как ляпнула Вика, такой чувак как раз есть в сюжете.{w} Прям чел, ты реал как с экрана слез!"
        $ portrait_vanya.morph(None, None, None, False)
        $ portrait_egor.morph(None, None, None, True)
        Character("???", kind = speech.egor) "Никто не будет проходить вашу тупейшую новеллу, бездари.{w} Вы головой шарите хоть чуть-чуть?{w} Идиоты."
        Character("???", kind = speech.egor) "Ваши фоны ни о чем, дизайн убогий.{w} А сюжет?{w} Ха-ха-ха.{w} Вы называете это сюжетом?{w} А вторая ветка вообще заканчивается..."
        $ portrait_egor.morph(None, None, None, False)
        $ portrait_kseniya.appear("undressed", "normal", .5, True)
        speech.kseniya "Чем?"
        $ portrait_kseniya.morph(None, None, None, False)
        $ portrait_egor.morph(None, None, None, True)
        Character("???", kind = speech.egor) "..."
        $ portrait_egor.morph(None, None, None, False)
        $ portrait_kseniya.morph(None, "happy", None, True)
        speech.kseniya "То есть, Вы прошли её?{w} Замечательно, можете поделиться впечатлениями?"
        $ portrait_kseniya.morph(None, None, None, False)
        $ portrait_egor.morph(None, None, None, True)
        Character("???", kind = speech.egor) "..."
        $ portrait_egor.morph(None, None, None, False)
        $ portrait_kseniya.morph(None, "surprised", None, True)
        speech.kseniya "Однако вы упомянули, что никто не будет проходить игру."
        $ portrait_kseniya.morph(None, None, None, False)
        $ portrait_egor.morph(None, None, None, True)
        Character("???", kind = speech.egor) "..."
        Character("???", kind = speech.egor) "У вас всё равно ничего не получится, идиоты."
        $ portrait_egor.morph(None, None, None, False)
        speech.main "У нас уже получилось, дружок."
        $ portrait_egor.disappear()
        $ portrait_kseniya.disappear()
        $ portrait_vanya.disappear()
        $ portrait_viktoriya.disappear()
        $ portrait_valeriya.disappear()
        hide screen finale_grande_scene_2 with usual_transition
        show screen finale_grande_scene_3 with usual_transition
        ""
        hide screen finale_grande_scene_3 with usual_transition
        $ tmp = "Тогда речь этого молодого человека привлекла просмотры к презентации, и её\nувидело много людей. Человеком из зала оказался отчисленный второкурсник.\n\nВыяснилось, что он наблюдал за “Пряниками” ещё на первом курсе и хотел\nукрасть идею их стартапа. ИИ, разработанный командой, стал популярен.\nТеперь каждый мог рассказать историю из своей жизни через игру."
        show screen text_scene(tmp) with usual_transition
        ""
        hide screen text_scene with usual_transition
        $ ending_index = 1
    return














screen finale_cats_scene_1(how):
    add "bg_prologue.jpg" fit "fill" at how
    zorder -10

screen finale_cats_scene_2:
    add "bg_audience.jpg" fit "fill"
    zorder -10

screen finale_cats_scene_3:
    add "bg_children_classroom.jpg" fit "fill"
    zorder -10

define finale_cats_music_1 = "Siren.mp3"
define finale_cats_music_2 = "Lorn — MSDOS.mp3"
define finale_cats_ambient_1 = "Lively Noise.mp3"
define finale_cats_ambient_2 = "Classroom Noise.mp3"
define finale_cats_sound_1 = "Short Applause.mp3"
define finale_cats_sound_2 = "Notification.mp3"


label finale_cats_script:
    stop ambient fadeout .5
    play ambient finale_cats_ambient_1 loop fadein .5
    stop music fadeout .5
    play music finale_cats_music_1 fadein .5
    speech.thought "..."
    show screen finale_cats_scene_1(None) with usual_transition
    ""
    show screen finale_cats_scene_1(blur_out)
    speech.thought "Я сидел на первом ряду в этом концертном зале и смотрел на пустую сцену."
    speech.thought "..."
    speech.main "Вся слава должна быть мне?{w} Или всё идет так, как и должно."
    speech.main "Я поступил неправильно, доверившись.{w} Или же наоборот, правильно?"
    speech.thought "..."
    play sound finale_cats_sound_1
    speech.thought "Я отдалённо слышал аплодисменты."
    speech.main "Мне выходить на сцену?"
    speech.thought "Я должен заполнить это пустое место?"
    speech.thought "..."
    speech.main "Почему вы не отвечаете на мои вопросы?"
    speech.thought "..."
    speech.main "{sc=5}Почему вы молчите?!{/sc}"

    stop music fadeout .5
    $ portrait_viktoriya.appear("undressed", "normal", .5, True)
    speech.viktoriya "Эй! Ты опять уснул?" 
    $ portrait_viktoriya.morph(None, None, .3, False)
    $ portrait_kseniya.appear("undressed", "normal", .7, True)
    speech.kseniya "У меня не найдется и малейшего слова..."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "В-Все нормально? [player_name]!"
    $ portrait_viktoriya.morph(None, None, None, False)
    speech.main "Да...{w} Привет.{w} Я засмотрелся... Я волнуюсь." 
    play sound finale_cats_sound_2
    $ portrait_kseniya.morph(None, None, None, True)
    speech.kseniya "Мой Наполеон, похоже, проголодался."
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "А я вообще в восторге.{w} Нет, я понимаю, думать среди кошек...{w} Но чтоб придумать такое..."
    $ portrait_viktoriya.morph(None, None, None, False)
    speech.main "И мне сейчас это ещё и презентовать..."
    $ portrait_viktoriya.morph(None, None, .2, None)
    $ portrait_kseniya.morph(None, None, .8, None)
    $ portrait_vanya.appear("undressed", "happy", .5, True)
    speech.vanya "Чувачел, это чё за интонация? Ты шурупишь, что все общажные, кому нельзя заводить питомцев, пользуются тем, что ты создал?"
    speech.vanya "Все-е-е, чувак, вообще все.{w} Давай, подбородок выше и пошлепал!"
    $ portrait_vanya.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_kseniya.disappear()
    hide screen finale_cats_scene_1 with usual_transition
    show screen finale_cats_scene_2 with usual_transition
    play music finale_cats_music_2 fadein .5
    Character("???", kind = speech.generic) "Тогда был его звёздный час.{w} Куча людей пришли на него посмотреть.{w} Он не чувствовал славу, не думал о деньгах. Он гордился, что сделал стольких людей счастливыми."
    Character("???", kind = speech.generic) "[player_name] придумал приложение, которое позволяло людям выбирать животное и ухаживать за ним.{w} Точнее, {b}придумал ИИ{/b}, который генерирует живого питомца."
    stop music fadeout .5
    hide screen finale_cats_scene_2 with usual_transition
    show screen finale_cats_scene_3 with usual_transition
    stop ambient fadeout .5
    play ambient finale_cats_ambient_2 loop fadein .5
    Character("Дети", kind = speech.generic) "И всё-ё-ё? Это всё-ё-ё?!{w} Валерия Алексеевна, ещё-ещё-ещё-ещё!"
    Character("Валерия Алексеевна", kind = speech.generic) "Всё, мои дорогие.{w} Вот вам мотивация приносить людям добро и создавать что-то новое."
    Character("Валерия Алексеевна", kind = speech.generic) "Вы главное запомните, что любые ваши идеи могут быть полезны другим, даже самые необычные."
    Character("Дети", kind = speech.generic) "Какая классная история!{w} Ещё-ещё!"
    Character("Валерия Алексеевна", kind = speech.generic) "Так, ну хорошо.{w} Раз вам понравилась эта сказка, то давайте расскажу и втор..."
    play sound finale_cats_sound_2
    Character("Котоприложение", kind = speech.egor) "Мяу..."
    hide screen finale_cats_scene_3 with usual_transition
    $ ending_index = 2
    return













screen finale_homeless_scene_1(how):
    add "bg_prologue.jpg" fit "fill" at how
    zorder -10

screen finale_homeless_scene_2(how):
    add "bg_audience.jpg" fit "fill" at how
    zorder -10

transform hmls(index):
    blur 15.
    alpha 0.
    linear index * .2
    alpha 1.
    linear .2
    alpha 0.
    linear (10 - index - 1) * .2
    repeat

screen finale_homeless_scene_3:
    add "bg_bar.jpg" fit "fill" at hmls(0)
    add "bg_room_books.jpg" fit "fill" at hmls(1)
    add "bg_rtf_staircase.jpg" fit "fill" at hmls(2)
    add "bg_scooter_street.jpg" fit "fill" at hmls(3)
    add "bg_wallet_zoomed.jpg" fit "fill" at hmls(4)
    add "bg_desk.jpg" fit "fill" at hmls(5)
    add "bg_rtf_parking.jpg" fit "fill" at hmls(6)
    add "bg_street_people.jpg" fit "fill" at hmls(7)
    add "bg_rtf_coffeeshop.jpg" fit "fill" at hmls(8)
    add "bg_first_desk.jpg" fit "fill" at hmls(9)
    zorder -10

define finale_homeless_music_1 = "Siren.mp3"
define finale_homeless_music_2 = "Lorn — ASH.mp3"
define finale_homeless_ambient = "Lively Noise.mp3"
define finale_homeless_sound_1 = "Short Applause.mp3"
define finale_homeless_sound_2 = "Laughter.mp3"

label finale_homeless_script:    
    stop ambient fadeout .5
    play ambient finale_homeless_ambient loop fadein .5
    stop music fadeout .5
    play music finale_homeless_music_1 fadein .5
    speech.thought "..."    
    show screen finale_homeless_scene_1(None) with usual_transition
    ""
    show screen finale_homeless_scene_1(blur_out)
    speech.thought "Я сидел на первом ряду в этом концертном зале и смотрел на пустую сцену."
    speech.thought "..."
    speech.main "Вся слава должна быть мне?{w} Или всё идет так, как и должно."
    speech.main "Я поступил неправильно, доверившись.{w} Или же наоборот, правильно?"
    speech.thought "..."
    play sound finale_homeless_sound_1
    speech.thought "Я отдалённо слышал аплодисменты."
    speech.main "Мне выходить на сцену?"
    speech.thought "Я должен заполнить это пустое место?"
    speech.thought "..."
    speech.main "Почему вы не отвечаете на мои вопросы?"
    speech.thought "..."
    stop music fadeout .5
    play music finale_homeless_music_2 fadein .5
    speech.main "{sc=5}Почему вы молчите?!{/sc}"
    hide screen finale_homeless_scene_1 with usual_transition
    show screen finale_homeless_scene_2(blur_out) with usual_transition
    $ portrait_egor.appear("undressed", "normal", .5, True)
    speech.egor "Друзья! Спасибо, что пришли.{w} Не хотел столь бурного внимания, но без этого никак.{w} Наше приложение начало работать только вчера, а сегодня мы получили уже тысячи игр и различных сюжетов."
    speech.egor "Впечатляет!{w} И я рад, что моя разработка оказалась настолько полезной.{w} Я стою перед вами, чтобы ответить на вопросы, так что смелей."
    $ portrait_egor.morph(None, None, None, False)
    Character("Слушатель", kind = speech.generic) "Как вам в голову пришла идея по созданию ИИ, который пишет игры?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Ну как пришла... Просто сидел и думал...{w} И так и пришла. Главное не как она пришла, а во что она выросла!"
    $ portrait_egor.morph(None, None, None, False)
    Character("Слушатель", kind = speech.generic) "Как вы продвигали свою идею?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "В УрФУ есть потрясающий центр — Точка Кипения.{w} Туда можно патентовать все свои стартапы и начальные идеи с первого курса.{w} И выигрывать деньги, конечно же."
    speech.egor "Только опережайте своих соперников.{w} Идей много, но важнее тот, кто первый их расскажет."
    $ portrait_egor.morph(None, None, None, False)
    speech.main "Разрешите?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Пожалуйста, ещё вопросы."
    $ portrait_egor.morph(None, None, None, False)
    speech.main "Разрешите, пожалуйста?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Так, ну, видимо, их нет, так что мы можем..."
    $ portrait_egor.morph(None, None, None, False)
    speech.main "Как вы будете развивать ваше приложение?{w} Какие обновления стоит ожидать?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Я не давал разрешения говорить." 
    $ portrait_egor.morph(None, None, None, False)
    speech.main "Как вы можете дать будущее тому, что не развивали сами?{w} Что сами не придумывали?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Простите, господа!{w} Сумасшедших тоже куча.{w} Охрана, выведите зрителя с первого ряда."
    $ portrait_egor.morph(None, None, None, False)
    play sound finale_homeless_sound_2
    speech.main "{sc=10}Это моя идея!!!{/sc}{w} {sc=5}Она моя!{/sc}{w} Она...{w} моя, это ведь я... придумал."
    $ portrait_egor.disappear()
    speech.narrator "*[player_name] вывели из зала под смех зрителей*"
    hide screen finale_homeless_scene_2 with usual_transition
    show screen text_scene("Он так и не смог смириться с тем, что у него украли то, что ему было так дорого...\nИдею. Его никто не слушал. Ему никто не верил.") with usual_transition
    ""
    hide screen text_scene with usual_transition
    show screen finale_homeless_scene_3 with usual_transition
    stop ambient fadeout .5
    $ portrait_kseniya.appear("undressed", "sad", .2, False)
    $ portrait_vanya.appear("undressed", "sad", .8, False)
    $ portrait_polina.appear("undressed", "sad", .5, False)
    speech.main "Он обманул меня, слышите?{w} Он, он..."
    $ portrait_kseniya.morph(None, None, None, True)
    speech.kseniya "..."
    $ portrait_kseniya.morph(None, None, None, False)
    speech.main "Он украл её!!!{w} Я должен быть на его месте, это моё, понимаете?{w} Вы слышите меня?"
    $ portrait_vanya.morph(None, None, None, True)
    speech.vanya "..."
    $ portrait_vanya.morph(None, None, None, False)
    speech.main "{sc=5}Почему вы молчите?!{/sc}"
    $ portrait_polina.disappear()
    $ portrait_vanya.disappear()
    $ portrait_kseniya.disappear()
    hide screen finale_homeless_scene_3 with usual_transition
    $ tmp = "Что случилось с " + player_name + "? С ним перестали общаться.\nЗа прогулы он был отчислен, и так и не нашёл в себе силы восстановиться.\nОн перестал программировать и утратил все свои навыки.\nПоследний раз его видели на вокзале. Сейчас же местоположение неизвестно."
    show screen text_scene(tmp) with usual_transition
    ""
    hide screen text_scene with usual_transition
    $ ending_index = 3
    return















screen finale_beer_scene_1(how):
    add "bg_prologue.jpg" fit "fill" at how
    zorder -10

screen finale_beer_scene_2(how):
    add "bg_audience.jpg" fit "fill" at how
    zorder -10

define finale_beer_music_1 = "Siren.mp3"
define finale_beer_music_2 = "Lorn — ASH.mp3"
define finale_beer_ambient = "Lively Noise.mp3"
define finale_beer_sound_1 = "Short Applause.mp3"
define finale_beer_sound_2 = "Laughter.mp3"

label finale_beer_script:     
    stop ambient fadeout .5
    play ambient finale_beer_ambient loop fadein .5
    stop music fadeout .5
    play music finale_beer_music_1 fadein .5
    speech.thought "..."   
    show screen finale_beer_scene_1(None) with usual_transition
    ""
    show screen finale_beer_scene_1(blur_out)
    speech.thought "Я сидел на первом ряду в этом концертном зале и смотрел на пустую сцену."
    speech.thought "..."
    speech.main "Вся слава должна быть мне?{w} Или всё идет так, как и должно."
    speech.main "Я поступил неправильно, доверившись.{w} Или же наоборот, правильно?"
    speech.thought "..."
    play sound finale_beer_sound_1
    speech.thought "Я отдалённо слышал аплодисменты."
    speech.main "Мне выходить на сцену?"
    speech.thought "Я должен заполнить это пустое место?"
    speech.thought "..."
    speech.main "Почему вы не отвечаете на мои вопросы?"
    speech.thought "..."
    stop music fadeout .5
    play music finale_beer_music_2 fadein .5
    speech.main "{sc=5}Почему вы молчите?!{/sc}"
    hide screen finale_beer_scene_1 with usual_transition
    show screen finale_beer_scene_2(blur_out) with usual_transition
    $ portrait_egor.appear("undressed", "normal", .5, True)
    speech.egor "Друзья! Спасибо, что пришли.{w} Не хотел столь бурного внимания, но без этого никак.{w} Наше приложение начало работать только вчера, а сегодня мы получили уже тысячи игр и различных сюжетов."
    speech.egor "Впечатляет!{w} И я рад, что моя разработка оказалась настолько полезной.{w} Я стою перед вами, чтобы ответить на вопросы, так что смелей."
    $ portrait_egor.morph(None, None, None, False)
    Character("Слушатель", kind = speech.generic) "Как вам в голову пришла идея по созданию ИИ, который пишет игры?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Ну как пришла... Просто сидел и думал...{w} И так и пришла. Главное не как она пришла, а во что она выросла!"
    $ portrait_egor.morph(None, None, None, False)
    Character("Слушатель", kind = speech.generic) "Как вы продвигали свою идею?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "В УрФУ есть потрясающий центр — Точка Кипения.{w} Туда можно патентовать все свои стартапы и начальные идеи с первого курса.{w} И выигрывать деньги, конечно же."
    speech.egor "Только опережайте своих соперников.{w} Идей много, но важнее тот, кто первый их расскажет."
    $ portrait_egor.morph(None, None, None, False)
    speech.main "Разрешите?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Пожалуйста, ещё вопросы."
    $ portrait_egor.morph(None, None, None, False)
    speech.main "Разрешите, пожалуйста?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Так, ну, видимо, их нет, так что мы можем..."
    $ portrait_egor.morph(None, None, None, False)
    speech.main "Как вы будете развивать ваше приложение?{w} Какие обновления стоит ожидать?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Я не давал разрешения говорить." 
    $ portrait_egor.morph(None, None, None, False)
    speech.main "Как вы можете дать будущее тому, что не развивали сами?{w} Что сами не придумывали?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Простите, господа!{w} Сумасшедших тоже куча.{w} Охрана, выведите зрителя с первого ряда."
    $ portrait_egor.morph(None, None, None, False)
    play sound finale_beer_sound_2
    speech.main "{sc=10}Это моя идея!!!{/sc}{w} {sc=5}Она моя!{/sc}{w} Она...{w} моя, это ведь я... придумал."
    $ portrait_egor.disappear()
    speech.narrator "*[player_name] вывели из зала под смех зрителей*"
    hide screen finale_beer_scene_2 with usual_transition
    show screen text_scene("Он так и не смог смириться с тем, что у него украли то, что ему было так дорого...\nИдею. Его никто не слушал. Ему никто не верил.") with usual_transition
    ""
    hide screen text_scene with usual_transition
    stop ambient fadeout .5
    $ portrait_viktoriya.appear("undressed", "sad", .3, False)
    $ portrait_valeriya.appear("undressed", "sad", .7, False)
    speech.main "Он обманул меня, слышите?{w} Он, он..."
    $ portrait_viktoriya.morph(None, None, None, True)
    speech.viktoriya "Слушай, тебе надо отдохнуть...{w} Ты не спишь уже четыре дня."
    $ portrait_viktoriya.morph(None, None, None, False)
    speech.main "Он украл её!!!{w} Я должен быть на его месте, это моё, понимаете?{w} Вы слышите меня?"
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "[player_name]..."
    $ portrait_valeriya.morph(None, None, None, False)
    speech.main "{sc=5}Почему вы молчите?!{/sc}"
    $ portrait_valeriya.disappear()
    $ portrait_viktoriya.disappear()
    $ tmp = "Что случилось с " + player_name + "? С ним перестали общаться.\nЗа прогулы он был отчислен, и так и не нашёл в себе силы восстановиться.\nОн перестал программировать и утратил все свои навыки.\nПоследний раз его видели на вокзале. Сейчас же местоположение неизвестно."
    show screen text_scene(tmp) with usual_transition
    ""
    hide screen text_scene with usual_transition
    $ ending_index = 4
    return












screen finale_alternative_scene_1:
    add "bg_egor_trash.jpg" fit "fill"
    zorder -10    

screen finale_alternative_scene_2:
    add "bg_none_4.jpg" fit "fill"
    zorder -10    

screen finale_alternative_scene_3:
    add "bg_history_teacher.jpg" fit "fill"
    zorder -10    

screen finale_alternative_scene_4(how):
    add "bg_alley_empty.jpg" fit "fill" at how
    zorder -10    

screen finale_alternative_scene_5(how):
    add "bg_finale.jpg" fit "fill" at how
    zorder -10    

screen finale_alternative_scene_6(how):
    add "bg_prologue.jpg" fit "fill" at how
    zorder -10    

screen finale_alternative_scene_7:
    add "bg_audience.jpg" fit "fill"
    zorder -10   

define finale_alternative_music_1 = "Surasshu — Eek!.mp3"
define finale_alternative_ambient = "Lively Noise.mp3"
define finale_alternative_music_2 = "Lorn — MSDOS.mp3"
define finale_alternative_sound = "Long applause.mp3"

label finale_alternative_script:
    show screen finale_alternative_scene_1 with usual_transition
    stop music fadeout .5
    play music finale_alternative_music_1 fadein .5
    Character("Вместе", kind = speech.generic) "Егор?!"
    speech.egor "Чё вы уставились, придурки?"
    $ portrait_vanya.appear("undressed", "happy", .8, True)
    speech.vanya "Тебе там норм вообще?"
    $ portrait_vanya.morph(None, None, None, False)
    speech.egor "Идите нафиг, чё с первого раза непонятно?"
    $ portrait_viktoriya.appear("dressed", "surprised", .2, True)
    speech.viktoriya "А почему ты на мусорке?"
    $ portrait_viktoriya.morph(None, None, None, False)
    speech.egor "Студик потерял и ищу, ясно?"
    $ portrait_vanya.disappear()
    $ portrait_main.appear("dressed", "normal", .8, True)
    speech.main "Так тебя же отчислили ещё на втором курсе, какой студик?"
    $ portrait_main.morph(None, None, None, False)
    speech.egor "А я восстановился, ясно?{w} И что, что отчислили?{w} Конечно, такого гения как ты не отчисляют, да же?{w} Ну и чего ты добился?{w} Идёшь рассказывать всем про свой ИИ? Про приложение?"
    speech.narrator "*Все в шоке молчат*"
    speech.egor "Кому оно сдалось, придурок?{w} Только вам и сдалось.{w} Идиоты.{w} У вас ничего не получится, ясно?{w} Ни-че-го.{w} Идите к чёрту, хватит пялиться на меня." 
    $ portrait_viktoriya.disappear()
    $ portrait_valeriya.appear("dressed", "surprised", .2, True)
    speech.valeriya "Да мы же просто хотели спросить как дела..."
    $ portrait_valeriya.morph(None, None, None, False)
    speech.egor "{sc=7}Я сижу на мусорке, какие у меня могут быть дела?{/sc}"
    $ portrait_valeriya.disappear()
    $ portrait_main.disappear()
    hide screen finale_alternative_scene_1 with usual_transition
    show screen finale_alternative_scene_2 with usual_transition
    stop ambient fadeout .5
    speech.thought "Мы ушли.{w} Ну, Ваня кинул в него снежок.{w} Да...{w} А ведь я последний раз видел его в радике около уголка с кофе.{w} Вот к чему ведут прогулы."
    speech.thought "Так что там про команду?{w} Даа, тогда, когда я не пошел с Егором, четыре года назад, мы выиграли на истории.{w} После этого стали чаще общаться."
    speech.thought "Всё также ходили на пары, только теперь уже вместе с Ксю, Викой и Лерой."
    hide screen finale_alternative_scene_2 with usual_transition
    show screen finale_alternative_scene_3 with usual_transition
    speech.thought "Гончаров однажды сказал нам:{w} “Ребят, вы так много времени проводите вместе.{w} Знаете, я вчера хотел попить чай, взял пряники и смотрю: они все слиплись.{w} Так я о вас сразу же вспомнил”."
    speech.thought "Так вот, с тех пор мы подумали, что надо бы сделать команду.{w} И сделали.{w} Назвались “Рекурсивными пряниками”."
    hide screen finale_alternative_scene_3 with usual_transition
    show screen finale_alternative_scene_4(blur_out) with usual_transition
    $ portrait_viktoriya.appear("dressed", "happy", .2, False)
    $ portrait_main.appear("dressed", "normal", .4, False)
    $ portrait_kseniya.appear("dressed", "normal", .6, False)
    $ portrait_valeriya.appear("dressed", "normal", .8, False)
    speech.thought "А ещё помните, четыре года назад я сказал Ксю, Вике и Лере, что..."
    $ portrait_main.morph(None, "happy", None, True)
    speech.main "Слушайте...{w} Да была у меня одна такая мысля..."
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    hide screen finale_alternative_scene_4 with usual_transition
    show screen finale_alternative_scene_5(None) with usual_transition
    play ambient finale_alternative_ambient loop fadein .5
    stop music fadeout .5
    play music finale_alternative_music_2 fadein .5
    speech.thought "Все эти люди уже знают о ней.{w} Сейчас узнаете и вы."
    hide screen finale_alternative_scene_5 with usual_transition
    show screen finale_alternative_scene_6(blur_out) with usual_transition
    $ portrait_valeriya.appear("undressed", "normal", .2, True)
    $ portrait_viktoriya.appear("undressed", "normal", .4, False)
    $ portrait_kseniya.appear("undressed", "normal", .6, False)
    $ portrait_vanya.appear("undressed", "normal", .8, False)
    speech.valeriya "Все готовы?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "happy", None, True)
    $ portrait_kseniya.morph(None, "happy", None, True)
    Character("Вместе", kind = speech.generic) "Да!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_vanya.morph(None, "happy", None, True)
    speech.narrator "*Ваня чавкает*"
    speech.vanya "Я тоже готов ваще-то."
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "Так ты не выступаешь..."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_vanya.morph(None, "sad", None, True)
    speech.vanya "А вот это обидно щас было.{w} Я так-то ваша лучшая группа поддержки, поняли, да?"
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, True)
    speech.valeriya "Мы поняли."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_vanya.morph(None, "happy", None, True)
    speech.vanya "Если сейчас плохо выступите, то я зафигачу в вас помидорами." 
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "happy", None, True)
    speech.kseniya "Твой выход, Карл Уизер!" 
    $ portrait_valeriya.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_vanya.disappear()
    hide screen finale_alternative_scene_6 with usual_transition
    show screen finale_alternative_scene_7 with usual_transition
    play sound finale_alternative_sound
    speech.main "Всем здравствуйте!"
    speech.main "Я рад...{w} Мы рады приветствовать вас на вечере, который посвящён нашему стартапу..."
    hide screen finale_alternative_scene_7 with usual_transition
    show screen finale_alternative_scene_6(blur_out) with usual_transition
    speech.main "Я с удовольствием представлю нашу команду..."
    $ portrait_viktoriya.appear("undressed", "normal", .5, True)
    speech.main "Дизайнер — Виктория."
    $ portrait_viktoriya.morph(None, None, .3, False)
    $ portrait_valeriya.appear("undressed", "normal", .7, True)
    speech.main "Гейм-дизайнер — Валерия."
    $ portrait_valeriya.morph(None, None, .8, False)
    $ portrait_viktoriya.morph(None, None, .2, None)
    $ portrait_kseniya.appear("undressed", "happy", .5, True)
    speech.main "Аналитик — Ксения."
    $ portrait_valeriya.morph(None, None, .8, None)
    $ portrait_viktoriya.morph(None, None, .2, None)
    $ portrait_kseniya.morph(None, None, .6, False)
    $ portrait_polina.appear("undressed", "normal", .4, True)
    speech.main "Тимлид — Полина."
    $ portrait_polina.morph(None, None, None, False)
    speech.main "И я, [player_name], разработчик.{w} А теперь мы готовы выслушать ваши вопросы, друзья."
    Character("Слушатель", kind = speech.generic) "В чём идея проекта?"
    $ portrait_viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Ну этот интриган вас совсем замучал, да ведь?{w} В чём была идея?{w} Сделать приложение, которое позволит вам создавать определённые эпизоды из истории."
    speech.viktoriya "Например, Конференцию либералов, социалов и консерваторов, про которую вы уже знаете."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, True)
    speech.valeriya "Но потом мы подумали: почему только из истории?{w} И у нас появилась другая идея: приложение, которое создает любые сюжеты, какие вы захотите."
    speech.valeriya "Воспоминания из вашей жизни? Пожалуйста!{w} Момент из истории? Вуаля!{w}"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, True)
    speech.kseniya "Было проанализировано, что данная идея вызовет спрос у аудитории, так как все любят создавать что-либо на память: альбомы, например."
    $ portrait_kseniya.morph(None, None, None, False)
    speech.main "А потом мы подумали: ну разве это будет просто обычный конструктор?{w} Обычный игровой движок?{w} Для этого уже есть Unity или Ren'Py...{w} Нет, у нас другая цель."
    speech.main "Мы хотим по одной вашей фразе создавать то, что вы пожелаете, поэтому..."
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "Перед вами не приложение по созданию сюжетов, а ИИ.{w} ИИ, который по одной вашей фразе напишет игру про ваше детство?{w} Жизнь в общаге?{w} Вам решать." 
    $ portrait_valeriya.morph(None, None, None, False)
    speech.main "Думаю вы нас поняли.{w} Следующий вопрос... Вот вы."
    Character("Слушатель", kind = speech.generic) "Откуда взялась Полина?"
    speech.main "Ах да, Полина.{w} Да я думаю она сама вам ответит." 
    $ portrait_polina.morph(None, "happy", None, True)
    speech.polina "Всем привет, ребята.{w} Помните, они были в шоке, когда в расписании появился другой препод по истории?{w} Ну..."
    $ portrait_polina.morph(None, "normal", None, False)
    $ portrait_kseniya.morph(None, "surprised", None, True)
    $ portrait_valeriya.morph(None, "surprised", None, True)
    $ portrait_viktoriya.morph(None, "surprised", None, True)
    Character("Вместе", kind = speech.generic) "{sc=3}Это была ты?{/sc}"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_polina.morph(None, "happy", None, True)
    speech.polina "Сюрпри-и-из!{w} Было сложно объяснить администрации, почему они должны были поменять расписание двум студентам.{w} После того как наш гений пролил на меня кофе и назвал меня истеричкой..."
    speech.polina "... я подумала, что именно такой человек нужен нашей команде.{w} В итоге, я собрала их в одной группе по истории как раз на момент командной работы.{w} Ну и они сработались." 
    $ portrait_polina.morph(None, "normal", None, None)
    speech.polina "Кстати говоря, они встретили меня намного позже, так что до этого момента не знали, что это я на самом деле их всех собрала." 
    $ portrait_polina.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_kseniya.disappear()
    hide screen finale_alternative_scene_6 with usual_transition
    show screen finale_alternative_scene_5(blur_out) with usual_transition
    $ portrait_vanya.appear("undressed", "happy", .5, True)
    speech.narrator "*Кричит из зала*"
    speech.vanya "А я говорил, она волшебник!"
    $ portrait_vanya.disappear()
    hide screen finale_alternative_scene_5 with usual_transition
    show screen finale_alternative_scene_6(blur_out) with usual_transition
    $ portrait_polina.appear("undressed", "normal", .4, False)
    $ portrait_kseniya.appear("undressed", "normal", .6, False)
    $ portrait_valeriya.appear("undressed", "normal", .8, False)
    $ portrait_viktoriya.appear("undressed", "normal", .2, False)
    Character("Слушатель", kind = speech.generic) "Какое место в вашей команде занимает Ваня?" 
    $ portrait_valeriya.morph(None, "happy", None, True)
    speech.valeriya "Ваня — легенда, его все любят."
    $ portrait_polina.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_kseniya.disappear()
    hide screen finale_alternative_scene_6 with usual_transition
    show screen finale_alternative_scene_5(blur_out) with usual_transition
    $ portrait_vanya.appear("undressed", "happy", .5, True)
    speech.narrator "*Кричит из зала*"
    speech.vanya "Я тоже вас люблю, чуваки!"
    $ portrait_vanya.disappear()
    hide screen finale_alternative_scene_5 with usual_transition
    show screen finale_alternative_scene_6(blur_out) with usual_transition
    $ portrait_polina.appear("undressed", "normal", .4, False)
    $ portrait_kseniya.appear("undressed", "normal", .6, False)
    $ portrait_valeriya.appear("undressed", "normal", .8, False)
    $ portrait_viktoriya.appear("undressed", "normal", .2, False)
    speech.main "На самом деле, он морально помогал нам на всём творческом пути, поэтому тоже является частью нашей команды.{w} Он самый главный пряник."
    speech.narrator "*Ваня кричит из зала*"
    speech.vanya "Юху-у, лучшие!"
    speech.main "Ну что, вроде мы всё рассказали.{w} У вас остались вопросы?" 
    $ portrait_polina.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_kseniya.disappear()
    hide screen finale_alternative_scene_6 with usual_transition
    show screen text_scene("Если остались, предлагаем задать их уже не героям, а настоящим\nучастникам команды “Рекурсивные пряники”. Мы будем рады поотвечать вам :D\nНаши контакты есть на странице нашего репозитория.") with usual_transition
    ""
    hide screen text_scene with usual_transition
    $ ending_index = 5
    return
















screen before_vengeance_scene_1(how):
    add "bg_kitchen_room.jpg" fit "fill" at how
    zorder -10

define before_vengeance_music = "Toby Fox — Shop.mp3"

label before_vengeance_script:
    show screen before_vengeance_scene_1(None) with usual_transition
    stop ambient fadeout .5
    stop music fadeout .5
    play music before_vengeance_music fadein .5
    speech.thought "Я рассказал им всю историю про бар и про то, как моя идея стала не моей."
    show screen before_vengeance_scene_1(blur_out)
    $ portrait_kseniya.appear("undressed", "normal", .6, False)
    $ portrait_valeriya.appear("undressed", "normal", .2, False)
    $ portrait_viktoriya.appear("undressed", "normal", .8, False)
    $ portrait_main.appear("undressed", "sad", .4, True)
    speech.main "... ну и вот, такие дела."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "Ты шутишь!"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "К сожалению, нет."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "В это пипец как сложно поверить..."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Да, я понимаю, он внушает доверие."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "surprised", None, True)
    speech.valeriya "Так с ним и Вика ходила гулять..."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Ты... чего?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "surprised", None, True)
    speech.viktoriya "Да я ж прошептала Лере на истории.{w} Мы с ним гуляли, всё нормально было, он выведывал всё, расспрашивал.{w} Потом прихожу домой, а он мне:"
    speech.viktoriya "“Нам надо перестать общаться”. Я и выпала."
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, "sad", None, True)
    speech.kseniya "Потому что, друзья мои, нужно молча учиться. Тогда и проблем не будет."
    $ portrait_kseniya.morph(None, None, None, False)
    speech.thought "Никто не понял, что это должно значить, мы просто в недоумении молчали."
    $ portrait_kseniya.morph(None, "happy", None, True)
    speech.kseniya "Да шучу я.{w} Или как вы там говорите?...{w} Прикалываюсь.{w} Делать то что будем?"
    $ portrait_kseniya.morph(None, None, None, False)

    $ portrait_main.morph(None, None, .32, None)
    $ portrait_kseniya.morph(None, None, .68, None)
    $ portrait_valeriya.morph(None, None, .16, None)
    $ portrait_viktoriya.morph(None, None, .84, None)
    $ portrait_vanya.appear("undressed", "happy", .5, True)
    speech.vanya "А давайте мы его {glitch=100}${/glitch}{glitch=150}#{/glitch}{glitch=125}&{/glitch}{glitch=75}@{/glitch}!"
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    $ portrait_kseniya.morph(None, "surprised", None, True)
    $ portrait_valeriya.morph(None, "sad", None, True)
    $ portrait_viktoriya.morph(None, "sad", None, True)
    Character("Вместе", kind = speech.generic) "{sc=3}Ваня, нет!{/sc}"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, False) 
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_vanya.morph(None, "sad", None, True)
    speech.vanya "Да лан, чувачки, я понял, кулаки мы не распускаем.{w} Но поплатиться он должен — это сто пудов."
    $ portrait_vanya.morph(None, "normal", None, False)
    menu:
        "Нужно принять решение."
        "Понять и простить":
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "Я принял решение.{w} Пусть оставляет идею себе."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_kseniya.morph(None, "sad", None, None) 
            $ portrait_valeriya.morph(None, "sad", None, None)
            $ portrait_viktoriya.morph(None, "sad", None, None)
            $ portrait_vanya.morph(None, "sad", None, True)
            speech.vanya "Братанчик ты чего?! Он же твою..."
            $ portrait_vanya.morph(None, None, None, False)
            $ portrait_main.morph(None, "sad", None, True)
            speech.main "Я знаю, Ваня.{w} Просто...{w} Я не думаю, что в силах бороться с этим..."
            $ double_ending = True
        "Восстать и крушить":
            $ portrait_main.morph(None, "normal", None, True)
            speech.main "Я принял решение.{w} Мы унизим его.{w} Прямо на презентации.{w} Правда, я понятия не имею, когда она будет."
            $ portrait_main.morph(None, None, None, False)
            $ portrait_valeriya.morph(None, "happy", None, True)
            speech.valeriya "А я даже знаю, кто нам с этим поможет..."
            $ portrait_valeriya.morph(None, "normal", None, False)
            $ portrait_viktoriya.morph(None, "surprised", None, True)
            speech.viktoriya "Кто?.."
            $ portrait_viktoriya.morph(None, None, None, False)
            $ portrait_valeriya.morph(None, "happy", None, True)
            speech.narrator "*Лера ехидно улыбается*"
    $ portrait_vanya.disappear()
    $ portrait_main.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_kseniya.disappear()
    hide screen before_vengeance_scene_1 with usual_transition
    return














screen preparations_scene_1(how):
    add "bg_coworking.jpg" fit "fill" at how
    zorder -10

screen preparations_scene_2(how):
    add "bg_coworking_dark.jpg" fit "fill" at how
    zorder -10

define preparations_music_1 = "Toby Fox — Danger Mystery.mp3"
define preparations_music_2 = "Toby Fox — It's Showtime!.mp3"

label preparations_script:
    stop music fadeout .5
    play music preparations_music_1 fadein .5
    show screen preparations_scene_1(blur_out) with usual_transition
    $ portrait_kseniya.appear("undressed", "normal", .6, True)
    $ portrait_valeriya.appear("undressed", "normal", .2, False)
    $ portrait_viktoriya.appear("undressed", "normal", .8, False)
    $ portrait_main.appear("undressed", "normal", .4, False)
    speech.kseniya "Подскажите, пожалуйста, зачем мы сюда пришли?"
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, True)
    speech.valeriya "Ох-ох, а вы не знаете?"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, True)
    speech.main "Ну, это коворкинг.{w} Дальше то что?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "И здесь нет света.{w} Лера, что за тайны?"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "sad", None, True)
    speech.valeriya "Тише...{w} Вы спугнёте..."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, "surprised", None, True)
    speech.viktoriya "Да кого?" 
    $ portrait_kseniya.disappear()
    $ portrait_valeriya.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    hide screen preparations_scene_1 with usual_transition
    show screen preparations_scene_2(None) with usual_transition
    Character("???", kind = speech.polina_hidden) "Кто вы?"
    speech.narrator "*Все стоят в шоке*"
    Character("???", kind = speech.polina_hidden) "Я ещё раз повторяю...{w} {sc=3}Кто вы?{/sc}"
    $ portrait_viktoriya.appear("undressed", "surprised", .3, True)
    speech.viktoriya "Э-э-э...{w} м...{w} мы..."
    $ portrait_viktoriya.morph(None, None, None, False)
    Character("???", kind = speech.polina_hidden) "Зря...{w} очень зря."
    $ portrait_viktoriya.morph(None, None, .2, None)
    $ portrait_main.appear("undressed", "surprised", .5, True)
    speech.main "Нас привела..."
    $ portrait_main.morph(None, None, None, False)
    Character("???", kind = speech.polina_hidden) "Разрешения говорить не было."
    $ portrait_viktoriya.morph(None, "sad", None, False)
    speech.viktoriya "Но..."
    $ portrait_viktoriya.morph(None, None, None, False)
    Character("???", kind = speech.polina_hidden) "{sc=3}Не было!{/sc}"
    $ portrait_main.morph(None, None, .4, False)
    $ portrait_valeriya.appear("undressed", "happy", .6, True)
    speech.valeriya "Ха-ха-ха, ладно, хватит."
    stop music fadeout .5
    $ portrait_valeriya.morph(None, None, None, False)
    speech.narrator "*Все стоят в шоке*"
    Character("???", kind = speech.polina_hidden) "Это было достаточно страшно?"
    $ portrait_valeriya.morph(None, None, None, True)
    speech.valeriya "Это было великолепно, посмотри на их лица!"
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_kseniya.appear("undressed", "surprised", .8, True)
    $ portrait_viktoriya.morph(None, None, None, True)
    $ portrait_main.morph(None, None, None, True)
    Character("Вместе", kind = speech.generic) "{sc=3}Это кто?{/sc}"
    show screen preparations_scene_2(blur_out)
    $ portrait_valeriya.morph(None, None, .68, None)
    $ portrait_kseniya.morph(None, None, .84, False)
    $ portrait_viktoriya.morph(None, None, .16, False)
    $ portrait_main.morph(None, None, .32, False)
    $ portrait_polina.appear("undressed", "happy", .5, True)
    play music preparations_music_2 fadein .5
    speech.polina "Это Полина.{w} Боже мой, что с вами, ха-ха-ха.{w} Неужели я так страшно говорю."
    $ portrait_polina.morph(None, None, None, False)
    $ portrait_viktoriya.morph(None, None, None, True)
    $ portrait_kseniya.morph(None, None, None, True)
    $ portrait_main.morph(None, None, None, True)
    Character("Вместе", kind = speech.generic) "{sc=3}Да!{/sc}"
    $ portrait_viktoriya.morph(None, None, None, False)
    $ portrait_kseniya.morph(None, None, None, False)
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "normal", None, True)
    speech.valeriya "Итак, это — ужасная Эриния, богиня Мегера, страшная Фурия, жажда правосудия, кровная месть.{w} Или по-другому — Полина."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_polina.morph(None, "normal", None, True)
    speech.polina "О-о, а кое-кто из вашей банды-команды мне уже знаком."
    $ portrait_polina.morph(None, None, None, False)
    $ portrait_main.morph(None, "sad", None, True)
    speech.main "..."
    $ portrait_main.morph(None, None, None, False)
    $ portrait_polina.morph(None, "happy", None, True)
    speech.polina "Моя кофта не отстирывается, держу в курсе, неуклюжка!"
    $ portrait_polina.morph(None, None, None, False)
    $ portrait_main.morph(None, "surprised", None, True)
    speech.main "Кто? Я-то неуклюжка?"
    $ portrait_main.morph(None, None, None, False)
    $ portrait_valeriya.morph(None, "happy", None, True)
    speech.valeriya "О-о, так вы ещё и знакомы.{w} Ну тем и лучше."
    $ portrait_valeriya.morph(None, None, None, False)
    $ portrait_polina.morph(None, "normal", None, True)
    speech.polina "А что собственно от меня нужно?"
    $ portrait_valeriya.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_polina.disappear()
    speech.thought "Мы рассказали Полине всю историю про бар, украденную идею, Егора...{w} Я сказал Егора?{w} Я имел в виду просто чокнутого при..."
    $ portrait_valeriya.appear("undressed", "normal", .68, True)
    $ portrait_kseniya.appear("undressed", "normal", .84, False)
    $ portrait_viktoriya.appear("undressed", "normal", .16, False)
    $ portrait_main.appear("undressed", "normal", .32, False)
    $ portrait_polina.appear("undressed", "normal", .5, False)
    speech.polina "... дурка...{w} Да, ему определённо надо в психушку.{w} Или в обезьянник.{w} Короче говоря, мы хотим мести."
    $ portrait_valeriya.morph(None, None, None, False)
    speech.narrator "*Полина крепко задумалась*"
    $ portrait_viktoriya.morph(None, "sad", None, True)
    speech.viktoriya "Но пока что идей нет."
    $ portrait_viktoriya.morph(None, None, None, False)
    speech.narrator "*Ваня кричит из другого конца коворкинга*"
    speech.vanya "{sc=3}Чуваки!!!{/sc}"
    $ portrait_polina.morph(None, "surprised", None, True)
    speech.polina "Это ещё кто?"
    $ portrait_valeriya.disappear()
    $ portrait_kseniya.disappear()
    $ portrait_viktoriya.disappear()
    $ portrait_main.disappear()
    $ portrait_polina.disappear()
    $ portrait_vanya.appear("undressed", "happy", .5, True)
    speech.vanya "Я надыбал, что у этого дебила завтра презентация этого...{w} Как его...{w} Ну, короче, стартапа.{w} В актовом ГУКа, билеты продают на {a=https://vk.com/@-185194559-baza}паркете{/a}."
    $ portrait_vanya.morph(None, None, .3, False)
    $ portrait_valeriya.appear("undressed", "happy", .7, True)
    speech.valeriya "А это — лучший человек на свете."
    $ portrait_valeriya.disappear()
    $ portrait_vanya.disappear()
    hide screen preparations_scene_2 with usual_transition
    return











screen finale_revenge_scene_1(how):
    add "bg_prologue.jpg" fit "fill" at how
    zorder -10

screen finale_revenge_scene_2(how):
    add "bg_finale.jpg" fit "fill" at how
    zorder -10

screen finale_revenge_scene_3(how):
    add "bg_audience.jpg" fit "fill"
    zorder -10

screen finale_revenge_scene_4:
    add "bg_egor_trash.jpg" fit "fill"
    zorder -10

screen finale_revenge_scene_5:
    add "bg_egor_squat.jpg" fit "fill"
    zorder -10

screen finale_revenge_scene_6:
    add "bg_apartment_wallet.jpg" fit "fill"
    zorder -10

define finale_revenge_music_1 = "Siren.mp3"
define finale_revenge_music_2 = "Lorn — MSDOS.mp3"
define finale_revenge_ambient = "Lively Noise.mp3"
define finale_revenge_sound_1 = "Short Applause.mp3"
define finale_revenge_sound_2 = "Laughter.mp3"

label finale_revenge_script:
    stop ambient fadeout .5
    play ambient finale_revenge_ambient loop fadein .5
    stop music fadeout .5
    play music finale_revenge_music_1 fadein .5
    speech.thought "..."
    show screen finale_revenge_scene_1(None) with usual_transition
    ""
    show screen finale_revenge_scene_1(blur_out)
    speech.thought "Я сидел на первом ряду в этом концертном зале и смотрел на пустую сцену."
    speech.thought "..."
    speech.main "Вся слава должна быть мне?{w} Или всё идет так, как и должно."
    speech.main "Я поступил неправильно, доверившись.{w} Или же наоборот, правильно?"
    speech.thought "..."
    play sound finale_revenge_sound_1
    speech.thought "Я отдалённо слышал аплодисменты."
    speech.main "Мне выходить на сцену?"
    speech.thought "Я должен заполнить это пустое место?"
    speech.thought "..."
    speech.main "Почему вы не отвечаете на мои вопросы?"
    speech.thought "..."
    speech.main "{sc=5}Почему вы молчите?!{/sc}"
    hide screen finale_revenge_scene_1 with usual_transition
    show screen finale_revenge_scene_2(None) with usual_transition
    stop music fadeout .5
    speech.main "Разве месть вообще что-то решает?" 
    speech.polina "Решает.{w} Вы готовы?{w} Ваня, только пожалуйста..."
    speech.vanya "Да помню я про план “Б”, не парься."
    play music finale_revenge_music_2 fadein .5
    hide screen finale_revenge_scene_2 with usual_transition
    show screen finale_revenge_scene_3(blur_out) with usual_transition
    $ portrait_egor.appear("undressed", "normal", .5, True)
    speech.egor "Друзья!{w} Спасибо, что пришли.{w} Не хотел столь бурного внимания, но без этого никак.{w} Понимаю, понимаю. Идея уникальна, невероятна, до меня ещё никто такого не придумывал, да..."
    speech.egor "Правда, не хочу всей этой славы и всего этого шума, ну ладно.{w} Сегодня вы можете спросить меня обо всем, о чём захотите.{w} На экране будут показаны первые эскизы приложения..."
    speech.egor "Прошу внимание на первый слайд."
    $ portrait_egor.disappear()
    hide screen finale_revenge_scene_3 with usual_transition
    show screen finale_revenge_scene_4 with usual_transition
    speech.egor "Э-э, так...{w} это что..."
    play sound finale_revenge_sound_2
    speech.egor "Простите, друзья, какие-то неполадки.{w} Давайте переключим на следующий слайд."
    hide screen finale_revenge_scene_4 with usual_transition
    show screen finale_revenge_scene_5(None) with usual_transition
    play sound finale_revenge_sound_2 if_changed
    speech.polina "Так вот где вы проводите свое свободное время!"
    show screen finale_revenge_scene_5(blur_out)
    $ portrait_polina.appear("undressed", "happy", .5, True)
    speech.polina "Идею приложения тоже там придумывали?"
    $ portrait_polina.morph(None, None, .3, False)
    $ portrait_egor.appear("undressed", "normal", .7, True)
    play sound finale_revenge_sound_2 if_changed
    speech.egor "Да, очень остроумно, спасибо за вопрос...{w} Нет, идея проекта пришла мне..."
    $ portrait_egor.morph(None, None, .8, False)
    $ portrait_polina.morph(None, None, .2, None)
    $ portrait_vanya.appear("undressed", "happy", .5, True)
    speech.vanya "Ну чего задумались?{w} Отвечай бырее!"
    $ portrait_vanya.morph(None, None, None, False)
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Эм...{w} Пришла мне..."
    $ portrait_egor.disappear()
    $ portrait_vanya.disappear()
    $ portrait_polina.disappear()
    hide screen finale_revenge_scene_5 with usual_transition
    show screen finale_revenge_scene_2(blur_out) with usual_transition
    $ portrait_viktoriya.appear("undressed", "surprised", .5, True)
    speech.viktoriya "{sc=3}Тихо все!{/sc}"
    $ portrait_viktoriya.morph(None, None, None, False)
    stop sound fadeout .5
    stop ambient fadeout .5
    $ portrait_viktoriya.morph(None, "surprised", None, True)
    speech.viktoriya "Зачем вы издеваетесь над человеком?"
    $ portrait_viktoriya.morph(None, None, None, False)
    speech.narrator "*Весь зал затих*"
    $ portrait_viktoriya.morph(None, "happy", None, True)
    play sound finale_revenge_sound_2
    play ambient finale_revenge_ambient loop fadein .5
    speech.viktoriya "Ему и так тяжело придумывать на ходу, а тут вы ещё сбиваете."
    $ portrait_viktoriya.disappear()
    hide screen finale_revenge_scene_2 with usual_transition
    show screen finale_revenge_scene_3(blur_out) with usual_transition
    $ portrait_egor.appear("undressed", "normal", .5, True)
    speech.egor "{sc=7}Заткнитесь!{/sc}{w} {sc=3}Ничего я не придумываю.{/sc}{w} Если кто-то здесь сомневается в оригинальности моей идеи, то прошу на выход." 
    $ portrait_egor.morph(None, None, None, False)
    speech.main "Разрешите вопрос?"
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Конечно...{w} Зада...{w} Эм..."
    $ portrait_egor.morph(None, None, None, False)
    speech.thought "Он заметно сбился, когда увидел меня."
    speech.main "Я ваш большой фанат..."
    $ portrait_egor.morph(None, None, None, True)
    speech.egor "Да что вы?"
    $ portrait_egor.morph(None, None, None, False)
    speech.main "Я хотел вас поблагодарить.{w} Друзья, перестаньте над ним смеяться.{w} Этот человек не только придумал такое полезное приложение, но и помог мне..."
    speech.thought "Он улыбался. Я не знаю, почему.{w} Но я продолжал свою речь."
    speech.main "Дело в том, что я пошёл в бар и там... Меня напоили.{w} Тогда я ничего не помнил, у меня украли кошелек и телефон."
    stop ambient fadeout .5
    speech.narrator "*Зал удивлённо притих.*"
    speech.main "Мне было так плохо...{w} Но, вы не поверите.{w} Егор нашёл мои украденные вещи!"
    speech.main "Да, представляете?{w} Он бережно положил их на пуфик у себя в прихожей, внимание на экран."
    $ portrait_egor.disappear()
    hide screen finale_revenge_scene_2 with usual_transition
    show screen finale_revenge_scene_6 with usual_transition
    speech.main "Наверное, хотел отдать мне.{w} Только вот когда? Как думаете?"
    hide screen finale_revenge_scene_6 with usual_transition
    show screen finale_revenge_scene_3(None) with usual_transition
    play sound finale_revenge_sound_2
    speech.narrator "*Егор с позором убегает со сцены*"
    speech.main "Думаю, вы уже поняли, кто залил в меня весь алкоголь.{w} И украл вещи. И присвоил идею.{w} Ну а раз вы тут собрались, чтобы послушать про приложение..."
    speech.main "... то можете задавать свои вопросы.{w} Я-то на них уж точно отвечу."
    hide screen finale_revenge_scene_3 with usual_transition
    show screen text_scene("Егор бежал из зала. Его видели вылетающим из главного\nкорпуса УрФУ, а дальше... От него и след простыл. На парах\nон больше не появлялся, из всех бесед удалился.") with usual_transition 
    ""
    hide screen text_scene with usual_transition
    show screen text_scene("Месть получилась настолько сладкой, что банда-команда\nнаших героев назвалась “Пряниками”, но не простыми, а рекурсивными.") with usual_transition 
    ""
    hide screen text_scene with usual_transition
    show screen text_scene("Их проект завирусился и понравился людям.\nА выступление в актовом зале породило множество мемов.") with usual_transition 
    ""
    hide screen text_scene with usual_transition
    $ ending_index = 6
    return