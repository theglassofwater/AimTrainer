import pygame, sys, random, time, math, random, os


current_directory = os.getcwd()
script_directory = os.path.dirname(os.path.abspath(__file__))

if current_directory != script_directory:
    os.chdir('AimTrainer')

pygame.init()

settings_image = pygame.image.load('settings_new.jpg')
background_image = pygame.image.load("stars.jpg")
headset_image = pygame.image.load('headset.jpg')
headset_image_no = pygame.image.load('headset_no.jpg')
sound = pygame.mixer.Sound("gun.wav")

width = 1280
height = 720
window = pygame.display.set_mode((width,height))
pygame.mixer.music.load("Cold.mp3")
pygame.display.set_caption('game')
frame_time = 20
pygame.mixer.music.play(-1)
volume = 1
pygame.mixer.music.set_volume(volume)

white = (255,255,255)
black = (0,0,0)
grey = (200,200,200)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,255)
purple = ()


def change_res(res):   #res hsould only be limited res' as backround doesnt scale in pygame
    global width
    global height
    global background_image
    global window

    pygame.quit
    pygame.init()

    settings_image = pygame.image.load('settings_new.jpg')
    if res[1] ==1080:
        background_image = pygame.image.load('stars1080.jpg')
    else:
        background_image = pygame.image.load("stars.jpg")
    headset_image = pygame.image.load('headset.jpg')
    headset_image_no = pygame.image.load('headset_no.jpg')
    sound = pygame.mixer.Sound("gun.wav")

    width = res[0]
    height = res[1]
    if res[2] == 0:
        window = pygame.display.set_mode((width,height))#,pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((width,height),pygame.FULLSCREEN)
    pygame.mixer.music.load("Cold.mp3")
    pygame.display.set_caption('game')

    pygame.mixer.music.play(-1)
    volume = 1
    pygame.mixer.music.set_volume(volume)
    settings()

def drawText(text, surface, x, y ,size,center, color = (255,0,0)):
    FONT = pygame.font.SysFont(None, size)
    textObject = FONT.render(text, 2, color)
    textRect = textObject.get_rect()
    if center == 1:
        x = x-(textObject.get_width()/2)
        y = y-(textObject.get_height()/2)
    textRect.topleft = (x,y)
    surface.blit(textObject, textRect)

def set_volume():
    pass

def unmute(volume):
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.unpause()
    #pygame.mixer.unpause()
    sound.set_volume(volume)

def mute():
    pygame.mixer.music.pause()
    #pygame.mixer.pause()
    sound.set_volume(0)

class box():
    def __init__(self,size_width,size_height,x_v,y_v,colour,hover_colour,health,surface_window_name_thing,screen_width,screen_height,frame_time):
        self.window_width = screen_width
        self.window_height = screen_height
        self.width = size_width
        self.height = size_height
        self.velocity_x = x_v
        self.velocity_y = y_v
        self.current_colour = colour
        self.colour = colour
        self.hover_colour = hover_colour
        self.start_health = health
        self.health = self.start_health   # health is how many (ms)it can have curser on it for
        self.window = surface_window_name_thing
        self.x = random.randint(0,self.window_width-self.width)
        self.y = random.randint(0,self.window_height-self.height)
        self.frame_time = frame_time

    def draw(self):
        self.rect = pygame.draw.rect(self.window,self.current_colour,(self.x,self.y,self.width,self.height))

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        if (self.x >= self.window_width-self.width) or (self.x <= 0):
            self.velocity_x = self.velocity_x*-1
        if (self.y >= self.window_height-self.height) or (self.y <= 0):
            self.velocity_y = self.velocity_y*-1

    def move_random(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        if (self.x >= self.window_width-self.width) or (self.x <= 0):
            self.velocity_x = self.velocity_x*-1
        elif (self.y >= self.window_height-self.height) or (self.y <= 0):
            self.velocity_y = self.velocity_y*-1

        elif random.randint(0,50) == 5:
            self.velocity_x = self.velocity_x*-1
        elif random.randint(0,50) == 5:
            self.velocity_y = self.velocity_y*-1

    def collistion(self,x,y): # collision with given coordinates
        if (x>=self.x) and (x<=self.x+self.width) and (y>=self.y) and (y<=self.y+self.height):
            return True
        else:
            return False

    def collistion_mouse(self): # collision with just curser
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos[0],pos[1]):
            self.health += -self.frame_time
            self.current_colour = self.hover_colour
            if self.health <= 0:
                self.health = self.start_health
                self.x = random.randint(0,self.window_width-self.width)
                self.y = random.randint(0,self.window_height-self.height)
            return True
        else:
            self.current_colour = self.colour
            return False

    def collistion_object_mouse(self,other_objects): # checks collision with curser and other (same) objects
        x = []
        y = []
        self.other_boxes = other_objects
        for i in range(len(self.other_boxes)):
            x.append(self.other_boxes[i].x)
            y.append(self.other_boxes[i].y)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos[0],pos[1]):
            self.health += -self.frame_time
            if self.health <= 0:
                self.health = self.start_health
                coords = 0
                while coords < len(x):
                    coords = 0
                    self.x = random.randint(0,self.window_width-self.width)
                    self.y = random.randint(0,self.window_height-self.height)
                    for i in range(len(x)):
                        if (x[i]>=self.x-self.width) and (x[i]<=self.x+self.width) and (y[i]>=self.y-self.height) and (y[i]<=self.y+self.height):
                            coords = coords
                        else:
                            coords += 1
                return True
        else:
            return False

