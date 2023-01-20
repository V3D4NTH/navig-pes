from tkinter import *
from PIL import ImageTk, Image
import random
i=-1
monster=''
rupees = 600  # used in store to buy items
hp = 100  # user's hp
opp_hp = 100  # monster's hp
extra_hp = 0  # extra opponent hp for boss round
chai = False  # increases attack by 20
puff = False  # increases attack by 30
mas_puri = False  # increases attack by 40
nippat = False  # increases attack by 50
bun_sam = False  # increases attack by 60
blubook = False  # decreases opp_att by 10
gonemad = False  # decreases opp_att by 20
printo = False  # decreases opp_att by 30
Uru_Armour = False  # decreases opp_att by 50
Adamantia_Armour = False  # decreases opp_att by 60
pixel = 1  # increases hp by 30. Cost=300 rupees
schezwan = 1  # increases hp by 50. Cost=600 rupees
chole = 1
# variable that lets you select the potion that you want to take.
which_potion = 0


def get_room():
    # room = ("isa1", "isa2", "isa3", "isa4", "isa5", "esa, treasure", "shop", "shop")
    # inside_room = random.choice(room)
    global i
    i+=1
    # print(inside_room)
    if i==0:
        frame1.destroy()
        isa1()
    elif i==1:
        frame1.destroy()
        isa2()
    elif i==2:
        frame1.destroy()
        isa3()
    elif i==3:
        frame1.destroy()
        isa4()
    elif i==4:
        frame1.destroy()
        isa5()
    elif i==5:
        frame1.destroy()
        esa()
    elif i==6:
        frame1.destroy()
        treasure_box()
    elif i==7:
        frame1.destroy()
        shop()
   

# treasure box room
def treasure_box():
    global rupees
    global frame_tb
    frame_tb = Frame(root)
    frame_tb.pack()
    prize = random.randint(1, 10)
    rupees = rupees + (prize * 10)
    L_TB = Label(frame_tb, text="\n\n\n\n\n It's your lucky day!\n On your way to the Pixel Food Court, you found some cash lying on the ground\n with no one else around to collect it. \n It's all yours for the taking! ( ͡° ͜ʖ ͡°) \n")
    L_TB.pack()

    prize = random.randint(1, 10)
    rupees = rupees + (prize * 10)

    L_TB_rupees = Label(
        frame_tb, text=f"Score! You just made a cool {prize*10} bucks. \n You now have {rupees} rupees.\n Looks like the BMTC bus ride back home is sorted.")
    L_TB_rupees.pack()

    B_TB = Button(frame_tb, text="Next", command=lambda: treasure_box_exit())
    B_TB .pack()


def treasure_box_exit():
    frame_tb.destroy()
    get_room()


def shop_pixel():
    global frame_shop_pixel
    frame_shop_1.destroy()
    frame_shop_pixel = Frame(root)
    frame_shop_pixel.pack()
    L_shop_pixel_1 = Label(frame_shop_pixel, text=f"You currently have {pixel} Limonatas, {schezwan} Schezwan Noodles, and {chole} Chole Bhature with you.\n"
                           f"We sell \n"
                           f"Limonata\n"
                           f"Schezwan Noodles\n"
                           f"Chole Bhature\n"
                           f"Would you like to know more about them?\n")
    L_shop_pixel_1.pack()
    B_shop_pixel_Y = Button(frame_shop_pixel, text="Yes",
                            command=lambda: shop_pixel_yes())
    B_shop_pixel_N = Button(frame_shop_pixel, text="No",
                            command=lambda: shop_pixel_no())
    B_shop_pixel_Y.pack(side=BOTTOM)
    B_shop_pixel_N.pack(side=BOTTOM)


def shop_pixel_no():
    global frame_shop_pixel_no
    frame_shop_pixel.destroy()

    frame_shop_pixel_no = Frame(root)
    frame_shop_pixel_no.pack()
    L_shop_pixel_No = Label(frame_shop_pixel_no, text="Ummm okay then..\n"
                            "What would you like to buy?")
    L_shop_pixel_No.pack()
    B_shop_pixel_No_SP = Button(
        frame_shop_pixel_no, text="Limonata", command=lambda: shop_pixels_small())
    B_shop_pixel_No_UP = Button(
        frame_shop_pixel_no, text="Schezwan Noodles", command=lambda: shop_pixels_ultra())
    B_shop_pixel_No_C = Button(
        frame_shop_pixel_no, text="Chole Bhature", command=lambda: shop_pixels_c())
    B_shop_pixel_No_UP.pack()
    B_shop_pixel_No_SP.pack()
    B_shop_pixel_No_C.pack()


def shop_pixel_yes():
    global frame_shop_pixel_yes
    frame_shop_pixel.destroy()
    frame_shop_pixel_yes = Frame(root)
    frame_shop_pixel_yes.pack()
    L_shop_pixel_Yes = Label(frame_shop_pixel_yes, text="Limonata: A unique blend of lime and a hint of mint\n"
                                                        "Cost: 15-----------------HP: +30\n"
                                                        "\n""\n""\n"
                                                        "Schezwan Noodles: One of the most famous Chinese take-out dishes. And with good reason\n"
                                                        "Cost: 30-----------------HP: +50\n"
                                                        "\n""\n""\n"
                                                        "Chole Bhature: It's not food. It's an emotion. My personal favourite\n"
                                                        "Cost: 40-----------------HP: +60")
    L_shop_pixel_Yes.pack()
    B_shop_pixel_Yes = Button(
        frame_shop_pixel_yes, text="Next", command=lambda: shop_pixel_yestono())
    B_shop_pixel_Yes.pack()


