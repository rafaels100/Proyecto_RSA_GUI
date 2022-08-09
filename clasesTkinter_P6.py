from tkinter import *
from PIL import ImageTk, Image
import os, sys
from pyautogui import alert
from random import sample
from RSA_funcion import RSA


class GUI(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        frame_base = Frame(self)
        self.menu = Menu(master=self)
        self.config(menu=self.menu)
        self.progMenu = Menu(self.menu)
        self.funcMenu = Menu(self.menu)
        self.menu.add_cascade(label="Programa", menu=self.progMenu)
        self.menu.add_cascade(label="Funciones", menu=self.funcMenu)
        self.progMenu.add_command(label="Pagina ppal",
                                  command=lambda:self.mostrar_frame(Pagina_ppal))
        self.funcMenu.add_command(label="RSA",
                                 command=lambda:self.mostrar_frame(Pagina_1))
        frame_base.pack()
        self.frames = {}
        self.asientosSelecc = []
        self.largoAsientosSelecc = 0
        #el equivalente a hacer una variable global en este metodo es hacer
        #a las variables que quieras usar en otros frames, parte de la clase ppal,
        #cosa de poder acceder a esas variables mediante controller.variablex

        for F in (Pagina_ppal, Pagina_1):
            frame = F(frame_base, self)
            #Segun estos argumentos que le estoy pasando a las clases
            #del tuple a iterar, el frame_base es el parent y el controller
            #es el objeto de la clase GUI_PSSE que se esta creando.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            
        self.mostrar_frame(Pagina_ppal)
    def mostrar_frame(self, frame):
        frame = self.frames[frame]
        frame.tkraise()

class Pagina_ppal(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
##        ancho = controller.winfo_screenwidth()
##        largo = controller.winfo_screenheight()
##        self.config(width=ancho-300, height=largo)
        self.config(width=500, height=600)
        pathFile = os.path.dirname(os.path.realpath(sys.argv[0]))
        imgName = r"Header_Encryption.png"
        pathImg = pathFile+ r"\\" + imgName
        self.img = ImageTk.PhotoImage(Image.open(pathImg))
        self.label_1 = Label(self, image=self.img)
        self.label_1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.boton_1 = Button(self, text="RSA crypto",
                              command=lambda:controller.mostrar_frame(Pagina_1))
        self.boton_1.place(relx=0.5, rely=0.7, anchor=CENTER)
            
class Pagina_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        largo = controller.winfo_screenheight()
        """
        De esta forma puedo agregar ventanas dentro de cada ventana definida    
        como clase, en este caso, Pagina_1. Las ventanas que van a estar
        adentro de pagina 1 las voy a ir llamando frame1, frame2, etc
        """
        self.label_1 = Label(self, text="Mensaje:")
##        self.label_1.place(relx = 0.1, rely = 0.3, anchor = NW)
        self.label_1.place(x = 20, y = 20)
        self.entry1 = Entry(self)
##        self.entry1.place(relx = 0.1, rely = 0.3, anchor = NW)
        self.entry1.place(x = 80, y = 20)
        self.boton1 = Button(self, text="Enviar",
                             command=lambda:encriptar(self))
##        self.boton1.place(relx = 0.1, rely = 0.3, anchor = NW)
        self.boton1.place(x = 220, y = 20)
##        self.boton2 = Button(self, text="Elegir Nuevamente", command=lambda:resetear(self))
##        self.boton2.place(relx = 0.2, rely = 0.4, anchor = CENTER)
        self.label2 = Label(self, text="Mensaje cifrado:")
        self.label2.place(x = 20, y = 60)
        self.label3 = Label(self)
        self.label3.place(x = 120, y = 60)
        self.label4 = Label(self, text="Ingrese clave privada:")
        self.label4.place(x = 20, y = 100)
        self.entry2 = Entry(self)
        self.entry2.place(x = 150, y = 100)
        self.boton2 = Button(self, text="Desencriptar mensaje:",
                             command=lambda:desencriptar(self))
        self.boton2.place(x = 290, y = 100)
        self.label5 = Label(self)
        self.label5.place(x = 20, y = 140)
        
        
        def encriptar(self):
            self.label3.config(text=RSA(self.entry1.get()))

        def desencriptar(self):
            p = 101
            q = 97
            n = p*q
##            print(self.entry2.get())
            
            C_A = [chr((x**int(self.entry2.get()) % n)) for x in RSA(self.entry1.get())]
            #Junto todas las letras que desencripte en una palabra, el mensaje original
            #de Alice:
            C_A_ = "".join(C_A)
            self.label5.config(text=C_A_)
            

        

        
            
   

"""
Al trabajar con clases de este modo, cada vez que crees un objeto de la clase
botones, dicho objeto se va a pasar como self por default y va a hacer lo que
sea que este en el init method, no es necesario llamar a ninguna funcion, ya
que desde el init method se estan llamando a otras funciones.

"""







