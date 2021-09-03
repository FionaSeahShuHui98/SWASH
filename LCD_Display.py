# Importing Relavant Modules
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import time
import smbus
from gpiozero import Buzzer
import RPi.GPIO as GPIO
from time import sleep

# Configuring Buzzer
buzzer = Buzzer(26) 
# Configuring LED
GPIO.setmode(GPIO.BCM)      
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
# Configuring I2C Connection
i2c = smbus.SMBus(1)
I2C_ADD = 0x08

# I2C Configuation
def writeI2C(data):
    i2c.write_byte(I2C_ADD, data)
def readI2C():
  inData = i2c.read_byte(I2C_ADD)
  return inData
# I2C Configuation
prevI2CData = 0

# Creating a New Window
root = Tk()
 
# Name the New Window as LCD Display
root.title("LCD Display")
# Set the LCD Display to full screen
root.attributes('-fullscreen',True)

# Skip to Drying Process Function
def menu_shortcut():
    # Change the current status to Drying
    current_status.config(text="Drying", bg = "yellow", font = ("Arial",12))
    countdown(15)   # Set timer as 15 seconds
    
# Start Button Function
def start():
    # Change the current status to Washing
    current_status.config(text="Washing", bg = "yellow", font = ("Arial",12))
    countdown(105)  # Set timer to 1 min 5 sec
    
# Countdown Timer Function
def countdown(count):
    # Conversion to HH:MM:SS
    hours = count // 3600
    mins = (count - (hours * 3600)) // 60
    secs = count - (hours * 3600) - (mins * 60)
    time_taken['text'] = str("{0:0=2d}".format(hours))+" : "+str("{0:0=2d}".format(mins))+" : "+str("{0:0=2d}".format(secs))
    # When time is not equal to 0
    if count > 0:
        # Change the start button to sop button
        start.config(text="Stop", bg="red", fg="white")
        # Timer count down after seconds
        root.after(1000, countdown, count-1)
    # When timer is at 42 seconds
    if count < 43:
        # Change the current status to Drying
        current_status.config(text="Drying", bg = "yellow", font = ("Arial",12))
    # When timer is at 15 seconds
    if count < 16:
        # Change the current status to Sterilizing
        current_status.config(text="Sterilizing", bg = "yellow", font = ("Arial",12))
    # When countdown timer is up
    if count == 0:
        # Change the pause button back to start button
        start.config(text="Start",bg="green",command=start)
        # Change the timer to dashes (--:--:--)
        time_taken.config(text="-- : -- : --")
        # Set the LED GPIO to HIGH
        GPIO.output(21,GPIO.HIGH)
        # Turn the buzzer on for one seconds
        buzzer.on()
        sleep(1)
        buzzer.off()
        # Alert screen
        tkinter.messagebox.showinfo('LCD Title','Remove Syringe')
        # LED switch off
        GPIO.output(21,GPIO.LOW)
        current_status.config(text="-----", bg = "yellow", font = ("Arial",12))

# Drying Button located at the top left of the screen
drying = tk.Button (root, text = "Drying", command = menu_shortcut, font = ("Arial",12),bg="black",fg="white")
drying.place(x = 240, y = 5)

# Quit Button located at the top right of the screen
quit_button = tk.Button (root, text = "Quit", command = root.destroy, font = ("Arial",12),bg="red",fg="white")
quit_button.place(x = 5, y = 5)

# Time Taken 
time_taken_label= Label(text = "Time Left", font = ("Arial",12))
time_taken_label.place(x = 120, y =70)
time_taken = tk.Label(root, font = ("Arial",12), text = "-- : -- : --")
time_taken.place(x=120, y=110)

# Current Status
curret_staus_label= Label(text = "Current Status : ", font = ("Arial",12))
curret_staus_label.place(x = 35, y = 150)
current_status = Label(root,text = "-----", bg = "yellow", font = ("Arial",12))
current_status.place(x = 150, y = 150)

# Start Button - To check if lid is closed
try:
    while True:
        # Lid is closed
        if in_data == 1:
            start = tk.Button (root, text = "Start", command = start, font = ("Arial",12),bg="green",fg="white")
            start.place(x = 125, y = 200)
        else: 
            tkinter.messagebox.showinfo('LCD Title','Please close the lid properly.')
            
except KeyboardInterrupt:
  GPIO.cleanup()