class bouncing_ball():
    def __init__(self,size,x_v,y_v,colour,health,surface_window_name_thing,screen_width,screen_height):
        self.window_width = screen_width
        self.window_height = screen_height
        self.radius = size
        self.start_velocity_x = x_v
        self.start_velocity_y = y_v
        self.velocity_x = self.start_velocity_x
        self.velocity_y = self.start_velocity_y
        self.colour = colour
        self.start_health = health
        self.health = self.start_health   # health is how many (ms)it can have curser on it for
        self.window = surface_window_name_thing
        self.acceleration = 3
        plane = random.randint(1,3)
        if plane <= 1:
            x = random.randint(0+self.radius,self.window_width-self.radius)
            y = 0+self.radius
            self.velocity_x = self.velocity_x * 1
            self.velocity_y = self.velocity_y * -1
        else:
            y = random.randint(0+self.radius,self.window_height-self.radius)
            if plane == 2:
                x = 0+self.radius
                self.velocity_x = self.velocity_x * 1
                self.velocity_y = self.velocity_y * 1 # or -1
            else:
                x = self.window_width-self.radius
                self.velocity_x = self.velocity_x * -1
                self.velocity_y = self.velocity_y * 1 # or 1
        self.x = x
        self.y = y

    def draw(self):
        self.circle = pygame.draw.circle(self.window,self.colour,(self.x,self.y),self.radius,0)

    def respawn(self):
        self.velocity_x = self.start_velocity_x
        self.velocity_y = self.start_velocity_y
        plane = random.randint(1,3)
        if plane <= 1:
            x = random.randint(0+self.radius,self.window_width-self.radius)
            y = 0+self.radius
            self.velocity_x = self.velocity_x * 1
            self.velocity_y = self.velocity_y * -1
        else:
            y = random.randint(0+self.radius,self.window_height-self.radius)
            if plane == 2:
                x = 0+self.radius
                self.velocity_x = self.velocity_x * 1
                self.velocity_y = self.velocity_y * 1 # or -1
            else:
                x = self.window_width-self.radius
                self.velocity_x = self.velocity_x * -1
                self.velocity_y = self.velocity_y * 1 # or 1
        self.x = x
        self.y = y

    def collistion(self,mouse_x,mouse_y):
        if (((self.x - mouse_x)**2) +((self.y - mouse_y)**2))**0.5 <= self.radius:
            return True

    def collistion_and_dead(self,mouse_x,mouse_y):
        if (((self.x - mouse_x)**2) +((self.y - mouse_y)**2))**0.5 <= self.radius:
            self.health = self.health - 20
            if self.health <= 0:
                self.health = self.start_health
                return True
        else:
            return False

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.velocity_y += self.acceleration
        if self.x >= self.window_width-self.radius or self.x <= 0+self.radius:
            self.velocity_x = self.velocity_x * -1
            if self.x >= self.window_width-self.radius:
                self.x = self.window_width-self.radius
            if self.x <= 0+self.radius:
                self.x = self.radius
        if self.y >= self.window_height-self.radius or self.y <= 0+self.radius:
            self.velocity_y = self.velocity_y * -1
            if self.y >= self.window_height-self.radius:
                self.y = self.window_height-self.radius
                self.velocity_y += self.acceleration*2
            if self.y <= 0+self.radius:
                self.y = self.radius

    def everything(self):
        pos = pygame.mouse.get_pos()
        self.draw()
        self.move()
        if self.collistion_and_dead(pos[0],pos[1]) == True:
            self.respawn()
            return 1
        else:
            return 0