def shop_pixel_yestono():
    frame_shop_pixel_yes.destroy()
    shop_pixel_no()


def shop_pixels_small():
    global frame_shop_pixel_small
    frame_shop_pixel_no.destroy()
    frame_shop_pixel_small = Frame(root)
    frame_shop_pixel_small.pack()
    L_shop_pixel_small = Label(frame_shop_pixel_small, text="How many Limonatas would you like to buy?\n"
                               "Cost=250 rupees\n"
                               f"You have {rupees} rupees")
    L_shop_pixel_small.pack()

    B_shop_pixel_small = Button(
        frame_shop_pixel_small, text="Buy", command=lambda: shop_pixel_small_buy())
    B_shop_pixel_small.pack()
    B_shop_pixel_small_main = Button(
        frame_shop_pixel_small, text="Back", command=lambda: shop_pixels_small_to_main())
    B_shop_pixel_small_main.pack(side=BOTTOM)


def shop_pixels_small_to_main():
    frame_shop_pixel_small.destroy()
    shop()


def shop_pixel_small_buy():
    global rupees
    global pixel
    if rupees - 250 < 0:
        L_shop_pixel_small = Label(frame_shop_pixel_small, text="You don't have enough rupees.\n"
                                   "Let's shop for something else..\n")
        L_shop_pixel_small.pack()
        # If user has enough rupees
    else:
        pixel = pixel + 1
        rupees = rupees - 250
        L_shop_pixel_small = Label(frame_shop_pixel_small, text=(f"You now have {rupees} rupees with you\n"
                                                                 f"You now have {pixel} Limonatas with you\n"
                                                                 "Let's continue shopping.."))
        L_shop_pixel_small.pack()


def shop_pixels_ultra():
    global frame_shop_pixel_ultra
    frame_shop_pixel_no.destroy()
    frame_shop_pixel_ultra = Frame(root)
    frame_shop_pixel_ultra.pack()
    L_shop_pixel_ultra = Label(frame_shop_pixel_ultra, text="How many Ultra potions would you like to buy?\n"
                               "Cost=600 rupees\n"
                               f"You have {rupees} rupees")
    L_shop_pixel_ultra.pack()
    B_shop_pixel_ultra = Button(
        frame_shop_pixel_ultra, text="Buy", command=lambda: shop_pixel_ultra_buy())
    B_shop_pixel_ultra.pack()
    B_shop_pixel_ultra_main = Button(
        frame_shop_pixel_ultra, text="Back", command=lambda: shop_pixels_ultra_to_main())
    B_shop_pixel_ultra_main.pack(side=BOTTOM)


def shop_pixels_ultra_to_main():
    frame_shop_pixel_ultra.destroy()
    shop()


def shop_pixel_ultra_buy():
    global rupees
    global schezwan
    # global frame_shop_pixel_ultra_buy
    # frame_shop_pixel_ultra_buy.destroy()
    # frame_shop_pixel_ultra_buy = Frame(root)
    # frame_shop_pixel_ultra_buy.pack()
    if rupees - 600 < 0:
        L_shop_pixel_ultra = Label(frame_shop_pixel_ultra, text="You don't have enough rupees.\n"
                                   f"You have {rupees} rupees with you\n"
                                   f"You have {schezwan} Ultra Potions with you\n"
                                   "Let's shop for something else..\n")
        L_shop_pixel_ultra.pack()
        # B_shop_pixel_ultra_main = Button(frame_shop_pixel_ultra, text="Back")
        # B_shop_pixel_ultra_main.pack()
        # If user has enough rupees
    else:
        schezwan = schezwan + 1
        rupees = rupees - 600
        L_shop_pixel_ultra = Label(frame_shop_pixel_ultra, text=(f"You now have {rupees} rupees with you\n"
                                                                 f"You now have {schezwan} Ultra Potions with you\n"
                                                                 "Let's continue shopping.."))
        L_shop_pixel_ultra.pack()


def shop_pixels_c():
    global frame_shop_pixel_c
    frame_shop_pixel_no.destroy()
    frame_shop_pixel_c = Frame(root)
    frame_shop_pixel_c.pack()
    L_shop_pixel_c = Label(frame_shop_pixel_c, text="How many Chole Bhatures would you like to buy?\n"
                           "Cost=40 rupees\n"
                           f"You have {rupees} rupees")
    L_shop_pixel_c.pack()

    B_shop_pixel_c = Button(frame_shop_pixel_c, text="Buy",
                            command=lambda: shop_pixel_c_buy())
    B_shop_pixel_c.pack()
    B_shop_pixel_c_main = Button(
        frame_shop_pixel_c, text="Back", command=lambda: shop_pixels_c_to_main())
    B_shop_pixel_c_main.pack(side=BOTTOM)


def shop_pixels_c_to_main():
    frame_shop_pixel_c.destroy()
    shop()


