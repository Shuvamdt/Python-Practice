from tkinter import *

window = Tk()
window.title("Miles to Kilometer")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(border=4, width=10)
miles_input.grid(row=0, column=1)

input_label = Label(text="Miles")
input_label.grid(row=0, column=2)

text_label1 = Label(text = "is equal to")
text_label1.grid(row=1, column=0)

text_output = Label(text = "0")
text_output.grid(row=1, column=1)

text_label2 = Label(text= "Km")
text_label2.grid(row=1, column=2)

def cal_miles_to_km():
    miles = miles_input.get()
    km = float(miles)* 1.6
    text_output.config(text=f"{round(km)}")

button = Button(text="Calculate", command=cal_miles_to_km)
button.grid(column=1, row=2)

window.mainloop()