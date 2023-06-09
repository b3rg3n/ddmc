################################################################################################
#Additional Definitions

#Happy Sayori hugging MC CG
image s_cg4:
    "mod_assets/cg/s_cg4.png"                                   #CREDIT: Malukah Maker#2907

#Monika Spaceroom #####################
image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1

image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image room_glitch = "images/cg/monika/monika_bg_glitch.png"
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
######################################


# Original Background Variants
image bedroom_night = "mod_assets/bg/bedroom_n.jpg"             #CREDIT: noah.rpy#1267 / nsmythddyas#5245
image class_sunset = "mod_assets/bg/class_s.jpg"                #CREDIT: Gorosona#8350
image class_night = "mod_assets/bg/class_n.jpg"                 #CREDIT: Alex [ORG]#9077
image club_sunset = "mod_assets/bg/club_s.jpg"                  #CREDIT: Gorosona#8350
image club_night = "mod_assets/bg/club_n.jpg"                   #CREDIT: Alex [ORG]#9077
image corridor_sunset = "mod_asset/bg/corridor_s.jpg"           #CREDIT: WAHnika (Current)#9757
image corridor_night = "mod_asets/bg/corridor_n.png"            #CREDIT: Alex [ORG]#9077
image corridor_rainy = "mod_asets/bg/corridor_r.png"            #CREDIT: Alex [ORG]#9077
image house_sunset = "mod_assets/bg/house_s.png"                #CREDIT: Crashpunk#0025
image house_night = "mod_assets/bg/house_n.jpg"                 #CREDIT: POBAWsiezmna#1550
image residential_sunset = "mod_assets/bg/residential_s.png"    #CREDIT: Crashpunk#0025
image residential_night = "mod_assets/bg/residential_n.png"     #CREDIT: TsunKrAZy#2862
image residential_rainy = "mod_asets/bg/residential_r.jpg"      #CREDIT: Astro Space#9989
image spaceroom_night = "mod_assets/bg/spaceroom_n.jpg"         #CREDIT: Alex [ORG]#9077

#House Backgrounds
image balcony = "mod_assets/bg/balcony.jpg"                     #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image bedroom_desk = "mod_assets/bg/bedroom_d.jpg"              #CREDIT: Akame#8940
image bedroom_2 = "mod_assets/bg/bedroom_2.jpg"                 #CREDIT osumashi
image dorm = "mod_assets/bg/dorm.jpg"                           #CREDIT osumashi
image dorm_sunset = "mod_assets/bg/dorm_s.jpg"                  #CREDIT osumashi
image dorm_night = "mod_assets/bg/dorm_n.jpg"                   #CREDIT osumashi
image entrance = "mod_assets/bg/entrance.jpg"                   #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image entrance_night = "mod_assets/bg/entrance_n.jpg"           #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image house_hallway = "mod_assets/bg/house_hallway.jpg"         #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image living_room = "mod_assets/bg/living_room.jpg"             #CREDIT: Nuxill#7870
image living_room_sunset = "mod_assets/bg/living_room_s.jpg"    #CREDIT: Nuxill#7870
image living_room_night = "mod_assets/bg/living_room_n.jpg"     #CREDIT: Nuxill#7870

image room = "mod_assets/bg/room.jpg"                           #CREDIT: Kimagure After
image room_sunset = "mod_assets/bg/room_s.jpg"                  #CREDIT: Kimagure After
image room_night = "mod_assets/bg/room_n.jpg"                   #CREDIT: Kimagure After
image moving_room = "mod_assets/bg/moving_room.jpg"             #CREDIT: Kimagure After
image moving_room_sunset = "mod_assets/bg/moving_room_s.jpg"    #CREDIT: Kimagure After
image moving_room_night = "mod_assets/bg/moving_room_n.jpg"     #CREDIT: Kimagure After

image monika_bedroom = "mod_assets/bg/monika_bedroom.jpg"       #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image monika_books = "mod_assets/bg/monika_room.jpg"             #CREDIT: Kimagure After
image monika_books = "mod_assets/bg/monika_room_s.jpg"    #CREDIT: Kimagure After
image monika_books = "mod_assets/bg/monika_room_n.jpg"     #CREDIT: Kimagure After

image natsuki_bedroom = "mod_assets/bg/natsuki_bedroom.jpg"             #CREDIT: Kimagure After
image natsuki_bedroom_sunset = "mod_assets/bg/natsuki_bedroom_s.jpg"    #CREDIT: Kimagure After
image natsuki_bedroom_night = "mod_assets/bg/natsuki_bedroom_n.jpg"     #CREDIT: Kimagure After
image natsuki_bedroom_midnight = "mod_assets/bg/natsuki_bedroom_m.jpg"  #CREDIT: Kimagure After

