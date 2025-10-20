#!/usr/bin/env python3

import tkinter as tk
import socket
import psutil

def percent():
    cpupercent = psutil.cpu_percent(interval=1, percpu=True)
    label.config(text=str(f"{cpupercent} %"), font=("Freesans", 15), bg="grey", fg="black")
    root.after(1000, percent) # Schedule this function to run again after 1000ms (or 1 second).

def freq():
    cpufreq = psutil.cpu_freq()
    label4.config(text=str(f"{cpufreq.current:.2f} MHz"), font=("Freesans", 15), bg="grey", fg="black")
    root.after(1000, freq) # Schedule this function to run again after 1000ms (or 1 second).

def get_cpu_temperature():
    sensors = psutil.sensors_temperatures()
    # Common keys for CPU temperature: 'coretemp' (Intel), 'cpu_thermal' (some systems)
    if 'coretemp' in sensors:
        return sensors['coretemp'][0].current
    elif 'cpu_thermal' in sensors:
        return sensors['cpu_thermal'][0].current
    else:
        # Print available sensors if none match
        print("Available temperature sensors:", list(sensors.keys()))
        return None

def temp():
    cputemp = get_cpu_temperature()
    label5.config(text=str(f"{cputemp} °C"), font=("Freesans", 15), bg="grey", fg="black")
    root.after(2000, temp)

def mem():
     percent_used = psutil.virtual_memory().percent
     label2.config(text=str(f"{percent_used} %"), font=("Freesans", 15), bg="grey", fg="black")
     root.after(3000, mem)

def ram_avail():
     mem_avail = psutil.virtual_memory().available / (1024 ** 3)
     label3.config(text=str(f"{mem_avail:.2f} GB"), font=("Freesans", 15), bg="grey", fg="black")
     root.after(3000, ram_avail)

## Window stuff
root = tk.Tk()

# Title for app
root.title('Info')

# Icon for app
icon = tk.PhotoImage(file="icon.png")
root.iconphoto(False, icon)

# Set the window size
#root.geometry("230x280")

# Change the background color using configure
root.configure(bg='grey')

label = tk.Label(root)
label4 = tk.Label(root)
label5 = tk.Label(root)
label2 = tk.Label(root)
label3 = tk.Label(root)
cpu = tk.Label(root, text="CPU usage", font=("Freesans", 16, "bold"), bg="grey", fg="black")
cpu.pack()
label.pack()

cpuFreq = tk.Label(root, text="CPU frequenzy", font=("Freesans", 16, "bold"), bg="grey", fg="black")
cpuFreq.pack()
label4.pack()



cpuTemp = tk.Label(root, text="CPU temp", font=("Freesans", 16, "bold"), bg="grey", fg="black")
cpuTemp.pack()
label5.pack()

mempro = tk.Label(root, text="RAM usage", font=("Freesans", 16, "bold"), bg="grey", fg="black")
mempro.pack()
label2.pack()

memavail = tk.Label(root, text="RAM available", font=("Freesans", 16, "bold"), bg="grey", fg="black")
memavail.pack()
label3.pack()

percent()
freq()
mem()
ram_avail()
temp()

root.mainloop()
