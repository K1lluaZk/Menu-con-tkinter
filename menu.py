import tkinter as tk

#Mario De Jesus Suero
#Programacion Orientada En Objetos

def abrir_menu():
    ventana_inicio.destroy()
    



def run_ejercicio1():
    try:
        print("-----------------------------------------")
        print("Ejercicio Ejecutandose")
        print("-----------------------------------------")
        """Considera estás desarrollando un programa python donde necesitas 
        trabajar con objetos de tipo Persona. Define una clase Persona, pero en 
        este caso considerando los siguientes atributos de clase: nombre (Str), 
        apellidos (Str), edad (int), casado (boolean), 
        numeroDocumentoIdentidad(Str) y 3 metodos como acciones diferentes 
        por persona de acuerdo a una profesión. Define un constructor y los 
        métodos para poder establecer y obtener los valores de los atributos. 
        Mínimo 7 personas diferentes con acciones diferentes. """
        class Persona:
        
            def __init__(self, nombre, apellidos, edad, casado, numeroDocumentoIdentidad, profesion):
                self.nombre = nombre
                self.apellidos = apellidos
                self.edad = edad
                self.casado = casado
                self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
                self.profesion = profesion
                
            def set_nombre(self, nombre):
                self.nombre = nombre
                
            def get_nombre(self):
                return self.nombre
                
            def set_apellidos(self, apellidos):
                self.apellidos = apellidos
                
            def get_apellidos(self):
                return self.apellidos
                
            def set_edad(self, edad):
                self.edad = edad
            
            def get_edad(self):
                return self.edad
                
            def set_casado(self, casado):
                self.casado = casado
                
            def get_casado(self):
                return self.casado
                
            def set_numeroDocumentoIdentidad(self, numeroDocumentoIdentidad):
                self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
            
            def get_numeroDocumentoIdentidad(self):
                return self.numeroDocumentoIdentidad
                
            def set_profesion(self, profesion):
                self.profesion = profesion
                
            def get_profesion(self):
                return self.profesion
            
            def trabajar(self):
                if self.profesion == "Maestra":
                    print(f"{self.nombre} esta impartiendo clases")
                elif self.profesion == "Doctor":
                    print(f"{self.nombre} esta atendiendo pacientes")
                elif self.profesion == "Ingeniero en sistemas":
                    print(f"{self.nombre} esta analizando un codigo")
                elif self.profesion == "Ingeniero civil":
                    print(f"{self.nombre} esta revisando unos planos")
                elif self.profesion == "Taxista":
                    print(f"{self.nombre} esta llevando a un cliente a su destino")
                elif self.profesion == "Cocinero":
                    print(f"{self.nombre} esta preparando el menu de un restaurante")
                elif self.profesion == "Psicologo":
                    print(f"{self.nombre} esta aplicando terapia")
            
            def descansar(self):
                print(f"{self.nombre} esta descansando")
                
            def presentar_documento(self):
                print(f"este es el documento de identidad de {self.nombre} |{self.numeroDocumentoIdentidad}|")
            
        persona1 = Persona("Natti", "Gutierrez", 27, True, "001-0023450",  "Maestra", )
        persona2 = Persona("Benito", "Martinez", 29, False, "402-1010293",  "Ingeniero civil", )
        persona3 = Persona("Emmanuel", "Gazmey", 25, True, "404-9394231",  "Ingeniero en sistemas", )
        persona4 = Persona("Alejandro", "Paz", 24, False, "001-9993229",  "Cocinero", )
        persona5 = Persona("Maicol", "Santos", 20, False, "239-9394023",  "Taxista", )
        persona6 = Persona("Myke", "Torres", 27, True, "001-9035042",  "Psicologo", )
        persona7 = Persona("Raul", "Ocasio", 21, False, "402-9284586",  "Doctor", )
        persona8 = Persona("Jésus", "Nieves", 32, False, "405-1290845",  "Ingeniero en sistemas", )
        persona9 = Persona("Carlos", "Morales", 33, False, "495-2930332",  "Cocinero", )
            
        persona1.trabajar()
        persona2.trabajar()
        persona3.trabajar()
        persona4.trabajar()    
        persona5.trabajar()
        persona6.trabajar()
        persona7.trabajar()
        persona8.trabajar()
        persona9.trabajar()
            
        persona1.presentar_documento()
        persona1.descansar()
    except ValueError: 
        print("Error en el ejercicio")
        
