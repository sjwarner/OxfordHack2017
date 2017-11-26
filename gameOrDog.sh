echo -e -n "Which game mode would you like? Type 'dogglegangers' or 'copy-me' \n"
read name

if [ $name = "dogglegangers" ]; then
    echo Dogglegangers game mode selected!
    echo Get ready! When the green light comes on, pull your face until it goes off again!
    ./dogglegangers.sh
else
    echo Copy My Emotion game mode selected!
    echo Get ready! When the green light comes on, pull your face until it goes off again!
    ./copyMyEmotion.sh
fi
