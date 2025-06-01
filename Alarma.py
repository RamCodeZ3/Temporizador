import tkinter as tk
import time

def creator_alarm(frame_alarm):
    global Entry_minute, Entry_hour, label_time, Button_alarm
    
    label_time = tk.Label(frame_alarm,text="00:00:00",width=11,height=2, font=("sans", 30),fg="#2ecc71",bg="#17202a")
    Entry_minute = tk.Entry(frame_alarm, width=2,font=("sans", 15),bg="#17202a",border=0,fg="#2ecc71")
    label1 = tk.Label(frame_alarm,text=":",font=("sans",15), bg="#1b2631",fg="#2ecc71")
    Entry_hour = tk.Entry(frame_alarm, width=2,font=("sans", 15),bg="#17202a",border=0,fg="#2ecc71")
    Button_alarm = tk.Button(frame_alarm, text="inicia",width=8,font=("sans",10),fg="white",border=0,bg="#3498db",command=alarm)
    
    label_time.pack(pady=(50,10))
    Entry_hour.pack(side=tk.LEFT, padx=(10,0))
    label1.pack(side=tk.LEFT)
    Entry_minute.pack(side=tk.LEFT)
    Button_alarm.pack(side=tk.LEFT, padx=(10,0))

list_hour = []
list_minute = []

def alarm():
 hour = int(Entry_hour.get())
 minute = int(Entry_minute.get())
 list_hour.append(hour)
 list_minute.append(minute)
 Entry_hour.delete(0,tk.END)
 Entry_minute.delete(0,tk.END)
 
 while True:
     time_alarm = time.localtime()
     time_hour = time_alarm.tm_hour
     time_min = time_alarm.tm_min
     label_time.config(text=f"{time_hour:02d}:{time_min:02d}:{time_alarm.tm_sec:02d}",fg="#2ecc71")
     Button_alarm.config(text="configurar")
     label_time.update()
     if list_minute[-1] == time_min and list_hour[-1] == time_hour: 
         label_time.config(text="finalizado", fg="#c0392b")
         label_time.update()
         break