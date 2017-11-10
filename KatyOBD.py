import obd
import tkinter as tk
import time
import threading

### OBD Connection

connection = obd.OBD()

### Helper Functions

str_rpm = '0'
str_speed = '0'
str_coolant_temp = '0'
str_fuel_level = '0'
str_intake_temp = '0'
str_throttle_pos = '0'

str_intake_pressure = '0'

indicator = 0

def parseAuto():
    global str_rpm, str_speed, str_coolant_temp, str_fuel_level, str_intake_temp, str_throttle_pos, str_intake_pressure, indicator
    
    while(1):
        
        # Determine Whether Meet the Requirements
        if indicator == 1:
            break
            
        # Parameter Adoptions
        cmd_rpm = obd.commands.RPM
        cmd_speed = obd.commands.SPEED
        cmd_coolant_temp = obd.commands.COOLANT_TEMP
        cmd_fuel_level = obd.commands.FUEL_LEVEL
        
        cmd_intake_temp = obd.commands.INTAKE_TEMP
        cmd_throttle_pos = obd.commands.THROTTLE_POS
        cmd_intake_pressure = obd.commands.INTAKE_PRESSURE
        
        # Assignment of Values to Varible 'Response'
        response_rpm = connection.query(cmd_rpm)
        response_speed = connection.query(cmd_speed)
        response_coolant_temp = connection.query(cmd_coolant_temp)
        response_fuel_level = connection.query(cmd_fuel_level)  
        
        response_intake_temp = connection.query(cmd_intake_temp)
        response_throttle_pos = connection.query(cmd_throttle_pos)
        response_intake_pressure = connection.query(cmd_intake_pressure)  
        
        # Change Obj to String
        str_rpm = str(response_rpm.value)
        str_speed = str(response_speed.value)
        str_coolant_temp = str(response_coolant_temp.value)
        str_fuel_level = str(response_fuel_level.value)   
        
        str_intake_temp = str(response_intake_temp.value)   
        str_throttle_pos = str(response_throttle_pos.value)   
        str_intake_pressure = str(response_intake_pressure.value)
        
        # Delay Parsing Time
        time.sleep(0.01) 

def stopParsing():
    global indicator
    indicator = 1

def about():
    about_root=tk.Tk()
    
    w = 780 # width for the Tk root
    h = 480 # height for the Tk root

    # get screen width and height
    ws = about_root.winfo_screenwidth() # width of the screen
    hs = about_root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    about_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    about_root.title('About Katy OBD')

    label_author=tk.Label(about_root,text='Katy OBD Version 1.0', font=('tahoma', 24))
    label_author.place(x=200,y=60)

    label_author=tk.Label(about_root,text='Copyright (C) 2017', font=('tahoma', 24))
    label_author.place(x=225,y=120)
    
    label_author=tk.Label(about_root,text='Author: Chuan Yang', font=('tahoma', 24))
    label_author.place(x=225,y=180)
    
    label_author=tk.Label(about_root,text='Shengjing Hospital of China Medical University', font=('tahoma', 22))
    label_author.place(x=100,y=240)   

    button_refresh=tk.Button(about_root, width=15, text='OK', font=('tahoma', 24), command=about_root.destroy)
    button_refresh.place(x=230, y=330)

    about_root.mainloop()

### Thread Management

def start_thread(event):
    global thread, indicator
    
    indicator = 0
    
    thread = threading.Thread(target=parseAuto)
    thread.daemon = True
    
    text_rpm.delete('1.0', tk.END)
    text_rpm.insert('1.0', str_rpm)
    text_speed.delete('1.0', tk.END)
    text_speed.insert('1.0', str_speed)
    text_coolant_temp.delete('1.0', tk.END)
    text_coolant_temp.insert('1.0', str_coolant_temp)
    text_fuel_level.delete('1.0', tk.END)
    text_fuel_level.insert('1.0', str_fuel_level)    
    
    text_intake_temp.delete('1.0', tk.END)
    text_intake_temp.insert('1.0', str_intake_temp)    
    text_throttle_pos.delete('1.0', tk.END)
    text_throttle_pos.insert('1.0', str_throttle_pos)
    text_intake_pressure.delete('1.0', tk.END)
    text_intake_pressure.insert('1.0', str_intake_pressure)    
 
    thread.start()
    root.after(20, check_thread)