image yuri_bedroom = "mod_assets/bg/yuri_bedroom.jpg"           #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image yuri_room = "mod_assets/bg/yuri_room.jpg"                 #CREDIT: Kimagure After
image yuri_room_sunset = "mod_assets/bg/yuri_room_s.jpg"        #CREDIT: Kimagure After
image yuri_room_night = "mod_assets/bg/yuri_room_n.jpg"         #CREDIT: Kimagure After
image yuri_room_midnight = "mod_assets/bg/yuri_room_m.jpg"      #CREDIT: Kimagure After

#Residential Backgrounds
image building = "mod_assets/bg/building.jpg"                   #CREDIT: Kimagure After
image building_sunset = "mod_assets/bg/building_s.jpg"          #CREDIT: Kimagure After
image building_night = "mod_assets/bg/building_n.jpg"           #CREDIT: Kimagure After
image building_midnight = "mod_assets/bg/building_m.jpg"        #CREDIT: Kimagure After
image building_rainy = "mod_assets/bg/building_r.jpg"           #CREDIT: Kimagure After
image garden = "mod_assets/bg/garden.jpg"                       #CREDIT: Kimagure After
image monika_house = "mod_assets/bg/monika_house.jpg"           #DDLC
image natsuki_house = "mod_assets/bg/natsuki_house.jpg"                 #CREDIT: Kimagure After
image natsuki_house_sunset = "mod_assets/bg/natsuki_house_s.jpg"        #CREDIT: Kimagure After
image natsuki_house_night = "mod_assets/bg/natsuki_house_n.jpg"         #CREDIT: Kimagure After

image park = "mod_assets/bg/park.jpg"                           #CREDIT: Creative Freaks
image park_sunset = "mod_assets/bg/park_s.jpg"                  #CREDIT: Creative Freaks
image park_night = "mod_assets/bg/park_n.jpg"                   #CREDIT: Creative Freaks
image park_overlook = "mod_assets/bg/park_overlook.jpg"         #CREDIT Cyrke#8043
image park_entrance = "mod_assets/bg/park_entrance.jpg"                 #CREDIT: Kimagure After
image park_entrance_sunset = "mod_assets/bg/park_entrance_s.jgp"        #CREDIT: Kimagure After
image park_entrance_night = "mod_assets/bg/park_entrance_n.jpg"         #CREDIT: Kimagure After
image pathway = "mod_assets/bg/pathway.jpg"                     #CREDIT: Kimagure After
image pathway_sunset = "mod_assets/bg/pathway_s.jpg"            #CREDIT: Kimagure After
image pathway_night = "mod_assets/bg/pathway_n.jpg"             #CREDIT: Kimagure After
image sidewalk = "mod_assets/bg/sidewalk.jpg"                   #CREDIT: Uncle Mugen

#City Backgrounds
image alley = "mod_assets/bg/alley.jpg"                         #CREDIT osumashi
image alley_2 = "mod_assets/bg/alley_2.jpg"                     #CREDIT osumashi
image intersection = "mod_assets/bg/intersection.jpg"                   #CREDIT: Kimagure After
image intersection_sunset = "mod_assets/bg/intersection_s.jpg"          #CREDIT: Kimagure After
image intersection_night = "mod_assets/bg/intersection_n.jpg"           #CREDIT: Kimagure After
image intersection_midnight = "mod_assets/bg/intersection_m.jpg"        #CREDIT: Kimagure After
image intersection_rainy = "mod_assets/bg/intersection_r.jpg"           #CREDIT: Kimagure After
        
image shops = "mod_assets/bg/shops.jpg"                         #CREDIT: (c) 安野譲 (Vanishing Point)
image shops_sunset = "mod_assets/bg/shops_s.jpg"                #CREDIT: (c) 安野譲 (Vanishing Point)
image shops_night = "mod_assets/bg/shops_n.jpg"                 #CREDIT: (c) 安野譲 (Vanishing Point)
image shops_midnight = "mod_assets/bg/shops_m.jpg"              #CREDIT: (c) 安野譲 (Vanishing Point)
image restaurant = "mod_assets/bg/restaurant.jpg"               #CREDIT: yagamirai10#7046
image public_library = "mod_assets/bg/public_library.jpg"       #CREDIT: Yukito

image street = "mod_assets/bg/street.jpg"                       #CREDIT: Kimagure After
image street_sunset = "mod_assets/bg/street_s.jpg"              #CREDIT: Kimagure After
image street_night = "mod_assets/bg/street_n.jpg"               #CREDIT: Kimagure After
image street_midnight = "mod_assets/bg/street_m.jpg"            #CREDIT: Kimagure After
image street_rainy = "mod_assets/bg/street_r.jpg"               #CREDIT: Kimagure After