def shop_pixel_c_buy():
    global rupees
    global chole
    if rupees - 40 < 0:
        L_shop_pixel_c = Label(frame_shop_pixel_c, text="You don't have enough rupees.\n"
                               "Let's shop for something else..\n")
        L_shop_pixel_c.pack()
        # If user has enough rupees
    else:
        chole = chole + 1
        rupees = rupees - 40
        L_shop_pixel_c = Label(frame_shop_pixel_c, text=(f"You now have {rupees} rupees with you\n"
                                                         f"You now have {chole} Chole Bhatures with you\n"
                                                         "Let's continue shopping.."))
        L_shop_pixel_c.pack()


def can():
    global frame_can
    global chai
    global puff
    global mas_puri
    global nippat
    global bun_sam
    frame_shop_1.destroy()
    frame_can = Frame(root)
    frame_can.pack()
    if chai:
        L_can_owned = Label(
            frame_can, text="Right now, you have the Chai Dagger")
        L_can_owned.pack()
    elif puff:
        L_can_owned = Label(
            frame_can, text="Right now you have a vial of Puff Corn Poison")
        L_can_owned.pack()
    elif mas_puri:
        L_can_owned = Label(
            frame_can, text="Right now you have the Masala Puri Mallet")
        L_can_owned.pack()
    elif nippat:
        L_can_owned = Label(
            frame_can, text="Right now you have the Nippat Nunchucks")
        L_can_owned.pack()
    elif bun_sam:
        L_can_owned = Label(
            frame_can, text="Right now you have the Bun Samosa BattleAxe")
        L_can_owned.pack()
    L_can_intro = Label(frame_can, text="We have 5 items..\n"
                                                      "Chai Dagger, Puff Corn Poison, Masala Puri Mallet, Nippat Nunchuks and Bun Samosa BattleAxe\n"
                                                      "Would you like to know more about them?\n")
    L_can_intro.pack()
    B_can_Y = Button(frame_can, text="Yes",
                            command=lambda: can_yes())
    B_can_N = Button(frame_can, text="No",
                            command=lambda: can_no())
    B_can_Y.pack()
    B_can_N.pack()


def can_yes():
    global frame_can_yes
    frame_can.destroy()
    frame_can_yes = Frame(root)
    frame_can_yes.pack()
    L_can_Y_info = Label(frame_can_yes, text="Chai Dagger: \n"
                                             "Cost: 200-----------Damage: 20 HP\n\n"
                                             "Puff Corn Poison: \n"
                                             "Cost: 300-----------Damage: 30 HP\n\n"
                                             "Masala Puri : \n"
                                             "Cost: 400-----------Damage: 40 HP\n"
                                             "Nippat Nunchucks: \n"    
                                             "Cost: 500-----------Damage: 50 HP\n"                            
                                             "Bun Samosa BattleAxe: \n"
                                             "Cost: 600-----------Damage: 60HP")
                                
    L_can_Y_info.pack()

    B_can_Yes = Button(
        frame_can_yes, text="Next", command=lambda: can_yestono())
    B_can_Yes.pack()


def can_yestono():
    frame_can_yes.destroy()
    can_no()


def can_no():
    global frame_cans_no
    frame_can.destroy()
    frame_cans_no = Frame(root)
    frame_cans_no.pack()
    L_cans_N = Label(frame_cans_no,
                            text="Which weapon would you like to prurchase?\n Choose wisely. These instruments will aid you in your conquest.")
    L_cans_N.pack()
    B_cans_Sword1 = Button(
        frame_cans_no, text="Chai Dagger", command=lambda: can1())
    B_cans_Sword1.pack()
    B_cans_Sword2 = Button(
        frame_cans_no, text="Puff Corn Poison", command=lambda: can2())
    B_cans_Sword2.pack()
    B_cans_Sword3 = Button(
        frame_cans_no, text="Masala Puri Mallet", command=lambda: can3())
    B_cans_Sword3.pack()
    B_cans_Sword4 = Button(
        frame_cans_no, text="Nippat Nunchuks", command=lambda: can4())
    B_cans_Sword4.pack()
    B_cans_Sword5 = Button(
        frame_cans_no, text="Bun Samosa BattleAxe", command=lambda: can5())
    B_cans_Sword5.pack()
    B_cans_back = Button(
        frame_cans_no, text="back", command=lambda: can_to_main())
    B_cans_back.pack(side=BOTTOM)


def can1():
    global chai
    global puff
    global mas_puri
    global nippat
    global bun_sam
    global rupees
    if chai == False:
        if rupees > 200:
            rupees = rupees - 200
            L_cans_sword1 = Label(frame_cans_no, text="You now have the Chai Dagger\n"
                                                                    f"You now have {rupees} rupees")
            L_cans_sword1.pack()
            chai = True
            puff = False
            mas_puri = False
            nippat = False
            bun_sam = False

        else:
            L_cans_sword1 = Label(frame_cans_no, text="You don't have enough rupees.\n"
                                                                    f"You have {rupees} rupees")
            L_cans_sword1.pack()
    else:
        L_cans_sword1 = Label(
            frame_cans_no, text="You already have the Chai Dagger.")
        L_cans_sword1.pack()


def can2():
    global chai
    global puff
    global mas_puri
    global nippat
    global bun_sam
    global rupees
    if puff == False:
        if rupees > 300:
            rupees = rupees - 300
            L_cans_sword2 = Label(frame_cans_no, text="You now have a vial of Puff Corn Poison\n"
                                                                    f"You now have {rupees} rupees")
            L_cans_sword2.pack()
            chai = False
            puff = True
            mas_puri = False

        else:
            L_cans_sword2 = Label(frame_cans_no, text="You don't have enough rupees.\n"
                                                                    f"You have {rupees} rupees")
            L_cans_sword2.pack()
    else:
        L_cans_sword2 = Label(
            frame_cans_no, text="You already have Puff Corn Poison")
        L_cans_sword2.pack()


