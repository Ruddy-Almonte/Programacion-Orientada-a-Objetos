
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos

class formularioarticulos:
    def __init__(self):
        self.articulo1 = articulos.Articulo()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Formulario de artículos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.cargar_articulos()
        self.consultar_por_codigo()
        self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()
    ...

    def cargar_articulos(self):
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="carga de articulos")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="articulos")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="descripcion: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, texvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Precio")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        # creamos los botones

        self.boton1=ttk.Button(self.labelframe1, text="confirmar", command=self.agregar)
    def agregar (self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("informacion", "los datos fueron cargados correctamente")
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consultar_por_codigo(self):

        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="consulta por codigo")
        self.labelframe2=ttk.Labelframe(self.pagina2, text="articulo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=0)
        self.label1=ttk.Label(self.labelframe2, text="codigo: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="descripcion: ")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Precio: ")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="consultar", command=self.consultar)
        self.boton1.grid(column=0, row=3, padx=4, pady=4)
    def consultar(self):
        datos=(self.codigo.get())
        respuesta=self.articulo1.consulta(datos)
        if len (respuesta) >0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set("")
            self.precio.set("")
            mb.showinfo("informacion", "no existe un articulo con dicho codigo")

    def listado_completo(self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Articulo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado Completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todo()
        self.scrolledtext1.delete(1.0, tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "codigo:"+ str(fila[0])+"\ndescripcion:"+str(fila[1])+"\nprecio:"+str(fila[2])+"\n\n")

aplicacion1=formularioarticulos()


         















