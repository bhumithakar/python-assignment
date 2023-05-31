from tkinter import*
root = Tk()
root.geometry("500x500")

age = StringVar()


e1 = Entry(root, textvariable=data)
e1.pack()

l1 = Listbox(root)
l1.pack()

root.mainloop()
