# Use Google Chrome only 
# Click on the Play button above to play the game
# venu.murthy@thoughtworks.com
# Thank YOU for taking the time to go through this code!

# Thanks to Kim Lathrop and Raj for the art.

import simplegui
import math
import random

# globals for user interface
width = 1024
height = 768
time = 0
started = False
max_score = 500


answer = ""
q1 = "Which app is going to complete 14 years in TW?"
q2 = "Where can you find Project Preference of employee within TW?"
q3 = "Which system is the primary Invoicing System in TW?"
q4 = "Which system is based on Jive?"
q5 = "Overview, Activity, Inbox, Action - Refer to which app?"
q6 = "Which system is responsible for paying our vendors?"
q7 = "Which system we use Transfer Employees to different Location?"
q8 = "Where do you find TWer with similiar skill set as yours?"
q9 = "How do you find what projects Zhen Yang has worked on?"
q10 ="Techops delivery team in Xian works on which app?"
q11 ="Who should you head to if we want correction in timecard?"
q12 ="Who should you head to if you want GTM account?"
q13 ="Who should you head to if you need return MS Office license?"
q14 ="Where can you scan receipt and submit your expense?"
q15 ="Who needs to do weekly review for timecards?"
q16= "Which open source tool was born in Techops ?"
q17 ="Go Figure , Cube are under which product line ?"
q18 = " What replaced GAB ?"

questions = { q1: "peoplesoft", q2: "jigsaw", q3: "ourtw", q4: "mytw", q5: "myTW", q6: "peoplesoft", q7: "peoplesoft", q8: "jigsaw", q9: "jigsaw", q10: "ourtw", q11: "helpDesk", q12: "helpDesk", q13: "helpDesk", q14: "expensify", q15: "projectManager",q16: "Selenium", q17: "OI",q18: "Contacts"}
questions_list = questions.keys()

#shuffling the questions
random.shuffle(questions_list)

# Class to store Image Information
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        
        self.center = center
        self.size = size
        self.radius = radius
        self.animated = animated
        # if there is some value in lifespan
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
            
    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

#Calss to store Image information and name
class ImageInfo_ans:
    def __init__(self, center, size, radius, name, lifespan = None, animated = False):
        
        self.center = center
        self.size = size
        self.radius = radius
        self.name = name
        self.animated = animated
        # if there is some value in lifespan
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        
            
    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius
    
    #new addition to get the name.
    def get_name(self):
        return self.name
    
    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
    
# this will have the image of apps

gapps_info = ImageInfo_ans([45, 45], [90, 90], 40, "gapps")
gapps_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/gapps_asteroid.png")

jigsaw_info = ImageInfo_ans([45, 45], [90, 90], 40, "jigsaw")
jigsaw_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/jigsaw_asteroid.png")

mytw_info = ImageInfo_ans([45, 45], [90, 90], 40, "mytw")
mytw_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/mytw_asteroid.png")

ourtw_info = ImageInfo_ans([45, 45], [90, 90], 40, "ourtw")
ourtw_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/our_asteroid_blue.png")

avature_info = ImageInfo_ans([45, 45], [90, 90], 40, "avature")
avature_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/avature_asteroid.png")

peoplesoft_info = ImageInfo_ans([45, 45], [90, 90], 40, "peoplesoft")
peoplesoft_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/people_soft_asteroid.png")

# ******************** new pics  helpDesk-expensify-projectManager
# ******************** new pics  helpDesk_info, expensify_info, projectManager_info, selenium_info, OI_info, contacts_info
# ******************** new pics  helpDesk_image, expensify_image, projectManager_image, selenium_image, OI_image, contacts_image
helpDesk_info = ImageInfo_ans([45, 45], [90, 90], 40, "helpDesk")
helpDesk_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/helpdesk_rock.png")

expensify_info = ImageInfo_ans([45, 45], [90, 90], 40, "expensify")
expensify_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/expensify_rock.png")

projectManager_info = ImageInfo_ans([45, 45], [90, 90], 40, "projectManager")
projectManager_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/pm_rock.png")

selenium_info = ImageInfo_ans([45, 45], [90, 90], 40, "Selenium")
selenium_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/selenium_rock.png")