class button():
    def __init__(self,width,height,center_x,center_y,surface,main_colour,hover_colour,text,action,perameter,image = 0): # how can i have a lot of variable = 0
        self.width = width
        self.height = height
        self.x = center_x
        self.y = center_y
        self.window = surface
        self.colour = main_colour
        self.hover_colour = hover_colour
        self.text = text
        self.action = action
        self.perameter = perameter
        self.image = image
    def draw(self):
        pos = pygame.mouse.get_pos()
        if (pos[0]>=self.x-0.5*self.width) and (pos[0]<=self.x+self.width-0.5*self.width) and (pos[1]>=self.y-0.5*self.height) and (pos[1]<=self.y+self.height-0.5*self.height):
            self.rect = pygame.draw.rect(self.window, self.hover_colour,((self.x-0.5*self.width),(self.y-0.5*self.height),self.width,self.height))
            drawText(self.text,self.window,(self.x),(self.y),48,1)
            if self.image != 0:
                window.blit(self.image, ((self.x-0.5*self.width),(self.y-0.5*self.height)))
        else:
            self.rect = pygame.draw.rect(self.window, self.colour,((self.x-0.5*self.width),(self.y-0.5*self.height),self.width,self.height))
            drawText(self.text,self.window,(self.x),(self.y),48,1)
            if self.image != 0:
                window.blit(self.image, ((self.x-0.5*self.width),(self.y-0.5*self.height)))

    def click(self):
        pos = pygame.mouse.get_pos()
        if (pos[0]>=self.x-0.5*self.width) and (pos[0]<=self.x+self.width-0.5*self.width) and (pos[1]>=self.y-0.5*self.height) and (pos[1]<=self.y+self.height-0.5*self.height):
            if self.perameter == 0:
                self.action()
            else:
                self.action(self.perameter)

class text_box():
    pass

def count_down(game):
    time = 0
    while True:
        pygame.time.delay(20)
        window.fill((0,0,0))
        time = time + 20
        drawText(str(round(3-time*0.001,3)),window,width/2,height/2,500,1)
        if time == 2800:
            pygame.mixer.Sound.play(sound)
        if time == 3000:
            game()
        pygame.display.update()

def bouncing():
    ball_list = []
    num_of_balls = 0
    for x in range(num_of_balls):
        ball_list.append(bouncing_ball(50,random.randint(5,10),random.randint(5,10),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),1000,window,width,height))
    ball = bouncing_ball(50,10,5,yellow,1000,window,width,height)
    score = 0
    time = 0
    while True:
        pygame.time.delay(frame_time)
        window.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        for x in range(num_of_balls):
            ball_list[x].everything()
        score += ball.everything()
        drawText("Time: " + str(round(time*0.001,3)), window, 8,8,48,0)
        drawText("health: " + str(round(ball.health)), window, 8,68,48,0)
        drawText("score: " + str(round(score)), window, 8,128,48,0)
        time = time + 20
        if time == 30000:
            after_game(bouncing,score,time*0.001)
        pygame.display.update()

def tile_frenzy():
    box_list = []
    num_of_boxes = 3          # all of the commmented is to have mor balls
    for x in range(num_of_boxes):
        box_list.append(box(150,150,0,0,(0,0,255),(255,0,0),1,window,width,height,frame_time))
    score = 0
    miss = 0
    time = 0
    while True:
        pygame.time.delay(frame_time)
        window.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                score_before = score
                for x in range(num_of_boxes):
                    if box_list[x].collistion_object_mouse(box_list):
                        score+=1
                if score_before == score:
                    miss += 1
        for x in range(num_of_boxes):
            box_list[x].draw()
        drawText("Time: " + str(round(time*0.001,3)), window, 8,8,48,0)
        drawText("hits: " + str(round(score)), window, 8,248,48,0)
        drawText("misses: " + str(round(miss)), window, 8,68,48,0)
        drawText("score: " + str(round(score - miss)), window, 8,128,48,0)
        drawText("num of boxes: " + str(round(num_of_boxes)), window, 8,188,48,0)
        time = time + 20
        if time == 2000:
            after_game(tile_frenzy,score,time*0.001)
        pygame.display.update()

def tracking_box():
    time = 0
    boxy = box(150,150,13,7,(0,0,255),(255,0,0),20000000000,window,width,height,frame_time)
    while True:
        pygame.time.delay(frame_time)
        window.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        boxy.draw()
        boxy.move_random()
        boxy.collistion_mouse()
        drawText("Time: " + str(round(time*0.001,3)), window, 8,8,48,0)
        drawText("score: " + str(boxy.start_health-boxy.health), window, 8,128,48,0)
        time = time + 20
        if time == 30000:
            after_game(tracking_box,(boxy.start_health-boxy.health),time*0.001)
        pygame.display.update()

def res():
    global volume
    global num_of_buttons_settings
    global settings_buttons

    for i in range(num_of_buttons_settings-len(settings_buttons)):
        settings_buttons.pop()

    settings_buttons.append(button(200,100,600,(50+height*0.2),window,white,grey,'720p',change_res,(1280,720,0)))
    settings_buttons.append(button(200,100,900,(50+height*0.2),window,white,grey,'1080p',change_res,(1920,1080,0)))
    settings_buttons.append(button(350,100,750,(50+height*0.6),window,white,grey,'FULLSCREEN 1080',change_res,(1920,1080,1)))

