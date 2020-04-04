from tkinter import *

root = Tk()

#Gives GUI window a title
root.title('GUI')
#Defines Size of GUI window
root.geometry("400x50")

#hello command, diplays text entered in the text widget
def hello():
	hello_label = Label(root, text="Hello " + myTextbox.get())
	hello_label.grid(row=1, column=1)

#Label Widget
myLabel = Label(root, text="Enter Your first name:")
myLabel.grid(row=0, column=0)

#Text Widget, takes in text from keyboard
myTextbox = Entry(root, width=30)
myTextbox.grid(row=0, column=1)

#Button Widget, calls hello command
myButton = Button(root, text='Submit', command=hello, bg="blue")
myButton.grid(row=0, column=2)

root.mainloop()
