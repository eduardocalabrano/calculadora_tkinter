"""
Clase que define a la calculadora
"""
from tkinter import *
from tkinter import ttk, font

class Calculadora():
    def __init__(self):
        #definición de ventana y algunas propiedades
        self.principal = Tk()
        self.principal.title("Mi Calculadora")
        self.principal.resizable(0,0)
        fuente = font.Font(weight='bold')
        #elementos necesarios y variables
        self.label1 = ttk.Label(self.principal, text="Calculadora en Python", font=fuente, padding=(5,5))
        self.marco = ttk.Frame(self.principal, borderwidth=2, relief="raised")
        self.ultima_ins = StringVar()
        self.ultima_ins.set('')
        self.numeroActivo = IntVar()
        self.resultadoProv = IntVar()
        self.resultadoProv.set(0)
        #Campo input donde se ingresan los números
        self.entrada_numeros = ttk.Entry(self.principal, width=60, textvariable=self.numeroActivo)
        #creación de botones
        self.botonSuma = ttk.Button(self.marco, text=" + ", padding=(2,2), command=self.suma_numeros)
        self.botonResta = ttk.Button(self.marco, text=" - ", padding=(2,2), command=self.resta_numeros)
        self.botonProd = ttk.Button(self.marco, text=" * ", padding=(2, 2), command=self.multiplica_numeros)
        self.botonDiv = ttk.Button(self.marco, text=" / ", padding=(2, 2), command=self.divide_numeros)
        self.botonExp = ttk.Button(self.marco, text=" ^ ", padding=(2,2), command=self.exponencial)
        self.botonIgual = ttk.Button(self.marco, text= " = ", padding=(2,2), command=self.muestra_resultado)
        self.botonReset = ttk.Button(self.marco, text=" C ", padding=(2,2), command=self.reset_calculadora)
        #distribución de los elementos en la ventana utilizando grid
        self.label1.grid(column=0, row=0)
        self.entrada_numeros.grid(column=0, row=1)
        self.marco.grid(column=0, row=2)
        self.botonSuma.grid(column=0, row=0)
        self.botonResta.grid(column=1, row=0)
        self.botonIgual.grid(column=2, row=0, rowspan=2, ipady=14)
        self.botonProd.grid(column=0, row=1)
        self.botonDiv.grid(column=1, row=1)
        self.botonExp.grid(column=0, row=2)
        self.botonReset.grid(column=2, row=2)
        self.principal.mainloop()

    def suma_numeros(self):
        if self.ultima_ins.get() == '':
            self.almacena_numero()
        else:
            self.calcula_operacion()
        self.ultima_ins.set('+')

    def resta_numeros(self):
        if self.ultima_ins.get() == '':
            self.almacena_numero()
        else:
            self.calcula_operacion()
        self.ultima_ins.set('-')

    def multiplica_numeros(self):
        if self.ultima_ins.get() == '':
            self.almacena_numero()
        else:
            self.calcula_operacion()
        self.ultima_ins.set('*')

    def divide_numeros(self):
        if self.ultima_ins.get() == '':
            self.almacena_numero()
        else:
            self.calcula_operacion()
        self.ultima_ins.set('/')

    def exponencial(self):
        if self.ultima_ins.get() == '':
            self.almacena_numero()
        else:
            self.calcula_operacion()
        self.ultima_ins.set('^')

    def muestra_resultado(self):
        #método que se ejecuta al presionar el botón " = "
        res = self.resolucion_final(self.ultima_ins.get(), self.resultadoProv.get(), self.numeroActivo.get())
        self.numeroActivo.set(res)
        self.ultima_ins.set('')

    def almacena_numero(self):
        self.resultadoProv.set(self.numeroActivo.get())
        self.numeroActivo.set(0)

    def calcula_operacion(self):
        self.resultadoProv.set(self.resolucion_final(self.ultima_ins.get(), self.resultadoProv.get(), self.numeroActivo.get()))
        self.numeroActivo.set(self.resultadoProv.get())

    def reset_calculadora(self):
        #Se reinicia la calculadora. Se ejecuta al presionar el botón " C "
        self.numeroActivo.set(0)
        self.resultadoProv.set(0)
        self.ultima_ins.set('')

    def resolucion_final(self, operacion, provisorio, activo):
        if operacion == '+':
            return(provisorio + activo)
        elif operacion == '-':
            return(provisorio - activo)
        elif operacion == '*':
            return(provisorio * activo)
        elif operacion == '/':
            if activo == 0:
                #se da aviso si quieren dividir por cero
                return('MATH ERROR')
            else:
                return(provisorio / activo)
        elif operacion == '^':
            return(provisorio ** activo)
