# -*- coding: UTF-8 -*-
# http://www.codeskulptor.org/#save2_Lxv8t2gEHF.py
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
t = 0
str_t = '0:00.0'
successful_stops = 0
total_stops = 0
str_score = '0/0'


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    global str_t
    minute = time / 600
    second = (time % 600) / 10
    tenth_second = time % 10
    str_t = '%d:%02d.%d' % (minute, second, tenth_second)


# define str_score
def format_score():
    global str_score
    str_score = '%d/%d' % (successful_stops, total_stops)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()


def stop():
    global successful_stops, total_stops
    if timer.is_running():
        total_stops += 1
        if t % 10 == 0:
            successful_stops += 1
        format_score()
    timer.stop()


def restart():
    global t, successful_stops, total_stops
    t = 0
    successful_stops = 0
    total_stops = 0
    format(t)
    format_score()
    timer.stop()


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1
    format(t)
    # print(str_t)


# define draw handler
def draw_handler(canvas):
    text_width_t = frame.get_canvas_textwidth(str_t, 40)
    x_point_t = (200 - text_width_t) / 2
    text_width_score = frame.get_canvas_textwidth(str_score, 20)
    x_point_score = 200 - text_width_score

    canvas.draw_text(str_t, (x_point_t, 85), 40, 'White')
    canvas.draw_text(str_score, (x_point_score, 20), 20, 'Green')

# create frame
frame = simplegui.create_frame("Stopwatch", 200, 150)

# register event handlers
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Restart', restart, 100)

frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()
