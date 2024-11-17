import tkinter as tk
from ejercicios import *

#Grupo 2
# Mario De Jesus Suero De Leon 2024-0263
# Gabriel Sánchez Reynoso 2024-0269
# Idelka Rodriguez 2024-0255
# Danuel Ezequiel Cuevas Tejeda 2024-0250



def abrir_menuprincipal():
    ventana_inicio.destroy()

    
#Segunda ventana
    global menuinicial
    menuinicial = tk.Toplevel()
    menuinicial.title("Menú Principal")
    menuinicial.geometry("")
    menuinicial.resizable(False,False)
    
    mensaje_menu_principal = tk.Label(menuinicial, text="Este es el Menú Principal", font=("Arial", 14))
    mensaje_menu_principal.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta0 = tk.Label(menuinicial, text="Programación Orientada a Objetos (POO)")
    etiqueta0.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta1 = tk.Label(menuinicial, text="1- Definir la clase Persona con atributos y métodos.")
    etiqueta1.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta2 = tk.Label(menuinicial, text="2- Crear la clase Cuenta con métodos de ingreso, reintegro y transferencia.")
    etiqueta2.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta3 = tk.Label(menuinicial, text="3- Implementar la clase Fracción con métodos para operaciones básicas.")
    etiqueta3.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta4 = tk.Label(menuinicial, text="4- Desarrollar la clase Complejo con métodos para operaciones.")
    etiqueta4.grid(row=5, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta5 = tk.Label(menuinicial, text="5- Crear las clases Cliente y Banco para manejo de depósitos y extracciones.")
    etiqueta5.grid(row=6, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta6 = tk.Label(menuinicial, text="6- Desarrollar la clase Cuenta con subclases PlazoFijo y CajaAhorro.")
    etiqueta6.grid(row=7, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta7 = tk.Label(menuinicial, text="Ciclos")
    etiqueta7.grid(row=8, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta8 = tk.Label(menuinicial, text="7- Solicitar notas de 10 alumnos e informar aprobados y suspendidos.")
    etiqueta8.grid(row=9, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta9 = tk.Label(menuinicial, text="8- Registrar sueldos de empleados e informar sobre sueldos y total gastado.")
    etiqueta9.grid(row=10, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta10 = tk.Label(menuinicial, text="9- Solicitar notas de 10 alumnos e informar aprobados y suspendidos (repetido).")
    etiqueta10.grid(row=11, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta11 = tk.Label(menuinicial, text=" 10- Cargar 10 números e imprimir la suma de los últimos 5.")
    etiqueta11.grid(row=12, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta12 = tk.Label(menuinicial, text="11- Solicitar un número del 1 al 10 y mostrar su tabla de multiplicar.")
    etiqueta12.grid(row=13, column=0, sticky="ew", padx=10, pady=5)
    
    etiqueta13 = tk.Label(menuinicial, text="12- Ingresar coordenadas x e y y contar puntos en cuadrantes.")
    etiqueta13.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
    
    etiqueta14 = tk.Label(menuinicial, text="13- Leer lados de n triángulos e informar su clasificación.")
    etiqueta14.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
    
    etiqueta15 = tk.Label(menuinicial, text="Funciones")
    etiqueta15.grid(row=3, column=1, sticky="ew", padx=10, pady=5)
    
    etiqueta16 = tk.Label(menuinicial, text="14- Crear funciones para calcular cuadrado y producto de enteros.")
    etiqueta16.grid(row=4, column=1, sticky="ew", padx=10, pady=5)
    
    etiqueta17 = tk.Label(menuinicial, text="15- Desarrollar una función que cuente vocales en un string.")
    etiqueta17.grid(row=5, column=1, sticky="ew", padx=10, pady=5)
    
    etiqueta18 = tk.Label(menuinicial, text="16- Cargar una lista de n enteros y separar positivos y negativos.")
    etiqueta18.grid(row=6, column=1, sticky="ew", padx=10, pady=5)
    
    etiqueta19 = tk.Label(menuinicial, text="17- Recibir edades y contar mayores de 18.")
    etiqueta19.grid(row=7, column=1, sticky="ew", padx=10, pady=5)
    
    etiqueta20 = tk.Label(menuinicial, text="Manipulación de Cadenas")
    etiqueta20.grid(row=8, column=1, sticky="ew", padx=10, pady=5)
    
    etiqueta21 = tk.Label(menuinicial, text="18- Solicitar un string y mostrar su longitud y manipulación de casos.")
    etiqueta21.grid(row=9, column=1, sticky="ew", padx=10, pady=5)

    etiqueta22 = tk.Label(menuinicial, text="Validación y Juegos")
    etiqueta22.grid(row=10, column=1, sticky="ew", padx=10, pady=5)
    
    etiqueta23 = tk.Label(menuinicial, text="19- Crear un módulo de validación de nombres de usuario con criterios específicos.")
    etiqueta23.grid(row=11, column=1, sticky="ew", padx=10, pady=5)
    
    etiqueta24 = tk.Label(menuinicial, text="20- Desarrollar un juego de adivinanza de números.")
    etiqueta24.grid(row=12, column=1, sticky="ew", padx=10, pady=5)
    
    boton_abrir_ejercicios = tk.Button(menuinicial, text="Ejercicios", command=abrir_menu_ejercicios, width=10)
    boton_abrir_ejercicios.grid(row=13, column=1, sticky="ew", padx=10, pady=5)



#Tercera ventana
def abrir_menu_ejercicios():

    menuinicial.withdraw() 
    
    global root
    root = tk.Toplevel()
    root.title("Menú de Ejercicios")
    root.geometry("")
    root.resizable(False,False)

    
    
    
    etiqueta = tk.Label(root, text= "Menu De Ejercicios")
    etiqueta.grid(row=0)

    button1 = tk.Button(root, text="Ejercicio 1", cursor="hand2", command=run_ejercicio1)
    button1.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

    button2 = tk.Button(root, text="Ejercicio 2", cursor="hand2", command=run_ejercicio2)
    button2.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

    button3 = tk.Button(root, text="Ejercicio 3", cursor="hand2", command=run_ejercicio3)
    button3.grid(row=3, column=0, sticky="ew", padx=10, pady=5)

    button4 = tk.Button(root, text="Ejercicio 4", cursor="hand2", command=run_ejercicio4)
    button4.grid(row=4, column=0, sticky="ew", padx=10, pady=5)

    button5 = tk.Button(root, text="Ejercicio 5", cursor="hand2", command=run_ejercicio5)
    button5.grid(row=5, column=0, sticky="ew", padx=10, pady=5)

    button6 = tk.Button(root, text="Ejercicio 6", cursor="hand2", command=run_ejercicio6)
    button6.grid(row=6, column=0, sticky="ew", padx=10, pady=5)

    button7 = tk.Button(root, text="Ejercicio 7", cursor="hand2", command=run_ejercicio7)
    button7.grid(row=7, column=0, sticky="ew", padx=10, pady=5)

    button8 = tk.Button(root, text="Ejercicio 8", cursor="hand2", command=run_ejercicio8)
    button8.grid(row=8, column=0, sticky="ew", padx=10, pady=5)

    button9 = tk.Button(root, text="Ejercicio 9", cursor="hand2", command=run_ejercicio9)
    button9.grid(row=9, column=0, sticky="ew", padx=10, pady=5)

    button10 = tk.Button(root, text="Ejercicio 10", cursor="hand2", command=run_ejercicio10)
    button10.grid(row=10, column=0, sticky="ew", padx=10, pady=5)

    button11 = tk.Button(root, text="Ejercicio 11", cursor="hand2", command=run_ejercicio11)
    button11.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

    button12 = tk.Button(root, text="Ejercicio 12", cursor="hand2", command=run_ejercicio12)
    button12.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

    button13 = tk.Button(root, text="Ejercicio 13", cursor="hand2", command=run_ejercicio13)
    button13.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

    button14 = tk.Button(root, text="Ejercicio 14", cursor="hand2", command=run_ejercicio14)
    button14.grid(row=4, column=1, sticky="ew", padx=10, pady=5)

    button15 = tk.Button(root, text="Ejercicio 15", cursor="hand2", command=run_ejercicio15)
    button15.grid(row=5, column=1, sticky="ew", padx=10, pady=5)

    button16 = tk.Button(root, text="Ejercicio 16", cursor="hand2", command=run_ejercicio16)
    button16.grid(row=6, column=1, sticky="ew", padx=10, pady=5)

    button17 = tk.Button(root, text="Ejercicio 17", cursor="hand2", command=run_ejercicio17)
    button17.grid(row=7, column=1, sticky="ew", padx=10, pady=5)

    button18 = tk.Button(root, text="Ejercicio 18", cursor="hand2", command=run_ejercicio18)
    button18.grid(row=8, column=1, sticky="ew", padx=10, pady=5)

    button19 = tk.Button(root, text="Ejercicio 19", cursor="hand2", command=run_ejercicio19)
    button19.grid(row=9, column=1, sticky="ew", padx=10, pady=5)

    button20 = tk.Button(root, text="Ejercicio 20", cursor="hand2", command=run_ejercicio20)
    button20.grid(row=10, column=1, sticky="ew", padx=10, pady=5)

    exitbutton = tk.Button(root, text="Salir Del Menú", cursor="hand2", command=exit)
    exitbutton.grid(row=11, column=1, sticky="ew", padx=10, pady=5)

    boton_regresar = tk.Button(root, text="Regresar al Menú Principal", command=regresar_al_menu_principal, width=20)
    boton_regresar.grid(row=11, column=0, sticky="ew", padx=10, pady=5)
    

    
def regresar_al_menu_principal():
    root.destroy()  
    menuinicial.deiconify()
    

#Primera ventana
ventana_inicio = tk.Tk()
ventana_inicio.title("Pantalla De Inicio")
ventana_inicio.geometry("")
ventana_inicio.resizable(False, False)

mensaje_bienvenida = tk.Label(ventana_inicio, text="Bienvenido A Nuestro Menu", font=("Arial", 14))
mensaje_bienvenida.pack(pady=20)

boton_inicio = tk.Button(ventana_inicio, text="Iniciar", command=abrir_menuprincipal, width=10)
boton_inicio.pack(pady=20)

grupo_label = tk.Label(ventana_inicio, text="Grupo 2\nMario Suero\nGabriel Sanchez\nIdelka Rodriguez\nDanuel Cuevas", anchor='s')
grupo_label.pack(side=tk.BOTTOM, pady=10)

ventana_inicio.mainloop()

