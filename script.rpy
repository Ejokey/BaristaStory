# Вы можете расположить сценарий своей игры в этом файле.
init:
    image cafe out = "cafe outside1.webp"
    image cafe kitchen = "kitchen.webp"
    image cafe inside = "cafe inside1.webp"
    image cafe inside full = "cafe inside1 full.webp"
    image bar = "bar1.webp"
    image main neutral = "images/mainChar neutral.webp"
    image main happy = "images/mainChar happy.webp"
    image main surprised = "images/mainChar surprised.webp"
    image main fartuk neutral = "images/mainChar neutral fartuk.webp"
    image main fartuk happy = "images/mainChar happy fartuk.webp"
    image main fartuk surprised = "images/mainChar surprised fartuk.webp"
    image admin neutral = "images/admin neutral.webp"
    image admin sweat = "images/admin sweat.webp"
    image admin winks = "images/admin winks.webp"
    image visitor neutral = "visitor neutral1.webp"
    image blackscreen = "blackscreenimg.webp"
    $ pts=0
# Определение персонажей игры.
define m = Character('Вы', color="#ff9900")
define a = Character('Администратор', color="#ff9900")
define v = Character('Гость', color="#ff9900")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:


label start:
    scene cafe out

    show main neutral at right with moveinright
    m "Привет, я прямо сейчас иду устраиваться баристой в кофейню, надеюсь, ты сможешь мне в этом помочь. "
    show main happy at right
    m "Не будем тянуть, погнали работать баристой!"
    queue music ["audio/Jazz.opus", "audio/Garden.opus"]
    scene cafe inside with fade
    show main surprised at right with moveinright
    m "Вау, а тут неплохо внутри!"
    show main neutral at right
    m "Надо найти администратора, который подскажет, как попасть на работу."

    show admin neutral at left
    m "Здравствуйте, как я могу попасть на работу в вашу кофейню?"
    a "Добрый день! Вы обратились по адресу, нам как раз нужны новые бариста, готовы прямо сейчас пройти опрос?"
    menu:
        a "Добрый день! Вы обратились по адресу, нам как раз нужны новые бариста, готовы прямо сейчас пройти опрос?"
        "Да":
            a "Ну что же, тогда приступим."

    menu:
        a "Был ли у вас опыт работы баристой?"
        "Да":
            $ have_exp = True
        "Нет":
            $ have_exp = False

    if have_exp:
        menu:
            a "На каком зерне вы работали до этого?"
            "Арабика":
                pass
            "Робуста":
                pass
            "Либерика":
                pass
    else:
        a "Хорошо, тогда начнем с нуля. Давай посмотрим, как ты справишься с первым заданием."

    if have_exp:
        menu:
            a "Знакомы ли вы с терминами холдер, питчер, темпер, джиггер?"
            "Да":

                $ pts = pts + 1
            "Нет":
                pass

    if have_exp:
        menu:
            a "Что бариста должен сделать в первую очередь, перед приготовлением кофе?"
            "Помыть руки":
                pass
            "Снять верхнюю одежду":
                $ pts+=1
            "Надеть фартук":
                pass

    if have_exp and pts==2:
        a "Отлично, я вижу у тебя уже очень неплохой опыт в нашей работе, давай перейдем к первому заданию."
    if have_exp and pts<=1:
        a "Неплохо, ты довольно перспективный ученик, давай перейдем к первому заданию."

    scene cafe kitchen with dissolve
    play music "audio/kitchensounds.opus"
    show admin neutral
    a "Сейчас тебе нужно будет сыграть в замечательную классику - три в ряд."
    a "Думаю, правила этой игры лишний раз объяснять не нужно, набери как можно больше очков, и я окончательно пойму твой потенциал."
    show admin winks
    pause 0.75
    show admin neutral
    pause 0.4
    stop music
    queue music ["audio/Garden.opus", "audio/Jazz.opus"]
    call krix
    pause 1
    centered "{size=52}Поздравляем \n Ваш результат {color=#f2b627}[pointk]"

    scene cafe inside with dissolve
    show admin neutral at left with moveinleft
    show main happy at right with moveinright
    a "А ты хорош, думаю, тебя пока  можно будет поставить на кассу."
    a "Приходи завтра, посмотрим на тебя в деле."
    scene blackscreen with dissolve
    pause 1

    scene cafe out with dissolve
    show main happy at right with moveinright
    m "Мой первый день в кофейне..."
    m "Черт, а я немного волнуюсь, каким будет мой первый клиент."
    show main surprised at right
    m "Вдруг это будет какой-то грубиян, а я не смогу сдержаться и отвечу ему лишнего..."
    m "Ну ладно, главное уверенность и спокойствие, захожу."

    scene cafe inside with dissolve
    show admin neutral
    a "О, привет, проходи, переодевайся и за кассу. Уже совсем скоро пойдут первые клиенты."

    scene cafe inside full with dissolve
    show main fartuk neutral at left
    m "Так, вон идет мой первый клиент, спокойно, я все смогу."
    show visitor neutral at right with moveinright
    m "Здравствуйте, что бы вы хотели сегодня?"
    v "Здравствуйте, один латте, пожалуйста."
    m "Хорошо, секунду."
    scene bar with dissolve
    show main fartuk happy
    m "Так, чтобы приготовить кофе, мне нужно пройти еще одну мини-игру."
    m "Главное здесь ловить капли кофе в стакан, не забывая поднимать стакан прямо перед тем, как капля упала в него."
    pause 1
    call fish_catcher


return