def can3():
    global chai
    global puff
    global mas_puri
    global nippat
    global bun_sam
    global rupees
    if mas_puri == False:
        if rupees > 400:
            rupees = rupees - 400
            L_cans_sword3 = Label(frame_cans_no, text="You now have the Masala Puri Mallet\n"
                                                                    f"You now have {rupees} rupees")
            L_cans_sword3.pack()
            chai = False
            puff = False
            mas_puri = True

        else:
            L_cans_sword3 = Label(frame_cans_no, text="You don't have enough rupees.\n"
                                                                    f"You have {rupees} rupees")
            L_cans_sword3.pack()
    else:
        L_cans_sword3 = Label(
            frame_cans_no, text="You already have the Masala Puri Mallet")
        L_cans_sword3.pack()


def can4():
    global chai
    global puff
    global mas_puri
    global nippat
    global bun_sam
    global rupees
    if nippat == False:
        if rupees > 500:
            rupees = rupees - 500
            L_cans_sword4 = Label(frame_cans_no, text="You now have the Nippat Nunchucks.\n"
                                                                    f"You now have {rupees} rupees")
            L_cans_sword4.pack()
            chai = False
            puff = False
            mas_puri = False
            nippat = True
            bun_sam = False

        else:
            L_cans_sword4 = Label(frame_cans_no, text="You don't have enough rupees.\n"
                                                                    f"You have {rupees} rupees")
            L_cans_sword4.pack()
    else:
        L_cans_sword4 = Label(
            frame_cans_no, text="You already have the Nippat Nunchucks.")
        L_cans_sword4.pack()


def can5():
    global chai
    global puff
    global mas_puri
    global nippat
    global bun_sam
    global rupees
    if bun_sam == False:
        if rupees > 600:
            rupees = rupees - 600
            L_cans_sword5 = Label(frame_cans_no, text="You now have the Bun Samosa BattleAxe\n"
                                                                    f"You now have {rupees} rupees")
            L_cans_sword5.pack()
            chai = False
            puff = False
            mas_puri = False
            nippat = False
            bun_sam = True

        else:
            L_cans_sword5 = Label(frame_cans_no, text="You don't have enough rupees.\n"
                                                                    f"You have {rupees} rupees")
            L_cans_sword5.pack()
    else:
        L_cans_sword5 = Label(
            frame_cans_no, text="You already have the Bun Samosa BattleAxe.")
        L_cans_sword5.pack()


def can_to_main():
    frame_cans_no.destroy()
    shop()


def stat():
    global frame_stat
    global blubook
    global gonemad
    global printo
    global Uru_Armour
    global Adamantia_Armour
    frame_shop_1.destroy()
    frame_stat = Frame(root)
    frame_stat.pack()
    if blubook:
        L_stat_owned = Label(
            frame_stat, text="Right now, you have the Book of Blue")
        L_stat_owned.pack()
    elif gonemad:
        L_stat_owned = Label(
            frame_stat, text="Right now you have the Gone Mad Armour")
        L_stat_owned.pack()
    elif printo:
        L_stat_owned = Label(
            frame_stat, text="Right now you have the Prinout Power Armour")
        L_stat_owned.pack()
  
    L_stat_intro = Label(frame_stat, text="Rations! Get your rations!\n We have 3 types of armors..\n"
                                                      "The Book of Blue, the Gone Mad Armour, and the Prinout Power Armour\n"
                                                      "Would you like to know more about them?\n")
    L_stat_intro.pack()
    B_stat_Y = Button(frame_stat, text="Yes",
                            command=lambda: stat_yes())
    B_stat_N = Button(frame_stat, text="No",
                            command=lambda: stat_no())
    B_stat_Y.pack()
    B_stat_N.pack()


def stat_yes():
    global frame_stat_yes
    frame_stat.destroy()
    frame_stat_yes = Frame(root)
    frame_stat_yes.pack()
    L_stat_Y_info = Label(frame_stat_yes, text="The Book of Blue costs 200 rupees and increases your attack by 20\n"
                                "Gone Mad Armour costs 300 rupees and increases your attack by 30\n"
                                "The Printout Power Armour costs 400 rupees and increases your attack by 40\n"
                               )
    L_stat_Y_info.pack()

    B_stat_Yes = Button(
        frame_stat_yes, text="Next", command=lambda: stat_yestono())
    B_stat_Yes.pack()


def stat_yestono():
    frame_stat_yes.destroy()
    stat_no()


def stat_no():
    global frame_stats_no
    frame_stat.destroy()
    frame_stats_no = Frame(root)
    frame_stats_no.pack()
    L_stats_N = Label(frame_stats_no,
                            text="What would you like to buy?\n")
    L_stats_N.pack()
    B_stats_armor1 = Button(
        frame_stats_no, text="The Book of Blue", command=lambda: stat_armor1())
    B_stats_armor1.pack()
    B_stats_armor2 = Button(
        frame_stats_no, text="The Gone Mad Armour", command=lambda: stat_armor2())
    B_stats_armor2.pack()
    B_stats_armor3 = Button(
        frame_stats_no, text="The Printout Power Armour", command=lambda: stat_armor3())
    B_stats_armor3.pack()
   
    B_stats_back = Button(
        frame_stats_no, text="back", command=lambda: stat_to_main())
    B_stats_back.pack(side=BOTTOM)


