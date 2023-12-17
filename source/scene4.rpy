label scene4_script:
    if branch_choice_a_b == 1:
        call kitchen_room_script
        call coworking_reveal_script
        call finale_grande_script
    else:
        show screen text_scene(stub)
        ""
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
    speech.thought "Теперь я хожу на все мероприятия, которые проводит вуз. Теперь мы банда-команда."
    show screen kitchen_room_scene_1(blur_out)
    $ portrait.viktoriya.appear("undressed", "happy", .3, False)
    $ portrait.vanya.appear("undressed", "normal", .7, False)
    speech.thought "Я не могу представить свой день без Леры и ее термоса с чаем, без Вики, которая стабильно опаздывает на 5 минут и рассказывает анекдоты."
    $ portrait.viktoriya.morph(None, "normal", None, None)
    $ portrait.vanya.morph(None, "happy", None, None)
    speech.thought "Без культурных бесед с Ксюшей. И без ее странных сообщений. Она продолжала анонимно писать мне после каждого мероприятия."
    $ portrait.viktoriya.morph(None, "happy", None, None)
    $ portrait.vanya.morph(None, "normal", None, None)
    speech.thought "“Ты молодец, успех сегодня был на твоей стороне”, “Сегодня Рекурсивные Пряники блистали”..."
    speech.thought "Я молчал, но знаете, мне это надое..."
    $ portrait.viktoriya.morph(None, None, .5, None)
    $ portrait.vanya.morph(None, None, .8, None)
    $ portrait.valeriya.appear("dressed", "happy", .2, True)
    speech.valeriya "Доставку заказывали?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.vanya.morph(None, None, None, True)
    speech.vanya "Опа, хоби-дохоби приехали. Коничева, курьерка."
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "normal", None, True)
    speech.valeriya "Сайонара, Ивантус, суши возьми, пожалуйста."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.vanya.disappear()
    $ portrait.viktoriya.disappear()
    $ portrait.valeriya.disappear()
    hide screen kitchen_room_scene_1 with usual_transition

    show screen kitchen_room_scene_2(blur_out) with usual_transition
    $ portrait.vanya.appear("undressed", "normal", .3, True)
    $ portrait.valeriya.appear("undressed", "normal", .7, False)
    speech.vanya "Чай, вино, медленные танцы?"
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "happy", None, True)
    speech.valeriya "Благопочтенный господин, желаю чаю, пожалуйста."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.vanya.morph(None, "happy", None, True)
    speech.vanya "Базару ноль, муадмуазель. Ван секонд сильвупле. А где Ксюша?"
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "normal", None, True)
    speech.valeriya "Чуть задерживается, только не съешь все онигири."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.vanya.morph(None, "normal", None, True)
    speech.vanya "Окей. Чувак, ёмаё, оторвись от мобилы. Чё за дела, хавать пойдём."
    $ portrait.vanya.morph(None, None, .2, False)
    $ portrait.valeriya.morph(None, None, .8, None)
    $ portrait.main.appear("undressed", "normal", .5, True)
    speech.main "Я тут, простите. Мы же идём сегодня в коворкинг? Ты звонила Ксюше?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Коворкинг? Зачем?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Она написала, что встреча в 16 в радике."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.vanya.morph(None, "happy", None, True)
    speech.narrator "*Ваня чавкает*"
    speech.vanya "Чуваки, вы видите друг друга чаще, чем я свою маму, клянусь. Хоть один день посидите в комнате."
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "sad", None, True)
    speech.valeriya "Она мне ничего не писала..."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "sad", None, True)
    speech.main "Да зачем ты смотришь в ВК? В СМС зайди."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "normal", None, True)
    speech.valeriya "В СМС? У меня даже нет её номера."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "normal", None, True)
    speech.main "Очень смешно, дай телефон."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.vanya.disappear()
    $ portrait.viktoriya.disappear()
    $ portrait.valeriya.disappear()
    $ portrait.main.disappear()
    show screen kitchen_room_scene_2(blur_in)
    speech.thought "Но у неё правда не было её номера. Последнее сообщение непонятно от кого. Смайл кота и сердечка."
    show screen kitchen_room_scene_2(blur_out)
    stop music fadeout .5
    play music kitchen_room_music_2 fadein .5
    $ portrait.main.appear("undressed", "normal", .3, False)
    $ portrait.valeriya.appear("undressed", "normal", .7, True)
    speech.valeriya "О чем речь? Кто тебе написал?"
    $ portrait.valeriya.morph(None, None, None, False)
    speech.thought "Я показал ей историю сообщений."
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Подожди..."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "surprised", None, True)
    speech.main "Я просто не понимаю, почему бы не писать в ВК, что за скрытность?"
    $ portrait.main.morph(None, None, None, False)
    play sound kitchen_room_sound
    Character("8-946-xxx-xx-42", kind = speech.polina_hidden) "Лера, коворкинг, 16:00. Важный разговор."
    $ portrait.main.morph(None, "sad", None, True)
    speech.main "..."
    speech.main "Это другой номер..."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "sad", None, True)
    speech.valeriya "Писал не ты?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "surprised", None, True)
    speech.main "При чём тут вообще я?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "normal", None, True)
    speech.valeriya "В смысле при чём? А кто позвал нас на первое меро по искусственному интеллекту, ещё в сентябре?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Я что ли?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "sad", None, True)
    speech.valeriya "Слушай, чувак, ты меня пугаешь..."
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "sad", None, True)
    speech.main "Нет, это ты меня пугаешь."
    $ portrait.main.morph(None, None, None, False)
    speech.narrator "*Ваня удивлённо чавкает*"
    $ portrait.main.morph(None, "surprised", None, True)
    $ portrait.valeriya.morph(None, "surprised", None, True)
    Character("Вместе", kind = speech.generic) "Это Ксюша?!"
    $ portrait.main.morph(None, None, .2, False)
    $ portrait.valeriya.morph(None, None, .8, False)
    $ portrait.vanya.appear("undressed", "normal", .5, True)
    speech.narrator "*Ваня чавкает*"
    speech.vanya "Обалдеть просто..."
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.main.morph(None, "surprised", None, True)
    $ portrait.valeriya.morph(None, "surprised", None, True)
    Character("Вместе", kind = speech.generic) "Это Ксюша!!!"
    $ portrait.main.morph(None, None, .2, False)
    $ portrait.valeriya.morph(None, None, .8, False)
    $ portrait.vanya.morph(None, "happy", None, True)
    speech.narrator "*Ваня чавкает*"
    speech.vanya "Опупеть просто..."
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, "sad", None, True)
    speech.valeriya "В радике в 16?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "sad", None, True)
    speech.main "Ну, походу."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.vanya.morph(None, None, None, True)
    speech.vanya "Если вы сейчас ливнёте, то я всё сожру, отвечаю!"
    $ portrait.main.disappear()
    $ portrait.valeriya.disappear()
    $ portrait.vanya.morph(None, "normal", None, None)
    speech.vanya "Э-э-й! Чуваки!"
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.vanya.morph(None, "sad", None, True)
    speech.vanya "Офигеть блин. Хоть еду оставили."
    $ portrait.vanya.morph(None, None, None, False)
    $ portrait.vanya.disappear()
    hide screen kitchen_room_scene_2 with usual_transition
    return