image train = "mod_assets/bg/train.jpg"                         #CREDIT: Kimagure After
image train_sunset = "mod_assets/bg/train_s.jpg"                #CREDIT: Kimagure After
image train_night = "mod_assets/bg/train_n.jpg"                 #CREDIT: Kimagure After

#School Backgrounds
image bathroom = "mod_assets/bg/bathroom.jpg"                   #CREDIT: u/AFewSecondsToLive
image board = "mod_assets/bg/board.jpg"                         #CREDIT: Cyrke#8043
image chalkboard = "mod_assets/bg/chalkboard.png"               #CREDIT yagamirai10#7046
image chalkboard_graffiti = "mod_assets/bg/chalkboard_g.png"    #CREDIT yagamirai10#7046
image classroom = "mod_assets/bg/class.jpg"                     #CREDIT: Kimagure After
image classroom_sunset = "mod_assets/bg/class_s.jpg"            #CREDIT: Kimagure After
image classroom_night = "mod_assets/bg/class_n.jpg"             #CREDIT: Kimagure After
image classroom_2 = "mod_assets/bg/classroom_2.jpg"             #CREDIT: Yukito
image club_desks = "mod_assets/bg/club_desks.jpg"               #CREDIT: Wheatley#3103, edited by Malukah Maker#2907
image empty_classroom = "mod_assets/bg/empty_classroom.jpg"             #CREDIT: Kimagure After
image empty_classroom_sunset = "mod_assets/bg/empty_classroom.jpg"      #CREDIT: Kimagure After
image empty_classroom_night = "mod_assets/bg/empty_classroom.jpg"       #CREDIT: Kimagure After
image lecture = "mod_assets/bg/lecture.jpg"                     #CREDIT: Kimagure After
image lecture_sunset = "mod_assets/bg/lecture_s.jpg"            #CREDIT: Kimagure After
image lecture_night = "mod_assets/bg/lecture_n.jpg"             #CREDIT: Kimagure After
image lecture_2 = "mod_assets/bg/lecture_2.jpg"                 #CREDIT: Yukito
image school = "mod_assets/bg/school.jpg"                       #CREDIT: Kimagure After
image school_sunset = "mod_assets/bg/school_s.jpg"              #CREDIT: Kimagure After
image school_night = "mod_assets/bg/school_n.jpg"               #CREDIT: Kimagure After

image hallway = "mod_assets/bg/hallway.jpg"                     #CREDIT: Kimagure After
image hallway_sunset = "mod_assets/bg/hallway_s.jpg"            #CREDIT: Kimagure After
image hallway_night = "mod_assets/bg/hallway_n.jpg"             #CREDIT: Kimagure After
image hallway_midnight = "mod_assets/bg/hallway_m.jpg"          #CREDIT: Kimagure After
image main_hall = "mod_assets/bg/main_hall.jpg"                 #CREDIT: Kimagure After
image main_hall_sunset = "mod_assets/bg/main_hall_s.jpg"        #CREDIT: Kimagure After
image main_hall_night = "mod_assets/bg/main_hall_n.jpg"         #CREDIT: Kimagure After
image main_hall_midnight = "mod_assets/bg/main_hall_m.jpg"      #CREDIT: Kimagure After

image ground_floor = "mod_assets/bg/ground.jpg"                 #CREDIT: Kimagure After
image ground_floor_sunset = "mod_assets/bg/ground_s.jpg"        #CREDIT: Kimagure After
image ground_floor_night = "mod_assets/bg/ground_n.jpg"         #CREDIT: Kimagure After
image second_floor = "mod_assets/bg/s_floor.jpg"                #CREDIT: Kimagure After
image second_floor_sunset = "mod_assets/bg/s_floor_s.jpg"       #CREDIT: Kimagure After
image second_floor_night = "mod_assets/bg/s_floor_n.jpg"        #CREDIT: Kimagure After
image stairway = "mod_assets/bg/stairway.jpg"                   #CREDIT: Kimagure After
image stairway_sunset = "mod_assets/bg/stairway_s.jpg"          #CREDIT: Kimagure After
image stairway_night = "mod_assets/bg/stairway_n.jpg"           #CREDIT: Kimagure After

image gate = "mod_assets/bg/gate.jpg"                           #CREDIT: Kimagure After
image gate_sunset = "mod_assets/bg/gate_s.jpg"                  #CREDIT: Kimagure After
image gate_night = "mod_assets/bg/gate_n.jpg"                   #CREDIT: Kimagure After
image gate_midnight = "mod_assets/bg/gate_m.jpg"                #CREDIT: Kimagure After
image gate_rainy = "mod_assets/bg/gate_r.jpg"                   #CREDIT: Kimagure After
image outside = "mod_assets/bg/outside.jpg"                     #CREDIT: Kimagure After
image outside_sunset = "mod_assets/bg/outside_s.jpg"            #CREDIT: Kimagure After
image outside_night = "mod_assets/bg/outside_n.jpg"             #CREDIT: Kimagure After