def stat_armor1():
    global blubook
    global gonemad
    global printo
    global Uru_Armour
    global Adamantia_Armour
    global rupees
    if blubook == False:
        if rupees > 200:
            rupees = rupees - 200
            L_stats_armor1 = Label(frame_stats_no, text="You now have the Blue of Book\n"
                                                                    f"You now have {rupees} rupees")
            L_stats_armor1.pack()
            blubook = True
            gonemad = False
            printo = False
            Uru_Armour = False
            Adamantia_Armour = False

        else:
            L_stats_armor1 = Label(frame_stats_no, text="You don't have enough rupees.\n"
                                                                    f"You have {rupees} rupees")
            L_stats_armor1.pack()
    else:
        L_stats_armor1 = Label(
            frame_stats_no, text="You're a greedy fellow. You already have the Book of Blue.")
        L_stats_armor1.pack()


def stat_armor2():
    global blubook
    global gonemad
    global printo
    global Uru_Armour
    global Adamantia_Armour
    global rupees
    if gonemad == False:
        if rupees > 300:
            rupees = rupees - 300
            L_stats_armor2 = Label(frame_stats_no, text="You now have the Gone Mad Armour\n"
                                                                    f"You now have {rupees} rupees")
            L_stats_armor2.pack()
            blubook = False
            gonemad = True
            printo = False
            Uru_Armour = False
            Adamantia_Armour = False

        else:
            L_stats_armor2 = Label(frame_stats_no, text="You don't have enough rupees.\n"
                                                                    f"You have {rupees} rupees")
            L_stats_armor2.pack()
    else:
        L_stats_armor2 = Label(
            frame_stats_no, text="You already have the Gone Mad Armour. But I get it. It's so nice you want it twice.")
        L_stats_armor2.pack()


def stat_armor3():
    global blubook
    global gonemad
    global printo
    global Uru_Armour
    global Adamantia_Armour
    global rupees
    if printo == False:
        if rupees > 400:
            rupees = rupees - 400
            L_stats_armor3 = Label(frame_stats_no, text="You now have the Printout Power Armour.\n"
                                                                    f"You now have {rupees} rupees")
            L_stats_armor3.pack()
            blubook = False
            gonemad = False
            printo = True
            Uru_Armour = False
            Adamantia_Armour = False

        else:
            L_stats_armor3 = Label(frame_stats_no, text="You don't have enough rupees.\n"
                                                                    f"You have {rupees} rupees")
            L_stats_armor3.pack()
    else:
        L_stats_armor3 = Label(
            frame_stats_no, text="What, you egg! Nothing can stab you\n because you already have the Prinout Power Armour")
        L_stats_armor3.pack()



def stat_to_main():
    frame_stats_no.destroy()
    shop()


def shop_exit():
    # L_shop_exit = Label(frame_shop_1, text="Leaving shop...")
    # L_shop_exit.pack()
    # time.sleep(2)
    frame_shop_1.destroy()
    get_room()


def shop():
    global rupees
    global chai
    global puff
    global mas_puri
    global nippat
    global bun_sam
    global blubook
    global gonemad
    global printo
    global Uru_Armour
    global Adamantia_Armour
    global pixel
    global schezwan
    global frame_shop_1
    frame_shop_1 = Frame(root)
    frame_shop_1.pack()
    L_Shop_Wel = Label(
        frame_shop_1, text="Ah, break time...\nWhere would you like to go to replenish your inventory today?\n")
    L_Shop_Wel.pack()
    # store1 variable to ask user what necessity do they need to buy
    # store1 = input("1=Potion, 2=Sword, 3=Armor, 4=Exit Store\n")
    B_shop_pixel = Button(
        frame_shop_1, text="Pixel's Food and Ale ", command=lambda: shop_pixel())
    B_shop_pixel.pack()
    B_can = Button(frame_shop_1, text="Armoury of the 4th and 5th",
                          command=lambda: can())
    B_can.pack()
    B_stat = Button(frame_shop_1, text="Stationary Bazaar",
                          command=lambda: stat())
    B_stat.pack()
    B_Shop_ExitStore = Button(
        frame_shop_1, text="Exit Store", command=lambda: shop_exit())
    B_Shop_ExitStore.pack()
    # if invalid input..

    # If user wants to buy potions

    # If user wants to buy swords

    # # If user wants to exit the store.
    # if int(store1) == 4:
    #     typing("Leaving the store..")


def monster_potion_1():
    global frame_monster_potion_1
    frame_monster_potion_1 = Frame(root)
    frame_monster_potion_1.pack()
    L_monster_potion_info = Label(frame_monster_potion_1, text=f"Limonata increases your HP by 30\n"
                                  f"Schezwan Noodles increases your HP by 50\n"
                                  f"And..\n"
                                  f"Chole Bhature increases your HP by 60\n"
                                  f"Your HP is {hp}\n"
                                  f"You have {pixel} Limonatas,\n "
                                  f" {schezwan} Schezwan Noodles\n"
                                  f"And {chole} Chole Bhature\n"
                                  "What would you like to use?\n")
    L_monster_potion_info.pack()
    B_monster_potion_lime = Button(
        frame_monster_potion_1, text="Limonata", command=lambda: monster_potion_1_lime())
    B_monster_potion_schezwan = Button(
        frame_monster_potion_1, text="Schezwan Noodles", command=lambda: monster_potion_1_schezwan())
    B_monster_potion_chole = Button(
        frame_monster_potion_1, text="Chole Bhature", command=lambda: monster_potion_1_chole())
    B_monster_potion_lime.pack()
    B_monster_potion_schezwan.pack()
    B_monster_potion_chole.pack()
    B_monster_potion_back = Button(
        frame_monster_potion_1, text="Back to the battle-->", command=lambda: monster_potion_to_attack())
    B_monster_potion_back.pack()


