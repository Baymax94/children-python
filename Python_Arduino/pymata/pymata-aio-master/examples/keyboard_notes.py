#!/usr/bin/python
"""
Example of playing notes from the keyboard
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

board = PyMata3()

BUZZER_PIN = 9
NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_D5 = 587
NOTE_E5 = 659
NOTE_F5 = 698


def setup():
    print("Virtual piano")


def loop():
    key = input("Enter a key in the range asdfghjkl;' to play a note (Space to stop, x to exit) ")
    if key == "a":
        board.play_tone(BUZZER_PIN, Constants.TONE_TONE, NOTE_C4, None)
    elif key == "s":
        board.play_tone(BUZZER_PIN,Constants.TONE_TONE, NOTE_D4, None)
    elif key == "d":
        board.play_tone(BUZZER_PIN,Constants.TONE_TONE, NOTE_E4, None)
    elif key == "f":
        board.play_tone(BUZZER_PIN,Constants.TONE_TONE, NOTE_F4, None)
    elif key == "g":
        board.play_tone(BUZZER_PIN,Constants.TONE_TONE, NOTE_G4, None)
    elif key == "h":
        board.play_tone(BUZZER_PIN,Constants.TONE_TONE, NOTE_A4, None)
    elif key == "j":
        board.play_tone(BUZZER_PIN,Constants.TONE_TONE, NOTE_B4, None)
    elif key == "k":
        board.play_tone(BUZZER_PIN,Constants.TONE_TONE, NOTE_C5, None)
    elif key == "l":
        board.play_tone(BUZZER_PIN,Constants.TONE_TONE, NOTE_D5, None)
    elif key == ";":
        board.play_tone(BUZZER_PIN,Constants.TONE_TONE, NOTE_E5, None)
    elif key == "'":
        board.play_tone(BUZZER_PIN,Constants.TONE_TONE, NOTE_F5, None)
    elif key == " ":
        board.play_tone(BUZZER_PIN,Constants.TONE_NO_TONE, 0, 0)
    elif key == "x":
        board.shutdown()
        exit(0)
    else:
        print("Unknown key:", key)


if __name__ == "__main__":
    setup()
    while True:
        loop()