image computers = "mod_assets/bg/computers.jpg"                 #CREDIT: Kimagure After
image computers_night = "mod_assets/bg/computers_n.jpg"         #CREDIT: Kimagure After
image office = "mod_assets/bg/office.jpg"                       #CREDIT: Kimagure After
image office_sunset = "mod_assets/bg/office_s.jpg"              #CREDIT: Kimagure After
image office_night = "mod_assets/bg/office_n.jpg"               #CREDIT: Kimagure After
image storage = "mod_assets/bg/storage.jpg"                     #CREDIT: Kimagure After
image storage_sunset = "mod_assets/bg/storage_s.jpg"            #CREDIT: Kimagure After
image storage_night = "mod_assets/bg/storage_n.jpg"             #CREDIT: Kimagure After

image art = "mod_assets/bg/art.jpg"                             #CREDIT: Kimagure After
image art_sunset = "mod_assets/bg/art_s.jpg"                    #CREDIT: Kimagure After
image art_night = "mod_assets/bg/art_n.jpg"                     #CREDIT: Kimagure After
image artroom = "mod_assets/bg/artroom.jpg"                     #CREDIT: Kimagure After
image artroom_sunset = "mod_assets/bg/artroom_s.jpg"            #CREDIT: Kimagure After
image artroom_night = "mod_assets/bg/artroom_n.jpg"             #CREDIT: Kimagure After
image art_empty = "mod_assets/bg/art_empty.jpg"                 #CREDIT: Kimagure After
image art_empty_sunset = "mod_assets/bg/art_empty_s.jpg"        #CREDIT: Kimagure After
image art_empty_night = "mod_assets/bg/art_empty_n.jpg"         #CREDIT: Kimagure After
image piano_room = "mod_assets/bg/piano.jpg"                    #CREDIT: Yukito
image piano_room_full = "mod_assets/bg/piano_full.jpg"          #CREDIT: Yukito

image gym = "mod_assets/bg/gym.jpg"                             #CREDIT: (c) 安野譲 (Vanishing Point)
image gym_sunset = "mod_assets/bg/gym_s.jpg"                    #CREDIT: (c) 安野譲 (Vanishing Point)
image gym_night = "mod_assets/bg/gym_n.jpg"                     #CREDIT: (c) 安野譲 (Vanishing Point)
image gym_midnight = "mod_assets/bg/gym_m.jpg"                  #CREDIT: (c) 安野譲 (Vanishing Point)
image pool = "mod_assets/bg/pool.jpg"
image pool_sunset = "mod_assets/bg/pool_s.jpg"                  #CREDIT: Kimagure After
image pool_night = "mod_assets/bg/pool_n.jpg"                   #CREDIT: Kimagure After
image pool_rainy = "mod_assets/bg/pool_r.jpg"                   #CREDIT: Kimagure After
image lockers = "mod_assets/bg/lockers.jpg"                     #CREDIT: Kimagure After
image lockers_sunset = "mod_assets/bg/lockers_s.jpg"            #CREDIT: Kimagure After
image lockers_night = "mod_assets/bg/lockers_n.jpg"             #CREDIT: Kimagure After

image library = "mod_assets/bg/library.jpg"                     #CREDIT: Kimagure After
image library_sunset = "mod_assets/bg/library_s.jpg"            #CREDIT: Kimagure After
image library_night = "mod_assets/bg/library_n.jpg"             #CREDIT: Kimagure After
image medical = "mod_assets/bg/medical.jpg"                     #CREDIT: Kimagure After
image medical_sunset = "mod_assets/bg/medical_s.jpg"            #CREDIT: Kimagure After
image medical_night = "mod_assets/bg/medical_n.jpg"             #CREDIT: Kimagure After
image staff_room = "mod_assets/bg/staff_room.jpg"               #CREDIT: Yukito

image roof = "mod_assets/bg/roof.jpg"                           #CREDIT: Kimagure After
image roof_sunset = "mod_assets/bg/roof_s.jpg"                  #CREDIT: Kimagure After
image roof_night = "mod_assets/bg/roof_n.jpg"                   #CREDIT: Kimagure After
image roof_rainy = "mod_assets/bg/roof_r.jpg"                   #CREDIT: Kimagure After
image yard = "mod_assets/bg/yard.jpg"                           #CREDIT: (c) 安野譲 (Vanishing Point)
image yard_sunset = "mod_assets/bg/yard_s.jpg"                  #CREDIT: (c) 安野譲 (Vanishing Point)
image yard_night = "mod_assets/bg/yard_n.jpg"                   #CREDIT: (c) 安野譲 (Vanishing Point)
image yard_midnight = "mod_assets/bg/yard_m.jpg"                #CREDIT: (c) 安野譲 (Vanishing Point)

