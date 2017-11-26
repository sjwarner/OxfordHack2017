echo -e -n "Which game mode would you like? Type 'dogglegangers' or 'copy-me' \n"
read name

if [ $name = "dogglegangers" ]; then
    echo Dogglegangers game mode selected!
    ./dogglegangers.sh
else
    echo Copy My Emotion game mode selected!
    ./copyMyEmotion.sh
fi
