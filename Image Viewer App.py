from tkinter import *
from  PIL import ImageTk,Image
import os 

root = Tk()
root.title("Image App Viewer")
root.geometry("1000x800")

#Getting and Resizing Images

raw_image_list = []

basepath = 'Enter folder path'
for item in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath,item)):
        if '.jpg' or '.png' in item:
            temporary_destination = Image.open(os.path.join(basepath,item),mode='r')
            temporary_destination = temporary_destination.resize((1000,750))
            raw_image_list.append(temporary_destination)

#Creating tkinter image
image_list = []
for item in raw_image_list:
    image_list.append(ImageTk.PhotoImage(item))
 
# Variables
global my_label
my_label = Label(image = image_list[0])
my_label.grid(row = 0, column = 0, columnspan = 3)

global pos 
pos = 0

#Buttons

button_back = Button(root, text = "<<", command = lambda: button_back_function(pos))
button_exit = Button(root, text = "Exit Program", command = root.quit)
button_forward = Button(root, text = ">>", command = lambda: button_forword_function(pos))

button_back.grid(row = 1 , column = 0)
button_exit.grid(row = 1 , column = 1)
button_forward.grid(row = 1 , column = 2)


# Funtions

def button_back_function(i):
    global pos
    global my_label
    
    if i == 0:
        pos = 4
    else:
        pos = i - 1

    my_label.grid_forget()
    my_label = Label(image = image_list[pos])
    my_label.grid(row = 0, column = 0, columnspan = 3)

def button_forword_function(i):
    global pos
    global my_label
    
    if i == 4:
        pos = 0
    else:
        pos = i + 1
    
    my_label.grid_forget()
    my_label = Label(image = image_list[pos])
    my_label.grid(row = 0, column = 0, columnspan = 3)



root.mainloop()
