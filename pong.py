import simplegui
import random


WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle_speed = 4
ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [0,0]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0



def spawn_ball(direction):
    global ball_pos, ball_vel 
    ball_vel = [0,0]
    ball_pos = [WIDTH/2,HEIGHT/2]
    if direction == RIGHT:
        ball_vel[1] = - random.randrange(1, 3)
        ball_vel[0] = random.randrange(1, 3)
    elif direction == LEFT:
        ball_vel[1] = - random.randrange(1, 3)
        ball_vel[0] = - random.randrange(1, 3)
    #print ball_vel
        
    
    
    

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel = [0,0]
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]    
        
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if ball_pos[1] > paddle1_pos-HALF_PAD_HEIGHT and ball_pos[1] < paddle1_pos+HALF_PAD_HEIGHT:
            ball_vel[0] = -(1.1)*ball_vel[0]
            score2 += 0
        else:
            score2 += 1
            spawn_ball(LEFT)
    
    elif ball_pos[0] >= WIDTH-(BALL_RADIUS+PAD_WIDTH):
        if ball_pos[1] > paddle2_pos-HALF_PAD_HEIGHT and ball_pos[1] < paddle2_pos+HALF_PAD_HEIGHT:
            ball_vel[0] = -(1.1)*ball_vel[0]
            score1 += 0
        else:
            score1 += 1
            spawn_ball(RIGHT) 
        
    elif ball_pos[1] >= HEIGHT-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]       
   
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    if paddle1_pos > HALF_PAD_HEIGHT and paddle1_pos < HEIGHT-HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    elif paddle1_pos == HALF_PAD_HEIGHT:
        if paddle1_vel >= 0:
            paddle1_pos += paddle1_vel
        else:
            paddle1_pos += 0
    elif paddle1_pos == HEIGHT-HALF_PAD_HEIGHT:
        if paddle1_vel <= 0:
            paddle1_pos += paddle1_vel
        else:
            paddle1_pos += 0
            
    if paddle2_pos > HALF_PAD_HEIGHT and paddle2_pos < HEIGHT-HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    elif paddle2_pos == HALF_PAD_HEIGHT:
        if paddle2_vel >= 0:
            paddle2_pos += paddle2_vel
        else:
            paddle2_pos += 0
    elif paddle2_pos == HEIGHT-HALF_PAD_HEIGHT:
        if paddle2_vel <= 0:
            paddle2_pos += paddle2_vel
        else:
            paddle2_pos += 0
    
    
    #canvas.draw_line([0,paddle1_pos-HALF_PAD_HEIGHT],[PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT],5,'White')
    #canvas.draw_line([0,paddle1_pos+HALF_PAD_HEIGHT],[PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT],5,'White')
    #canvas.draw_line([(WIDTH-PAD_WIDTH),paddle2_pos+HALF_PAD_HEIGHT],[WIDTH,paddle2_pos+HALF_PAD_HEIGHT],5,'White')
    #canvas.draw_line([(WIDTH-PAD_WIDTH),paddle2_pos-HALF_PAD_HEIGHT],[WIDTH,paddle2_pos-HALF_PAD_HEIGHT],5,'White')
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT]], 1, 'White', "White")
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 1, 'White', "White")   
    
            
    
    canvas.draw_text(str(score1),[250,25],24,'White')
    canvas.draw_text(str(score2),[350,25],24,'White')

def keydown(key):
    global paddle1_vel, paddle2_vel,paddle_speed
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = - paddle_speed
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_speed
    elif key == simplegui.KEY_MAP["up"] and key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = - paddle_speed
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel =  paddle_speed
    elif key == simplegui.KEY_MAP["w"] and key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"] and key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"] and key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

        


frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset",new_game,100)



new_game()
frame.start()
