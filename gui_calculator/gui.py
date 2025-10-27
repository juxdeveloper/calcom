#import tkinter
#m = tkinter.Tk()
'''
widgets are added here
'''
#m.mainloop()
import tkinter as tk

# Texto
root = tk.Tk()
#root.title('Counting Seconds')

l = tk.Label(root, text='Hola we')
l.pack()
b = tk.Button(root, text='Stop', width=25, command=root.destroy)
b.pack()
e = tk.Entry(root)
e.pack()

root.mainloop()

# Entrada
#Label(master, text='First Name').grid(row=0)
#Label(master, text='Last Name').grid(row=1)
#e1 = Entry(master)
#e1.grid(row=0, column=1)
#e2 = Entry(master)
#e2.grid(row=1, column=1)
#mainloop()