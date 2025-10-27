from tkinter import *

# widgets: ELEMENTOS DE LA GUI, botones, cajas de texto, labels, imágenes, etc.
# windows: contenedor

ventana1 = Tk() #instanciar una ventana
#ventana1.geometry("820x820") #tamaño, largo * alto
ventana1.title("TESTESTESTESTTESTESTESTESTTESTESTESTEST")
ventana1.config(background="#FFC180")

img1 = PhotoImage(file='TESTS/TEST_GUI/TEST_img/icon.png') #convierte la imagen a un formato que tkinter puede usar de icono
ventana1.iconphoto(True,img1) #mostrar, variable

'''
LABEL
txt1 = Label(ventana1,
    text="bro, do you even code?",
    font=('Arial',20,'bold'),
    fg="#FF8303",
    bg="#FFC180",
    relief=RAISED,
    bd=10,
    padx=20,
    pady=30,
    image=img1,
    compound='bottom')

txt1.place(x=310,y=220)
'''

'''
BUTTON
contador = 0

def click():
    global contador
    contador += 1
    print(contador)

boton1 = Button(ventana1,
    text="click me!",
    command=click,
    font=("Arial",20),
    fg="#00FF00",
    bg="#FF0000",
    activeforeground="#00FF00",
    activebackground="#FF0000",
    #state=DISABLED
    image=img1,
    compound='bottom')
boton1.place(x=310,y=220)
'''

'''
TEXT BOX
def enviar():
    r = txtbox1.get()
    print("R => "+r)
    txtbox1.config(state=DISABLED)

def borrar():
    txtbox1.delete(0,END)

def retroceder():
    txtbox1.delete(len(txtbox1.get())-1,END)

txtbox1 = Entry(ventana1,
    font=("Arial",50),
    show=" ")
txtbox1.pack(side=LEFT)

enviar = Button(ventana1,
    text="Enviar",
    font=("Arial",10),
    command=enviar)
enviar.pack(side=RIGHT)

borrar = Button(ventana1,
    text="Borrar",
    font=("Arial",10),
    command=borrar)
borrar.pack(side=RIGHT)

retroceder = Button(ventana1,
    text="Retroceder",
    font=("Arial",10),
    command=retroceder)
retroceder.pack(side=RIGHT)
'''

'''
CHECKBOX
def imprimir():
    if(aceptado.get()):
        print("Has aceptado el contrato malvado! >:D")
    else:
        print("Has rechazado el contrato! D:<")

aceptado = BooleanVar()

check = Checkbutton(ventana1,
    text="Acepto!",
    variable=aceptado,
    onvalue=True,
    offvalue=False,
    command=imprimir,
    font=('Arial',30),
    fg="#00FF00",
    bg="#000000",
    activeforeground="#00FF00",
    activebackground="#000000",
    padx=25,
    pady=25,
    image=img1,
    compound='left')
check.pack()
'''

'''
RADIOBUTTON
comida = ["Pizza","Hamburguesa","Hot Dog"]

def orden():
    if(x.get()==0):
        print("Ordenaste Pizza!")
    elif(x.get()==1):
        print("Ordenaste Hamburguesa!")
    else:
        print("Ordenaste Hot dog!")

x = IntVar()

for i in range(len(comida)):
    grupo_comida = Radiobutton(ventana1,
        text=comida[i],
        variable=x,
        value=i, #asigna a cada boton un valor distinto
        padx=10,
        pady=10,
        fg="#75150e",
        bg="#FFC180",
        font=("Arial",50),
        indicatoron=0,
        width='15',
        command=orden
        )
    grupo_comida.pack(anchor=W)
'''

'''
SCALE
img3 = PhotoImage(file='TEST/img_TEST/img3.png')
img3_label = Label(image=img3)
img3_label.pack()

def imprimir():
    print("La temperatura actual es de => "+str(escala_temperatura.get())+"°")

escala_temperatura = Scale(ventana1,
    from_=100,
    to=0,
    length=800,
    orient=VERTICAL,
    font=("Consolas",10),
    tickinterval=10,
    #showvalue=0,
    resolution=5,
    troughcolor="#69EAFF",
    fg="#FF1C00",
    bg="#111111"
    )
escala_temperatura.set(((escala_temperatura['from']-escala_temperatura['to'])/2)+escala_temperatura['to'])
escala_temperatura.pack()

img2 = PhotoImage(file='TEST/img_TEST/img2.png')
img2_label = Label(image=img2)
img2_label.pack()

btn_registrar = Button(ventana1,
    text="REGISTRAR",
    font=("Arial",15),
    padx=15,
    pady=15,
    command=imprimir)
btn_registrar.pack()
'''

def enviar():
    if(lista.get(lista.curselection())=="Pizza"):
        print("pizzatime:D")
    else:
        print(lista.get(lista.curselection()))
    
def añadir():
    lista.insert(lista.size(),entrada.get())
    lista.config(height=lista.size())

def borrar():
    lista.delete(lista.curselection())
    lista.config(height=lista.size())

lista = Listbox(ventana1,
    bg="#f7ffde",
    font=("Constantia",30),
    width=12)

lista.insert(1,"Pizza")
lista.insert(2,"Pasta")
lista.insert(3,"Pan de ajo")
lista.insert(4,"Sopa")
lista.insert(5,"Ensalada")

lista.config(height=lista.size())

lista.pack()

entrada = Entry(ventana1)
entrada.pack()

btn_enviar = Button(ventana1,text="Enviar",command=enviar)
btn_enviar.pack()

btn_añadir = Button(ventana1,text="Añadir",command=añadir)
btn_añadir.pack()

btn_borrar = Button(ventana1,text="Borrar",command=borrar)
btn_borrar.pack()

ventana1.mainloop() #desplegarla en pantalla