def run_ejercicio2():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """Crea una clase Cuenta con los métodos ingreso, reintegro y 
    transferencia. La clase contendrá un constructor por defecto, un 
    constructor con parámetros y los métodos mostrar y ingresar."""
    try:
        class Cuenta:
            def __init__(self, titular="Desconocido", saldo=0.0):
                self.titular = titular
                self.saldo = saldo

            def ingreso(self, cantidad):
                if cantidad > 0:
                    self.saldo += cantidad
                    print(f"Se han ingresado {cantidad} a la cuenta de {self.titular}. Saldo actual: {self.saldo}")
                else:
                    print("La cantidad a ingresar debe ser positiva.")

            def reintegro(self, cantidad):
                if cantidad > 0 and cantidad <= self.saldo:
                    self.saldo -= cantidad
                    print(f"Se han retirado {cantidad} de la cuenta de {self.titular}. Saldo actual: {self.saldo}")
                else:
                    print("Cantidad no válida o saldo insuficiente.")

            def transferencia(self, otra_cuenta, cantidad):
                if cantidad > 0 and cantidad <= self.saldo:
                    self.saldo -= cantidad
                    otra_cuenta.saldo += cantidad
                    print(f"Se han transferido {cantidad} de la cuenta de {self.titular} a la cuenta de {otra_cuenta.titular}.")
                else:
                    print("Cantidad no válida o saldo insuficiente.")

            def mostrar(self):
                print(f"Titular: {self.titular}, Saldo: {self.saldo}")
                
            def ingresar(self, cantidad):
                self.ingreso(cantidad)
                

        cuenta1 = Cuenta("Mario", 1000)
        cuenta2 = Cuenta("Luis", 500)

        cuenta1.mostrar()
        cuenta1.ingreso(200)
        cuenta1.reintegro(100)
        cuenta1.transferencia(cuenta2, 150)

        cuenta1.mostrar()
        cuenta2.mostrar()
    except ValueError: 
        print("Error En El Ejercicio")

def run_ejercicio3():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """Crea una clase Fracción con métodos para sumar, restar, multiplicar y 
    dividir fracciones."""  
    try:
        import math  

        class Fraccion:
            def __init__(self, numerador, denominador):
                if denominador == 0:
                    raise ValueError("El denominador no puede ser cero.")
                self.numerador = numerador
                self.denominador = denominador
                self.simplificar()

            def simplificar(self):
                divisor_comun = math.gcd(self.numerador, self.denominador)
                self.numerador //= divisor_comun
                self.denominador //= divisor_comun

            def sumar(self, otra):
                nuevo_numerador = self.numerador * otra.denominador + otra.numerador * self.denominador
                nuevo_denominador = self.denominador * otra.denominador
                return Fraccion(nuevo_numerador, nuevo_denominador)

            def restar(self, otra):
                nuevo_numerador = self.numerador * otra.denominador - otra.numerador * self.denominador
                nuevo_denominador = self.denominador * otra.denominador
                return Fraccion(nuevo_numerador, nuevo_denominador)

            def multiplicar(self, otra):
                nuevo_numerador = self.numerador * otra.numerador
                nuevo_denominador = self.denominador * otra.denominador
                return Fraccion(nuevo_numerador, nuevo_denominador)

            def dividir(self, otra):
                if otra.numerador == 0:
                    raise ValueError("No se puede dividir por una fracción con numerador cero.")
                nuevo_numerador = self.numerador * otra.denominador
                nuevo_denominador = self.denominador * otra.numerador
                return Fraccion(nuevo_numerador, nuevo_denominador)

            def mostrar(self):
                return f"{self.numerador}/{self.denominador}"
                
        fraccion1 = Fraccion(3, 4)
        fraccion2 = Fraccion(2, 5)

        suma = fraccion1.sumar(fraccion2)
        resta = fraccion1.restar(fraccion2)
        multiplicacion = fraccion1.multiplicar(fraccion2)
        division = fraccion1.dividir(fraccion2)

        print("Suma:", suma.mostrar())
        print("Resta:", resta.mostrar())
        print("Multiplicación:", multiplicacion.mostrar())
        print("División:", division.mostrar())
    except ValueError:
        print("Error En El Ejercicio")