#Misc Backgrounds
image breakdown = "mod_assets/bg/breakdown.jpg"                 #CREDIT: Trueloverofmonika#5084



# Sayori
image sayori 1z = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/z.png")         #HEAD CREDIT: SpringingTraps#5243
image sayori 1za = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/za.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 1zb = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zb.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 1zc = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zc.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 1zd = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zd.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 1ze = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/ze.png")       #HEAD CREDIT: LeoDeCraprio#4239

image sayori 1bz = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/z.png")      #HEAD CREDIT: SpringingTraps#5243
image sayori 1bza = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/za.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 1bzb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zb.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 1bzc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zc.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 1bzd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zd.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 1bze = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/ze.png")    #HEAD CREDIT: LeoDeCraprio#4239

image sayori 2z = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/z.png")         #HEAD CREDIT: SpringingTraps#5243
image sayori 2za = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/za.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 2zb = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zb.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 2zc = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zc.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 2zd = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zd.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 2ze = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/ze.png")       #HEAD CREDIT: LeoDeCraprio#4239

image sayori 2bz = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/z.png")      #HEAD CREDIT: SpringingTraps#5243
image sayori 2bza = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/za.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 2bzb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zb.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 2bzc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zc.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 2bzd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zd.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 2bze = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/ze.png")    #HEAD CREDIT: LeoDeCraprio#4239

image sayori 3z = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/z.png")         #HEAD CREDIT: SpringingTraps#5243
image sayori 3za = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/za.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 3zb = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zb.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 3zc = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zc.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 3zd = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zd.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 3ze = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/ze.png")       #HEAD CREDIT: LeoDeCraprio#4239

image sayori 3bz = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/z.png")      #HEAD CREDIT: SpringingTraps#5243
image sayori 3bza = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/za.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 3bzb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zb.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 3bzc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zc.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 3bzd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zd.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 3bze = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/ze.png")    #HEAD CREDIT: LeoDeCraprio#4239

image sayori 4z = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/z.png")         #HEAD CREDIT: SpringingTraps#5243
image sayori 4za = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/za.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 4zb = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zb.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 4zc = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zc.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 4zd = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zd.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 4ze = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/ze.png")       #HEAD CREDIT: LeoDeCraprio#4239

image sayori 4bz = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/z.png")      #HEAD CREDIT: SpringingTraps#5243
image sayori 4bza = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/za.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 4bzb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zb.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 4bzc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zc.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 4bzd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zd.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 4bze = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/ze.png")    #HEAD CREDIT: LeoDeCraprio#4239

#BODY CREDIT: u/NormallyAverage##########
image sayori 6a = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/a.png")
image sayori 6b = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/b.png")
image sayori 6c = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/c.png")
image sayori 6d = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/d.png")
image sayori 6e = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/e.png")
image sayori 6f = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/f.png")
image sayori 6g = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/g.png")
image sayori 6h = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/h.png")
image sayori 6i = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/i.png")
image sayori 6j = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/j.png")
image sayori 6k = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/k.png")
image sayori 6l = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/l.png")
image sayori 6m = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/m.png")
image sayori 6n = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/n.png")
image sayori 6o = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/o.png")
image sayori 6p = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/p.png")
image sayori 6q = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/q.png")
image sayori 6r = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/r.png")
image sayori 6s = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/s.png")
image sayori 6t = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/t.png")
image sayori 6u = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/u.png")
image sayori 6v = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/v.png")
image sayori 6w = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/w.png")
image sayori 6x = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/x.png")
image sayori 6y = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/y.png")
image sayori 6z = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/z.png")   #HEAD CREDIT: SpringingTraps#5243
image sayori 6za = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/za.png") #HEAD CREDIT: u/NormallyAverage
image sayori 6zb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/zb.png") #HEAD CREDIT: u/NormallyAverage
image sayori 6zc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/zc.png") #HEAD CREDIT: u/NormallyAverage
image sayori 6zd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/zd.png") #HEAD CREDIT: u/NormallyAverage
image sayori 6ze = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/ze.png") #HEAD CREDIT: LeoDeCraprio#4239
########################################

#Natsuki
image natsuki 1za = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/za.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1zb = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zb.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1zc = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zc.png")           #DDLC
image natsuki 1zd = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zd.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1ze = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/ze.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 1zf = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zf.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 1zg = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zg.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 1zh = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zh.png")           #HEAD CREDIT: u/DeliRoxeD

