import os, random
from PIL import Image

emotions_file = open('./emotions1.txt', 'r')
emotion_string = emotions_file.read()

if 'happiness' in emotion_string :
    img = Image.open('./dogs/happy-dog/' + random.choice(os.listdir("./dogs/happy-dog/")))
else :
    img = Image.open('./dogs/sad-dog/' + random.choice(os.listdir("./dogs/sad-dog/")))

img.show()