def run_ejercicio4():
 print("-----------------------------------------")
 print("Ejercicio Ejecutandose")
 print("-----------------------------------------")
 """Crea una clase Complejo con métodos para sumar, restar, multiplicar y 
    dividir números complejos."""
 try:
    class Complejo:
        def __init__(self, real, imaginario):
            self.real = real
            self.imaginario = imaginario

        def sumar(self, otro):
            real = self.real + otro.real
            imaginario = self.imaginario + otro.imaginario
            return Complejo(real, imaginario)

        def restar(self, otro):
            real = self.real - otro.real
            imaginario = self.imaginario - otro.imaginario
            return Complejo(real, imaginario)

        def multiplicar(self, otro):
            real = self.real * otro.real - self.imaginario * otro.imaginario
            imaginario = self.real * otro.imaginario + self.imaginario * otro.real
            return Complejo(real, imaginario)

        def dividir(self, otro):
            if otro.real == 0 and otro.imaginario == 0:
                raise ValueError("No se puede dividir por un número complejo cero.")
            divisor = otro.real ** 2 + otro.imaginario ** 2
            real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
            imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
            return Complejo(real, imaginario)

        def mostrar(self):
            signo = '+' if self.imaginario >= 0 else '-'
            return f"{self.real} {signo} {abs(self.imaginario)}i"
            
    complejo1 = Complejo(3, 4)
    complejo2 = Complejo(1, -2)

    suma = complejo1.sumar(complejo2)
    resta = complejo1.restar(complejo2)
    multiplicacion = complejo1.multiplicar(complejo2)
    division = complejo1.dividir(complejo2)

    print("Suma:", suma.mostrar())
    print("Resta:", resta.mostrar())
    print("Multiplicación:", multiplicacion.mostrar())
    print("División:", division.mostrar())
 except ValueError:
     print("Error En El Ejercicio")
def run_ejercicio5():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """En un banco tienen clientes que pueden hacer depósitos y extracciones 
    de dinero. El banco requiere también al final del día calcular la cantidad 
    de dinero que se ha depositado. Se deberán crear dos clases, la clase 
    cliente y la clase banco. La clase cliente tendrá los atributos nombre y 
    cantidad y los métodos __init__, depositar, extraer, mostrar_total. La clase 
    banco tendrá como atributos 3 objetos de la clase cliente y los métodos 
    __init__, operar y deposito_total."""
    try:
        class Cliente:
            def __init__(self, nombre, cantidad=0):
                self.nombre = nombre
                self.cantidad = cantidad

            def depositar(self, monto):
                if monto > 0:
                    self.cantidad += monto
                    print(f"{self.nombre} ha depositado {monto}. Saldo actual: {self.cantidad}")
                else:
                    print("El monto a depositar debe ser positivo.")

            def extraer(self, monto):
                if monto > 0 and monto <= self.cantidad:
                    self.cantidad -= monto
                    print(f"{self.nombre} ha extraído {monto}. Saldo actual: {self.cantidad}")
                else:
                    print("Monto no válido o saldo insuficiente.")

            def mostrar_total(self):
                return f"{self.nombre} tiene un saldo de {self.cantidad}"


        class Banco:
            def __init__(self):
                self.cliente1 = Cliente("Mario")
                self.cliente2 = Cliente("Ana")
                self.cliente3 = Cliente("Luis")

            def operar(self):
                # Ejemplo de operaciones
                self.cliente1.depositar(100)
                self.cliente2.depositar(150)
                self.cliente3.depositar(200)
                self.cliente1.extraer(50)
                self.cliente2.extraer(30)

            def deposito_total(self):
                total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad
                print("Total de dinero en el banco al final del día:", total)

            def mostrar_clientes(self):
                print(self.cliente1.mostrar_total())
                print(self.cliente2.mostrar_total())
                print(self.cliente3.mostrar_total())
                
        
        banco = Banco()

        banco.operar()

        banco.mostrar_clientes()

        banco.deposito_total()
    except ValueError:
     print("Error En El Ejercicio")

