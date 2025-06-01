import tkinter as tk
import time
from Cronometro import creator_chronometer
from Alarma import creator_alarm

time_hours = []
time_minutes = []
time_seconds = []
pause = False

def show_timer():
    frame_timer.pack()
    frame_chronometer.pack_forget()
    frame_alarm.pack_forget()
    
def show_chronometer():
    frame_timer.pack_forget()
    frame_chronometer.pack()
    frame_alarm.pack_forget()

def show_Alarm():
    frame_timer.pack_forget()
    frame_chronometer.pack_forget()
    frame_alarm.pack()

def tempo():
    seconds = int(Entry_seconds.get())
    minutes = int(Entry_minutes.get())
    hours = int(Entry_hours.get())
    global pause
    time_seconds.append(seconds)
    time_minutes.append(minutes)
    time_hours.append(hours)
    
    while pause:
        if seconds == 0 and minutes == 0 and hours == 0:
            break
        
        if seconds == 0 and minutes == 0 and hours >= 0:
            minutes += 60
            Entry_hours.delete(0, tk.END)
            hours -= 1
            Entry_hours.insert(tk.END, str(f"{hours:02d}"))
        
        if seconds == 0:
            seconds += 60
            Entry_minutes.delete(0, tk.END)
            minutes -= 1
            Entry_minutes.insert(tk.END, str(f"{minutes:02d}"))
        
        Entry_seconds.delete(0, tk.END) 
        time.sleep(1)
        seconds -= 1
        Entry_seconds.insert(tk.END, str(f"{seconds:02d}"))
        app.update()

def start_stop():
    global pause
    if  pause == False:
        button_start.config(text="interrumpir", bg="#c0392b")
        pause = True
        button_reboot.config(state=tk.DISABLED)
        tempo()
    else:
        button_start.config(text="Comenzar", bg="#6ad15e")
        pause = False
        button_reboot.config(state=tk.NORMAL)

def reboot():
    Entry_seconds.delete(0, tk.END) 
    Entry_minutes.delete(0, tk.END) 
    Entry_hours.delete(0, tk.END) 
    Entry_seconds.insert(tk.END, f'{time_seconds[-1]:02d}')
    Entry_minutes.insert(tk.END, f'{time_minutes[-1]:02d}')
    Entry_hours.insert(tk.END, f'{time_hours[-1]:02d}')
      
app = tk.Tk()
app.geometry("260x200")
app.configure(background="#1b2631")
app.resizable(height=False,width=False)

frame_timer = tk.Frame(app, background="#1b2631")
frame_chronometer = tk.Frame(app, background="#1b2631")
frame_alarm = tk.Frame(app, background="#1b2631")

Entry_seconds = tk.Entry(frame_timer, width=3, font=("sans", 25), bg="#1b2631", borderwidth=0, fg="#2ecc71")
Entry_minutes = tk.Entry(frame_timer, width=3, font=("sans", 25), bg="#1b2631", border=0, fg="#2ecc71")
Entry_hours = tk.Entry(frame_timer, width=3, font=("sans", 25), bg="#1b2631", border=0, fg="#2ecc71")
Entry_seconds.insert(tk.END, "00")
Entry_minutes.insert(tk.END, "00")
Entry_hours.insert(tk.END, "00")

label = tk.Label(frame_timer, text=":", font=("sans", 30), bg="#1b2631", border=0, fg="#2ecc71")
label2 = tk.Label(frame_timer, text=":", font=("sans", 30), bg="#1b2631", border=0, fg="#2ecc71")

Entry_hours.pack(side=tk.LEFT, padx=(15,0),pady=70)
label.pack(side=tk.LEFT)

Entry_minutes.pack(side=tk.LEFT, pady=20)
label2.pack(side=tk.LEFT)

Entry_seconds.pack(side=tk.LEFT, pady=20)

button_start = tk.Button(frame_timer, text="Comenzar", command=start_stop, width=10, font=("sans", 10), bg="#6ad15e", fg="#fff", border=0)
button_reboot = tk.Button(frame_timer, text="Resets", command=reboot, width=10, font=("sans", 10), bg="#3498db", fg="#fff", border=0)

button_start.pack()
button_start.place(x=15,y=120)
button_reboot.pack()
button_reboot.place(x=130,y=120)

Button_timer = tk.Button(app, text="Timer",width=8,border=0,bg="#212f3c",fg="white", command=show_timer)
Button_timer.place(x=0,y=0)

Button_chronometer = tk.Button(app, text="Chrono",width=7,border=0,bg="#212f3c",fg="white", command=show_chronometer)
Button_chronometer.place(x=86,y=0)

Button_Alarm = tk.Button(app, text="Alarm",width=8,border=0,bg="#212f3c",fg="white", command=show_Alarm)
Button_Alarm.place(x=168,y=0)

creator_chronometer(frame_chronometer)
creator_alarm(frame_alarm)
show_timer()

app.mainloop()