# even=[2,4,6,8]
# odd=[1,3,5,7,9]
# numbers=[even,odd]
# for number_set in numbers:
#     print(number_set)
#     for values in number_set:
#         print(values)


# import tkinter
# tkinter._test()

from tkinter import *
# top = tkinter.Tk()
# top.mainloop()

# root = Tk()
# var = stringVar()
# label = Label( root, textvariable=var, cursor="dot", font=)
#
# var.set("Global Opportunties")
# label.pack()
# root.mainloop()


# top = Tk()
# L1 = Label(top,text= "User Name").grid(row=0)
# L2 = Label(top,text= "Name").grid(row=1)
# L3 = Label(top,text= "Father's Name").grid(row=2)
# L4 = Label(top,text= "Mobile No.").grid(row=3)
# E1= Entry(top).grid(row=0, column=1)
# E2= Entry(top).grid(row=1, column=1)
# E3= Entry(top).grid(row=2, column=1)
# E4= Entry(top).grid(row=3, column=1)
# top.mainloop()


# import tkinter as tk
# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()


# top=Tk()
# top.geometry("100x100")
# def hello():
#     messagebox.showinfo("Say Hello","Welcome to python programming")
# B1=Button(top,text="Say Hello",command="hello")
# B1.place(x=30,y=30)
# top.mainloop()

# from tkinter as tk
# def show_entry_fields():
#     print(f"First Name: {e1.get()}\n Last Name: {e2.get()}")
# master = tk.Tk()
# tk.label(master,text="First Name").grid(row=0)
# tk.label(master,text="Last Name").grid(row=1)
#
# e1=tk.Entry(master)
# e2=tk.Entry(master)
#
# e1.grid(row=0, column=1)
# e1.grid(row=0, column=1)
#
# tk.button(master,text='Quit',command=master.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
# tk.button(master,text="show", command=show_entry_fields).grid(row=3,column=1,sticky=tk.w,padt=4)
# tk.mainloop()


# top = Tk()
# listbox= Listbox(top)
# listbox.insert(1, "Physics")
# listbox.insert(2, "Manga")
# listbox.insert(3, "Qunatum Physics")
# listbox.insert(4, "Astronomy")
# listbox.pack()
# top.mainloop()


# root = Tk()
# frame = Frame(root)
# frame.pack()
# bottomframe = Frame(root)
# bottomframe.pack(side=BOTTOM)
# redbutton = Button(frame, text='Red', fg='red')
# redbutton.pack(side=LEFT)
# greenbutton = Button(frame, text='Brown', fg='brown')
# greenbutton.pack(side=LEFT)
# bluebutton = Button(frame, text='Blue', fg='blue')
# bluebutton.pack(side=LEFT)
# blackbutton = Button(bottomframe, text='Black', fg='black')
# blackbutton.pack(side=BOTTOM)
# root.mainloop()



import numpy as np
# list = np.array(list)
# arr = np.array(list)
# print(type(arr))


# arr= np.array(43)
# print(arr)
# print(type(arr))
# print(arr.ndim)

# arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr[0,1,2])


arr=np.array([1,2,3,4,5,6])
print(arr)
print(arr[0:5:2])