def monster_potion_to_attack():
    frame_monster_potion_1.destroy()
    fight_monster()


def monster_potion_1_lime():
    global pixel
    global hp
    if pixel == 0:
        L_monster_potion_1_small = Label(
            frame_monster_potion_1, text="You have no more Limonata")
        L_monster_potion_1_small.pack()
    else:
        pixel = pixel - 1
        hp = hp + 30
        if hp > 100:
            hp = 100
        L_monster_potion_1_small = Label(frame_monster_potion_1, text=f"You HP is now {hp}\n"
                                                                      f"You have {pixel} Limonata remaining")
        L_monster_potion_1_small.pack()


def monster_potion_1_schezwan():
    global schezwan
    global hp
    if schezwan == 0:
        L_monster_potion_1_schezwan = Label(
            frame_monster_potion_1, text="You have no Schezwan Noodles")
        L_monster_potion_1_schezwan.pack()
    else:
        schezwan = schezwan - 1
        hp = hp + 50
        if hp > 100:
            hp = 100
        L_monster_potion_1_schezwan = Label(frame_monster_potion_1, text=f"You HP is now {hp}\n"
                                            f"You have {schezwan} Schezwan Noodles remaining")
        L_monster_potion_1_schezwan.pack()


def monster_potion_1_chole():
    global chole
    global hp
    if chole == 0:
        L_monster_potion_1_chole = Label(
            frame_monster_potion_1, text="You have no Chole Bhature")
        L_monster_potion_1_chole.pack()
    else:
        chole = chole - 1
        hp = hp + 60
        if hp > 100:
            hp = 100
        L_monster_potion_1_chole = Label(frame_monster_potion_1, text=f"You HP is now {hp}\n"
                                                                      f"You have {chole} Chole Bhature remaining")
        L_monster_potion_1_chole.pack()


def you_died():
    global monster
    frame_you_died = Frame(root)
    frame_you_died.pack()
    L_You_Died = Label(frame_monster_attack_1, text=f"Wow! Absolutely stellar. After your abysmal performance at {monster}, \nyou now have backlog hanging over your head.\nYou have enough to extend your stay at PES for the semester by a few weeks.\n Who knew you loved the university enough to flunk your exams! \n"
                                                    f"You will not be able to complete this semster in time.\n Thus, you are deemed unworthy to continue this awesome game\n made by Vedanth, Udit and Rithvik..\n"
                                                    f"Now click that quit button before we throw up in our mouths.")
    L_You_Died.pack()
    B_You_died = Button(frame_monster_attack_1,
                        text="Quit", command=lambda: quit())
    B_You_died.pack()


def quit():
    global quit_frame
    quit_frame = Frame(root)
    quit_frame.pack()
    quit_frame.place(anchor='center', relx=0.5, rely=0.5)
    img = ImageTk.PhotoImage(Image.open('supebatsy.jpg'))
    label = Label(quit_frame, image=img)
    label.image = img
    label.pack()
    label2 = Label(quit_frame, text="Thanks for playing :D")
    label2.pack()


def monster_counterattack_1():
    global monster
    global hp
    L_monster_counterattack_1 = Label(
        frame_monster_attack_1, text=f"Now {monster} will take it's turn.\n")
    L_monster_counterattack_1.pack()
    opp_attack = random.randint(((m - 1) * 10), (m * 10))
    hp = hp - opp_attack

    if blubook == True:
        hp = hp + 0
    elif gonemad == True:
        hp = hp + 0
    elif printo == True:
        hp = hp + 0
 
    if hp < 0:
        hp = 0
        L_monster_counterattack_result = Label(
            frame_monster_attack_1, text=f"Your HP={hp}\n")
        L_monster_counterattack_result.pack()
        you_died()
    else:
        L_monster_counterattack_result = Label(
            frame_monster_attack_1, text=f"Your HP={hp}\n")
        L_monster_counterattack_result.pack()
        B_monster_attack_2 = Button(
            frame_monster_attack_1, text="Attack", command=lambda: monster_counter_to_attack())
        B_monster_potion_2 = Button(
            frame_monster_attack_1, text="Potion", command=lambda: monster_counter_to_potion())
        B_monster_attack_2.pack()
        B_monster_potion_2.pack()


def monster_counter_to_potion():
    frame_monster_attack_1.destroy()
    monster_potion_1()


def monster_counter_to_attack():
    frame_monster_attack_1.destroy()
    monster_attack_1()


