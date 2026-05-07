#This is the file for any helper functions that could be used throughout the code
import hashlib

import pygame

#hash password 
def hash_pass(hashing):
    hash_value = hashlib.sha256(hashing.encode('utf-8')).hexdigest()
    return hash_value

#This is a function that returns a object that is the image
def crop_img(x,y, width,height,img, output_path):
    image = pygame.image.load(img).convert_alpha()
    crop_rect = pygame.Rect(x,y,width,height)
    cropped_image = image.subsurface(crop_rect)
    pygame.image.save(cropped_image, output_path)
    return cropped_image

img = crop_img()
    



