import tkinter
import time
import random

go_through = True
down = True
down_check = True
left_check = True
right_check = True
game_over = False
garb_time = 2 * (time.time())
lower_time = time.time()
garbage = []
total_lines = 0
pieces = ["o", "i", "z", "s", "l", "j", "t"]
window = tkinter.Tk()
window.geometry("350x525")
program_done = False
drop_check = True
time_check = 0
charb_time = 0
count_lazy = 0
level = 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#controls the upwards rotation of tetriminos WITH KEYPRESS
def move_up():
    global side_up1, side_down1, side_up2, side_down2
    global side_up3, side_down3, side_up4, side_down4

    side_up1 -= 25
    side_down1 -= 25

    side_up2 -= 25
    side_down2 -= 25

    side_up3 -= 25
    side_down3 -= 25

    side_up4 -= 25
    side_down4 -= 25

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#controls the right movement of tetriminos
def move_right(event = " "):
    global side_left1, side_right1, side_left2, side_right2
    global side_left3, side_right3, side_left4, side_right4, right

    if side_right1 < 250 and side_right2 < 250 and side_right3 < 250 and side_right4 < 250 and right:
        side_left1 += 25
        side_right1 += 25

        side_left2 += 25
        side_right2 += 25

        side_left3 += 25
        side_right3 += 25

        side_left4 += 25
        side_right4 += 25

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#controls the left movement of tetriminos
def move_left(event = " "):
    global side_left1, side_right1, side_left2, side_right2
    global side_left3, side_right3, side_left4, side_right4, left
    if side_left1 > 0 and side_left2 > 0 and side_left3 > 0 and side_left4 > 0 and left:
        side_left1 -= 25
        side_right1 -= 25

        side_left2 -= 25
        side_right2 -= 25

        side_left3 -= 25
        side_right3 -= 25

        side_left4 -= 25
        side_right4 -= 25

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#controls the down movement of tetriminos
def move_down(event = " "):
    global side_up1, side_down1, side_up2, side_down2
    global side_up3, side_down3, side_up4, side_down4, down
    for x in garbage:
        if side_down1 == x[0] and side_left1 == x[2]:
            down = False
        elif side_down2 == x[0] and side_left2 == x[2]:
            down = False
        elif side_down3 == x[0] and side_left3 == x[2]:
            down = False
        elif side_down4 == x[0] and side_left4 == x[2]:
            down = False
    if side_down1 < 525 and side_down2 < 525 and side_down3 < 525 and side_down4 < 525 and down:
        side_up1 += 25
        side_down1 += 25

        side_up2 += 25
        side_down2 += 25

        side_up3+= 25
        side_down3 += 25

        side_up4 += 25
        side_down4 += 25
    down = True


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#controls the rotation of tetriminos
def rotate(event = " "):
    global side_down1, side_up1, side_left1, side_right1
    global side_down2, side_up2, side_left2, side_right2
    global side_down3, side_up3, side_left3, side_right3
    global side_down4, side_up4, side_left4, side_right4
    global cure_piece, garbage
    blocks1 = [side_up1, side_down1, side_left1, side_right1, piece_colour]
    blocks2 = [side_up2, side_down2, side_left2, side_right2, piece_colour]
    blocks3 = [side_up3, side_down3, side_left3, side_right3, piece_colour]
    blocks4 = [side_up4, side_down4, side_left4, side_right4, piece_colour]
    norm_state = []
    norm_state.append(blocks1)
    norm_state.append(blocks2)
    norm_state.append(blocks3)
    norm_state.append(blocks4)
    if cure_piece != "square":
        #block 1 being rotated from 1 left
        if side_right1 == side_left2 and side_up2 == side_up1:
            side_left1 += 25
            side_right1 += 25
            side_up1 -= 25
            side_down1 -= 25
        #block being rotated from 2 left
        elif side_left2 > side_right1 and side_up2 == side_up1:
            side_left1 += 50
            side_right1 += 50
            side_up1 -= 50
            side_down1 -= 50
        #block being rotated from top left
        elif side_left2 == side_right1 and side_up2 == side_down1:
            side_left1 += 50
            side_right1 += 50
        #block being rotated from up
        elif side_left2 == side_left1 and side_up2 == side_down1:
            side_left1 += 25
            side_right1 += 25
            side_up1 += 25
            side_down1 += 25
        #block being rotated from 2 up
        elif side_left2 == side_left1 and side_up2 > side_down1:
            side_left1 += 50
            side_right1 += 50
            side_up1 += 50
            side_down1 += 50
        #block being rotated from top right corner
        elif side_down1 == side_up2 and side_left1 == side_right2:
            side_up1 += 50
            side_down1 += 50
        #block being rotated from right
        elif side_up2 == side_up1 and side_right2 == side_left1:
            side_left1 -=25
            side_right1 -= 25
            side_up1 += 25
            side_down1 += 25
        #block being rotated from 2 right
        elif side_up1 == side_up2 and side_right2 < side_left1:
            side_left1 -= 50
            side_right1 -= 50
            side_up1 += 50
            side_down1 += 50
        #block being rotated from bottom right
        elif side_up1 == side_down2 and side_right2 == side_left1:
            side_left1 -= 50
            side_right1 -= 50
        #block being rotated from bottom
        elif side_up1 == side_down2 and side_left2 == side_left1:
            side_left1 -= 25
            side_right1 -= 25
            side_up1 -= 25
            side_down1 -= 25
        #rotate from bottom 2
        elif side_up1 > side_down2 and side_left2 == side_left1:
            side_left1 -= 50
            side_right1 -= 50
            side_up1 -= 50
            side_down1 -= 50
        #rotate from bottom left
        elif side_up1 == side_down2 and side_left2 == side_right1:
            side_up1 -= 50
            side_bottom1 -= 50


        #block 1 being rotated from 1 left
        if side_right3 == side_left2 and side_up2 == side_up3:
            side_left3 += 25
            side_right3 += 25
            side_up3 -= 25
            side_down3 -= 25
        #block being rotated from 2 left
        elif side_left2 > side_right3 and side_up2 == side_up3:
            side_left3 += 50
            side_right3 += 50
            side_up3 -= 50
            side_down3 -= 50
        #block being rotated from top left
        elif side_left2 == side_right3 and side_up2 == side_down3:
            side_left3 += 50
            side_right3 += 50
        #block being rotated from up
        elif side_left2 == side_left3 and side_up2 == side_down3:
            side_left3 += 25
            side_right3 += 25
            side_up3 += 25
            side_down3 += 25
        #block being rotated from 2 up
        elif side_left2 == side_left3 and side_up2 > side_down3:
            side_left3 += 50
            side_right3 += 50
            side_up3 += 50
            side_down3 += 50
        #block being rotated from top right corner
        elif side_down3 == side_up2 and side_left3 == side_right2:
            side_up3 += 50
            side_down3 += 50
        #block being rotated from right
        elif side_up2 == side_up3 and side_right2 == side_left3:
            side_left3 -=25
            side_right3 -= 25
            side_up3 += 25
            side_down3 += 25
        #block being rotated from 2 right
        elif side_up3 == side_up2 and side_right2 < side_left3:
            side_left3 -= 50
            side_right3 -= 50
            side_up3 += 50
            side_down3 += 50
        #block being rotated from bottom right
        elif side_up3 == side_down2 and side_right2 == side_left3:
            side_left3 -= 50
            side_right3 -= 50
        #block being rotated from bottom
        elif side_up3 == side_down2 and side_left2 == side_left3:
            side_left3 -= 25
            side_right3 -= 25
            side_up3 -= 25
            side_down3 -= 25
        #rotate from bottom 2
        elif side_up3 > side_down2 and side_left2 == side_left3:
            side_left3 -= 50
            side_right3 -= 50
            side_up3 -= 50
            side_down3 -= 50
        #rotate from bottom left
        elif side_up3 == side_down2 and side_left2 == side_right3:
            side_up3 -= 50
            side_down3 -= 50


        #block 1 being rotated from 1 left
        if side_right4 == side_left2 and side_up2 == side_up4:
            side_left4 += 25
            side_right4 += 25
            side_up4 -= 25
            side_down4 -= 25
        #block being rotated from 2 left
        elif side_left2 > side_right4 and side_up2 == side_up4:
            side_left4 += 50
            side_right4 += 50
            side_up4 -= 50
            side_down4 -= 50
        #block being rotated from top left
        elif side_left2 == side_right4 and side_up2 == side_down4:
            side_left4 += 50
            side_right4 += 50
        #block being rotated from up
        elif side_left2 == side_left4 and side_up2 == side_down4:
            side_left4 += 25
            side_right4 += 25
            side_up4 += 25
            side_down4 += 25
        #block being rotated from 2 up
        elif side_left2 == side_left4 and side_up2 > side_down4:
            side_left4 += 50
            side_right4 += 50
            side_up4 += 50
            side_down4 += 50
        #block being rotated from top right corner
        elif side_down4 == side_up2 and side_left4 == side_right2:
            side_up4 += 50
            side_down4 += 50
        #block being rotated from right
        elif side_up2 == side_up4 and side_right2 == side_left4:
            side_left4 -=25
            side_right4 -= 25
            side_up4 += 25
            side_down4 += 25
        #block being rotated from 2 right
        elif side_up4 == side_up2 and side_right2 < side_left4:
            side_left4 -= 50
            side_right4 -= 50
            side_up4 += 50
            side_down4 += 50
        #block being rotated from bottom right
        elif side_up4 == side_down2 and side_right2 == side_left4:
            side_left4 -= 50
            side_right4 -= 50
        #block being rotated from bottom
        elif side_up4 == side_down2 and side_left2 == side_left4:
            side_left4 -= 25
            side_right4 -= 25
            side_up4 -= 25
            side_down4 -= 25
        #rotate from bottom 2
        elif side_up4 > side_down2 and side_left2 == side_left4:
            side_left4 -= 50
            side_right4 -= 50
            side_up4 -= 50
            side_down4 -= 50
        #rotate from bottom left
        elif side_up4 == side_down2 and side_left2 == side_right4:
            side_up4 -= 50
            side_down4 -= 50

        #collision
        for y in range(2):
            for x in garbage:
                #push block left
                if side_left2 < x[2]:
                    if side_up1 == x[0] and side_left1 == x[2]:
                        move_left()
                    if side_up3 == x[0] and side_left3 == x[2]:
                        move_left()
                    if side_up4 == x[0] and side_left4 == x[2]:
                        move_left()

                #push block up
                if side_left2 == x[2] and side_up2 < x[0]:
                    if side_up1 == x[0] and side_left1 == x[2]:
                        move_up()
                    if side_up3 == x[0] and side_left3 == x[2]:
                        move_up()
                    if side_up4 == x[0] and side_left4 == x[2]:
                        move_up()

                #push block right
                if side_right2 > x[3]:
                    if side_up1 == x[0] and side_left1 == x[2]:
                        move_right()
                    if side_up3 == x[0] and side_left3 == x[2]:
                        move_right()
                    if side_up4 == x[0] and side_left4 == x[2]:
                        move_right()

                #push block down
                if side_left2 == x[2] and side_down2 > x[1]:
                    if side_up1 == x[0] and side_left1 == x[2]:
                        move_down()
                    if side_up3 == x[0] and side_left3 == x[2]:
                        move_down()
                    if side_up4 == x[0] and side_left4 == x[2]:
                        move_down()
        for x in range(2):
            if side_left1 < 0:
                move_right()
            if side_left2 < 0:
                move_right()
            if side_left3 < 0:
                move_right()
            if side_left4 < 0:
                move_right()
            if side_right1 > 250:
                move_left()
            if side_right2 > 250:
                move_left()
            if side_right3 > 250:
                move_left()
            if side_right4 > 250:
                move_left()

        fail_rot = False
        for x in garbage:
            if side_up1 == x[0] and side_left1 == x[2]:
                fail_rot = True
            if side_up2 == x[0] and side_left2 == x[2]:
                fail_rot = True
            if side_up3 == x[0] and side_left3 == x[2]:
                fail_rot = True
            if side_up4 == x[0] and side_left4 == x[2]:
                fail_rot = True
            if side_left1 < 0:
                fail_rot = True
            if side_left2 < 0:
                fail_rot = True
            if side_left3 < 0:
                fail_rot = True
            if side_left4 < 0:
                fail_rot = True
            if side_right1 > 250:
                fail_rot = True
            if side_right2 > 250:
                fail_rot = True
            if side_right3 > 250:
                fail_rot = True
            if side_right4 > 250:
                fail_rot = True
        if fail_rot:
            side_up1 = norm_state[0][0]
            side_up2 = norm_state[1][0]
            side_up3 = norm_state[2][0]
            side_up4 = norm_state[3][0]

            side_down1 = norm_state[0][1]
            side_down2 = norm_state[1][1]
            side_down3 = norm_state[2][1]
            side_down4 = norm_state[3][1]

            side_left1 = norm_state[0][2]
            side_left2 = norm_state[1][2]
            side_left3 = norm_state[2][2]
            side_left4 = norm_state[3][2]

            side_right1 = norm_state[0][3]
            side_right2 = norm_state[1][3]
            side_right3 = norm_state[2][3]
            side_right4 = norm_state[3][3]



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#controls the creation of tetriminos (6 random choices)
def drop_piece():
    global side_down1, side_up1, side_left1, side_right1
    global side_down2, side_up2, side_left2, side_right2
    global side_down3, side_up3, side_left3, side_right3
    global side_down4, side_up4, side_left4, side_right4
    global piece_colour, cure_piece, level, total_lines
    cure_piece = pieces[random.randint(0,6)]
    #cure_piece = "line"
    if cure_piece == "i":
        piece_colour = "cyan"
        #top left corner
        side_up1 = 0
        side_down1 = 25
        side_left1 = 100
        side_right1 = 125
        #top right corner
        side_up2 = 0
        side_down2 = 25
        side_left2 = 125
        side_right2 = 150
        #bottom left
        side_up3 = 0
        side_down3 = 25
        side_left3 = 150
        side_right3 = 175
        #bottom right
        side_up4 = 0
        side_down4 = 25
        side_left4 = 175
        side_right4 = 200

    if cure_piece == "o":
        piece_colour = "yellow"
        #top left corner
        side_up1 = 0
        side_down1 = 25
        side_left1 = 125
        side_right1 = 150
        #top right corner
        side_up2 = 0
        side_down2 = 25
        side_left2 = 150
        side_right2 = 175
        #bottom left
        side_up3 = 25
        side_down3 = 50
        side_left3 = 125
        side_right3 = 150
        #bottom right
        side_up4 = 25
        side_down4 = 50
        side_left4 = 150
        side_right4 = 175
    if cure_piece == "z":
        piece_colour = "red"
        #top left
        side_up1 = 0
        side_down1 = 25
        side_left1 = 125
        side_right1 = 150
        #up
        side_up2 = 0
        side_down2 = 25
        side_left2 = 150
        side_right2 = 175
        #down
        side_up3 = 25
        side_down3 = 50
        side_left3 = 150
        side_right3 = 175
        #down right
        side_up4 = 25
        side_down4 = 50
        side_left4 = 175
        side_right4 = 200
    if cure_piece == "s":
        piece_colour = "lime"
        #top right corner
        side_up1 = 0
        side_down1 = 25
        side_left1 = 175
        side_right1 = 200
        #top left corner
        side_up2 = 0
        side_down2 = 25
        side_left2 = 150
        side_right2 = 175
        #bottom left
        side_up3 = 25
        side_down3 = 50
        side_left3 = 125
        side_right3 = 150
        #bottom right
        side_up4 = 25
        side_down4 = 50
        side_left4 = 150
        side_right4 = 175
    if cure_piece == "t":
        piece_colour = "purple"
        #left
        side_up1 = 0
        side_down1 = 25
        side_left1 = 100
        side_right1 = 125
        #middle
        side_up2 = 0
        side_down2 = 25
        side_left2 = 125
        side_right2 = 150
        #right
        side_up3 = 0
        side_down3 = 25
        side_left3 = 150
        side_right3 = 175
        #bottom
        side_up4 = 25
        side_down4 = 50
        side_left4 = 125
        side_right4 = 150
    if cure_piece == "l":
        piece_colour = "blue"
        #top left
        side_up1 = 0
        side_down1 = 25
        side_left1 = 125
        side_right1 = 150
        #middle
        side_up2 = 0
        side_down2 = 25
        side_left2 = 150
        side_right2 = 175
        #right
        side_up3 = 0
        side_down3 = 25
        side_left3 = 175
        side_right3 = 200
        #right down
        side_up4 = 25
        side_down4 = 50
        side_left4 = 175
        side_right4 = 200
    if cure_piece == "j":
        piece_colour = "orange"
        #right
        side_up1 = 0
        side_down1 = 25
        side_left1 = 175
        side_right1 = 200
        #middle
        side_up2 = 0
        side_down2 = 25
        side_left2 = 150
        side_right2 = 175
        #left
        side_up3 = 0
        side_down3 = 25
        side_left3 = 125
        side_right3 = 150
        #bottom left
        side_up4 = 25
        side_down4 = 50
        side_left4 = 125
        side_right4 = 150

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def garbage_creation():
    global side_down1, side_up1, side_left1, side_right1
    global side_down2, side_up2, side_left2, side_right2
    global side_down3, side_up3, side_left3, side_right3
    global side_down4, side_up4, side_left4, side_right4
    global garbage, drop_check, total_lines, level
    blocks1 = [side_up1, side_down1, side_left1, side_right1, piece_colour]
    blocks2 = [side_up2, side_down2, side_left2, side_right2, piece_colour]
    blocks3 = [side_up3, side_down3, side_left3, side_right3, piece_colour]
    blocks4 = [side_up4, side_down4, side_left4, side_right4, piece_colour]
    side_downs = [side_up1, side_up2, side_up3, side_up4]
    garbage.append(blocks1)
    garbage.append(blocks2)
    garbage.append(blocks3)
    garbage.append(blocks4)
    drop_check = True
    line1 = 0
    line2 = 0
    line3 = 0
    line4 = 0
    line1_clear = False
    line2_clear = False
    line3_clear = False
    line4_clear = False
    for x in garbage:
        if blocks1[0] == x[0]:
            line1 += 1
            line1_height = blocks1[0]
        if blocks2[0] == x[0]:
            line2 += 1
            line2_height = blocks2[0]
        if blocks3[0] == x[0]:
            line3 += 1
            line3_height = blocks3[0]
        if blocks4[0] == x[0]:
            line4 += 1
            line4_height = blocks4[0]
    line_clear = 0
    if line1 == 10:
        line1_clear = True
        line_clear += 1
    if line2 == 10:
        line2_clear = True
        line_clear += 1
    if line3 == 10:
        line3_clear = True
        line_clear += 1
    if line4 == 10:
        line4_clear = True
        line_clear += 1

    unique_list = []
    for x in side_downs:
        unique = True
        clear = False
        for y in unique_list:
            if x == y:
                unique = False
        if x == line1_height and line1_clear:
            clear = True
        if x == line2_height and line2_clear:
            clear = True
        if x == line3_height and line3_clear:
            clear = True
        if x == line4_height and line4_clear:
            clear = True
        if unique and clear:
            unique_list.append(x)
    unique_list.sort()
    print(str(unique_list))


    garb2 = []
    for x in garbage:
        re_add = True
        for y in unique_list:
            if x[0] == y:
                re_add = False
        if re_add:
            garb2.append(x)
    count = 0
    if line1_clear or line2_clear or line3_clear or line4_clear:
        for x in garb2:
            for y in unique_list:
                if x[0] < y:
                    garb2[count][0] += 25
                    garb2[count][1] += 25

            count += 1
    lines_cleared = len(unique_list)
    if lines_cleared == 1:
        print("single")
    elif lines_cleared == 2:
        print("double")
    elif lines_cleared == 3:
        print("triple")
    elif lines_cleared == 4:
        print("tetris")
    total_lines += lines_cleared
    lines_cleared = 0
    print("total lines: ", total_lines)
    garbage = garb2
    for x in garbage:
        if x[0] <= 0:
            game_over = True
    unique_list = []



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#binding for game: < ^ > ↓
window.bind("<Right>", move_right)
window.bind("<Left>", move_left)
window.bind("<Up>", rotate)
window.bind("<Down>", move_down)

