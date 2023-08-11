#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import pygame
import os

root = Tk()
root.title("Music Player")
root.geometry("500x350")

pygame.mixer.init()


def play():
    pygame.mixer.music.load(listbox.get(ACTIVE))
    var.set(listbox.get(ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def resume():
    pygame.mixer.music.unpause()


def directorychooser():
    directory = filedialog.askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listbox.insert(END, files)


var = StringVar()
songtitle = Label(root, textvariable=var)

listbox = Listbox(root)
listbox.pack()

play_button = Button(root, text="Play", command=play)
play_button.pack()

stop_button = Button(root, text="Stop", command=stop)
stop_button.pack()

pause_button = Button(root, text="Pause", command=pause)
pause_button.pack()

resume_button = Button(root, text="Resume", command=resume)
resume_button.pack()

directory_chooser_button = Button(
    root, text="Choose Directory", command=directorychooser)
directory_chooser_button.pack()

songtitle.pack()

root.mainloop()

