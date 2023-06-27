from tkinter import *
from funtions import *
from tkinter import messagebox
from PIL import Image, ImageTk
gui = Tk()
gui.title("Calculator created by Jhay")
gui.geometry("500x630")
def ButtonClick(num):
    global EquationText
    EquationText = EquationText + str(num)
    lbl_equation.set(EquationText)
def Equals():
    global EquationText
    try:
        total = str(eval(EquationText))
        lbl_equation.set(total)
        EquationText = total
    except SyntaxError:
        #messagebox.OK("Opss", "Syntax Error")
        lbl_equation.set("Syntax Error")
        EquationText = ""
    except ZeroDivisionError:
        #messagebox.OK("Opss", "Arithmetic Error")
        lbl_equation.set("Arithmetic Error")
        EquationText = ""
def Clear():
    global EquationText
    lbl_equation.set("")
    EquationText = ""
EquationText = ""
# for user input
lbl_equation = StringVar()
lbl_userInput = Label(gui, textvariable=lbl_equation, font=("Arial", 20), bg="yellowgreen",width=29, height=3)
lbl_userInput.pack()
# images edited in https://apps.lospec.com/pixel-editor
# declaration fro images
btn1 = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\1.png")
btn2 = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\2.png")
btn3 = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\3.png")
btn4 = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\4.png")
btn5 = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\5.png")
btn6 = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\6.png")
btn7 = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\7.png")
btn8 = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\8.png")
btn9 = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\9.png")
btn0 = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\0.png")
btnclear = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\clear.png")
btnminus = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\minus.png")
btnplus = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\plus.png")
btndiv = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\div.png")
btnmulti = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\multi.png")
btndec = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\dec.png")
btnequal = PhotoImage(file = "C:\\Users\\penal\\Desktop\\SimpleCalculatorInPython\\images\\eq.png")
frame_gui = Frame(gui)
frame_gui.pack()
# declaration of buttons
Btn1 = Button(frame_gui, image=btn1, text="1", height=100,
              width=100,font=35,command=lambda :  ButtonClick(1))
Btn2 = Button(frame_gui,image=btn2, text="2", height=100,
              width=100,font=35,command=lambda :  ButtonClick(2))
Btn3 = Button(frame_gui,image=btn3, text="3", height=100,
              width=100,font=35,command=lambda :  ButtonClick(3))
Btn100 = Button(frame_gui, image=btn4, text="100", height=100,
          width=100,font=35,command=lambda :  ButtonClick(4))
Btn5 = Button(frame_gui, image=btn5, text="5", height=100,
              width=100,font=35,command=lambda :  ButtonClick(5))
Btn6 = Button(frame_gui, image=btn6, text="6", height=100,
              width=100,font=35,command=lambda :  ButtonClick(6))
Btn7 = Button(frame_gui, image=btn7, text="7", height=100,
              width=100,font=35,command=lambda :  ButtonClick(7))
Btn8 = Button(frame_gui,image=btn8, text="8", height=100,
              width=100,font=35,command=lambda :  ButtonClick(8))
Btn9 = Button(frame_gui,image=btn9, text="100", height=100,
              width=100,font=35,command=lambda :  ButtonClick(9))
Btn0 = Button(frame_gui, image=btn0, text="0", height=100,
              width=100,font=35,command=lambda :  ButtonClick(0))
Btn_plus = Button(frame_gui, image=btnplus,text="+",height=100,
              width=100,font=35, command=lambda : ButtonClick("+"))
Btn_multi = Button(frame_gui, image=btnmulti,text="*",height=100,
              width=100,font=35, command=lambda : ButtonClick("*"))
Btn_minus = Button(frame_gui, image=btnminus,text="-",height=100,
              width=100,font=35, command=lambda : ButtonClick("-"))
Btn_div = Button(frame_gui, image=btndiv,text="/",height=100,
              width=100,font=35, command=lambda : ButtonClick("/"))
Btn_equal = Button(frame_gui, image=btnequal,text="=",height=100,
              width=100,font=35, command=Equals)
Btn_decimal = Button(frame_gui, image=btndec,text=".",height=100,
              width=100,font=35, command=lambda : ButtonClick("."))
Btn_clear = Button(gui, image=btnclear,text="clear",height=100,
              width=1100,font=35, command=Clear)
# where to put buttons usin grig
Btn7.grid(row=0,column=0)
Btn8.grid(row=0,column=1)
Btn9.grid(row=0,column=2)
Btn_equal.grid(row=0,column=3)

Btn100.grid(row=1,column=0)
Btn5.grid(row=1,column=1)
Btn6.grid(row=1,column=2)
Btn_multi.grid(row=1,column=3)

Btn1.grid(row=2,column=0)
Btn2.grid(row=2,column=1)
Btn3.grid(row=2,column=2)
Btn_plus.grid(row=2,column=3)

Btn0.grid(row=3,column=0)
Btn_decimal.grid(row=3,column=1)
Btn_minus.grid(row=3,column=2)
Btn_div.grid(row=3,column=3)

Btn_clear.pack()
gui.mainloop()