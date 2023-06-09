#This is a copy of credits.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Import the datetime library for using time
init python:
    import datetime

#This defines the CGs that disappear after a few seconds
#These are the colored CGs used for scene cgs
image credits_cg1:
    "images/cg/cretits/1.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    size(640, 360)

image credits_cg3:
    "images/cg/credits/3.png"
    size(640, 360)

image credits_cg4:
    "images/cg/credits/4.png"
    size(640, 360)

image credits_cg5:
    "images/cg/credits/5.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "images/cg/credits/9.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "images/cg/credits/10.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

#These are the grayed out CGs for unseen cgs
image credits_cg1_locked:
    "images/cg/y_kill/1a.png"
    size(640, 360)

image credits_cg2_locked:
    "images/bg/gym_n.jpg"
    size(640, 360)

image credits_cg3_locked:
    "images/bg/pathway_n.jpg"
    size(640, 360)

image credits_cg4_locked:
    "images/bg/school_n.jpg"
    size(640, 360)

image credits_cg5_locked:
    "mod_assets/anarchisty.png"
    size(640, 360)

image credits_cg6_locked:
    "images/bg/building.jpg"
    size(640, 360)

image credits_cg7_locked:
    "images/bg/main_hall_m.jpg"
    size(640, 360)

image credits_cg8_locked:
    "images/bg/train_n.jpg"
    size(640, 360)

image credits_cg9_locked:
    "images/bg/yard_m.jpg"
    size(640, 360)

image credits_cg10_locked:
    "images/bg/house_n.jpg"
    size(640, 360)

#This defines the CGs that don't fade for a "perfect ending"
image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size(640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size(640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size(640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size(640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size(640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size(640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size(640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size(640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size(640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size(640, 360)

#DDLC Logo
image credits_logo:
    "mod_assets/ddmc.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

#Team Salvato logo
image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

#This styles the different text in the credits
style credits_header:
    font "gui/font/comicbd.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/comic.ttf"
    color "#fff"
    size 14
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)

#These are the animations applied to the make the credits and images scroll
transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

#This defines the Karaoke for Monika's singing
image mcredits_1a:
    ypos credits_ypos
    xoffset -205
    "black"
    10.33
    Text("Every day,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -35
    "black"
    11.75
    Text("I imagine a future where", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 170
    "black"
    13.76
    Text("I can be with you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -226
    "black"
    19.45
    Text("In my hand", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -10
    "black"
    20.9
    Text(" is a pen that will write a poem", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 225
    "black"
    23.27
    Text("of me and you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("The ink flows down into a dark puddle", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(" Just move your hand -- write the way into his heart!", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("But in this world of infinite choices", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -145
    "black"
    42.0
    Text(" What will it take", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 85
    "black"
    43.47
    Text(" just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("What will it take just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4)

#Glitchy images
image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

#Start for the actual credits scene
label credits:
    $ persistent.autoload = "credits" #Come back to the credits if the game is quit
    #Disable player interactions
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    #Start Monika's spoken dialogue
    play music "bgm/end-voice.ogg" noloop

    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat

    #Play monika's song with Karaoke lines
    pause 41
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole("renpy.music.play(\"ddlc.ogg\")", "Playing audio \"ddlc.ogg\"...") from _call_updateconsole
    pause 1.0
    call hideconsole from _call_hideconsole
    play music "<to 50.0>bgm/credits.ogg" noloop
    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_1c zorder 48
    show mcredits_2a zorder 47
    show mcredits_2b zorder 46
    show mcredits_2c zorder 45
    show mcredits_3 zorder 44
    show mcredits_4 zorder 43
    show mcredits_5 zorder 42
    show mcredits_6a zorder 41
    show mcredits_6b zorder 40
    show mcredits_7 zorder 51

    pause 50
    jump credits2

#This is where the credits scroll starts
label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    play music "sfx/tonn.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12
    #Each CG is shown. If it's unseen gray it out, if it's not a perfect ending
    #make each image get deleted after a few seconds
    #Actual names for the credits
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Автор идеи и сценарист" at credits_text_scroll_left as credits_header_1
    show credits_text "Brifyjek aka u/IGI86" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())

    ##The rest of the sections follow this same pattern
    show image ("credits_cg2" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "В главных ролях:" at credits_text_scroll_right as credits_header_2
    show credits_text "\n\nЮри – Юри Рок Оккульта\n[player] – Король [player] изъ Ада\nСайори – Некросадистическая Сайори Павулон Инжектор\nи Ритуальный Пожиратель Нерождённой Ангельской Плоти\nНацуки – Пинки Лоулесс\nМоника – Лилдемоникс" at credits_text_scroll_right as credits_text_2
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(25.55 - (datetime.datetime.now() - starttime).total_seconds())
    
    show image ("credits_cg3" + lockedtext) at credits_scroll_right as credits_image_1
    show credits_header "Музыка" at credits_text_scroll_left as credits_header_1
    show credits_text "\n\nKorn – Twist (изолированный вокал)\nType o Negative – I Don't Wanna Be Me(MIDI)\nMayhem – Freezing Moon(Live in Leipzig)(opening words only)\nMayhem – Freezing Moon(MIDI)\nDaashino/niu – Ura Atama Yume\nImmortal – Tyrants(MIDI)" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show image ("credits_cg4" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Отдельное спасибо" at credits_text_scroll_right as credits_header_2
    show credits_text "\n\n\n\n\n\n\n\n\nОригинальная игра – Team Salvato\nИзображение леса – Dietmar Rabich (Wikimedia Commons)\nОбычный спрайт Моники – u/DestinyPvEGal\nhouse_n – POBAWsiezmna#1550\nbuilding – Kimagure After\nclub_n – Alex[[ORG]#9077\ngym_n – Vanishing Point\nlockers_n – Kimagure After\nmain_hall_m – Kimagure After\npathway – Kimagure After\nschool_n – Kimagure After\nstreet_m – Kimagure After\ntrain_n – Kimagure After\nyard_m – Vanishing Point" at credits_text_scroll_right as credits_text_2
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(43.75 - (datetime.datetime.now() - starttime).total_seconds())

    show image ("credits_cg5" + lockedtext) at credits_scroll_right as credits_image_1
    show credits_header "Перевод и локализация" at credits_text_scroll_left as credits_header_1
    show credits_text "Team Анархисты (https:\\vk.com/teamanarkhisty)" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
  
    show image ("credits_cg6" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Огромное спасибо всем за\nтёплые слова и поддержку!" at credits_text_scroll_right as credits_header_2
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())

    show image ("credits_cg7" + lockedtext) at credits_scroll_right as credits_image_1
    show credits_header "Спасибо вам за игру" at credits_text_scroll_left as credits_header_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())

    show image ("credits_cg8" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Это мой первый мод" at credits_text_scroll_right as credits_header_2
    show credits_text "Я знаю, что он и так\nнемного отстойный" at credits_text_scroll_right as credits_text_2
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    
    show image ("credits_cg9" + lockedtext) at credits_scroll_right as credits_image_1
    show credits_header "Однако, если он получит\nдостаточное внимание," at credits_text_scroll_left as credits_header_1
    show credits_text "Я сделаю вторую часть" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
  
    show image ("credits_cg10" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Значит..." at credits_text_scroll_right as credits_header_2
    show credits_text "Продолжение следует?.." at credits_text_scroll_right as credits_text_2
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())

    $ renpy.pause (10.0)

    return
