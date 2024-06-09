import tkinter
from PIL import Image , ImageTk
import math



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
sprint = 0
current_sprint = [WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,SHORT_BREAK_MIN,LONG_BREAK_MIN]
rounds = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global sprint
    global rounds
    sprint = 0
    window.config(bg="YELLOW")
    rounds = 0
    window.after_cancel(timer)
    return

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def set_label(label_sprint):
    print(f"set_label {label_sprint}")
    title_label.config(text=label_sprint)

def start():
    global sprint
    label_sprint = ""
    print(current_sprint[sprint])
    if current_sprint[sprint] == 25:
        label_sprint = "Good Luck"
        window.config(bg="GREEN")

    else:
        label_sprint = "Break"
        window.config(bg="RED")
    set_label(label_sprint)
    counter(current_sprint[sprint]*60)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    global sprint
    global rounds
    global timer
    if count == 0:
        sprint += 1
        rounds += 1
        start()    
    if count > 0:
        timer = window.after(1000,counter,count-1)
    seconds = count % 60
    minutes = count/60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f'{math.floor(minutes)}:{seconds}')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("pomodoro")
window.config(width=300,height=300,bg=YELLOW)

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

canvas = tkinter.Canvas(width=150, height=150)
canvas.config(bg=YELLOW)

tomato_img = resize_image('./tomato.png', 200, 200)
canvas.create_image(75,75, image=tomato_img)


timer_text = canvas.create_text(75,75, text="25:00", fill="white", font=(FONT_NAME, 20, "bold"))

title_label = tkinter.Label(text="pomodoro",anchor='center',bg=YELLOW)
amount_label = tkinter.Label(text=rounds,bg=YELLOW)

start_button = tkinter.Button(text="start", command=start,bg=GREEN)
reset_button = tkinter.Button(text="reset", command=reset,bg=RED)

canvas.grid(row=4, column=2)
title_label.grid(row=2,column=2,pady=40)
amount_label.grid(row=5, column=2,pady=40)
start_button.grid(row=5, column=0,padx=20,pady=20)
reset_button.grid(row=5, column=5,padx=20,pady=20)




window.mainloop()