import sys
from rich import print
from time import sleep
import time
import os

speed = 1
Lines = [
      ("I wanna da-", 0.2, 0.08, "yellow"),
      ("I wanna dance in the lights", 0.45, 0.085, "yellow"),
      ("I wanna ro-", 0.2, 0.09, "yellow"),
      ("I wanna rock your body", 0.31, 0.10, "yellow"),
      ("I wanna go-", 0.2, 0.09, "yellow"),
      ("I wanna go for a ride", 0.4, 0.10, "yellow"),
      ("Hop in the music and", 0.3, 0.07, "yellow"),
      ("Rock your body", 0.3, 0.09, "yellow"),
      ("Rock that body", 0.30, 0.07, "magenta"),
      ("come on, come on", 0.0, 0.06, "magenta"),
      ("Rock that body", 0.1, 0.07, "magenta"),
      ("Rock your body", 0.1, 0.07, "yellow"),
      ("Rock that body", 0.1, 0.07, "magenta"),
      ("come on, come on", 0.0, 0.06, "magenta"),
      ("Rock that body", 0.06, 0.13, "magenta"),
    ]

def display():
  for text, Time1, Time2, color in Lines:
      delay = Time1 / speed
      for char in text:
          print("[" + color +"]" + char, end = "", flush = True)
          time.sleep(Time2 / speed)
      print()
      time.sleep(delay)
      
inic=input("cmç? ")
if inic == "s":
    time.sleep(31)
    display()