from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=40, pady=40)

my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)

def m_to_km():
    km = float(inputs.get())
    km *= 1.6
    my2_label.config(text=km)

inputs = Entry(width=10)
inputs.grid(column=1, row=0)

my2_label = Label(text="0")
my2_label.grid(column=1, row=1)

myButton = Button(text="Calculate", width=10, command=m_to_km)
myButton.grid(column=1, row=2)

my3_label = Label(text="Miles")
my3_label.grid(column=2, row=0)

my4_label = Label(text="Km")
my4_label.grid(column=2, row=1)

# class Car:
#
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#
# my_car = Car(make="Nissan", model="idk")
# print(my_car)

window.mainloop()