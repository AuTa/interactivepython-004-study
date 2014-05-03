# implementation of card game - Memory
# http://www.codeskulptor.org/#user31_CYz0496VrY_2.py
# import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


# helper function to initialize globals
def new_game():
    global state, list1, array, turns
    state = []
    list1 = list2 = list(range(8))
    list1.extend(list2)
    array = {}
    turns = 0
    label.set_text("Turns = %d" % turns)
    for i in range(4):
        for j in range(4):
            array[(i, j)] = list1.pop(random.randrange(len(list1)))


def pokemon_game():
    global state, array, turns, image
    state = []
    array = {}
    turns = 0
    label.set_text("Turns = %d" % turns)
    image = []
    for i in range(8):
        image.append(simplegui.load_image('http://dex.pm222.com/images/pokemon_img_cg/%03d.png' % (i * 3 + 1)))
        print 'http://dex.pm222.com/images/pokemon_img_cg/%03d.png' % (i * 3 + 1)
    image[7] = simplegui.load_image('http://dex.pm222.com/images/pokemon_img_cg/025.png')
    image.extend(image)
    for i in range(4):
        for j in range(4):
            array[(i, j)] = image.pop(random.randrange(len(image)))


# define event handlers
def mouseclick(pos):
    global state, turns
    pos = list(pos)
    state_pos = [int(pos[0] / 100), int(pos[1] / 100)]
    if not state or state_pos != state[-1]:
        state.append(state_pos)
        if len(state) % 2 == 1 and len(state) > 1:
            if array[tuple(state[-3])] != array[tuple(state[-2])]:
                state.pop(-2)
                state.pop(-2)
        if len(state) % 2 == 0 and len(state) > 0:
            turns += 1
            label.set_text("Turns = %d" % turns)


# cards are logically 100x100 pixels in size
def draw(canvas):
    for i in range(4):
        for j in range(4):
            polygon_point = [[i * 100, j * 100], [(i + 1) * 100, j * 100], [(i + 1) * 100, (j + 1) * 100], [i * 100, (j + 1) * 100]]
            canvas.draw_polygon(polygon_point, 4, 'Black', '#66ccff')
    if state:
        for x in range(len(state)):
            i = state[x][0]
            j = state[x][1]
            polygon_point = [[i * 100, j * 100], [(i + 1) * 100, j * 100], [(i + 1) * 100, (j + 1) * 100], [i * 100, (j + 1) * 100]]
            canvas.draw_polygon(polygon_point, 4, 'Black', 'Black')
            if type(array[tuple(state[x])]) == int:
                canvas.draw_text(str(array[tuple(state[x])]), [i * 100 + 35, j * 100 + 75], 60, '#cc66ff')
            else:
                canvas.draw_image(array[tuple(state[x])], (array[tuple(state[x])].get_width() / 2, array[tuple(state[x])].get_height() / 2), (array[tuple(state[x])].get_width(), array[tuple(state[x])].get_height()), (i * 100 + 50, j * 100 + 50), (100, 100))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 400, 400)
frame.add_button("Reset", new_game)
frame.add_button("Pokemon", pokemon_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
pokemon_game()
new_game()
frame.start()