#Gabriel Sanchez Reynoso
def run_ejercicio6():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """Desarrollar un programa que conste de una clase padre Cuenta y dos 
    subclases PlazoFijo y CajaAhorro. Definir los atributos titular y cantidad y 
    un método para imprimir los datos en la clase Cuenta. La clase 
    CajaAhorro tendrá un método para heredar los datos y uno para mostrar 
    la información. La clase PlazoFijo tendrá dos atributos propios, plazo e 
    interés. Tendrá un método para obtener el importe del interés 
    (cantidad*interés/100) y otro método para mostrar la información, datos 
    del titular plazo, interés y total de interés. Crear al menos un objeto de 
    cada subclase."""
    try:
        
        class Cuenta:
            def __init__(self, titular, cantidad):
                self.titular = titular
                self.cantidad = cantidad

            def imprimir_datos(self):
                print(f"Titular: {self.titular}, Cantidad: {self.cantidad}")

        class CajaAhorro(Cuenta):
            def __init__(self, titular, cantidad):
                super().__init__(titular, cantidad)

            def mostrar_info(self):
                self.imprimir_datos()

        class PlazoFijo(Cuenta):
            def __init__(self, titular, cantidad, plazo, interes):
                super().__init__(titular, cantidad)
                self.plazo = plazo
                self.interes = interes

            def calcular_interes(self):
                return self.cantidad * self.interes / 100

            def mostrar_info(self):
                total_interes = self.calcular_interes()
                print(f"Titular: {self.titular}, Cantidad: {self.cantidad}, Plazo: {self.plazo} meses, Interés: {self.interes}%")
                print(f"Total interés: {total_interes}")

        # Creación de objetos
        caja_ahorro = CajaAhorro("Messi", 23400)
        plazo_fijo = PlazoFijo("Antonella", 15670, 12, 5)

        # Mostrar información
        caja_ahorro.mostrar_info()
        plazo_fijo.mostrar_info()

    except ValueError:
     print("Error En El Ejercicio")
     
#Ciclo While
     
def run_ejercicio7():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """Escribir un programa que solicite ingresar la nota de 10 alumnos, el 
    programa debe informar de cuantos han aprobado y cuantos han 
    suspendido."""
    try:
        
        aprobados = 0
        suspendidos = 0
        contador = 0
        resultados = []

        while contador < 10:
            nota = float(input(f"Ingrese la nota del alumno {contador + 1}: "))
            if nota >= 70:
                aprobados += 1
                resultados.append(f"Alumno {contador + 1}: Aprobado")
            else:
                suspendidos += 1
                resultados.append(f"Alumno {contador + 1}: Suspendido")
            contador += 1

        # Impresión de resultados
        print("\nResultados individuales:")
        for resultado in resultados:
            print(resultado)

        print(f"\nTotal de aprobados: {aprobados}")
        print(f"Total de suspendidos: {suspendidos}")
    except ValueError:
     print("Error En El Ejercicio")
     
def run_ejercicio8():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """En una empresa trabajan n empleados cuyos sueldos oscilan entre 100 y 
    1000. Realizar un programa que informe de cuantos empleados cobran 
    menos de 500 y cuantos más de 500. Informar también del total que 
    gasta la empresa en pagar a sus empleados."""
    try:
       
        menos_500 = 0
        mas_500 = 0
        total_gasto = 0

        n = int(input("Ingrese la cantidad de empleados: "))

        contador = 0
        while contador < n:
            sueldo = float(input("Ingrese el sueldo del empleado: "))
            if sueldo < 500:
                menos_500 += 1
            else:
                mas_500 += 1
            total_gasto += sueldo
            contador += 1

        print(f"Empleados que ganan menos de 500: {menos_500}")
        print(f"Empleados que ganan 500 o más: {mas_500}")
        print(f"Gasto total de la empresa: {total_gasto}")
    except ValueError:
     print("Error En El Ejercicio")
     
def run_ejercicio9():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """Escribir un programa que solicite ingresar la nota de 10 alumnos, el programa debe 
    informar de cuantos han aprobado y cuantos han suspendido."""
    try:
     
        aprobados = 0
        suspendidos = 0
        contador = 0
        resultados = []

        while contador < 10:
            nota = float(input(f"Ingrese la nota del alumno {contador + 1}: "))
            if nota >= 70:
                aprobados += 1
                resultados.append(f"Alumno {contador + 1}: Aprobado")
            else:
                suspendidos += 1
                resultados.append(f"Alumno {contador + 1}: Suspendido")
            contador += 1

        # Impresión de resultados
        print("\nResultados individuales:")
        for resultado in resultados:
            print(resultado)

        print(f"\nTotal de aprobados: {aprobados}")
        print(f"Total de suspendidos: {suspendidos}")

    except ValueError:
     print("Error En El Ejercicio")
    
#CICLO FOR 
     
