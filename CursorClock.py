from datetime import datetime
import pyautogui as pag
import keyboard
import time
import tkinter as tk

# Declares bools
canRun : bool = False
canClick : bool = False

# Creates a new window variable
window = tk.Tk()
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(1, minsize=100, weight=1)
window.config(bg="#444")
window.title('Cursor Clock')
window.geometry("300x200+10+20")

# Functions
def exit_app():
    window.destroy()
    exit()

def on_closing():
    window.destroy()
    exit()

def toggle_clicks():
    global canClick
    canClick = not canClick
    if canClick:
        click_btn.configure(fg="#73f473")
    else:
        click_btn.configure(fg="#ff6868")

def start_clock():
    global canRun
    canRun = not canRun
    if canRun:
        toggle_btn.configure(fg="#73f473")
    else:
        toggle_btn.configure(fg="#ff6868")

# Buttons
exit_btn = tk.Button(text="exit (i)",command=exit_app)
exit_btn.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

click_btn = tk.Button(text="Allow clicks (u)", command=toggle_clicks)
click_btn.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

toggle_btn = tk.Button(text="toggle (y)", command=start_clock)
toggle_btn.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

# text
timeLabel = tk.Label(text="current time goes here")
timeLabel.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

while True:
    mouseX : float = pag.position().x
    mouseY : float = pag.position().y
    
    # Sets the spread of the mouse movements
    xSpread : float = pag.size().width / 60
    ySpread : float = (pag.size().height / 120)       

    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    clock = f"{hour:02}:{minute:02}:{second:02}"

    timeLabel.configure(text=(clock))

    if canRun:
        x = second * xSpread
        y = minute * ySpread + pag.size().height / 4
        pag.moveTo(x,y)
        if canClick:
            pag.click()

    if keyboard.is_pressed("i"):
        exit_app()
    if keyboard.is_pressed("u"):
        toggle_clicks()
        time.sleep(0.1)
    if keyboard.is_pressed("y"):
        start_clock()
        time.sleep(0.1)

    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.update()
