import tkinter as tk
import random

#APP WINDOWS DIMENSIONS
root= tk.Tk()
root.geometry('500x300')

#APP CUSTOM FUNCTION
def randomNum():
    num1= int(entry1.get())
    num2= int(entry2.get())
    digit= random.randint(num1, num2)
    data3= tk.Label(root, text=f"""Here's a Randomly Gassed Number For You: {digit}""")
    data3.place(x=110, y=200)


#LABEL FOR THE APP
head= tk.Label(root, text='~~~~~RANDOM NUMBER GENERATOR~~~~~', font='Times 14 bold')
data1= tk.Label(root, text='Enter Your First Value:', font='Times 10 bold italic')
data2= tk.Label(root, text='Enter Your Second Value:', font='Times 10 bold italic')

#LABEL PLACEMENT KEYS
head.place(x=50, y=30)
data1.place(x=60, y=70)
data2.place(x=60, y=120)

#ENTRY FOR THE APP
entry1= tk.Entry(root)
entry2= tk.Entry(root)

#ENTRY PLACEMENT KEYS
entry1.place(x=250, y=70)
entry2.place(x=280, y=120)

#BUTTON FOR THE APP
button= tk.Button(root, text='CLICK HERE TO GENERATE', font='Times 8 underline', command= randomNum )

#BUTTON PLACEMENT KEY
button.place(x=150, y=160)


#APP WINDOW POPUP
root.mainloop()