image natsuki 1bza = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/za.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1bzb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zb.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1bzc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zc.png")        #DDLC 
image natsuki 1bzd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zd.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1bze = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/ze.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 1bzf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zf.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 1bzg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zg.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 1bzh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zh.png")        #HEAD CREDIT: u/DeliRoxeD

image natsuki 2za = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/za.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2zb = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zb.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2zc = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zc.png")           #DDLC 
image natsuki 2zd = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zd.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2ze = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/ze.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 2zf = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zf.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 2zg = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zg.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 2zh = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zh.png")           #HEAD CREDIT: u/DeliRoxeD

image natsuki 2bza = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/za.png")         #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2bzb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zb.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2bzc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zc.png")        #DDLC 
image natsuki 2bzd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zd.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2bze = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/ze.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 2bzf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zf.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 2bzg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zg.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 2bzh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zh.png")        #HEAD CREDIT: u/DeliRoxeD

image natsuki 3za = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/za.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3zb = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zb.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3zc = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zc.png")           #DDLC 
image natsuki 3zd = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zd.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3ze = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/ze.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 3zf = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zf.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 3zg = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zg.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 3zh = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zh.png")           #HEAD CREDIT: u/DeliRoxeD

image natsuki 3bza = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/za.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3bzb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zb.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3bzc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zc.png")        #DDLC 
image natsuki 3bzd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zd.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3bze = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/ze.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 3bzf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zf.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 3bzg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zg.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 3bzh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zh.png")        #HEAD CREDIT: u/DeliRoxeD

image natsuki 4za = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/za.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4zb = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zb.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4zc = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zc.png")           #DDLC 
image natsuki 4zd = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zd.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4ze = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/ze.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 4zf = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zf.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 4zg = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zg.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 4zh = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zh.png")           #HEAD CREDIT: u/DeliRoxeD

image natsuki 4bza = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/za.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4bzb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zb.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4bzc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zc.png")        #DDLC 
image natsuki 4bzd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zd.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4bze = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/ze.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 4bzf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zf.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 4bzg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zg.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 4bzh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zh.png")        #HEAD CREDIT: u/DeliRoxeD

image natsuki 5za = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/za.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5zb = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zb.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5zc = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zc.png", (0, 0), "natsuki/3.png")            #DDLC 
image natsuki 5zd = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zd.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5ze = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/ze.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: u/DeliRoxeD
image natsuki 5zf = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zf.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: u/DeliRoxeD
image natsuki 5zg = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zg.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: u/DeliRoxeD
image natsuki 5zh = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zh.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: u/DeliRoxeD

image natsuki 5bza = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/za.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5bzb = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zb.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5bzc = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zc.png", (0, 0), "natsuki/3b.png")          #DDLC 
image natsuki 5bzd = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zd.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5bze = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/ze.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: u/DeliRoxeD
image natsuki 5bzf = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zf.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: u/DeliRoxeD
image natsuki 5bzg = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zg.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: u/DeliRoxeD
image natsuki 5bzh = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zh.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: u/DeliRoxeD


#BODY CREDIT: u/NormallyAverage##########
image natsuki 61 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/1t.png")
image natsuki 6a = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/a.png")
image natsuki 6b = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/b.png")
image natsuki 6c = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/c.png")
image natsuki 6d = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/d.png")
image natsuki 6e = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/e.png")
image natsuki 6f = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/f.png")
image natsuki 6g = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/g.png")
image natsuki 6h = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/h.png")
image natsuki 6i = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/i.png")
image natsuki 6j = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/j.png")
image natsuki 6k = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/k.png")
image natsuki 6l = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/l.png")
image natsuki 6m = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/m.png")
image natsuki 6n = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/n.png")
image natsuki 6o = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/o.png")
image natsuki 6p = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/p.png")
image natsuki 6q = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/q.png")
image natsuki 6r = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/r.png")
image natsuki 6s = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/s.png")
image natsuki 6t = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/t.png")
image natsuki 6u = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/u.png")
image natsuki 6v = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/v.png")
image natsuki 6w = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/w.png")
image natsuki 6x = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/x.png")
image natsuki 6y = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/y.png")
image natsuki 6z = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/z.png")
image natsuki 6za = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/za.png")     #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 6zb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zb.png")     #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 6zc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zc.png")     #DDLC 
image natsuki 6zd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zd.png")     #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 6ze = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/ze.png")     #HEAD CREDIT: u/DeliRoxeD
image natsuki 6zf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zf.png")     #HEAD CREDIT: u/DeliRoxeD
image natsuki 6zg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zg.png")     #HEAD CREDIT: u/DeliRoxeD
image natsuki 6zh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zh.png")     #HEAD CREDIT: u/DeliRoxeD
########################################