def monster_attack_1():
    global opp_hp
    global monster
    global frame_monster_attack_1
    frame_monster_1.destroy()
    frame_monster_attack_1 = Frame(root)
    frame_monster_attack_1.pack()
    L_monster_attack_1 = Label(
        frame_monster_attack_1, text="You chose to attack.\n")
    L_monster_attack_1.pack()
    userattack = random.randint(40, 70)
    opp_hp = opp_hp - userattack
    if chai == True:
        opp_hp = opp_hp - 20

    elif puff == True:
        opp_hp = opp_hp - 30

    elif mas_puri == True:
        opp_hp = opp_hp - 40

    elif nippat == True:
        opp_hp = opp_hp - 50

    elif bun_sam == True:
        opp_hp = opp_hp - 60

    if opp_hp > 0:
        L_monster_attack_result = Label(
            frame_monster_attack_1, text=f"{monster}'s HP={opp_hp}\n")
        L_monster_attack_result.pack()
        monster_counterattack_1()

    if opp_hp <= 0:
        opp_hp = 0
        L_monster_attack_result = Label(frame_monster_attack_1, text=f"{monster}'s HP={opp_hp}\n"
                                                                     f"Your HP = {hp}\n"
                                                                     f"you defeated {monster}\n"
                                                                     "You have some time to rest.\n"
                                                                     "Would you like to use eat or drink something?\n")
        L_monster_attack_result.pack()
        B__monster_attack_result_yes = Button(
            frame_monster_attack_1, text="Yes", command=lambda: drink_potion())
        B__monster_attack_result_no = Button(
            frame_monster_attack_1, text="No", command=lambda: monster_rest_no_to_room())
        B__monster_attack_result_yes.pack()
        B__monster_attack_result_no.pack()


def monster_rest_no_to_room():
    frame_monster_attack_1.destroy()
    get_room()


def monster_rest_to_room():
    frame_monster_potion_1.destroy()
    get_room()


def drink_potion():
    global frame_monster_potion_1
    frame_monster_attack_1.destroy()
    frame_monster_potion_1 = Frame(root)
    frame_monster_potion_1.pack()
    L_monster_potion_info = Label(frame_monster_potion_1, text=f"Limonata increases your HP by 30\n"
                                  f"Schezwan Noodles increases your HP by 50\n"
                                  f"Chole Bhature increases your HP by 60\n"
                                  f"Your HP is {hp}\n"
                                  f"You have {pixel} Limonatas,\n"
                                  f"{schezwan} Schezwan Noodles,\n"
                                  f" and {chole} Chole Bhatures"
                                  "What would you like to use?\n")
    L_monster_potion_info.pack()
    B_monster_potion_lime = Button(
        frame_monster_potion_1, text="Limonata", command=lambda: monster_potion_1_lime())
    B_monster_potion_schezwan = Button(
        frame_monster_potion_1, text="Schezwan Noodles", command=lambda: monster_potion_1_schezwan())
    B_monster_potion_chole = Button(
        frame_monster_potion_1, text="Chole Bhature", command=lambda: monster_potion_1_chole())
    B_monster_potion_lime.pack()
    B_monster_potion_schezwan.pack()
    B_monster_potion_chole.pack()
    B_next_room = Button(frame_monster_potion_1, text="Next",
                         command=lambda: monster_rest_to_room())
    B_next_room.pack()


def fight_monster_to_monster_attack():
    frame_fight_monster.destroy()
    monster_attack_1()


def fight_monster_to_monster_potion():
    frame_fight_monster.destroy()
    frame_monster_1.destroy()
    monster_potion_1()


def fight_monster():
    global opp_hp
    global monster
    global hp
    global frame_fight_monster
    frame_fight_monster = Frame(root)
    frame_fight_monster.pack()
    L_monster_intro = Label(frame_fight_monster, text=f"Your HP = {hp}\n"
                                                      f"{monster}'s HP = {opp_hp}\n"
                                                      "Would you like to attack or use potion??\n")
    L_monster_intro.pack()
    B_monster_attack_1 = Button(
        frame_fight_monster, text="Attack", command=lambda: fight_monster_to_monster_attack())
    B_monster_potion_1 = Button(
        frame_fight_monster, text="Potion", command=lambda: fight_monster_to_monster_potion())
    B_monster_attack_1.pack()
    B_monster_potion_1.pack()


def isa1():
    global m
    global monster
    global opp_hp
    monster="ISA 1"
    global frame_monster_1
    frame_monster_1 = Frame(root)
    frame_monster_1.pack()
    L_monster_Wel = Label(
        frame_monster_1, text="Grab your ID card! Don't forget your calculator!\n And even more importantly, don't forget to take off the calc cover.\n It's that time again. It's ISA time!")
    L_monster_Wel.pack()
   
    opp_hp = 100
    if monster == "ISA 1":
      m = 1
        # monster 1
        # Attack in range of 0-10
      L_m1_intro = Label(frame_monster_1, text="You have to face ISA 1.\n Ah, the first. You always remember your first.\n ISA, I mean! You always remember your first ISA. \n That's obviously what I meant."
                                                 "You've made your way to the Mech Block. Sat at your terminal.\n The test has started! Good luck!")
      L_m1_intro.pack()
      fight_monster()

        # opp_att = random.randint(0, 10)