OI_info = ImageInfo_ans([45, 45], [90, 90], 40, "OI")
OI_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/OI_rock.png")

contacts_info = ImageInfo_ans([45, 45], [90, 90], 40, "Contacts")
contacts_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/contact_rock.png")
# ******************** new pics


# debris in space images *********** background - rocks
debris_info = ImageInfo([320, 240], [640, 480])
#origin one
#debris_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/debris4_blue.png")
#new one
#debris_image = simplegui.load_image("http://picapi.ooopic.com/10/62/79/48b1OOOPIC50.jpg")
debris_image = simplegui.load_image("")


# nebula images - nebula_brown.png, nebula_blue.png *********** background - space
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/background.jpg")

# splash image *********** main menu
splash_info = ImageInfo([200, 200], [400, 400])
splash_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/splashscreen.png")

# splash screen for the winner image *********** say "You Won"
winner_info = ImageInfo([200, 150], [400, 300])
winner_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/winner.png")
    
# ship image *********** space ship
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png *********** 
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png *********** 
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/soundtrack.mp3")
missile_sound = simplegui.load_sound("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/thrust.mp3")
explosion_sound = simplegui.load_sound("https://raw.githubusercontent.com/tcz001/ace-battle/master/assets/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

# Helper function using pythogrous theorm to find the length of hypthoneus
def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

# Helper function to upate and draw each sprite in a group        
def process_sprite_group(sprits, canvas):
    
    for a_rock in sprits:
        a_rock.draw(canvas)
        a_rock.update()
        
        if not a_rock.update():
            sprits.remove(a_rock)

# Helper function to keep track of collision of a ship and sprite            
def group_collide(sprite_group, other_object):
    global explosion_group
    collisions = 0 
    for a_sprite in sprite_group:
        if a_sprite.collide(other_object):
            sprite_group.remove(a_sprite)
            collisions +=1
            explosion_group.add(Sprite(a_sprite.get_pos(),[0, 0], 0, 0, explosion_image, explosion_info, explosion_sound))
    return collisions 

# Helper function to keep track of collisions of missiles with astroids
def group_group_collide(sprite_group, missile_group):
    global score, explosion_group
    for sprite in sprite_group:
        for missile in missile_group:
            if sprite.collide(missile):
                sprite_group.remove(sprite)
                missile_group.remove(missile)
                explosion_group.add(Sprite(sprite.get_pos(),[0, 0], 0, 0, explosion_image, explosion_info, explosion_sound))
                score += 5
    return sprite_group     

# Helper Function to keep track of collisions of missiles with Right answers
def group_group_collide_ans(ans_group, missile_group):
    global score, explosion_group, user_ans, question_list_index
    for ans in ans_group:
        for missile in missile_group:
            if ans.collide(missile):
                user_ans = ans.get_ans_name()

                # now we want to see if the ans given by user is the same as the ans in index
                if user_ans == questions[questions_list[question_list_index]]:

                    # after taking the name of the ans astroid, we remove it from the screen
                    ans_group.remove(ans)

                    score += 100
                    # we then move on to another question
                    question_list_index += 1

                else:
                    score -= 50


                missile_group.remove(missile)
                explosion_group.add(Sprite(ans.get_pos(),[0, 0], 0, 0, explosion_image, explosion_info, explosion_sound))

    return ans_group

def reset():
    #Helper function to reset the game
    global started, my_ship, missile_group, rock_group, ans_group, explosion_group, app_image_list, app_info_list, question_list_index, user_ans, score, lives
    # Brining the ship to center of the screen when the game is reset
    my_ship = Ship([width / 2, height / 2], [0, 0], 0, ship_image, ship_info)
    missile_group = set([])
    rock_group = set([])
    explosion_group = set([])
    ans_group = set([])
    app_image_list = [gapps_image, jigsaw_image, mytw_image, ourtw_image, avature_image, peoplesoft_image, helpDesk_image, expensify_image, projectManager_image, selenium_image, OI_image, contacts_image]
    app_info_list = [gapps_info, jigsaw_info, mytw_info, ourtw_info, avature_info, peoplesoft_info, helpDesk_info, expensify_info, projectManager_info, selenium_info, OI_info, contacts_info]
    question_list_index = 0
    user_ans = ""
    score = 0
    lives = 7
    global timer0, timer1, timer2, global_timer
    timer0 = simplegui.create_timer(1000.0, global_time_update)
    timer1 = simplegui.create_timer(1000.0, rock_spawner)
    # loading the answers after 10secs
    timer2 = simplegui.create_timer(2000.0, ans_spawner)
    # initialize stuff
    global_timer = 0

# Ship class to create ship objects
class Ship:

    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        # To draw the image depending on if the thruster are On or Off
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, self.angle)

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % width
        self.pos[1] = (self.pos[1] + self.vel[1]) % height

        # update velocity
        if self.thrust:
            acc = angle_to_vector(self.angle)
            # self.vel[0] += acc[0] * .1
            self.vel[0] = acc[0] * 10
            # self.vel[1] += acc[1] * .1
            self.vel[1] = acc[1] * 10

        self.vel[0] *= .5
        self.vel[1] *= .5

    def set_thrust(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
       
    def increment_angle_vel(self):
        self.angle_vel += .05
        
    def decrement_angle_vel(self):
        self.angle_vel -= .05
        
    def shoot(self):
        global missile_group
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 15 * forward[0], self.vel[1] + 15 * forward[1]]
        missile_group.add (Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound))
        
    def get_pos(self):
        # to return the position of the ship
        return self.pos
    
    def get_radius(self):
        # Method to return the radius of the ship
        return self.radius
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated:
            # To draw the explosions, sorry for using constants due to time contstrain
            
            canvas.draw_image(self.image, [64+self.age*128, 64], self.image_size, self.pos, self.image_size)
            
        else:
            # draw the sprite
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % width
        self.pos[1] = (self.pos[1] + self.vel[1]) % height
        
        # we will update the age everytime update is called
        self.age += 1
        
        # keep it if the age is less than the lifespan
        if self.age <= self.lifespan:
            return True
        else:
            return False

    def get_pos(self):
        return self.pos
    def get_radius(self):
        return self.radius
    
    def collide(self, other_object):
        
        # Return True if there is a collision else false by using distance between Sprite and ship
        
        if dist(self.pos, other_object.get_pos()) < (self.radius + other_object.get_radius()):
            
            return True
            
        else:
            return False

