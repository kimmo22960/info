#!/usr/bin/env python3

import tkinter as tk
import socket
import psutil

def percent():
    cpupercent = psutil.cpu_percent(interval=1, percpu=True)
    label.config(text=str(cpupercent), font=("Freesans", 15))
    root.after(1000, percent) # Schedule this function to run again after 1000ms (or 1 second).

def freq():
    cpufrequenzy = psutil.cpu_freq()
    label2.config(text=str(cpufrequenzy), font=("Freesans", 15))
    root.after(1000, freq) # Schedule this function to run again after 1000ms (or 1 second).

root = tk.Tk()
label = tk.Label(root)
label2 = tk.Label(root)
cpu = tk.Label(root, text="CPU %", font=("Freesans", 20, "bold"))
cpu.pack()
label.pack()

cpufreq = tk.Label(root, text="CPU frequenzy", font=("Freesans", 20, "bold"))
cpufreq.pack()
label2.pack()

percent() # start the event loop with an initial call to update_label().
freq()

root.mainloop()