screen coworking_reveal_scene_1(how):
    add "bg_coworking.jpg" fit "fill" at how
    zorder -10

define coworking_reveal_ambient = "Quiet Noise.mp3"

label coworking_reveal_script:
    show screen coworking_reveal_scene_1(blur_out) with usual_transition
    play ambient coworking_reveal_ambient fadein .5
    $ portrait.main.appear("undressed", "sad", .7, False)
    $ portrait.valeriya.appear("undressed", "sad", .3, True)
    speech.valeriya "То есть, всё это время она просто завела несколько симок и писала нам? Но зачем?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.main.morph(None, "surprised", None, True)
    speech.main "Я вообще думал, что она просто таким образом сообщает инфу, у меня отключены все уведомления в ВК, а в СМС нет."
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Просто, зачем писать мне, если и так практически везде ходим вместе?"
    $ portrait.valeriya.disappear()
    $ portrait.main.disappear()
    hide screen coworking_reveal_scene_1 with usual_transition
    speech.thought "Пока я думал, что ответить Лере, мои глаза закрыли чьи-то руки."
    Character("???", kind = speech.polina_hidden) "Приветствую! Угадай, пожалуйста, кто это."
    speech.main "Ксюша, это уже вообще не смешно. Давай мы в игры ещё поиграем, конечно."
    speech.kseniya "Что-то случилось?"
    speech.main "Что случилось? Писать мне с неизвестного номера, ещё и Лере, звать нас сюда..."
    speech.kseniya "Подождите, давайте внесём ясность. Это ведь вы меня позвали, я вообще учила историю."
    speech.narrator "*Свет в коворкинге гаснет*"
    Character("???", kind = speech.polina_hidden) "Ха-ха-ха!"
    speech.thought "..."
    Character("???", kind = speech.polina_hidden) "Ты писал, нет ты писала..."
    speech.thought "..."
    Character("???", kind = speech.polina_hidden) "Забавно, ребята."
    speech.thought "Мы не видели лица человека, силуэт стоял в тени."
    Character("???", kind = speech.polina_hidden) "Ну чего затихли? Нечего сказать?"
    speech.thought "..."
    Character("???", kind = speech.polina_hidden) "Я думала вы быстрее всё поймёте."
    speech.viktoriya "Йоу, всем приветики, я тут задержалась немно..."
    speech.viktoriya "Эм... А что тут происходит? Вы чего в потемках..."
    speech.viktoriya "О-о, Полина-а-а!"
    show screen coworking_reveal_scene_1(blur_out) with usual_transition
    $ portrait.polina.appear("undressed", "normal", .5, False)
    $ portrait.main.appear("undressed", "sad", .16, False)
    $ portrait.viktoriya.appear("undressed", "surprised", .68, False)
    $ portrait.valeriya.appear("undressed", "sad", .32, False)
    $ portrait.kseniya.appear("undressed", "surprised", .84, True)
    speech.kseniya "Извини, кто?.."
    $ portrait.kseniya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Что за бред, кто это?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.valeriya.morph(None, None, None, True)
    speech.valeriya "Силь ву пле, кто?"
    $ portrait.valeriya.morph(None, None, None, False)
    $ portrait.polina.morph(None, "sad", None, True)
    speech.polina "Вика, ну ты вот нормальная вообще?"
    $ portrait.polina.morph(None, None, None, False)
    $ portrait.viktoriya.morph(None, "happy", None, True)
    speech.viktoriya "Да представляешь, я захотела кофе, а в итоге меня на 20 минут задержали."
    $ portrait.viktoriya.morph(None, "sad", None, None)
    speech.viktoriya "Я что-то испортила?"
    $ portrait.viktoriya.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Я, если честно, чуть не умер. Ты, ёптель, кто вообще?"
    $ portrait.main.morph(None, None, None, False)
    $ portrait.polina.morph(None, "happy", None, True)
    speech.polina "Ха-ха-ха, я тот самый неизвестный номер, всем рекурсивным пряникам привет!"
    $ portrait.polina.morph(None, None, None, False)
    $ portrait.main.morph(None, None, None, True)
    speech.main "Ты... Чего?!"
    $ portrait.main.morph(None, None, None, False)
    speech.thought "..."
    $ portrait.viktoriya.morph(None, "sad", None, None)
    speech.viktoriya "Может анекдот?..."
    $ portrait.viktoriya.disappear()
    $ portrait.polina.disappear()
    $ portrait.main.disappear()
    $ portrait.valeriya.disappear()
    $ portrait.kseniya.disappear()
    hide screen coworking_reveal_scene_1 with usual_transition
    return