def check_thread():
    if thread.is_alive():
        text_rpm.delete('1.0', tk.END)
        text_rpm.insert('1.0', str_rpm)
        text_speed.delete('1.0', tk.END)
        text_speed.insert('1.0', str_speed)
        text_coolant_temp.delete('1.0', tk.END)
        text_coolant_temp.insert('1.0', str_coolant_temp)
        text_fuel_level.delete('1.0', tk.END)
        text_fuel_level.insert('1.0', str_fuel_level)    

        text_intake_temp.delete('1.0', tk.END)
        text_intake_temp.insert('1.0', str_intake_temp)    
        text_throttle_pos.delete('1.0', tk.END)
        text_throttle_pos.insert('1.0', str_throttle_pos) 
        text_intake_pressure.delete('1.0', tk.END)
        text_intake_pressure.insert('1.0', str_intake_pressure)    
        
        root.after(20, check_thread)    

### TKinter Mainflow

root = tk.Tk()

root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.attributes('-fullscreen', True)
root.title('Katy OBD -- On Board Diagnostics Parser')
#root.iconbitmap('dna.ico')

y0 = 150
y1 = 400
y2 = 580
y3 = 690

# Label & Edit Box

text_rpm = tk.Text(root, width=10, height=1, font=('tahoma', 80), bd=2, wrap='none')
text_rpm.place(x=50, y=y0)
label_rpm = tk.Label(root, text='RPM', font=('tahoma', 40))
label_rpm.place(x=50,y=y0-100)

text_speed = tk.Text(root, width=10, height=1, font=('tahoma', 80), bd=2, wrap='none')
text_speed.place(x=750, y=y0)
label_speed = tk.Label(root, text='Speed', font=('tahoma', 40))
label_speed.place(x=750,y=y0-100)

# ////////////////////////////

text_coolant_temp = tk.Text(root, width=10, height=1, font=('tahoma', 40), bd=2, wrap='none')
text_coolant_temp.place(x=50, y=y1)
label_coolant_temp = tk.Label(root, text='Coolant Temperature', font=('tahoma', 30))
label_coolant_temp.place(x=50,y=y1-80)

text_fuel_level = tk.Text(root, width=17, height=1, font=('tahoma', 40), bd=2, wrap='none')
text_fuel_level.place(x=650, y=y1)
label_fuel_level = tk.Label(root, text='Fuel Level', font=('tahoma', 30))
label_fuel_level.place(x=650,y=y1-80)
label_fuel_level_percentage = tk.Label(root, text='%', font=('tahoma', 40))
label_fuel_level_percentage.place(x=1200,y=y1)

# ////////////////////////////////////

text_intake_temp = tk.Text(root, width=10, height=1, font=('tahoma', 30), bd=2, wrap='none')
text_intake_temp.place(x=50, y=y2)
label_intake_temp = tk.Label(root, text='Intake Air Temperature', font=('tahoma', 25))
label_intake_temp.place(x=50,y=y2-70)

text_intake_pressure = tk.Text(root, width=10, height=1, font=('tahoma', 30), bd=2, wrap='none')
text_intake_pressure.place(x=500, y=y2)
label_intake_pressure = tk.Label(root, text='Intake Manifold Pressure', font=('tahoma', 25))
label_intake_pressure.place(x=500,y=y2-70)

text_throttle_pos = tk.Text(root, width=10, height=1, font=('tahoma', 30), bd=2, wrap='none')
text_throttle_pos.place(x=950, y=y2)
label_throttle_pos = tk.Label(root, text='Throttle Position', font=('tahoma', 25))
label_throttle_pos.place(x=950,y=y2-70)
label_throttle_pos_percentage = tk.Label(root, text='%', font=('tahoma', 30))
label_throttle_pos_percentage.place(x=1220,y=y2)

# Buttons

button_start = tk.Button(root, text="Start", width=12, font=('tahoma', 30), command=lambda:start_thread(None))
button_start.place(x=50, y=y3)

button_stop = tk.Button(root, text="Stop", width=12, font=('tahoma', 30), command=stopParsing)
button_stop.place(x=400, y=y3)

button_about = tk.Button(root, text="About...", width=12, font=('tahoma', 30), command=about)
button_about.place(x=745, y=y3)

button_exit = tk.Button(root, text="Exit", width=10, font=('tahoma', 30), command=root.destroy)
button_exit.place(x=1100, y=y3)

root.bind('<Return>', start_thread)

root.mainloop()