def run_ejercicio10():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """Desarrollar un programa que solicite la carga de 10 números e imprima la suma de 
    los últimos 5 valores ingresados."""
    try:

        numeros = []

        for i in range(10):
            num = int(input("Ingrese un número: "))
            numeros.append(num)

        # Sumar los últimos 5 valores
        suma_ultimos_5 = sum(numeros[-5:])
        print(f"La suma de los últimos 5 valores es: {suma_ultimos_5}")
    except ValueError:
     print("Error En El Ejercicio")
     
#Idelka  
def run_ejercicio11():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """11. Realizar un programa que solicite la carga de un valor entero del 1 al 10. Mostrar
    después la tabla de multiplicar de dicho número."""

    try:
     
        def tabla_multiplicar():
            print ("Ejercicio 11")

            numero = int(input("Ingrese un número entero del 1 al 10: "))
            print(f"Tabla de multiplicar del número {numero}:")
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")      
        tabla_multiplicar()
    except ValueError:
     print("Error En El Ejercicio")
         
def run_ejercicio12():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """12. Realizar un programa que pida ingresar dos datos enteros (coordenadas x e y). 
    comenzar el programa se pedirá ingresar el total de puntos a procesar. Informar de
    cuantos puntos se han ingresado en cada uno de los cuatro cuadrantes."""
    try:

        def puntos_cuadrantes():
            print ("Ejercicio 12")

            total_puntos = int(input("Ingrese el total de puntos a procesar: "))
            cuadrantes = [0, 0, 0, 0]  # cuadrantes[0] -> primer cuadrante, cuadrantes[1] -> segundo cuadrante, etc.
            print('----------------------------------------------------------------------------------------------')
            
            for i in range(total_puntos):
                x = float(input(f"Ingrese la coordenada x del punto {i + 1}: "))
                y = float(input(f"Ingrese la coordenada y del punto {i + 1}: "))
                
                print('----------------------------------------------------------------------------------------------')

                if x > 0 and y > 0:
                    cuadrantes[0] += 1
                elif x < 0 and y > 0:
                    cuadrantes[1] += 1
                elif x < 0 and y < 0:
                    cuadrantes[2] += 1
                elif x > 0 and y < 0:
                    cuadrantes[3] += 1
                print('----------------------------------------------------------------------------------------------')

            print(f"Puntos en el primer cuadrante: {cuadrantes[0]}")
            print(f"Puntos en el segundo cuadrante: {cuadrantes[1]}")
            print(f"Puntos en el tercer cuadrante: {cuadrantes[2]}")
            print(f"Puntos en el cuarto cuadrante: {cuadrantes[3]}")
        puntos_cuadrantes()
    except ValueError:
     print("Error En El Ejercicio")
        
def run_ejercicio13():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """13. Realizar un programa que lea los lados de n triángulos. Informar después de cada
    triángulo si es equilátero (tres lados iguales), isósceles (dos lados iguales) o
    escaleno (ningún lado igual). Informar después del total de triángulos de cada tipo."""
    try:

        def tipo_triangulo():
            print ("Ejercicio 13")

            n = int(input("Ingrese la cantidad de triángulos a procesar: "))
            equilateros = 0
            isosceles = 0
            escalenos = 0

            print('-------------------------------------------------------------------------------------------')
            for i in range(1, n + 1):
                lado1 = float(input(f"Ingrese la longitud del lado 1 del triángulo {i}: "))
                lado2 = float(input(f"Ingrese la longitud del lado 2 del triángulo {i}: "))
                lado3 = float(input(f"Ingrese la longitud del lado 3 del triángulo {i}: "))
                
                if lado1 == lado2 == lado3:
                    print(f"El triángulo {i} es equilátero.")
                    equilateros += 1
                elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                    print(f"El triángulo {i} es isósceles.")
                    isosceles += 1
                else:
                    print(f"El triángulo {i} es escaleno.")
                    escalenos += 1
            
            print('-------------------------------------------------------------------------------------------')
            print(f"Total de triángulos equiláteros: {equilateros}")
            print(f"Total de triángulos isósceles: {isosceles}")
            print(f"Total de triángulos escalenos: {escalenos}")
        tipo_triangulo()
    except ValueError:
       print("Error En El Ejercicio")

#Funciones

