from tkinter import*
from tkinter import messagebox

libros= []


def anadir():
    t=titulo.get()

    a=autor.get()

    e=editorial.get()

    np= NdePaginas.get()

    fl=fechalimite.get()

    libros.append(t+"$"+a+"$"+e+"$"+str(np)+"$"+fl)

    escribirLibro ()

    messagebox.showinfo ("Guardado", "El libro que tiene que leer ha sido guardado")

    titulo.set("")

    autor.set("")

    editorial.set("")

    NdePaginas.set("")

    fechalimite.set("")

    consultar()


def escribirLibro():

    archivo=open ("biblioteca.txt", "w")

    libros.sort()

    for elemento in libros:

        archivo.write(elemento+"\n")

    archivo.close()

def eliminarLibro():

    eliminado=eliminarlibro.get()

    removido= False

    for elemento in libros:

        arreglo = elemento.split("$")

        if eliminarlibro.get()==arreglo [0]:

            respuesta=messagebox.askyesno ("Eliminar libro", "Desea eliminar el libro con el titulo: \n"+eliminado)

            if respuesta:

                libros.remove (elemento)

                removido=True

                escribirLibro ()

                consultar()

                respuesta=""

        if removido:

            messagebox.showinfo ("Eliminar", "Se ha eliminado el tituno\n"+eliminado)

def salir ():
    sa=messagebox.askyesno("Salir","¿Deseas finalizar?")
    if sa==True:
        quit()

def iniciarArchivo():
    archivo = open("bibioteca.txt", "a")
    archivo.close()

def cargar():

    archivo=open("biblioteca.txt", "r")

    linea = archivo.readline ()

    if linea:

        while linea:

            if linea [-1]=='\n':

                linea=linea [:-1]

            libros.append(linea)

            linea=archivo.readline ()

        archivo.close()



def consultar():

    r=Text (ventana, width=80, height=15)

    libros.sort()

    valores=[]

    r.insert (INSERT, "\tTitulo del libro\n")

    r.insert (INSERT,"----------------------------------------\
--------------------------------------------------\n")

    for elemento in libros:

        arreglo=elemento.split("$")

        valores.append (arreglo [0])

        r.insert (INSERT, "\t"+arreglo [0] +"\n Autor: "+arreglo [1] +
                "\tEditorial: "+arreglo [2]+"\tN° de páginas: "+arreglo [3]+
                 "\tFecha limite:"+arreglo [4]+"\n")
                

        r.insert (INSERT, "--------------------------------------\
-----------------------------------------------------\n")

    spinTitulo=Spinbox (ventana, value= (valores),

        textvariable=eliminarlibro,width=50) .place (x=110, y=450)

    r.place (x=20,y=190)

    if libros==[]:

        
        r.config (state=DISABLED)

ventana=Tk()
titulo=StringVar()
autor=StringVar()
editorial=StringVar()
NdePaginas=IntVar()
fechalimite=StringVar()
eliminarlibro=StringVar()
colorFondo="navajowhite"
colorLetra="black"
iniciarArchivo()
cargar()
consultar()
ventana.title("Relación de Libros que tengo que leer")
ventana.geometry ("700x500")
ventana.configure (background=colorFondo)
etiquetaTitulo =Label (ventana, text="Relación de libros\
    que tengo que leer", bg=colorFondo, fg= colorLetra) .place (x=250,y=10)

eTitulo=Label (ventana, text="Titulo: ", bg=colorFondo\
    ,fg= colorLetra) .place (x=30, y=40)

cTitulo =Entry (ventana, textvariable=titulo, width=50). place (x=120,y=40)
eAutor=Label (ventana, text="Autor: ", bg =colorFondo,\
    fg=colorLetra) .place (x=30,y=70)

cAutor=Entry (ventana, textvariable=autor). place (x=120,y=70)
eEditorial=Label (ventana, text="Editorial: ",\
    bg=colorFondo, fg = colorLetra) .place (x=30, y=100)

cEditorial=Entry (ventana, textvariable=editorial) .place (x=120,y=100) 
eNpaginas=Label (ventana, text="N de páginas: ",\
    bg=colorFondo, fg=colorLetra) .place (x=30, y=130)

cNpaginas=Entry (ventana, textvariable=NdePaginas). place (x=123,y=130) 
eFechaLimite=Label (ventana, text="Fecha limite: ",\
    bg=colorFondo, fg=colorLetra). place (x=30, y=160) 
botonAnadir=Button (ventana, text="Añadir libro",\
    command=anadir, bg="cyan4", fg="white") .place (x=530,y=38)

cFechaLimite=Entry (ventana, textvariable=fechalimite)\
.place (x=120,y=160)

spinTitulo=Label (ventana, text="Titulo leido:",\
    bg= colorFondo, fg= colorLetra) .place (x=30,y=450) 
botonLeido=Button (ventana, text="Libro ya leido",\
    command=eliminarLibro, bg="cyan4",fg= "white") .place (x=526,y=448)

imgbtn=PhotoImage (file="salir.png")

sal =Button (ventana, image=imgbtn, command=salir) .place (x=335, y=60)

ventana.mainloop()