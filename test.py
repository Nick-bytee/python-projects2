import tkinter
from pytube import YouTube

def a():
    pass


root = tkinter.Tk()
root.title("Test")
root.geometry('700x500')

option_list = [1]

value_inside = tkinter.StringVar(root)

value_inside.set("Select an Option")

question_menu = tkinter.OptionMenu(root, value_inside, *option_list)
question_menu.pack()

def print_answers():
    print("Selected Option: {}".format(value_inside.get()))
    return None

submit_button = tkinter.Button(root, text='Submit', command=print_answers)
submit_button.pack()







root.mainloop()