#Class for Answer Sprites        
class Sprite_ans:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.name = info.get_name()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated:
            # To draw the explosions, sorry for using constants due to time contstrain    
            canvas.draw_image(self.image, [64+self.age*128, 64], self.image_size, self.pos, self.image_size)
            
        else:
            # draw the sprite
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % width
        self.pos[1] = (self.pos[1] + self.vel[1]) % height
        
        # we will update the age everytime update is called
        self.age += 1
        
        # keep it if the age is less than the lifespan
        if self.age <= self.lifespan:
            return True
        else:
            return False

    def get_pos(self):
        return self.pos
    def get_radius(self):
        return self.radius
    
    #method to return the name of the file
    def get_ans_name(self):
        return self.name
    
    def collide(self, other_object):
        
        # Return True if there is a collision else false by using distance between Sprite and ship
        
        if dist(self.pos, other_object.get_pos()) < (self.radius + other_object.get_radius()):
            return True
            
        else:
            return False

# key handlers to control ship, no changes made as provided in the template, this does has a bug though
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
        
def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(False)
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, score, lives
    center = [width / 2, height / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        soundtrack.play()

# the crux of the code which runs everthing
def draw(canvas):
    global time, started, lives, rock_group, ans_group
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width/2, height/2], [width, height])
    canvas.draw_image(debris_image, [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]], [width/2+1.25*wtime, height/2], [width-2.5*wtime, height])
    if wtime:
        canvas.draw_image(debris_image, [size[0]-wtime, center[1]], [2*wtime, size[1]], [1.25*wtime, height/2], [2.5*wtime, height])

    # draw UI
    canvas.draw_text("Lives", [50, height-50], 30, "White")
    canvas.draw_text("Score", [width-100, height-50], 30, "White")
    canvas.draw_text(str(lives), [50, height-30], 30, "White")
    canvas.draw_text(str(score), [width-100, height-30], 30, "White")

    #Tutorial
    if global_timer <3 and started:
        canvas.draw_text("Welcome to the mission!", [20, 25], 30, "White")
    if  2< global_timer <5 and started:
        canvas.draw_text("Stir the space ship to avoid being hit by the astroids", [25, 25], 30, "White")
    if 4 < global_timer < 7 and started:
        canvas.draw_text("Fire missiles to destroy astroids", [25, 25], 30, "White")
        
    
    #After some time and only when the lives are there, we will display the apps on the screen
    if global_timer > 8 and lives > 0 and question_list_index < len(questions_list) and started :
        canvas.draw_text(questions_list[question_list_index], [25, 25], 25, "White")
        
    # draw ship and sprites
    my_ship.draw(canvas)
    # to process sprites    
    process_sprite_group(rock_group, canvas)
    # to process answers
    process_sprite_group(ans_group, canvas)
    # to process missiles
    process_sprite_group(missile_group, canvas)
    # To draw explosions
    process_sprite_group(explosion_group, canvas)
    
    # update ship
    my_ship.update()
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), [width/2, height/2], splash_info.get_size())
    
    lives -= group_collide(rock_group, my_ship)
    #We would not like the ans rock to go away when the ship collides
    #lives -= group_collide_ans(ans_group, my_ship)
    
    group_group_collide(rock_group, missile_group)
    group_group_collide_ans(ans_group, missile_group)
    
    if not started:
        soundtrack.rewind()

    if lives <= 0:
        stop()
        canvas.draw_text("Game Over", [200, 70], 70, "Red")
        canvas.draw_text("Game by Venu Murthy", [200, 350], 30, "Red")
        canvas.draw_text("Thanks to ", [200, 400], 30, "Red")
        canvas.draw_text("TechOps team", [200, 460], 30, "Red")
        
    
    # to display winner
    if score > 720 and started:
        canvas.draw_image(winner_image, winner_info.get_center(), winner_info.get_size(), [width/2, height/2], winner_info.get_size())
        rock_group = set([])
        ans_group = set([])
        canvas.draw_text("Game by Venu Murthy", [200, 350], 25, "Red")
        canvas.draw_text("Thanks to ", [200, 400], 25, "Red")
        canvas.draw_text("TechOps team", [200, 460], 20, "Red")
        
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    rock_pos = [random.randrange(0, width), random.randrange(0, height)]
    rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
    rock_avel = random.random() * .2 - .1
    
    # condition to ensure that not more than 10 rocks are there on screen
    # and the rocks are spawned 100 pixels away from ship
    
    if len(rock_group) <= 9 and dist(rock_pos, my_ship.get_pos()) > 100 and started:
        
        rock_group.add(Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info))
