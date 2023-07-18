# Name: Muhammad Hassan Noorsumar
# Day: Tuesday
# Date: 18/07/2023
# Sub: Python
# Topic: Assignment-10
# Assignment-10: Q1
# Q1: Implement the tkinter and webbrowser module
# Let's Start

# from tkinter import *  # Implemanting tkinter module

import tkinter as tk # Implemanting a tkinter module

import webbrowser # Implemanting a webbrowser madule

def open_webpage(): # creating a function named as open_webpage
    url = entry.get()
    webbrowser.open(url)


window = tk.Tk() # Create the main window
window.title("Web Browser")

entry = tk.Entry(window) # Create an entry field for the URL
entry.pack(padx=10, pady=10)

button = tk.Button(window, text="Open", command=open_webpage) # Create a button to open the web page
button.pack(pady=5)

window.mainloop() # Run the application
