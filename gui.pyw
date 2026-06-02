import tkinter as tk
import time
import random
import os
import winsound
from tkinterweb import HtmlFrame
calculator = None
start = None
udun = None
def browser():
    win = tk.Toplevel(window)
    win.title("browser.wpp")
    win.geometry("800x600")
    
    url_frame = tk.Frame(win)
    url_frame.pack(fill=tk.X, padx=5, pady=5)
    
    tk.Label(url_frame, text="url:").pack(side=tk.LEFT)
    url_entry = tk.Entry(url_frame)
    url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    webframe = HtmlFrame(win)
    webframe.pack(fill=tk.BOTH, expand=True)
    
    def load_page():
        url = url_entry.get()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        webframe.load_url(url)
    
    tk.Button(url_frame, text="find", command=load_page).pack(side=tk.LEFT)
    
    # Стартовая страница
    webframe.load_url("https://google.com")
def nameop():
    with open("lists/nnd.txt", "r") as f:
        global udun
        udun = f.read()
def clocks():
    now = time.strftime("%H:%M:%S")
    clock.config(text=now)
    window.after(1000, clocks)
def backcolor():
    colors = ["lightblue", "lightgreen", "lightyellow", "orange"]
    colorise = random.choice(colors)
    window.config(background=colorise)
def stopop():
    os._exit(0)
def calc():
    global calculator
    if calculator is None or not calculator.winfo_exists():
        def clc():
            try:
                espcalc = calcentry.get()
                result = eval(espcalc)
                labclc.config(text=result, fg="black")
            except:
                winsound.Beep(500, 300)
                labclc.config(text="err", fg="red")
        calculator = tk.Toplevel(window)
        calculator.title("wspcalc.wpp")
        calculator.geometry("320x240")
        calculator.resizable(False, False)
        labclc = tk.Label(calculator, font=("None", 20), text="result", fg="grey")
        labclc.pack(pady=20)
        calcentry = tk.Entry(calculator, font=("None", 20), fg="black")
        calcentry.pack(pady=10)
        accept = tk.Button(calculator, font=("None", 20), text="calculate", command=clc)
        accept.pack(pady=10)
    else:
        calculator.lift()
def runit():
    global start
    if start is None or not start.winfo_exists():
        start = tk.Toplevel(window)
        start.title("run.sys")
        start.geometry("200x280")
        start.resizable(False, False)
        rback = tk.Button(start, text="edit background color", command=backcolor)
        rback.pack(pady=10)
        rcalce = tk.Button(start, text="calculator", command=calc)
        rcalce.pack(pady=10)
        rquit = tk.Button(start, text="stop pc", command=stopop)
        rquit.pack(pady=10)
    else:
        start.lift()
nameop()
window = tk.Tk()
window.title("wispgui.sys")
window.geometry("640x480")
window.resizable(False, False)
back = tk.Button(window, text="edit clr", command=backcolor)
back.place(relx=0.0, rely=0.0, anchor='nw', x=10, y=10)
calce = tk.Button(window, text="wspcalc", command=calc)
calce.place(relx=0.0, rely=0.0, anchor='nw', x=10, y=55)
brows = tk.Button(window, text="browser", command=browser)
brows.place(relx=0.0, rely=0.0, anchor='nw', x=10, y=100)
run = tk.Button(window, text="run", command=runit)
run.place(relx=0.0, rely=1.0, anchor='sw', x=10, y=-10)
clock = tk.Label(window, font=("None", 14))
clock.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-5)
name = tk.Label(window, font=("None", 14), text=f"user: {udun}   /")
name.place(relx=1.0, rely=1.0, anchor='se', x=-100, y=-5)
clocks()
window.mainloop()