screen finale_grande_scene_1:
    add "bg_finale.jpg" fit "fill"
    zorder -10

screen finale_grande_scene_2:
    add "bg_audience.jpg" fit "fill"
    zorder -10

define finale_grande_music = "Surasshu — Eek!.mp3"
define finale_grande_ambient = "Lively Noise.mp3"

label finale_grande_script:
    show screen finale_grande_scene_1 with usual_transition
    stop ambient fadeout .5
    play ambient finale_grande_ambient loop fadein .5
    stop music fadeout .5
    play music finale_grande_music fadein .5
    speech.main "Это было настолько давно, друзья мои... Мы тогда даже не могли представить, что нас ждет."
    speech.main "Вам, наверное, интересно, кто такая Полина. И как она нас нашла." 
    speech.narrator "*В зале взмывает лес рук*"
    speech.main "Да, пожалуйста... Наверное, пришло время вопросов."
    while not meeting_tried_game or not meeting_tried_start or not meeting_tried_polina or not meeting_tried_who:
        menu: 
            "Про что игра?" if not meeting_tried_game:
                $ meeting_tried_game = True
                Character("Слушатель", kind = speech.generic) "Эмм... Так мы не очень поняли... Вы сделали игру про свой путь в ИИ?"
                speech.main "Не совсем, мы... {b}Мы сделали ИИ, который сделал игру{/b}... Мы сделали ИИ, который не только выполняет команды, он... Он чувствует."
                speech.main "Ну, это вам судить, на самом деле. Если игра получилась душевной, то моя работа выполнена качественно... Наша работа."
                speech.main "Основной посыл игры в том (по крайней мере, так решил ИИ), что {b}выбрав УрФУ, я смог достичь таких высот{/b}."
                speech.main "И, насколько я могу судить по себе, искусственный интелект нисколько не ошибся."
            "С чего всё началось?" if not meeting_tried_start:
                $ meeting_tried_start = True
                Character("Слушатель", kind = speech.generic) "То есть, вы хотите сказать, что именно первый курс в УрФУ положил начало в вашей профессии?"
                speech.main "Ха-ха, вы удивлены? А я то как! Да, представляете."
                speech.main "Образование в России не отбило у меня желание учиться. На самом деле структура ИОТ помогла. Как и мероприятия, как вы уже поняли, олимпиады."
                speech.main "Моя команда. Ваня тоже. Че бы я, блин, делал без него!"
                speech.narrator "*Ваня кричит из зала*"
                speech.vanya "Загнулся бы без меня, ха-ха-ха-ха!"
            "Кто такая Полина?" if not meeting_tried_polina:
                $ meeting_tried_polina = True
                Character("Слушатель", kind = speech.generic) "Так кто такая Полина? Как она нашла ваши номера?"
                speech.main "Наш тимлид. Она залезла в ведомость и посмотрела наши номера, представляете. Писала нам, на какие мероприятия приходить."
                speech.main "Она собрала команду. С Викой они были в одной группе. Вика рассказала про меня, потом про Леру и Ксюшу."
                speech.main "А Полина решила сделать нас командой. У неё талант. После того разговора в коворкинге мы отправились есть пиццу."
                speech.main "А потом, через две недели, мы подали заявку на наш первый стартап. И теперь, я стою перед вами с нашим уже финальным проектом."
            "Кем вы стали?" if not meeting_tried_who:
                $ meeting_tried_who = True
                Character("Слушатель", kind = speech.generic) "Так кем вы стали после обучения в вузе?"
                speech.main "Я — разработчик искусственного интеллекта, Лера — гейм-дизайнер. Она придумывает идеи для наших стартапов."
                speech.main "Вика — дизайнер. Ей помогает Ваня с некоторыми проектами. Они хорошо работают вместе."
                speech.main "Ксюша — аналитик. Её любовь к математике позволяет нам обходить конкурентов."
                speech.main "Ну, а Полина — чокнутый человек, который сплотил нас и подарил нам возможность быть не просто командой... А друзьями."
                speech.main "ИИ очень хорошо передал {b}важность тимбилдинга в процессе обучения{/b}."
    speech.main "Вижу кучу рук.. Понимаю вас! Но это не конец игры. ИИ дописал её до конца, поэтому вы можете поиграть в неё и узнать, как мы выживали на втором курсе..."
    speech.main "... прогуливали пары, чтобы закончить проекты, и выиграли первый миллион. Тот ИИ, который написал эту игру, есть с этой секунды в свободном доступе."
    speech.main "Если вам хочется рассказать миру историю из своей жизни и сделать это душевно, то силь ву пле! Для этого мы и делали этот проект." 
    hide screen finale_grande_scene_1 with usual_transition
    show screen finale_grande_scene_2 with usual_transition
    ""
    hide screen finale_grande_scene_2 with usual_transition
    show screen text_scene("fin") with usual_transition
    ""
    hide screen text_scene with usual_transition
    return