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

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("pomodoro")
window.config(width=300,height=300)

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

canvas = tkinter.Canvas(width=300, height=300)
canvas.config(bg=YELLOW)

tomato_img = resize_image('./tomato.png', 250, 250)
canvas.create_image(150,120, image=tomato_img)
canvas.grid(row=0, column=0)

canvas.create_text(150,150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))





window.mainloop()