def isa2():
    global m
    global opp_hp
    global monster
    monster= "ISA 2"
    global frame_monster_1
    frame_monster_1 = Frame(root)
    frame_monster_1.pack()
    L_monster_Wel = Label(
        frame_monster_1, text="Grab your ID card! Don't forget your calculator!\n And even more importantly, don't forget to take off the calc cover.\n It's that time again. It's ISA time!")
    L_monster_Wel.pack()
    opp_hp = 100
    if monster == "ISA 2":
      m = 2
        # monster 2
        # Attack in range of 10-20
      L_m2_intro = Label(frame_monster_1, text="You have to face ISA 2\n"
                                                 "The match starts. You get the first chance\n")
      L_m2_intro.pack()
      fight_monster()
        # opp_att = random.randint(10, 20)

def isa3():
    global m
    global opp_hp
    global monster
    monster= "ISA 3"
    global frame_monster_1
    frame_monster_1 = Frame(root)
    frame_monster_1.pack()
    L_monster_Wel = Label(
        frame_monster_1, text="Grab your ID card! Don't forget your calculator!\n And even more importantly, don't forget to take off the calc cover.\n It's that time again. It's ISA time!")
    L_monster_Wel.pack()
   
    opp_hp = 100
    if monster == "ISA 3":
        m = 3
        # monster 3
        # Attack in range of 20-30
        L_m3_intro = Label(frame_monster_1, text="You have to face ISA 3\n"
                                                 "The match starts. You get the first chance\n")
        L_m3_intro.pack()
        fight_monster()
        # opp_att = random.randint(20, 30)
def isa4():
    global m
    global opp_hp
    global monster
    monster= "ISA 4"
    global frame_monster_1
    frame_monster_1 = Frame(root)
    frame_monster_1.pack()
    L_monster_Wel = Label(
        frame_monster_1, text="Grab your ID card! Don't forget your calculator!\n And even more importantly, don't forget to take off the calc cover.\n It's that time again. It's ISA time!")
    L_monster_Wel.pack()
   
    opp_hp = 100
    if monster == "ISA 4":
        m = 4
        # monster 4
        # Attack in range of 30-40
        L_m4_intro = Label(frame_monster_1, text="You have to face ISA 4\n"
                                                 "The match starts. You get the first chance\n")
        L_m4_intro.pack()
        fight_monster()
        # opp_att = random.randint(30, 40)
def isa5():
    global m
    global opp_hp
    global monster
    monster= "ISA 5"
    global frame_monster_1
    frame_monster_1 = Frame(root)
    frame_monster_1.pack()
    L_monster_Wel = Label(
        frame_monster_1, text="Grab your ID card! Don't forget your calculator!\n And even more importantly, don't forget to take off the calc cover.\n It's that time again. It's ISA time!")
    L_monster_Wel.pack()
   
    opp_hp = 100
    if monster == "ISA 5":
        m = 5
        # monster 5
        # Attack in range of 40-50
        L_m5_intro = Label(frame_monster_1, text="You have to face ISA 5\n"
                                                 "The match starts. You get the first chance\n")
        L_m5_intro.pack()
        fight_monster()
        # opp_att = random.randint(40, 50)
def esa():
    global m
    global opp_hp
    global monster
    monster= "ESA"
    global frame_monster_1
    frame_monster_1 = Frame(root)
    frame_monster_1.pack()
    L_monster_Wel = Label(
        frame_monster_1, text="Grab your ID card! Don't forget your calculator!\n And even more importantly, don't forget to take off the calc cover.\n It's that time again. It's ISA time!")
    L_monster_Wel.pack()
   
    opp_hp = 100
    if monster == "ESA":
        m = 6
        # monster 6
        # Attack in range of 50-60
        L_m6_intro = Label(frame_monster_1, text="You have to face the ESA.\n"
                                                 "The match starts. You get the first chance\n")
        L_m6_intro.pack()
        fight_monster()
        # opp_att = random.randint(50, 60)


def gate():
    global frame_gate
    frame1.destroy()
    frame_gate = Frame(root)
    frame_gate.pack()
    L_gate = Label(frame_gate, text="\n\n\n\n\n As you make your way to the entrance of the main block, \n you hear cries that have a tone of urgency and persuasion. \n 'ID CARD HAKOLI! ID CARD HAKOLI! '\n They seem to be coming from an older gentleman in a sky blue attire. \n Standing beside the apparent quinquagenarian are \ntwo even larger men guarding the entrance like sentinels. \n Gargantuan in physique, they execute their job with extreme proficiency,\n grabbing a hold of anyone who tries to enter the block without their ID card.\n Phew! Thank God you got yours! \n ")
    L_gate.pack()

    B_gate = Button(frame_gate, text="Next", command=lambda: gate_exit())
    B_gate.pack()


def gate_exit():
    frame_gate.destroy()
    get_room()


root = Tk()
root.title("Navigating PES")
frame1 = Frame(root, padx=1, pady=1)
frame1.pack(padx=10, pady=10)

root.geometry("500x500")
label = Label(frame1, text="\n\n\n\n\n\nWelcome to PESUECC!\n Students have walked through its hallowed gates in pursuit of\n knowledge since 2005.This knowledge comes at a price!\n You must face the 5 ISAs.\n Each increasing in difficulty, the ISAs will be a test of your mental endurance.\n After conquering the ISAs, your journey does not end. Finally, there is the ESA.\n A 3 hour written test, combining everything you've learnt over the semester,\n vanquishing it is a result of all your learnings from your professors.\n The road that lies ahead of you is long and hard.\n To begin, let's make our way to the main block.\n ")
label.pack()

welcome_button = Button(
    frame1, text='Go to the main block-->', command=lambda: gate())
welcome_button.pack()

root.mainloop()