while not program_done:
    while not game_over:
        create_garbage = False
        not_done = True
        canvas = tkinter.Canvas(window, width = 350, height = 525, bg = "pink")
        if drop_check == True:
            drop_piece()
            drop_check = False
        border = canvas.create_line(250,0,250,525)
        block_1 = canvas.create_rectangle(side_left1, side_up1,side_right1,side_down1, fill = piece_colour)
        block_2 = canvas.create_rectangle(side_left2, side_up2,side_right2,side_down2, fill = piece_colour)
        block_3 = canvas.create_rectangle(side_left3, side_up3,side_right3,side_down3, fill = piece_colour)
        block4 = canvas.create_rectangle(side_left4, side_up4,side_right4,side_down4, fill = piece_colour)

        cure_time = time.time()



        if side_down1 == 525 or side_down2 == 525 or side_down3 == 525 or side_down4 == 525:
            time_check = cure_time - start_time
            if time_check >= 1:
                create_garbage = True
        else:
            start_time = time.time()
        for x in garbage:
            garbage_blocks = canvas.create_rectangle(x[2], x[0], x[3], x[1], fill = x[4])
        time_start = True
        for x in garbage:
            charb_time = cure_time - garb_time
            if side_down1 == x[0] and side_left1 == x[2]:
                down = False
                down_check = False
                time_start = False
            elif side_down2 == x[0] and side_left2 == x[2]:
                down = False
                down_check = False
                time_start = False
            elif side_down3 == x[0] and side_left3 == x[2]:
                down = False
                down_check = False
                time_start = False
            elif side_down4 == x[0] and side_left4 == x[2]:
                down = False
                down_check = False
                time_start = False

            if side_left1 == x[3] and side_up1 == x[0]:
                left_check = False
                left = False
            elif side_left2 == x[3] and side_up2 == x[0]:
                left_check = False
                left = False
            elif side_left3 == x[3] and side_up3 == x[0]:
                left_check = False
                left = False
            elif side_left4 == x[3] and side_up4 == x[0]:
                left_check = False
                left = False
            if side_right1 == x[2] and side_up1 == x[0]:
                right_check = False
                right = False
            elif side_right2 == x[2] and side_up2 == x[0]:
                right_check = False
                right = False
            elif side_right3 == x[2] and side_up3 == x[0]:
                right_check = False
                right = False
            elif side_right4 == x[2] and side_up4 == x[0]:
                right_check = False
                right = False
        if charb_time > 1:
            count_lazy += 1
            if count_lazy == 1:
                create_garbage = True
            else:
                count_lazy = 0
        if time_start:
            garb_time = time.time()
        if create_garbage:
            garbage_creation()

        if right_check:
            right = True

        if left_check:
            left = True

        if down_check:
            down = True
        if side_down1 > 525:
            move_up()
        if side_down3 > 525:
            move_up()
        if side_down4 > 525:
            move_up()
        #lowering the block
        #10% faster every 10 blocks cleared

        if total_lines >= 10:
            level = (int(total_lines / 10)) + 1
        time_check = cure_time - lower_time
        lower_now = 2.0 - (0.1 * level)
        if time_check > lower_now:
            move_down()
            lower_time = time.time()
            print("level: ", level)
        down_check = True
        left_check = True
        right_check = True
        canvas.pack()
        canvas.update()
        canvas.destroy()
    over_check = input("would you like to play again? (y/n): ")
    if over_check == "n" or over_check == "N":
        program_done = True
    else:
        game_over == False

window.mainloop()
window.destroy()
