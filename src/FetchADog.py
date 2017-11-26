import os, random
from PIL import Image

emotions_file = open('./emotions1.txt', 'r')
emotion_string = emotions_file.read()
emotion_confidence = emotion_string.split(',')[1]

best_dog = ""
difference = 100

if 'happiness' in emotion_string :
    with open('happy_dog_database.txt') as f:
        for line in f:
            if abs(float(emotion_confidence) - float(line.split(',')[2])) < difference :
                best_dog = './dogs/happy-dog/' + line.split(',')[0]
                difference = abs(float(emotion_confidence) - float(line.split(',')[2]))
#    img = Image.open('./dogs/happy-dog/' + random.choice(os.listdir("./dogs/happy-dog/")))
else :
    with open('sad_dog_database.txt') as f:
        for line in f:
            if abs(float(emotion_confidence) - float(line.split(',')[1])) < difference :
                best_dog = './dogs/sad-dog/' + line.split(',')[0]
                difference = abs(float(emotion_confidence) - float(line.split(',')[1]))

#    img = Image.open('./dogs/sad-dog/' + random.choice(os.listdir("./dogs/sad-dog/")))

img = Image.open(best_dog)
img.show()
