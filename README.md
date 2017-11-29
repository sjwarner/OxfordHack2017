# OxfordHack2017 - Dogglegangers!

OxfordHack2017 project - *by Sam Warner, Sagar Vaze and Adrian Aboyoun.*

## Dependencies:

You'll need:
* A Microsoft FaceAPI key
* [Java Webcam Capture](http://webcam-capture.sarxos.pl/)
* Python 3
* Java 1.8+

## Dogglegangers

Dogglegangers is a project made at OxfordHack2017. The project uses some Java (responsible for webcam control) and Python
(responsible for communicating with the Microsoft FaceAPI, and also where we made our dog-emotion neural net).

Very basically, the idea is you pull a face (either happy or sad) and you get a picture of a dog back that is feeling the same
way! This was all very hacked together, so it isn't perfect, but we're proud of what we made!

## Copy Me

copy-me is a side-project we made while we waited for our dog-emotion neural net to train. Simply the idea is to copy a friend's
emotion. Player One pulls a face, the Microsoft FaceAPI decides which of the 7 primary emotions is most prominent, and Player
Two has to copy this. If you succeed, a small line of text will appear showing how far apart your facial expressions were, whereas
if you fail you will just be told which emotion FaceAPI thought you were each displaying.
