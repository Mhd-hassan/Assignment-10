# Name: Muhammad Hassan Noorsumar
# Day: Tuesday
# Date: 18/07/2023
# Sub: Python
# Topic: Assignment-10
# Assignment-10: Q3
# Q3: Also display the user entered text in the command prompt with message of navigating to "..." whichever site you chooses
# Let's Start

import tkinter as tk
import webbrowser

def open_webpage():
    url = entry.get()
    print(f"Navigating to: {url}")
    webbrowser.open(url)

window = tk.Tk() # Create the main window
window.title("Web Browser")

label = tk.Label(window, text="Enter URL:") # Create a label for the URL entry
label.pack(padx=10, pady=10)

entry = tk.Entry(window) # Create an entry field for the URL
entry.pack(padx=10, pady=5)

button = tk.Button(window, text="Open", command=open_webpage) # Create a button to open the web page
button.pack(pady=10)

window.mainloop() # Run the application

"""
Ouptput of open_webbrowser:
Navigating to: www.blogger.com
"""