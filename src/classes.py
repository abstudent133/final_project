#Pseudocode
from helper import*
import pygame


#User class
class User:
    #initiate(username, password)
    def __init__(self, username):
        self.username = username
    #formate to add
    def formate_dict(self):
        #take username, hashed password, starting amount of money, and an empty invintory and create a dictionary
        #return it
        #avatar base is a sprite that we will input
        avatar_base = None
        user = {"password": self.password(),
                "money": 100,
                "avatar base": avatar_base,
                "inventory": {}                
}
    #avatar choice
    def avatar(self):
        #show all the availible avatars
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        

        #as user to choose
        #return that choice
    #password
    def password(self):
        #ask for the password
        pw = input("Please create a password and input it here: ")
        #take the password, hash it
        hash_value = hash_pass(pw)
        return hash_value
    
#this is a button class to create a button in pygame
class Button:
    #You have to input what you want the button to say, the x and y coordinates of it's position, the width and heigth of the button, the color of the button(must be RGB style), and the color of the button when the mouse is hovering over it
    def __init__(self, x, y, width, height, color, hover_color, text="button"):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("Arial", 30)
    #this is the methode that actually creates the button
    #the screen parameter is just the screen variable used when creating the screen
    def draw(self, screen):
        # Hover effect: Change color if mouse is over button
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        
        pygame.draw.rect(screen, current_color, self.rect)
        
        # Render and center text
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
    #This is the method that tells you if the button has been clicked
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

#this is a class for a image button  
class ImageButton:
    #You must input the x and y coordinates for the button, the image path, and the scale
    def __init__(self, x, y, image_path, scale=1):
        # Load and scale the image
        img = pygame.image.load(image_path).convert_alpha()
        width, height = img.get_size()
        self.image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        
        # Create a rect for positioning and collision detection
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
#again this is what creates the button and it returns if it has been pressed or not
    def draw(self, screen):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check for hover and click conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
    
#message class
class Message:
    #initiates all the parameters which are the text, the x and y coordinates, the font(not necesary), the size(not necesary), and the color(not necesary)
    def __init__(self, text,x,y,font="Ariel",size=30,color=(0,0,0)):
        self.txt = text
        self.font = font
        self.size = size
        self.color = color
        self.x = x
        self.y = y

    def draw(self, screen):
        font = pygame.font.SysFont(self.font,self.size)
        text_surface = font.render(self.txt,True,self.color)
        screen.blit(text_surface,(self.x,self.y))

#class for text inputs
class TextInput:

    def __init__(self, x, y, width, height, font_size=32):

        self.rect = pygame.Rect(x, y, width, height)

        self.active_color = pygame.Color('dodgerblue2')
        self.passive_color = pygame.Color('lightskyblue3')

        self.color = self.passive_color

        self.font = pygame.font.Font(None, font_size)

        #stores current text
        self.text = ''

        #checks if box is active
        self.active = False

    #handles typing and clicking
    def handle_event(self, event):

        #if mouse clicked
        if event.type == pygame.MOUSEBUTTONDOWN:

            #if mouse clicked inside box
            if self.rect.collidepoint(event.pos):
                self.active = True

            #otherwise deactivate
            else:
                self.active = False

            #change border color
            self.color = self.active_color if self.active else self.passive_color

        #if key pressed while active
        if event.type == pygame.KEYDOWN and self.active:

            #delete last character
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]

            #ignore enter key
            elif event.key != pygame.K_RETURN:
                self.text += event.unicode

    #draws text box
    def draw(self, screen):

        #render text
        txt_surface = self.font.render(self.text, True, (255,255,255))

        #draw text
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))

        #draw rectangle
        pygame.draw.rect(screen, self.color, self.rect, 2)