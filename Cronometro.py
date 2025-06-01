import tkinter as tk
import time

pause = False

def creator_chronometer(frame_chronometer):
 global label_seconds,label_minutes,label_hours,button_start_chronometer,button_reboot_chronometer
 
 label_seconds = tk.Label(frame_chronometer,text="00s",font=("sans", 25), bg="#1b2631",fg="#5198f3")
 label_hours = tk.Label(frame_chronometer,text="00h",font=("sans", 25), bg="#1b2631",fg="#1b2631")
 label_minutes = tk.Label(frame_chronometer,text="00m",font=("sans", 25), bg="#1b2631",fg="#1b2631")
 
 label_seconds.pack(side=tk.RIGHT,padx=5, pady=60)
 label_minutes.pack(side=tk.RIGHT,padx=5, pady=60)
 label_hours.pack(side=tk.RIGHT,padx=5, pady=60)

 button_start_chronometer = tk.Button(frame_chronometer, text="Comenzar",border=0,bg="#3498db",fg="white",command=start_stop)
 button_reboot_chronometer = tk.Button(frame_chronometer, text="Reiniciar",border=0,bg="#e67e22",fg="white",command=reboot_chronometer)
 button_start_chronometer.place(x=140,y=120)
 button_reboot_chronometer.place(x=50, y=120)
 
seconds = 0
minutes = 0
hours = 0
 
def start_chronometer():
 global pause, seconds, minutes, hours
 while pause:
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
            label_minutes.config(text=str(f"{minutes:02d}m"),fg="#5198f3") 
            if minutes == 60:
             minutes = 0
             hours += 1
             label_hours.config(text=str(f"{hours:02d}h"),fg="#5198f3")

        label_seconds.config(text=str(f"{seconds:02d}s"))
        time.sleep(1)
        label_seconds.update()

def start_stop():
    global pause
    if  pause == False:
        button_start_chronometer.config(text="interrumpir", bg="#c0392b")
        pause = True
        start_chronometer()
    else:
        button_start_chronometer.config(text="Comenzar", bg="#3498db")
        pause = False

def reboot_chronometer():
    global seconds,minutes,hours
    seconds = 0
    minutes = 0
    hours = 0
    label_seconds.config(text=str(f"{seconds:02d}s"))
    label_minutes.config(text=str(f"{minutes:02d}m"))
    label_hours.config(text=str(f"{hours:02d}h"))