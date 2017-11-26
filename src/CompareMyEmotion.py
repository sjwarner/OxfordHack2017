emotion1_file = open('emotions1.txt', 'r')
emotion2_file = open('emotions2.txt', 'r')

emotion1 = emotion1_file.read()
emotion2 = emotion2_file.read()

emotion1_emotion = emotion1.split(',', 1)[0]
emotion1_confidence = float(emotion1.split(',', 1)[1])
emotion2_emotion = emotion2.split(',', 1)[0]
emotion2_confidence = float(emotion2.split(',', 1)[1])

if emotion1_emotion == emotion2_emotion:
    print ('Difference: ' + str(((emotion2_confidence - emotion1_confidence)/emotion1_confidence)*100) + '%')
else:
    print ('Not even close:')
    print ('First photo: ' + emotion1_emotion)
    print ('Your photo: ' + emotion2_emotion)
