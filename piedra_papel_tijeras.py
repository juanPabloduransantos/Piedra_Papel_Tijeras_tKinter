from tkinter import *
from tkinter import messagebox

# -----------------------------
# funciones de la app
# -----------------------------

# -----------------------------
# Ventana principal de la app
# -----------------------------

# Se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto de tipo Tk()

ventana_principal = Tk()

# Titulo de la ventana

ventana_principal.title("Piedra Papel o Tijeras")

# Tamaño de la ventana
ventana_principal.geometry("800x500")

# deshabilitar boton maximizar de la ventana
ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg="white")

# ------------------------
# Variables globales
#-------------------------


# ------------------
# Frame 1
# ------------------

frame_1 = Frame(ventana_principal)
frame_1.config(bg="gray", width=780, height=300)
frame_1.place(x=10,y=10)

# ------------------
# Frame 2 - operaciones
# ------------------

frame_2 = Frame(ventana_principal)
frame_2.config(bg="gray", width=780, height=150)
frame_2.place(x=10,y=325)

# Etiqueta para subtitulo 1 de la app
subtitulo1 = Label(frame_1, text="!PIEDRA, PAPEL O TIJERAS!")
subtitulo1.config(bg="darkgray", fg="red", font=("Arial",20))
subtitulo1.place(x=220,y=30)

# Etiqueta para subtitulo 2 de la app
subtitulo2 = Label(frame_2, text="!ELIJE TU ACCION!")
subtitulo2.config(bg="darkgray", fg="blue", font=("Arial", 10),)
subtitulo2.place(x=333,y=10)

# imagen - logo de la app
logo = PhotoImage(file="img_ppt/ppt.png")
label_logo = Label(frame_1, image=logo)
label_logo.place(x=10, y=10)

# Metodo principal que despliega la ventana en pantalla
ventana_principal.mainloop()