# -*- coding: utf-8 -*-
import tkinter as tk

#Global vars
OText1 = "Обов'язкова плата становить \t: "
OText2 = "Допомога держави становить : "
OutputSum = OText1
OutputHelp = OText2
Output1 = Output2 = None

root = FrameEntry = FrameLabels = None

ButtonCalc = ButtonExit = None

EntryAvr = EntryPeo = EntrySum = EntryMin = None

def Calc():
    global root,EntryAvr,EntryMin,EntryPeo,EntrySum,Output1,Output2,OutputHelp,OutputSum,OText1,OText2,ButtonCalc,ButtonExit
    Avr = str(EntryAvr.get())
    People = str(EntryPeo.get())
    Sum = str(EntrySum.get())
    Min = str(EntryMin.get())
    if(Avr.isdigit() and People.isdigit() and Sum.isdigit() and Min.isdigit()):
        res_pr = ((int(Avr) / int(People)) / int(Min) / 2 * 15) / 100
        res = res_pr * int(Avr)
        help = int(Sum) - res
        res = round(res,2)
        help = round(help,2)
        OutputSum = OText1 + str(res)
        OutputHelp = OText2 + str(help)
        Output1.configure(text = OutputSum)
        Output2.configure(text = OutputHelp)
    else:
        exit()

def Main():
    global root,EntryAvr,EntryMin,EntryPeo,EntrySum,Output1,Output2,OutputHelp,OutputSum,OText1,OText2,ButtonCalc,ButtonExit
    root = tk.Tk()
    root.title("Калькулятор субсидій")
    root.resizable(False,False)
    root.geometry("500x450")
    root.configure(bg = 'lightblue')
    FrameLabels = tk.Frame(root,bg = 'lightblue')
    FrameEntry = tk.Frame(root,bg = 'lightblue')

    ButtonCalc = tk.Button(root,font = "Arial 14",text = "Розрахувати",command = lambda: Calc())
    ButtonExit = tk.Button(root,font = "Arial 14",text = "Закрити",command = lambda: root.quit())

    #Labels
    tk.Label(FrameLabels,bg = 'lightblue',font = "Arali 14", text = "Середній дохід \t\t: ").place(x = 10,y = 10)
    tk.Label(FrameLabels,bg = 'lightblue',font = "Arali 14", text = "Кількість людей \t\t: ").place(x = 10,y = 50)
    tk.Label(FrameLabels,bg = 'lightblue',font = "Arali 14", text = "Сума нарахувань \t\t: ").place(x = 10,y = 90)
    tk.Label(FrameLabels,bg = 'lightblue',font = "Arali 14", text = "Прожитковий мінімум \t: ").place(x = 10,y = 130)
    tk.Label(FrameLabels,bg = 'lightblue',font = "Arali 10", text = "Прожитковий мінімум на 1 січня 2019 р. \nдорівнює 1853 грн. ").place(x = 10,y = 170)

    #OutputLabels
    Output1 = tk.Label(root,bg = 'lightblue',font = "Arali 14", text = OutputSum)
    Output2 = tk.Label(root,bg = 'lightblue',font = "Arali 14", text = OutputHelp)

    Output1.place(x = 10,y = 220)
    Output2.place(x = 10,y = 250)

    #Entry
    EntryAvr = tk.Entry(FrameEntry,font = "Arial 12")
    EntryPeo = tk.Entry(FrameEntry,font = "Arial 12")
    EntrySum = tk.Entry(FrameEntry,font = "Arial 12")
    EntryMin = tk.Entry(FrameEntry,font = "Arial 12")

    EntryAvr.place(x = 10,y = 10)
    EntryPeo.place(x = 10,y = 50)
    EntrySum.place(x = 10,y = 90)
    EntryMin.place(x = 10,y = 130)

    ButtonCalc.place(x = 10,y = 320,width = 480,height = 50)
    ButtonExit.place(x = 10,y = 390,width = 480,height = 50)
    FrameLabels.place(x = 0,y = 0,width = 300,height = 400)
    FrameEntry.place(x = 300,y = 0,width = 200,height = 400)
    root.mainloop()


if __name__ == "__main__":
    Main()
