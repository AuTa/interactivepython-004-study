#http://www.codeskulptor.org/#save2_W8VdxUrlg0.py

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    # ball_vel = [20, 10]
    if direction:
        ball_vel = [random.randrange(120, 240) / 60, -random.randrange(60, 180) / 60]
    else:
        ball_vel = [-random.randrange(120, 240) / 60, -random.randrange(60, 180) / 60]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    direction = [LEFT, RIGHT]
    spawn_ball(direction[random.randrange(0, 2)])
    paddle_pos1 = [[0, HEIGHT / 2 - HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT]]
    paddle_pos2 = [[PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT], [WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT]]
    paddle_pos3 = [[PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT], [WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]
    paddle_pos4 = [[0, HEIGHT / 2 + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]
    paddle1_pos = [paddle_pos1[0], paddle_pos2[0], paddle_pos3[0], paddle_pos4[0]]
    paddle2_pos = [paddle_pos1[1], paddle_pos2[1], paddle_pos3[1], paddle_pos4[1]]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    score1 = score2 = 0


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    if ball_pos[1] < BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_vel[0] > 0:
        if (WIDTH - PAD_WIDTH) - ball_pos[0] <= BALL_RADIUS:
            if paddle2_pos[0][1] <= ball_pos[1] <= paddle2_pos[3][1]:
                ball_vel[0] = -ball_vel[0] * 1.1
                ball_vel[1] *= 1.1
            else:
                score1 += 1
                spawn_ball(False)
    if ball_vel[0] < 0:
        if ball_pos[0] - PAD_WIDTH <= BALL_RADIUS:
            if paddle1_pos[0][1] <= ball_pos[1] <= paddle1_pos[3][1]:
                ball_vel[0] = -ball_vel[0] * 1.1
                ball_vel[1] *= 1.1
            else:
                score2 += 1
                spawn_ball(True)
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[0][1] >= 0 and paddle1_pos[3][1] <= HEIGHT:
        for i in range(4):
            paddle1_pos[i][1] += paddle1_vel[1]
    if paddle1_pos[0][1] < 0:
        difference = 0 - paddle1_pos[0][1]
        for i in range(4):
            paddle1_pos[i][1] += difference
    if paddle1_pos[3][1] > HEIGHT:
        difference = HEIGHT - paddle1_pos[3][1]
        for i in range(4):
            paddle1_pos[i][1] += difference
    if paddle2_pos[0][1] >= 0 and paddle2_pos[3][1] <= HEIGHT:
        for i in range(4):
            paddle2_pos[i][1] += paddle2_vel[1]
    if paddle2_pos[0][1] < 0:
        difference = 0 - paddle2_pos[0][1]
        for i in range(4):
            paddle2_pos[i][1] += difference
    if paddle2_pos[3][1] > HEIGHT:
        difference = HEIGHT - paddle2_pos[3][1]
        for i in range(4):
            paddle2_pos[i][1] += difference
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 1, "White", "White")
    canvas.draw_polygon(paddle2_pos, 1, "White", "White")
    # draw scores
    if score1 or score2 != 0:
        canvas.draw_text(str(score1), (200, 50), 40, "Green")
        canvas.draw_text(str(score2), (400, 50), 40, "Green")


def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += acc
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= acc
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += acc
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= acc


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = [0, 0]
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = [0, 0]
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = [0, 0]
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = [0, 0]


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game, 200)


# start frame
new_game()
frame.start()