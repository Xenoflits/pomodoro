import tkinter
from PIL import Image , ImageTk



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    return

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    counter(25)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    if count > 0:
        window.after(1000,counter,count-1)
    canvas.itemconfig(timer, text=count)


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


timer = canvas.create_text(75,75, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))

title_label = tkinter.Label(text="pomodoro",anchor='center',bg=YELLOW)
amount_label = tkinter.Label(text="V",bg=YELLOW)

start_button = tkinter.Button(text="start", command=start,bg=GREEN)
reset_button = tkinter.Button(text="reset", command=reset,bg=RED)

canvas.grid(row=4, column=2)
title_label.grid(row=2,column=2,pady=40)
amount_label.grid(row=5, column=2,pady=40)
start_button.grid(row=5, column=0,padx=20,pady=20)
reset_button.grid(row=5, column=5,padx=20,pady=20)




window.mainloop()