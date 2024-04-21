import os
import time
from PIL import Image
import pywhatkit
import tempfile
import sys
import pygame


def resize_image(image, new_width=100):

    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def convert_to_ascii(image_path):

    ascii_representation = pywhatkit.image_to_ascii_art(image_path)
    return ascii_representation

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def play_music():

    pygame.mixer.init()
    pygame.mixer.music.load("badapple.mp3") 
    pygame.mixer.music.play(-1)  

def main():
 
    image_folder = "badapple"  
    image_paths = [os.path.join(image_folder, image) for image in os.listdir(image_folder) if image.endswith(".jpg") or image.endswith(".png")]
    
    play_music()
    
    for image_path in image_paths:
            try:
                image = Image.open(image_path)
                resized_image = resize_image(image)
                temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
                resized_image.save(temp_file.name)
                ascii_art = convert_to_ascii(temp_file.name)
                clear_screen()
                print(ascii_art, end='\r')
                sys.stdout.flush()
                temp_file.close()
                os.unlink(temp_file.name)
            except Exception as e:
                print("Error al procesar la imagen:", e)
    
            time.sleep(0.08)

 

if __name__ == "__main__":
    main()