def darkmode():
    global white
    global black
    global grey
    global blue
    global green
    global yellow

    if white == (0,0,0):
        black = (0,0,0)
        white = (255,255,255)
        grey = (200,200,200)
    else:
        white = (0,0,0)
        black = (255,255,255)
        grey = (100,100,100)
    settings()

def colour():

    global num_of_buttons_settings
    global settings_buttons

    for i in range(num_of_buttons_settings-len(settings_buttons)):
        settings_buttons.pop()


    settings_buttons.append(button(200,100,600,(50+height*0.2),window,white,grey,'i dont',change_res,(1280,720,0)))
    settings_buttons.append(button(200,100,900,(50+height*0.2),window,white,grey,'know',change_res,(1920,1080,0)))
    settings_buttons.append(button(350,100,750,(50+height*0.6),window,white,grey,'dark toggle',darkmode,0))

def sensitivity():
    global num_of_buttons_settings
    global settings_buttons

    for i in range(num_of_buttons_settings-len(settings_buttons)):
        settings_buttons.pop()

def soundd():
    global num_of_buttons_settings
    global settings_buttons

    for i in range(num_of_buttons_settings-len(settings_buttons)):
        settings_buttons.pop()

def settings():
    global volume
    global num_of_buttons_settings
    global settings_buttons

    time = 0
    settings_buttons = []
    num_of_buttons_settings = 6

    settings_buttons.append(button(50,50,width-50,50,window,white,grey,'X',exit,0))
    settings_buttons.append(button(200,100,120,(50+height*0.2),window,white,grey,'res',res,0))
    settings_buttons.append(button(200,100,120,(50+height*0.4),window,white,grey,'colour',colour,0))
    settings_buttons.append(button(200,100,120,(50+height*0.6),window,white,grey,'sensitivity',sensitivity,0))
    settings_buttons.append(button(200,100,120,(50+height*0.8),window,white,grey,'sound',soundd,0))
    settings_buttons.append(button(150,75,width-100,height-60,window,white,grey,'main',main,0))

    while True:
        pygame.time.delay(frame_time)
        window.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(settings_buttons)):
                    settings_buttons[i].click()
        for i in range(len(settings_buttons)):
            settings_buttons[i].draw()
        time = time + 20
        drawText('Settings',window,width/2,70,100,1,(50,00,200))
        pygame.display.update()

def after_game(game,score,time):
    buttons =  []
    num_of_buttons = 5

    buttons.append(button(50,50,width-50,50,window,white,grey,'X',exit,0))
    buttons.append(button(50,50,400,height-100,window,white,grey,'',settings,0,settings_image))
    buttons.append(button(250,100,200,height-100,window,white,grey,'play again',game,0))
    buttons.append(button(250,100,375+226,height-100,window,white,grey,'main menu',main,0))
    buttons.append(button(400,650,1000,height/2,window,green,blue,'table of scores',mute,0))

    while True:
        pygame.time.delay(frame_time)
        window.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(len(buttons)):
                    buttons[x].click()
        for x in range(len(buttons)):
            buttons[x].draw()

        #drawText('gg bro',window,200,20,200,(50,00,200))
        drawText('score : '+ str(score),window,270,170,100,0,(255,00,200))
        drawText('time : '+ str(time),window,270,350,100,0,(250,00,200))
        pygame.display.update()

def main():
    time = 0
    buttons = []
    num_of_buttons = 7

    buttons.append(button(50,50,width-50,50,window,white,grey,'X',exit,0))
    buttons.append(button(300,100,width/2,260+(150*0),window,white,grey,'bouncing',count_down,bouncing))
    buttons.append(button(300,100,width/2,260+(150*1),window,white,grey,'tile frenzy',count_down,tile_frenzy))
    buttons.append(button(300,100,width/2,260+(150*2),window,white,grey,'tracking box',count_down,tracking_box))
    buttons.append(button(50,50,width-50,height-50,window,white,grey,'',settings,0,settings_image))
    buttons.append(button(50,50,50,height-50,window,white,grey,'',unmute,0.1,headset_image))
    buttons.append(button(50,50,125,height-50,window,white,grey,'',mute,0,headset_image_no))

    while True:
        pygame.time.delay(frame_time)
        window.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(len(buttons)):
                    buttons[x].click()
        for x in range(len(buttons)):
            buttons[x].draw()
        time = time + 20
        drawText('Game Menu',window,width/2,70,100,1,(50,00,200))
        pygame.display.update()

def game_settings():
    time = 0
    colour = 0



main()