class converter():
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text
    def __add__(self, other):
        return str(self) + other

#timer handler that will spawn the answers on the screen        
def ans_spawner():
    global ans_group, app_list
    ans_pos = [random.randrange(0, width), random.randrange(0, height)]
    ans_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
    ans_avel = 0

    # we will not rotate the answers
    # they are spawned 100 pixels away from ship
    if app_image_list and app_info_list and dist(ans_pos, my_ship.get_pos()) > 100 and started:
        app_image = app_image_list.pop(0)
        app_info = app_info_list.pop(0)
        ans_group.add(Sprite_ans(ans_pos, ans_vel, 0, ans_avel, app_image, app_info))

# Helper to exit program gracefully and silently
def exit_program():
    timer0.stop()
    timer1.stop()
    timer2.stop()
    frame.stop()
    soundtrack.rewind()

# This is to keep track of the time since the app started
def global_time_update():
        global global_timer
        global_timer += 1
        print global_timer


def stop():
    timer0.stop()
    timer1.stop()
    timer2.stop()


def start():
    timer0.start()
    timer1.start()
    timer2.start()

def replay():
    reset()
    start()

def init():
    global frame
    frame = simplegui.create_frame("TechOps Rocks!", width, height, 0)
    # initialize ship and two sprites and the info about the images
    reset()
    # register handlers
    frame.set_keyup_handler(keyup)
    frame.set_keydown_handler(keydown)
    frame.set_mouseclick_handler(click)
    frame.set_draw_handler(draw)
    # frame buttons
    frame.add_button("Quit", exit_program)
    frame.add_button("Replay", replay)
    frame.start()

init()
start()