image natsuki 7a2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/5.png", (0, 0), "mod_assets/natsuki/a2.png")    #DDLC


# Yuri
image yuri 1x = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/x.png")         #HEAD CREDIT: u/NormallyAverage
image yuri 1y = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/y.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1z = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/z.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1za = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/za.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1zb = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zb.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1zc = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zc.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zd = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zd.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1ze = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/ze.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zf = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zf.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zg = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zg.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zh = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zh.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zi = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zi.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zj = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zj.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zk = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zk.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zl = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zl.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zm = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zm.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zn = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zn.png")       #HEAD CREDIT: yagamirai10#7046

image yuri 1y8 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y8.png")
image yuri 1y9 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y9.png")
image yuri 1y10 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y10.png")
image yuri 1y11 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y11.png")

image yuri 1bx = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/x.png")      #HEAD CREDIT: u/NormallyAverage
image yuri 1by = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/y.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1bz = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/z.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1bza = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/za.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1bzb = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zb.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1bzc = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zc.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzd = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zd.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bze = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/ze.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzf = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zf.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzg = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zg.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzh = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zh.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzi = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zi.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzj = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zj.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzk = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zk.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzl = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zl.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzm = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zm.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzn = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zn.png")    #HEAD CREDIT: yagamirai10#7046

image yuri 2x = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/x.png")         #HEAD CREDIT: u/NormallyAverage
image yuri 2y = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/y.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2z = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/z.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2za = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/za.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2zb = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zb.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2zc = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zc.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zd = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zd.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2ze = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/ze.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zf = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zf.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zg = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zg.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zh = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zh.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zi = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zi.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zj = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zj.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zk = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zk.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zl = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zl.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zm = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zm.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zn = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zn.png")       #HEAD CREDIT: yagamirai10#7046

image yuri 2y8 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y8.png")
image yuri 2y9 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y9.png")
image yuri 2y10 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y10.png")
image yuri 2y11 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y11.png")

image yuri 2bx = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/x.png")      #HEAD CREDIT: u/NormallyAverage
image yuri 2by = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/y.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2bz = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/z.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2bza = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/za.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2bzb = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zb.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2bzc = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zc.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzd = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zd.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bze = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/ze.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzf = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zf.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzg = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zg.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzh = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zh.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzi = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zi.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzj = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zj.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzk = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zk.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzl = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zl.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzm = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zm.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzn = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zn.png")    #HEAD CREDIT: yagamirai10#7046

image yuri 3x = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/x.png")         #HEAD CREDIT: u/NormallyAverage
image yuri 3y = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/y.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3z = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/z.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3za = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/za.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3zb = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zb.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3zc = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zc.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zd = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zd.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3ze = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/ze.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zf = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zf.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zg = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zg.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zh = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zh.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zi = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zi.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zj = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zj.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zk = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zk.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zl = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zl.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zm = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zm.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zn = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zn.png")       #HEAD CREDIT: yagamirai10#7046

image yuri 3y8 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y8.png")
image yuri 3y9 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y9.png")
image yuri 3y10 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y10.png")
image yuri 3y11 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y11.png")

image yuri 3bx = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/x.png")      #HEAD CREDIT: u/NormallyAverage
image yuri 3by = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/y.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3bz = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/z.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3bza = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/za.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3bzb = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zb.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3bzc = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zc.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzd = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zd.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bze = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/ze.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzf = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zf.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzg = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zg.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzh = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zh.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzi = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zi.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzj = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zj.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzk = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zk.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzl = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zl.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzm = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zm.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzn = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zn.png")    #HEAD CREDIT: yagamirai10#7046

image yuri 4f = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "mod_assets/yuri/f2.png")
image yuri 4g = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "mod_assets/yuri/g2.png")

# Monika
image monika 1s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/s.png")         #HEAD CREDIT: u/NormallyAverage
image monika 1t = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/t.png")         #HEAD CREDIT: greenbean01#6360
image monika 1u = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/u.png")         #HEAD CREDIT: greenbean01#6360
image monika 1v = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/v.png")         #HEAD CREDIT: u/NormallyAverage
image monika 1w = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/w.png")         #HEAD CREDIT: TsunKrAZy#2862
image monika 1x = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/x.png")         #HEAD CREDIT: yagamirai10#7046
image monika 1y = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/y.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 1z = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/z.png")         #HEAD CREDIT: yagamirai10#7046
image monika 1za = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/za.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 1zb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zb.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 1zc = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zc.png")       #HEAD CREDIT: u/NormallyAverage
image monika 1zd = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zd.png")       #HEAD CREDIT: yagamirai10#7046
image monika 1ze = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/ze.png")       #HEAD CREDIT: u/NormallyAverage

