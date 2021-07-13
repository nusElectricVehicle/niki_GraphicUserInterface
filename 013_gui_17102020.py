'''
This is the docs used. Signed in using willoughby.nuseco@gmail.com
https://docs.google.com/spreadsheets/d/12OdxolUzGm2LjfO5vwwMhhdhNAUsxQ7rdyF8dbFmCyE/edit#gid=0

Created on: 16 October 2020
Created by: Willoughby Niki (lynxDigital)
Last edited: 02 November 2020
'''

from tkinter import *
import tkinter as tk

import random
import tkinter.messagebox
import tkinter.font as font
import cv2
import d
import math
import objectTracker, meterScale, scaleFunction

#myFont = font.Font(family='Helvetica')

root = tk.Tk() #the initialisation of the window
root.title("NUS Eco Car") #the title of the window
root.geometry("985x550") #the size of the window (in pixels) rmbr its a string

#image2 =Image.open('C:\\Users\\adminp\\Desktop\\titlepage\\front.gif')

canvas = tk.Canvas(root, width=20, height=20)
canvas.pack()

def fetchData():

   list_of_hashes = sheet.get_all_records()
   print(list_of_hashes)

def scaledChoice():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)
   
def helloCallBack():
    tkinter.messagebox.showinfo("Hello, welcome to the Eco Car! Select Drive to begin!")
    print("Hello button pressed")

def lightReading():
   return random.random()
   
def openFile():
   capture = cv2.VideoCapture(0)
   dddd = tk.Tk() #the initialisation of the window
   dddd.title("NUS")
   dddd.after(300, lambda: dddd.destroy()) # Destroy the widget after 30 seconds

   while True:
       _, frame = capture.read()

       if _:
          imagedFrame = objectTracker.findVehicle(frame)
          imagedFrame = scaleFunction.rescale(imagedFrame, 20)
          cv2.imshow("Frame", imagedFrame)
          lightConditions = tk.Label(root, text = lightReading)
          
          

       if cv2.waitKey(5) == ord('q'):
          break

def getSquareRoot():
    print(entry1)
    x = entry1.get()
    y = float(x)
    print(math.sqrt(y))

bg_image = tk.PhotoImage(file = "dash.png") #the size is 985 by 550 pixels
bk_label = tk.Label(root, image = bg_image)
bk_label.place (x=0, y=0)

w = tk.Label(root, text="Hello Tkinter!")
e = tk.Button(root,
              text ="Begin Drive",
              #font=myFont,
              bg='orange',
              fg='black',
              command = openFile)

checkStats = tk.Button(root,
              text ="Car Statistics",
              #font=myFont,
              bg='orange',
              fg='black',
              command = helloCallBack)

hello = meterScale.shellEcoScreen()
hello.place(x=-50, y=200)

hello = meterScale.shellEcoScreen()
hello.place(x=-50, y=20)

var = DoubleVar()
scale = tk.Scale( root, variable = var )
scale.pack(padx=5, pady=10, side=tk.LEFT)

button = tk.Button(root, text = "Get Scale Value", command = fetchData)
button.pack(padx=5, pady=20, side=tk.LEFT)

track = tk.Scale(root, from_=1500, to=1000)
track.place(x=500, y=200)
#track.pack(anchor = CENTER)

ttraa = tk.Scale(root, from_=1000, to=2000, orient=HORIZONTAL)
ttraa.pack()

entry1 = tk.Entry(root)
button1 = tk.Button(text='Get the Square Root', command=fetchData)

gpsLocation = tk.Text(root, height=1, width=20)
gpsReading = "00"
gpsLocation.insert(tk.END, gpsReading, 'color')
gpsLocation.place(x=477, y=447) #coordinates of the textbox

lightReadingg = 0
lightConditions = tk.Label(root, text = lightReading())
lightConditions.place(x=844, y=460) #coordinates of the textbox

relativeHumidity = tk.Text(root, height=1, width=5)
relativeReading = "___ %"
relativeHumidity.insert(tk.END, relativeReading, 'color')
relativeHumidity.place(x=800, y=510) #coordinates of the textbox

print(entry1)
print(e)


w.pack()
e.pack()

checkStats.pack()
entry1.pack()
button1.pack()

root.mainloop()
