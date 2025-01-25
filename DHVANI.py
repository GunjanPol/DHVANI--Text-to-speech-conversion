from gtts import gTTS
import tkinter as tk
from tkinter import Button, Entry, Label, StringVar, OptionMenu
from googletrans import Translator

import pygame

# Initialize pygame mixer
pygame.mixer.init()

import os


def Text_to_speech():
    message = entry_field.get()
    translator = Translator()
    translation = translator.translate(message, dest=selected_language.get())
    speech = gTTS(text=translation.text)

    # Get the current working directory
    cwd = os.getcwd()

    # Save the audio file to the current working directory
    speech.save(os.path.join(cwd, 'Dhvani.mp3'))

    # Load the audio file
    pygame.mixer.music.load(os.path.join(cwd, 'Dhvani.mp3'))

    # Play the audio file
    pygame.mixer.music.play()


def Exit():
    root.destroy()


def Reset():
    Msg.set("")


root = tk.Tk()
root.geometry("400x400")
root.configure(bg='ghost white')
root.title("Text to Speech with Translation")

Label(root, text="TEXT TO SPEECH", font="Courier 20 bold ", bg='white smoke').pack()
Label(text='Dhvani', font='Courier 30 bold', bg='white smoke', width='30').pack(side='bottom')

Msg = StringVar()
Label(root, text="Enter Text", font='Courier 15 ', bg='white smoke').place(x=20, y=60)

entry_field = Entry(root, textvariable=Msg, width='60')
entry_field.place(x=20, y=100)

Label(root, text="Select Language", font='Courier 15 bold', bg='white smoke').place(x=20, y=140)
# Add regional languages to the languages list
languages = ['en', 'es', 'fr', 'de', 'hi', 'te', 'ta']  # Add more languages if needed
selected_language = StringVar()
selected_language.set(languages[0])  # Default language
language_dropdown = OptionMenu(root, selected_language, *languages)
language_dropdown.config(width=10)
language_dropdown.place(x=230, y=140)

Button(root, text="PLAY", font='Courier 15 bold', command=Text_to_speech, width='4').place(x=20, y=210)
Button(root, font='Courier 15 bold', text='EXIT', width='4', command=Exit, bg='cyan').place(x=100, y=210)
Button(root, font='Courier 15 bold', text='RESET', width='6', command=Reset).place(x=300, y=210)

root.mainloop()
