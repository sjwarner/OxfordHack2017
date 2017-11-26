#!/bin/bash

rm emotions1.txt &>/dev/null
rm emotions2.txt &>/dev/null  
rm test.jpg &>/dev/null

javac  -cp .:./libs/* src/*.java
java  -cp .:./libs/* src/TakePicture &>/dev/null
open src/test.png
python3 src/CopyMyEmotion.py

echo --------------------------------------------------------------------

java  -cp .:./libs/* src/TakePicture &>/dev/null
open src/test.png
python3 src/CopyMyEmotion.py

python3 src/CompareMyEmotion.py
