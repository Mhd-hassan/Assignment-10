# Name: Muhammad Hassan Noorsumar
# Day: Tuesday
# Date: 18/07/2023
# Sub: Python
# Topic: Assignment-10
# Assignment-10: Q2
# Q2: create a gui for taking input from the user and create a button to navigate to a browser site.
# Let's Start

import tkinter as tk

import webbrowser

def open_webpage():
    url = entry.get()
    webbrowser.open(url)

window=tk.Tk() # Create the main window
window.title("Web Browser")

label=tk.Label(window, text="Enter Url: ") # Create a label for the URL entry
label.pack(padx=10,pady=10)

entry=tk.Entry(window) # Create an entry field for the URL
entry.pack(padx=10,pady=5)

button=tk.Button(window,text="open",command=open_webpage) # Create a button to open the web page
button.pack(pady=10)

window.mainloop() # Run the application