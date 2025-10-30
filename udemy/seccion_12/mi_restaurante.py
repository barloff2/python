from tkinter import *
from os import system
import random
import datetime
from tkinter import filedialog, messagebox

system('cls')

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


# Función para los botones
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


# Funcion para borrar pantalla
def borrar():
    global operador
    visor_calculadora.delete(0, END)
    operador = ''


# Obtener resultado
def obtener_resultado():
    global operador
    operador = operador.replace('x', '*')
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


# Función para revisar el check
def revisar_check(variables, cuadros, textos):
    i = 0
    for i, var in enumerate(variables):
        if var.get() == 1:
            cuadros[i].config(state=NORMAL)
            if cuadros[i].get() == '0':
                cuadros[i].delete(0, END)
            cuadros[i].focus()
        else:
            cuadros[i].config(state=DISABLED)
            textos[i].set('0')


# Función total
def total():
    # Subtotal comida
    sub_total_comida = 0
    for i, cantidad in enumerate(texto_comida):
        sub_total_comida = sub_total_comida + float(cantidad.get()) * precios_comida[i]

    # Subtotal bebida
    sub_total_bebida = 0
    for i, cantidad in enumerate(texto_bebida):
        sub_total_bebida = sub_total_bebida + float(cantidad.get()) * precios_bebida[i]

    # Subtotal postres
    sub_total_postres = 0
    for i, cantidad in enumerate(texto_postre):
        sub_total_postres = sub_total_postres + float(cantidad.get()) * precios_postres[i]

    # Calculo subtotal
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres

    # Calculo impuestos
    impuestos = sub_total * 0.07

    # Total
    total = sub_total + impuestos

    # Mostras Costo comida
    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')

    # Mostras Costo bebida
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')

    # Mostras Costo postre
    var_costo_postre.set(f'$ {round(sub_total_postres, 2)}')

    # Mostrar subtotal
    var_subtotal.set(f'$ {round(sub_total, 2)}')

    # Mostrar impuestos
    var_impuesto.set(f'$ {round(impuestos, 2)}')

    # Mostrar total
    var_total.set(f'$ {round(total, 2)}')


# Funcion recibo
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day} / {fecha.month} / {fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    for i, comida in enumerate(texto_comida):
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[i]}\t\t{comida.get()}\t'
                                     f'$ {int(comida.get()) * precios_comida[i]}\n')

    for j, bebida in enumerate(texto_bebida):
        if bebida.get() != '0':
            print(int(bebida.get()) * precios_bebida[j])
            texto_recibo.insert(END, f'{lista_bebidas[j]}\t\t{bebida.get()}\t'
                                     f'$ {int(bebida.get())}\n')

    for k, postre in enumerate(texto_postre):
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[k]}\t\t{postre.get()}\t'
                                     f'$ {int(postre.get()) * precios_postres[k]}\n')

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')


# Funcion guardar
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode=W,
                                       defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')


# Funcion resetear
def rasetear():
    texto_recibo.delete(1.0, END)

    for i, texto in enumerate(texto_comida):
        # reset cantidad
        texto.set('0')
        texto_bebida[i].set('0')
        texto_postre[i].set('0')
        # Reset texto
        cuadros_comida[i].config(state=DISABLED)
        cuadros_bebida[i].config(state=DISABLED)
        cuadros_postre[i].config(state=DISABLED)
        # Reset variable comida
        variables_comida[i].set(0)
        variables_bebida[i].set(0)
        variables_postre[i].set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# Iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1070x630+0+0')

# Evitar maximizar
aplicacion.resizable(False, False)

# Titulo de la ventana
aplicacion.title('Restaurante Vatenina - Sistema de Facturación')

# Color de fondo de la ventana
aplicacion.config(bg='burlywood')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de facturación',
                        fg='azure4', font=('Dosis', 58), bg='burlywood',
                        width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierda
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=30)
panel_costos.pack(side='bottom')

# Panel Comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida',
                           font=('Dosis', 19, 'bold'), bd=1,
                           relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas',
                           font=('Dosis', 19, 'bold'), bd=1,
                           relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres',
                           font=('Dosis', 19, 'bold'), bd=1,
                           relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel Dercha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT,
                          bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT,
                     bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT,
                      bg='burlywood')
panel_botones.pack()

# Lista de productos

lista_comidas = ['Frijol', 'Pollo', 'Carne', 'Salmon', 'Chicharron',
                 'Hamburguesa', 'Pizza', 'Hotdog']
lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Gaseosa', 'Vino',
                 'Cerveza', 'Malteada', 'Café']
lista_postres = ['Helado', 'Fruta', 'Brownies', 'Flan', 'Mousse',
                 'Pastel1', 'Pastel2', 'Pastel3']


# generar items comida

variables_comida = []
cuadros_comida = []
texto_comida = []

# Checkbuttom loop de creación

contador = 0
for comida in lista_comidas:
    # Crear checkbuttom
    # Creación de variable
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=lambda: revisar_check(variables_comida, cuadros_comida, texto_comida))
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     width=6,
                                     state='disabled',
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# generar items Bebidas

variables_bebida = []
cuadros_bebida = []
texto_bebida = []

# Checkbuttom loop de creación

contador = 0
for bebida in lista_bebidas:
    # Crear checkbuttom
    # Creación de variable
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=lambda: revisar_check(variables_bebida, cuadros_bebida, texto_bebida))
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     width=6,
                                     state='disabled',
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1
# generar items postres

variables_postre = []
cuadros_postre = []
texto_postre = []

# Checkbuttom loop de creación

contador = 0
for postre in lista_postres:
    # Crear checkbuttom
    # Creación de variable
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command=lambda: revisar_check(variables_postre, cuadros_postre, texto_postre))
    postre.grid(row=contador, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     width=6,
                                     state='disabled',
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Lista de variables costo

var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()
# Etiquetas de costo y campos de entrada comida

etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0,
                           column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,
                        column=1,
                        padx=65)


# Etiquetas de costo y campos de entrada bebida

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1,
                           column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,
                        column=1,
                        padx=65)

# Etiquetas de costo y campos de entrada postre

etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2,
                           column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2,
                        column=1,
                        padx=65)

# Etiquetas de costo y campos de entrada subtotal

etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_subtotal.grid(row=0,
                       column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0,
                    column=3,
                    padx=65)

# Etiquetas de costo y campos de entrada impuesto

etiqueta_impuesto = Label(panel_costos,
                          text='impuesto',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_impuesto.grid(row=1,
                       column=2)

texto_impuesto = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_impuesto)
texto_impuesto.grid(row=1,
                    column=3,
                    padx=65)

# Etiquetas de costo y campos de entrada total

etiqueta_total = Label(panel_costos,
                       text='total',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_total.grid(row=2,
                    column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2,
                 column=3,
                 padx=65)

# Botones

botones = ['total', 'recibo', 'guardar', 'resetear']
funcion_botones = [total, recibo, guardar, rasetear]
for i, boton in enumerate(botones):
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9,
                   command=funcion_botones[i])
    boton.grid(row=0,
               column=i)

# Area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

# Botones calculadora

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'Resultado', 'Borrar', '0', '/']

fila = 1
columna = 0
for texto in botones_calculadora:
    if texto == 'Borrar':
        comando = lambda t=texto: borrar()
    elif texto == 'Resultado':
        comando = lambda t=texto: obtener_resultado()
    else:
        comando = lambda t=texto: click_boton(t)
    boton = Button(panel_calculadora,
                   text=texto.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8,
                   command=comando)
    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0

# Evitar que la pantalla de cierre
aplicacion.mainloop()