def run_ejercicio14():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """14. Realizar un programa con dos funciones. La primera debe solicitar la carga de un
    dicho vlor entero y mostrar el cuadrado. La segunda que solicite la carga
    de dos valores y muestre el producto de los mismos. Deberán llamar a estas dos
    funciones desde el bloque principal (Fuera de toda función, como en el ejemplo
    realizado al principio de este tema)."""
    try:

        def cuadrado_valor():
            valor = int(input("Ingrese un valor entero: "))
            cuadrado = valor ** 2
            print(f"El cuadrado de {valor} es: {cuadrado}")
        cuadrado_valor()

        def producto_valores():
            valor1 = float(input("Ingrese el primer valor: "))
            valor2 = float(input("Ingrese el segundo valor: "))
            producto = valor1 * valor2
            print(f"El producto de {valor1} y {valor2} es: {producto}")
        producto_valores()
    except ValueError:
     print("Error En El Ejercicio")
     
def run_ejercicio15():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """15. Realizar un programa que tenga una función que reciba un string como parámetro.
    Debe mostrar la cantidad de vocales que tiene dicho string. Se deberá llamar 3
    veces desde el bloque principal, con 3 strings diferentes."""

    try:

        def contar_vocales(cadena):
            """Función que cuenta la cantidad de vocales en un string."""
            vocales = 'aeiouAEIOU'
            contador = 0
            for letra in cadena:
                if letra in vocales:
                    contador += 1
            return contador
        
    except ValueError:
     print("Error En El Ejercicio")
     
    def ejercicio15():
        """Función que ejecuta el ejercicio 15."""
        try:
            string1 = input("Ingresa el primer string: ")
            string2 = input("Ingresa el segundo string: ")
            string3 = input("Ingresa el tercer string: ")

            # Llamada a la función contar_vocales con tres strings diferentes
            vocales_string1 = contar_vocales(string1)
            vocales_string2 = contar_vocales(string2)
            vocales_string3 = contar_vocales(string3)

            # Mostrar la cantidad de vocales en cada string
            print(f"El string '{string1}' tiene {vocales_string1} vocales.")
            print(f"El string '{string2}' tiene {vocales_string2} vocales.")
            print(f"El string '{string3}' tiene {vocales_string3} vocales.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            
    ejercicio15()
    
#Danuel
def run_ejercicio16():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")

    """Realizar un programa que cargue una lista de n valores enteros. Generar dos listas, 
    una con valores negativos y otra con los valores positivos e imprimir ambas listas."""
    try:
        
        def numero_valores():
            while True:
                try:
                    n = int(input("Ingrese el número de valores que va a ingresar: "))
                    return n
                except ValueError:
                    print("Ingrese un valor válido.")

        def pedida_valores(v):
            valores = []
            for i in range(v):
                while True:
                    try:
                        pedida = int(input(f"Ingrese el valor {i + 1}: "))
                        valores.append(pedida)
                        break  
                    except ValueError:
                        print("Ingrese un valor válido.")
            return valores  

        def clasificacion(valores):
            negativos = []
            positivos = []
            for valor in valores:
                if valor > 0:
                    positivos.append(valor)
                elif valor < 0:
                    negativos.append(valor)
            return negativos, positivos  

        def main():
            n = numero_valores()
            valores = pedida_valores(n)
            negativos, positivos = clasificacion(valores)
            print("Valores:", valores)
            print("Valores negativos:", negativos)
            print("Valores positivos:", positivos)

        if __name__ == "__main__":
            main()
    except ValueError:
     print("Error En El Ejercicio")
         
def run_ejercicio17():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """Realizar un programa que reciba una serie de edades y retorne la cantidad de 
    personas con una edad igual o superior a 18 (como mínimo deben introducirse 3 
    valores enteros)"""
    try:
        def edades ():
            almacenedades = []
            while True:
                try:
                    edad1= int(input("Ingrese la edad 1: "))
                    almacenedades.append(edad1)
                except ValueError:
                    print("Ingrese un valor valido")
                try:
                    edad2= int(input("Ingrese la edad 2: "))
                    almacenedades.append(edad2)
                except ValueError:
                    print("Ingrese un valor valido")
                try:
                    edad3= int(input("Ingrese la edad 3: "))
                    almacenedades.append(edad3)
                except ValueError:
                    print("Ingrese un valor valido")
                return almacenedades
    
        
        def clasificacion(edad):
            mayoresoigualescontador= 0
            menorescontador= 0
            for n in edad:
                if n >= 18:
                    mayoresoigualescontador = mayoresoigualescontador + 1
                elif n < 18:
                    menorescontador = menorescontador + 1
            print("la cantidad de personas mayores o iguales son: ",mayoresoigualescontador)
            print("la cantidad de personas menores son: ",menorescontador)
                        
        clasificacion(edades())
    
    except ValueError:
        print("Error En El Ejercicio")
   
#Simples
def run_ejercicio18():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """Solicitar la carga por teclado de un string. Mostrar el total de caracteres del string y 
    utilizar las funciones explicadas anteriormente (upper, lower y capitalize)"""
    try:
        def carga():

            while True:
                    palabra = input("Escribe una palabra: ")
                    if palabra.isalpha():
                        return palabra
                    else:
                        print("Ingresa un valor valido")
            
        def formas(palabra):
            caracteres = len(palabra)
            mayuscula= palabra.upper()
            minuscula = palabra.lower()
            capitalizada= palabra.capitalize()
            print("Total de caracteres: ",caracteres)
            print("Palabra en mayusculas: ", mayuscula)
            print("Palabra en minusculas: ", minuscula)
            print("Palabra en capitalizado: ", capitalizada)
        formas(carga())
    except ValueError:
        print("Error En El Ejercicio")

#OTROS

def run_ejercicio19():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá 
    cumplir con los siguientes criterios de aceptación:
    El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
    El nombre de usuario debe ser alfanumérico.
    Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El 
    nombre de usuario debe contener al menos 6 caracteres".
    Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre 
    de usuario no puede contener más de 12 caracteres".
    Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el 
    mensaje "El nombre de usuario puede contener solo letras y números".
    Nombre de usuario válido, retorna True."""
    try:
        def condiciones(nombreusuario):
            if len(nombreusuario)> 12:
                print("El nombre de usuario no puede contener más de 12 caracteres")
                return False
            if len(nombreusuario)<6:
                print("El nombre de usuario debe contener al menos 6 caracteres")
                return False
            if not nombreusuario.isalnum():
                print("El nombre de usuario puede contener solo letras y números")
                return False
            return True

        def usuario():
            while True:
                nombreusuario= input("Escriba su nombre de usuario: ")
                nombre_sin_espacios= nombreusuario.strip()
                resultado = condiciones(nombre_sin_espacios)
                if resultado is True:
                    print("Usuario valido")
                    return resultado
                else:
                    print ("Intentelo nuevamente")
        usuario()
    except ValueError:
        print("Error En El Ejercicio")    
    

def run_ejercicio20():
    print("-----------------------------------------")
    print("Ejercicio Ejecutandose")
    print("-----------------------------------------")
    """Escribe un programa que almacene un número y pida al usuario 
    adivinar"""
    try:

        import random

        def adivina(numero_usuario, numero_secreto):
            
            return numero_usuario == numero_secreto  

        def admin():
            numero_secreto = random.randint(1, 10)  
            print(numero_secreto)
            print("Adivina el número que estoy pensando del 1 al 10, tienes 5 intentos")
            contador = 1
            while True:
                try:
                    numero_usuario = int(input("Creo que es el: "))  
                    resultado = adivina(numero_usuario, numero_secreto)  
                    if resultado == True:
                        print("¡Siii, ese era!, ganasteeee, que duro tu eres")
                        break  
                    if contador < 6:
                        print("Nop, ese no es, tienes ",contador," intento fallido")
                    if contador == 5:
                        print("Perdisteee, que mal :(")
                        break
                    contador = contador+1
                except ValueError:
                    print("Por favor, ingresa un número válido.")  
        
        admin()
        
    except ValueError:
       print("Error")

ventana_inicio = tk.Tk()
ventana_inicio.title("Pantalla De Inicio")
ventana_inicio.geometry("300x300")

mensaje_bienvenida = tk.Label(ventana_inicio, text="Bienvenido A Nuestro Menu", font=("Arial", 14))
mensaje_bienvenida.pack(pady=20)




boton_inicio = tk.Button(ventana_inicio, text="Iniciar", command=abrir_menu, width=10)
boton_inicio.pack(pady=20)

grupo_label = tk.Label(ventana_inicio, text="Grupo 1\nMario Suero\nGabriel Sanchez\nIdelka Rodriguez\nDanuel Cuevas", anchor='s')
grupo_label.pack(side=tk.BOTTOM, pady=10)

ventana_inicio.mainloop()


root = tk.Tk()
root.title("Menú")
root.geometry("400x500")




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


root.mainloop()

