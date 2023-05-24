from tkinter import*

#-----------------
#variables globales
#------------------

BASE=460
ALTURA=220

#----------------------
#ventana principal
#----------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#-----------------------
#frame de graficacion
#-----------------------

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10,y=10)

#creacion canvas

c= Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

""""#dibujar una linea recta
linea_1 = c.create_line(BASE/2, ALTURA/2, BASE,0, fill="red", width=2)
linea_2 = c.create_line(BASE,ALTURA, BASE/2, ALTURA/2,fill="thistle", width=2)
linea_3 = c.create_line(0, ALTURA, BASE/2, ALTURA/2, fill="blue", width=2)
linea_4 = c.create_line(0,0, BASE/2, ALTURA/2, fill="green", width=2)
linea_5 = c.create_line(0,ALTURA/2, BASE/2, ALTURA/2, fill="medium purple", width=2)
linea_6 = c.create_line(BASE,0/2, BASE/2, ALTURA/2, fill="cyan", width=2)
linea_7 = c.create_line(BASE/2, ALTURA/2, BASE,ALTURA/2, fill="white", width=2)

#dibujar texto
texto_1 = c.create_text(BASE/4, ALTURA/2, anchor="center", text="sistemas!", font=("Arial",25, "bold"),fill="blue",
activefill="cyan")
texto_2 = c.create_text(3*BASE/4, ALTURA/2, anchor="center", text="colegio", font=("Arial",25, "bold"),fill="blue",
activefill="cyan")
texto_3 = c.create_text(BASE/2, ALTURA/4, anchor="center", text="especialidad",font=("Arial",25, "bold"), fill="thistle",
activefill="cyan")
texto_4 = c.create_text(BASE/2,ALTURA/1.5, anchor="center", text="guanenta",font=("Arial",25, "bold"), fill="thistle",
activefill="cyan")

#dibujar rectangulo
rect_1 = c.create_rectangle(BASE/2,ALTURA/2, BASE,ALTURA, fill="pink", outline="blue")
rect_2 = c.create_rectangle(0,0, 0.5*BASE/2,1*ALTURA/2, fill="lime green", outline="black")


#dibujar circulos
circ_1 = c.create_oval(BASE/2,0,BASE,ALTURA/2, fill="orange")
circ_2 = c.create_oval(0,ALTURA/2,BASE/4,ALTURA, fill="yelow")
circ_3 = c.create_oval(BASE/4,ALTURA/2,BASE/2,ALTURA, fill="red") 



#dibijar ṕoligonos
polig_1= c.create_polygon(3*BASE/4,ALTURA/2,BASE,ALTURA,BASE/2,ALTURA,fill="red")
polig_2= c.create_polygon(BASE/1,0,BASE/2,ALTURA/4,BASE/4,ALTURA/2,0,ALTURA/4, fill="white", outline="black")"""""

#dibujar cruz
polig_3 = c.create_polygon(0,0/4,fill="thistle")
#--------------------
#frame de controles
#-------------------

frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

#desplegar ventana
ventana_principal.mainloop()