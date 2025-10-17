from time import strftime, localtime
import time
import turtle

#print(strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))

def hour_hand(hours, minutes, seconds):
  global hourShown
  hrTurtle.ht()
  hrTurtle.speed(0)
  if (minutes == 0 and seconds == 0 and hourShown == True):
    hrTurtle.goto(0,0)
    hrTurtle.clear()
    hrTurtle.pd()
    hrTurtle.setheading(90 - (30 * hours))
    hrTurtle.forward(100)
    hrTurtle.pu()
  if (hourShown == False):
    hrTurtle.goto(0,0)
    hrTurtle.pd()
    hrTurtle.setheading(90 - (30 * hours))
    hrTurtle.forward(100)
    hrTurtle.pu()
    hourShown = True

def minute_hand(minutes, seconds):
  global minuteShown
  minTurtle.speed(0)
  if (seconds % 12 == 0 and minuteShown == True):
    minTurtle.goto(0,0)
    minTurtle.clear()
    minTurtle.pd()
    minTurtle.setheading(90 - (6 * minutes) - int(seconds / 12))
    minTurtle.forward(150)
    
  if (minuteShown == False):
    minTurtle.goto(0,0)
    minTurtle.clear()
    minTurtle.pd()
    minTurtle.setheading(90 - (6 * minutes))
    minTurtle.forward(150)
    minuteShown = True

def second_hand(seconds):
  secTurtle.speed(0)
  secTurtle.goto(0,0)
  secTurtle.clear()
  secTurtle.pd()
  secTurtle.setheading(90 - (6 * seconds))
  secTurtle.forward(150)

def am_or_pm():
  clockTurtle.pu()
  clockTurtle.goto(0,50)
  clockTurtle.pd()
  clockTurtle.begin_fill()
  clockTurtle.circle(50, 360, 4)
  clockTurtle.end_fill()
  clockTurtle.color("red")
  clockTurtle.pu()
  if (int(strftime("%H", localtime()))) % 12 <= 1:
    clockTurtle.goto(-27.5, 85)
    clockTurtle.write("PM", font=('Arial', '30'))
  else:
    clockTurtle.goto(-27.5, 85)
    clockTurtle.write("AM", font=('Arial', '30'))
  
hrTurtle = turtle.Turtle()
hrTurtle.ht()
hrTurtle.pensize(3)
minTurtle = turtle.Turtle()
minTurtle.pensize(2.5)
minTurtle.ht()
secTurtle = turtle.Turtle()
secTurtle.color("red")
secTurtle.ht()

hourShown = False
minuteShown = False

clockTurtle = turtle.Turtle()
clockTurtle.speed(0)
clockTurtle.ht()
clockTurtle.pu()
clockTurtle.goto(0, 200)
clockTurtle.pd()
clockTurtle.circle(-200)

# Draws the clock with minute ticks and 5 minute increments
for i in range(60):
  clockTurtle.circle(-200, 6)
  heading = (clockTurtle.heading())
  clockTurtle.setheading(-96 - 6*i)
  if ((i + 1) % 5 == 0):
    clockTurtle.pu()
    clockTurtle.forward(15)
    clockTurtle.write((i + 1) / 5, font=('Arial', '10'))
    clockTurtle.backward(15)
    clockTurtle.pd()
  else:
    clockTurtle.forward(20)
    clockTurtle.backward(20)
  clockTurtle.setheading(heading)

### Makes seconds, minutes, and hours not equal to a possible time to make the if statements initally work
seconds = -1
minutes = -1
hours = -1
while True:
  if (seconds != int(strftime("%S", localtime()))):     ### Every second it changes the second_hand location
    seconds = int(strftime("%S", localtime()))
    second_hand(seconds)  
    
  if (minutes != int(strftime("%M", localtime()))):     ### Every minute it changes the minute_hand location
    minutes = int(strftime("%M", localtime()))
    minute_hand(minutes, seconds)
    
  if (hours != int(strftime("%H", localtime()))):       ### Every hour it changes the hour_hand location
    hours = int(strftime("%H", localtime()))
    hour_hand(hours, minutes, seconds)
    
  if seconds < 10:                                      ### Adds a "0" to the seconds counter (EX: XX:XX:00 or XX:XX:05)
    seconds = "0" + str(seconds)
    
  if minutes < 10:                                      ### Adds a "0" to the minutes counter (EX: XX:00:XX or XX:09:XX)
    minutes = "0" + str(minutes)
    
  if hours < 10:                                        ### Adds a "0" to the hours counter (EX: 00:XX:XX or 04:XX:XX)
    hours = "0" + str(hours)
    
  print(str(hours) + ":" + str(minutes) + ":" + str(seconds))     ### Returns the time in the format XX:XX:XX
  time.sleep(1)
