import tkinter

from tkinter import *
x = ""



def numbers(mm):
   global x 
   x = x + str(mm) #dodaje stringi do siebie.
   equation.set(x) #ustawia stringi

def equalpress():
    try:
        global x
        total = str(eval(x)) #eval() daje nam moliwość przekazać operacje przekazane jako argumenty.
        equation.set(total)
        x = ""

    except:
        equation.set(" error ")
        x = ""

def clear():
    global x
    x = ""
    equation.set("")


window = Tk()
window.title('Kalkulator')
window.geometry("450x200")
equation = StringVar()
console = Entry(window, textvariable=equation)
console.grid(row=0, columnspan=4, ipadx=103)


# 90x112,5
button1 = Button(window, text=' 1 ', command=lambda: numbers(1), height=1, width=6)
button1.grid(row=2, column=0)
 
button2 = Button(window, text=' 2 ', command=lambda: numbers(2), height=1, width=6)
button2.grid(row=2, column=1)
 
button3 = Button(window, text=' 3 ', command=lambda: numbers(3), height=1, width=6)
button3.grid(row=2, column=2)
 
button4 = Button(window, text=' 4 ', command=lambda: numbers(4), height=1, width=6)
button4.grid(row=3, column=0)

button5 = Button(window, text=' 5 ', command=lambda: numbers(5), height=1, width=6)
button5.grid(row=3, column=1)
 
button6 = Button(window, text=' 6 ', command=lambda: numbers(6), height=1, width=6)
button6.grid(row=3, column=2)
 
button7 = Button(window, text=' 7 ', command=lambda: numbers(7), height=1, width=6)
button7.grid(row=4, column=0)

button8 = Button(window, text=' 8 ', command=lambda: numbers(8), height=1, width=6)
button8.grid(row=4, column=1)
 
button9 = Button(window, text=' 9 ', command=lambda: numbers(9), height=1, width=6)
button9.grid(row=4, column=2)
 
button0 = Button(window, text=' 0 ', command=lambda: numbers(0), height=1, width=6)
button0.grid(row=5, column=0)
 
plus = Button(window, text=' + ', command=lambda: numbers("+"), height=1, width=6)
plus.grid(row=2, column=3)

minus = Button(window, text=' - ', command=lambda: numbers("-"), height=1, width=6)
minus.grid(row=3, column=3)
 
multiply = Button(window, text=' * ', command=lambda: numbers("*"), height=1, width=6)
multiply.grid(row=4, column=3)
 
divide = Button(window, text=' / ', command=lambda: numbers("/"), height=1, width=6)
divide.grid(row=5, column=3)
 
equal = Button(window, text=' = ', command=equalpress, height=1, width=6)
equal.grid(row=5, column=2)

clear = Button(window, text='C' ,command = clear, height=1, width=6)
clear.grid(row=5, column='1')
 
Decimal= Button(window, text='.', command=lambda: numbers('.'), height=1, width=6)
Decimal.grid(row=6, column=0)

window.mainloop()






