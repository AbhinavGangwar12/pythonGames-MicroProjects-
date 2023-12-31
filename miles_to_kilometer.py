from tkinter import *
window = Tk()
window.minsize(width=250,height=100)
window.config(padx=10,pady=10)

# Text labels
lbl1 = Label(text="MILES",font=("Arial",10,"bold"),height=1)
lbl1.grid(column=2,row=0)
lbl1.config(padx=5,pady=5)
lbl2 = Label(text="KILOMETERS",font=("Arial",10,"bold"),height=1)
lbl2.grid(column=2,row=1)
lbl2.config(padx=5,pady=5)

# Entry boxes and output box
miles_enter = Entry(width=10)
miles_enter.grid(column=1,row=0)
# miles_enter.config(padx=5,pady=5)
km_enter = Entry(width=10)
km_enter.grid(column=1,row=1)
# km_enter.config(padx=5,pady=5)
lbl = Label(text="0",background="white",font=('arial',9,"normal"))
# lbl.config(padx=5,pady=5)
lbl.grid(column=1,row=1)

# Button to interact with user
def convert():
    kilometer = round(int(miles_enter.get()) * 1.609,3)
    lbl.config(text=f"{kilometer}")

btn = Button(text="Calculate",width=10,command=convert)
btn.grid(column=1,row=2)
btn.config(padx=5,pady=5)

# To keep the window open
window.mainloop()