from tkinter import *

window = Tk()
window.title("My first App")
window.minsize(width=500,height=500)
window.config(padx=20, pady=20)

#label

my_label=Label(text="I am label" ,font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

#Button
def button_clicked():
    input_str = label_input.get()
    my_label.config(text = input_str)
    print("I got clicked!")
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Input
label_input = Entry(width=10)
label_input.grid(column=3, row=2)


# #Text Entry
# text_input=Text(height=5, width=30)
# text_input.focus()
# text_input.insert(END, "Example")
# print(text_input.get("1.0", END))
# text_input.pack()
#
# #spinbox
# def spinbox_used():
#     print(spinbox.get())
#
# spinbox = Spinbox(from_=0, to=10,width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# def scale_used(value):
#     print(value)
# scale=Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbox
# def checkbox_used():
#     print(checked_state.get())
# checked_state=IntVar()
# checkbox = Checkbutton(text="Is on?", variable=checked_state, command=checkbox_used)
# checked_state.get()
# checkbox.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
window.mainloop()