#import tkinter
#m = tkinter.Tk()
'''
widgets are added here
'''
#m.mainloop()
import tkinter as tk

# Texto
root = tk.Tk()
root.title('Título de la ventana')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

l = tk.Label(root, text='::Introduce algo::')
#b.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.5)
b = tk.Button(root, text='🛑', width=24, command=root.destroy)
e = tk.Entry(root)

# Formas de acomodo

# .place()      [posicion absoluta x,y] #
#########################################
#b.place(x=200,y=500)                                       #[coordenadas]
#b.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.2)  #[relativo]



# .pack()       [posicion relativa  LEFT,RIGHT...]
##################################################
#b.pack()
#b.pack(padx=10, pady=10, ipadx=50, ipady=50)
# [padding; margin]

#b.pack(side=tk.TOP, before=b)
# [lado; antes/despues de]

#b.pack(expand=True, fill=tk.BOTH)
#b.pack(expand=False, fill=tk.BOTH)
#b.pack(fill=tk.Y)
# [a donde expandir si muevo ventana]



# .grid(row=y, column=x, columnspan=W)
# [filas, columnas, expansion columnas]
b.grid(row=0,column=1)
e.grid(row=0,column=0, columnspan=2, stick='ns')
#e.grid(row=0,column=0, stick='nsew')
root.mainloop()
