from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#003049"
RED = "#669BBC"
GREEN = "#003049"
YELLOW = "#FDF0D5"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_str=""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check_str
    global reps
    window.after_cancel(timer)
    check_str = ""
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="Timer")
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps % 2 == 0:
        count_down(WORK_MIN*60)
        reps+=1
        text_label.config(text="Work")
    elif reps == 7:
        count_down(LONG_BREAK_MIN*60)
        reps=0
        text_label.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN*60)
        reps += 1
        text_label.config(text="Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    global reps
    global check_str
    count_min=count // 60
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec=count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 != 0:
            check_str+="✔"
            check_mark.config(text=check_str)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
text_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
text_label.grid(row=0, column=1)
check_mark = Label(fg=RED, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark.grid(row=3, column=1)

st_button=Button(text="Start", highlightthickness=0, command=start_timer)
st_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()