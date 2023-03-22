from tkinter import *
from  tkinter import ttk
from tkinter.messagebox import showerror
import back

root = Tk()
root.title("Badania operacyjne i logistyka projekt")
root.geometry("1000x900")

fr = Frame(root)
fr.pack(side="top", expand=True, fill="both")


def clear():
    for widget in fr.winfo_children():
        widget.destroy()

def start_screen():
    Button(fr, text="CPM", padx=26, pady=20, command=CRM_input).pack()
    Button(fr, text="Zagadnienie pośrednika", padx=29, pady=20).pack()

def CRM_input():
    clear()
    root.title("CRM")

    ll = Label(fr, text="Add event", font=("Arial", 12, 'bold'))
    ll.grid(row=0, column=1, columnspan=3, sticky=W)

    Label(fr, text="Name", font=("Arial", 12)).grid(column=1, row=2, sticky=W, padx=5, pady=10)
    Label(fr, text="Duration(min)", font=("Arial", 12)).grid(column=1, row=3, sticky=W, padx=5, pady=10)
    Label(fr, text="Predecessors [eg.: 1,2,4]", font=("Arial", 12)).grid(column=1, row=4, sticky=W, padx=5, pady=10)

    b_name = Entry(fr)
    b_name.grid(column=2, row=2)
    b_time = Entry(fr)
    b_time.grid(column=2, row=3)
    b_pre = Entry(fr)
    b_pre.grid(column=2, row=4)

    add = Button(fr, text="Add Next", padx=20, pady=10, command=lambda: addNext(b_name.get(), b_time.get(), b_pre.get()))
    add.grid(column=1, row=6, sticky=W, padx=20, pady=20)
    cal = Button(fr, text="Calculate", padx=20, pady=10, command=calculate)
    cal.grid(column=2, row=6, sticky=W, padx=20, pady=20)

    Label(fr, text="Added events", font=("Arial", 12, 'bold')).grid(column=0, row=7, sticky=W,padx=5, pady=10, columnspan=3)

    list = ttk.Treeview(fr)
    list.grid(column=1, row=9, sticky=W, padx=20, pady=20)

    list['columns'] = ('ID', 'EventName', 'Predecessors', 'Time')

    list.column("#0", width=0, stretch=NO)
    list.column("ID", anchor=CENTER, width=30)
    list.column("EventName", anchor=CENTER, width=90)
    list.column("Predecessors", anchor=CENTER, width=90)
    list.column("Time", anchor=CENTER, width=90)

    list.heading("#0", text="", anchor=CENTER)
    list.heading("ID", text="ID", anchor=CENTER)
    list.heading("EventName", text="Name", anchor=CENTER)
    list.heading("Predecessors", text="Predecessors", anchor=CENTER)
    list.heading("Time", text="Time", anchor=CENTER)

    pos = 0
    for x in range(len(back.eventTable)):
        list.insert(parent='', index='end', iid=pos, text='',
        values=(pos+1,
                back.eventTable[pos].name,
                back.eventTable[pos].predecessors,
                back.eventTable[pos].time))
        pos +=1

def addNext(name, time, predecessors):

    def checkIfCorrect(time, predecessors):
        try:
            float(time)
        except ValueError:
            showerror(
                title='Error',
                message='Time value not an number')
            return False

        try:
            float(predecessors)
            return True
        except ValueError:
            try:
                [float(x.strip()) for x in predecessors.split(",")]
                return True
            except ValueError:
                showerror(
                    title='Error',
                    message='predecessors value not a number of a list of numbers separated by coma')
                return False

    if(checkIfCorrect(time, predecessors) == True):

        int_list = [int(x) for x in predecessors.split(",")]
        newEvent = back.Event(name, float(time), int_list)
        back.eventTable.append(newEvent)

        CRM_input()

def newCRM():
    back.eventTable.clear()
    CRM_input()

def calculate():
    #funkcja liczaca wszystko
    clear()

    #sciezka krytyczna i czas
    list = ttk.Treeview(fr)

    #bedzie wyswietlal grant chart w nowym oknie
    chartBtn = Button(fr, text="Grant Chart", padx=20, pady=10)
    chartBtn.grid(column=1, row=6, sticky=W, padx=20, pady=20)

    #wraca do wpisywania i zeruje liste
    newBtn = Button(fr, text="new CRM", padx=20, pady=10, command=newCRM)
    newBtn.grid(column=2, row=6, sticky=W, padx=20, pady=20)

    list.grid(column=2, row=9, padx=20, pady=20)

    list['columns'] = ('ID', 'EventName', 'Time', 'ES', 'EF', 'LS', 'LF', 'Slack', 'Critical')

    list.column("#0", width=0, stretch=NO)
    list.column("ID", anchor=CENTER, width=30)
    list.column("EventName", anchor=CENTER, width=90)
    list.column("Time", anchor=CENTER, width=90)
    list.column("ES", anchor=CENTER, width=40)
    list.column("EF", anchor=CENTER, width=40)
    list.column("LS", anchor=CENTER, width=40)
    list.column("LF", anchor=CENTER, width=40)
    list.column("Slack", anchor=CENTER, width=40)
    list.column("Critical", anchor=CENTER, width=90)

    list.heading("#0", text="", anchor=CENTER)
    list.heading("ID", text="ID", anchor=CENTER)
    list.heading("EventName", text="Name", anchor=CENTER)
    list.heading("Time", text="Time", anchor=CENTER)
    list.heading("ES", text="ES", anchor=CENTER)
    list.heading("EF", text="EF", anchor=CENTER)
    list.heading("LS", text="LS", anchor=CENTER)
    list.heading("LF", text="LF", anchor=CENTER)
    list.heading("Slack", text="Slack", anchor=CENTER)
    list.heading("Critical", text="Is critical", anchor=CENTER)

    pos = 0
    for x in range(len(back.eventTable)):
        if(back.eventTable[pos].critical == False):
            isCritical = "False"
        else:
            isCritical = "True"

        list.insert(parent='', index='end', iid=pos, text='',
                    values=(pos + 1,
                            back.eventTable[pos].name,
                            back.eventTable[pos].time,
                            back.eventTable[pos].es,
                            back.eventTable[pos].ef,
                            back.eventTable[pos].ls,
                            back.eventTable[pos].lf,
                            back.eventTable[pos].slack,
                            isCritical,
                            ))
        pos += 1


def Zagadnienie_posrednika():
    clear()
    root.title("Zagadnienie pośrednika")
    # tu miejsce na projekt nr 2

start_screen()
root.mainloop()