from tkinter import *
import back_end

def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

def delete_command():
    back_end.delete(selected_row[0])

def view_command():
    list.delete(0, END)
    for row in back_end.view():
        list.insert(END, row)


def search_command():
    list.delete(0, END)
    for row in back_end.search(name_text.get(), college_text.get(), address_text.get(), phone_number.get(), room_number.get(), payment_status.get()):
        list.insert(END, row)


def add_command():
    back_end.insert(name_text.get(), college_text.get(), address_text.get(
    ), phone_number.get(), room_number.get(), payment_status.get())

    list.delete(0, END)
    list.insert(END, (name_text.get(), college_text.get(), address_text.get(
    ), phone_number.get(), room_number.get(), payment_status.get()))


win = Tk()
win.wm_title("SARIM'S ACADEMY REGISTRATION FORM")
win.iconbitmap('iec.ico')

l1 = Label(win, text="Name")
l1.grid(row=0, column=0)
l2 = Label(win, text="College")
l2.grid(row=0, column=2)

l3 = Label(win, text="Address")
l3.grid(row=1, column=0)
l4 = Label(win, text="Phone")
l4.grid(row=1, column=2)

l3 = Label(win, text="Room")
l3.grid(row=2, column=0)
l4 = Label(win, text="Payment")
l4.grid(row=2, column=2)
############################################
name_text = StringVar()
e1 = Entry(win, textvariable=name_text)
e1.grid(row=0, column=1)

college_text = StringVar()
e2 = Entry(win, textvariable=college_text)
e2.grid(row=0, column=3)

address_text = StringVar()
e3 = Entry(win, textvariable=address_text)
e3.grid(row=1, column=1)

phone_number = StringVar()
e4 = Entry(win, text=phone_number)
e4.grid(row=1, column=3)

room_number = StringVar()
e5 = Entry(win, textvariable=room_number)
e5.grid(row=2, column=1)

payment_status = StringVar()
e6 = Entry(win, text=payment_status)
e6.grid(row=2, column=3)

###############################
list = Listbox(win, height=20, width=50)  # OUTPUT LISTBOX
list.grid(row=3, column=1, rowspan=9, columnspan=3)

sb = Scrollbar(win)  # scroll bar
sb.grid(row=3, column=4, rowspan=13)
##################################

# to select list_item from o/p listbox
list.bind('<<ListboxSelect>>',get_selected_row)

#################################
b1 = Button(win, text="ADD", width=6, pady=5, command=add_command)
b1.grid(row=3, column=0)

b2 = Button(win, text="Search", width=6, pady=5, command=search_command)
b2.grid(row=4, column=0)

b3 = Button(win, text="Delete", width=6, pady=5,command= delete_command)
b3.grid(row=5, column=0)

b4 = Button(win, text="View All", width=6, pady=5, command=view_command)
b4.grid(row=6, column=0)

b5 = Button(win, text="Close", width=6, pady=5, command=win.destroy)
b5.grid(row=7, column=0)


win.mainloop()
