from tkinter import *
from tkinter import ttk, font

class Calculadora():
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Mi Calculadora")
        # self.principal.resizable(0,0)
        fuente = font.Font(weight='bold')

        self.label1 = ttk.Label(self.principal, text="Calculadora en Python", font=fuente, padding=(5,5))
        self.marco = ttk.Frame(self.principal, borderwidth=2, relief="raised")
        self.ultima_ins = StringVar()
        self.numeroActivo = IntVar()
        self.resultadoProv = IntVar()
        self.resultadoProv.set(0)
        self.entrada_numeros = ttk.Entry(self.principal, width=60, textvariable=self.numeroActivo)

        self.botonSuma = ttk.Button(self.marco, text=" + ", padding=(2,2), command=self.suma_numeros)
        self.botonResta = ttk.Button(self.marco, text=" - ", padding=(2,2), command=self.resta_numeros)
        self.botonIgual = ttk.Button(self.marco, text= " = ", padding=(2,2), command=self.muestra_resultado)
        self.label1.grid(column=0, row=0)
        self.entrada_numeros.grid(column=0, row=1)
        self.marco.grid(column=0, row=2)
        self.botonSuma.grid(column=0, row=0)
        self.botonResta.grid(column=1, row=0)
        self.botonIgual.grid(column=2, row=0)
        self.principal.mainloop()

    def suma_numeros(self):
        self.resultadoProv.set(self.resultadoProv.get() + self.numeroActivo.get())
        self.numeroActivo.set(0)
        self.ultima_ins.set('+')

    def resta_numeros(self): #resta no la tengo bien hecha
        self.resultadoProv.set(self.resultadoProv.get() - self.numeroActivo.get())
        self.numeroActivo.set(0)
        self.ultima_ins.set('-')

    def muestra_resultado(self):
        res = resolucion_final(self.ultima_ins.get(), self.resultadoProv.get(), self.numeroActivo.get())
        self.numeroActivo.set(res)
        # if self.ultima_ins.get() == ''
        # self.numeroActivo.set(self.resultadoProv.get())

def resolucion_final(operacion, provisorio, activo):
    print('Se apretó el igual: {}'.format(operacion))
    if operacion == '+':
        return(provisorio + activo)
    elif operacion == '-':
        return(provisorio - activo)
if __name__ == '__main__':
    calc = Calculadora()