image monika 2s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/s.png")         #HEAD CREDIT: u/NormallyAverage
image monika 2t = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/t.png")         #HEAD CREDIT: greenbean01#6360
image monika 2u = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/u.png")         #HEAD CREDIT: greenbean01#6360
image monika 2v = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/v.png")         #HEAD CREDIT: u/NormallyAverage
image monika 2w = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/w.png")         #HEAD CREDIT: TsunKrAZy#2862
image monika 2x = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/x.png")         #HEAD CREDIT: yagamirai10#7046
image monika 2y = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/y.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 2z = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/z.png")         #HEAD CREDIT: yagamirai10#7046
image monika 2za = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/za.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 2zb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zb.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 2zc = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zc.png")       #HEAD CREDIT: u/NormallyAverage
image monika 2zd = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zd.png")       #HEAD CREDIT: yagamirai10#7046
image monika 2ze = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/ze.png")       #HEAD CREDIT: u/NormallyAverage

image monika 3s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/s.png")         #HEAD CREDIT: u/NormallyAverage
image monika 3t = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/t.png")         #HEAD CREDIT: greenbean01#6360
image monika 3u = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/u.png")         #HEAD CREDIT: greenbean01#6360
image monika 3v = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/v.png")         #HEAD CREDIT: u/NormallyAverage
image monika 3w = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/w.png")         #HEAD CREDIT: TsunKrAZy#2862
image monika 3x = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/x.png")         #HEAD CREDIT: yagamirai10#7046
image monika 3y = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/y.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 3z = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/z.png")         #HEAD CREDIT: yagamirai10#7046
image monika 3za = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/za.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 3zb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zb.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 3zc = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zc.png")       #HEAD CREDIT: u/NormallyAverage
image monika 3zd = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zd.png")       #HEAD CREDIT: yagamirai10#7046
image monika 3ze = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/ze.png")       #HEAD CREDIT: u/NormallyAverage

image monika 4s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/s.png")         #HEAD CREDIT: u/NormallyAverage
image monika 4t = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/t.png")         #HEAD CREDIT: greenbean01#6360
image monika 4u = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/u.png")         #HEAD CREDIT: greenbean01#6360
image monika 4v = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/v.png")         #HEAD CREDIT: u/NormallyAverage
image monika 4w = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/w.png")         #HEAD CREDIT: TsunKrAZy#2862
image monika 4x = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/x.png")         #HEAD CREDIT: yagamirai10#7046
image monika 4y = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/y.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 4z = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/z.png")         #HEAD CREDIT: yagamirai10#7046
image monika 4za = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/za.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 4zb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zb.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 4zc = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zc.png")       #HEAD CREDIT: u/NormallyAverage
image monika 4zd = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zd.png")       #HEAD CREDIT: yagamirai10#7046
image monika 4ze = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/ze.png")       #HEAD CREDIT: u/NormallyAverage

#BODY CREDIT: u/NormallyAverage##########
image monika 6a = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/a.png")
image monika 6b = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/b.png")
image monika 6c = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/c.png")
image monika 6d = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/d.png")
image monika 6e = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/e.png")
image monika 6f = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/f.png")
image monika 6g = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/g.png")
image monika 6h = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/h.png")
image monika 6i = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/i.png")
image monika 6j = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/j.png")
image monika 6k = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/k.png")
image monika 6l = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/l.png")
image monika 6m = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/m.png")
image monika 6n = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/n.png")
image monika 6o = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/o.png")
image monika 6p = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/p.png")
image monika 6q = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/q.png")
image monika 6r = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/r.png")
image monika 6s = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/s.png")           #HEAD CREDIT: u/NormallyAverage
image monika 6t = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/t.png")           #HEAD CREDIT: greenbean01#6360
image monika 6u = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/u.png")           #HEAD CREDIT: greenbean01#6360
image monika 6v = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/v.png")           #HEAD CREDIT: u/NormallyAverage
image monika 6w = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/w.png")           #HEAD CREDIT: TsunKrAZy#2862
image monika 6x = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/x.png")           #HEAD CREDIT: yagamirai10#7046
image monika 6y = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/y.png")           #HEAD CREDIT: JaxxHunter#3435
image monika 6z = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/z.png")           #HEAD CREDIT: yagamirai10#7046
image monika 6za = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/za.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 6zb = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/zb.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 6zc = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/zc.png")         #HEAD CREDIT: u/NormallyAverage
image monika 6zd = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/zd.png")         #HEAD CREDIT: yagamirai10#7046
image monika 6ze = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/ze.png")         #HEAD CREDIT: u/NormallyAverage
########################################