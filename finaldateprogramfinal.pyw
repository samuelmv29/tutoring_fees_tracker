from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import datetime
import xlwt
import xlrd
from xlutils.copy import copy
from functools import partial


#this contains the current date
complete_date = datetime.datetime.now()
date = complete_date.strftime("%x")


root = Tk()
root.geometry("500x500")


main_label = tkFont.Font(size = 17)
button_label = tkFont.Font(size = 13)

def func_button(i, index):
    subject,fees,classes = i.split(" ")
    global master_i
    master_i = Toplevel(root)
    master_i.geometry("500x500")
    master_i.title(i+" record")


    
    def i_edit():
        loc = r"C:\Users\samue\Desktop\recordbookfinal.xls"
        rb = xlrd.open_workbook(loc)
        wb = copy(rb)
        i_sheet = wb.get_sheet(index+1)
        isheet = rb.sheet_by_index(index+1)
        
        current_row_i = len(i_sheet._Worksheet__rows)


        if isheet.cell(current_row_i-1, 5).value != date:        
            i_sheet.write(current_row_i, 4, (current_row_i-4))
            i_sheet.write(current_row_i, 5, date)

            if ((current_row_i - 4) % (int(classes))) == 0:
                messagebox.showinfo("fees", "Please pay the fees for "+i)        
                i_sheet.write(current_row_i, 6, int(fees))
        wb.save(r"C:\Users\samue\Desktop\recordbookfinal.xls")
    
    ##deleting 
    def i_edit_delete():
        loc = r"C:\Users\samue\Desktop\recordbookfinal.xls"
        rb = xlrd.open_workbook(loc)
        i_sheet = rb.sheet_by_index(index+1)
        i_sheet.cell_value(0,0)
        for a in range(4,i_sheet.nrows):
            cell_value = i_sheet.cell(a, 5).value
            if cell_value == date:
                wb = copy(rb)
                i_sheet_1 = wb.get_sheet(index+1)
                i_sheet_1.write(a, 5, "")
                i_sheet_1.write(a, 4, "")
                i_sheet_1.write(a, 6, "")
                wb.save(r"C:\Users\samue\Desktop\recordbookfinal.xls")
            else:
                pass
            
        
    frame_i_1 = Frame(master_i)
    frame_i_2 = Frame(master_i)
    frame_i_1.pack()
    frame_i_2.pack()
    text_i = Label(frame_i_1, text = "Please confirm if you want to add this date to the record book").pack()
    button_confirm_i = Button(frame_i_2, text = "confirm", command = i_edit).pack(side = "left")
    button_delete_i = Button(frame_i_2, text = "delete", command = i_edit_delete).pack(side = "right")
    #button_show = tk.Button(master_maths, text = "Show the dates recorded", command = show).pack()
    master_i.mainloop()
        
def button_creator(canvas_1):
    file = open(r"C:\Users\samue\Desktop\samuel_dates.txt", "r")
    list_1 = (file.read()).split(",")
    list_1.remove("0 0 0")
    new = 150
    
    for i in list_1:


        new += 50
        button_1 = Button(canvas_1, text = (i.split(" "))[0], font = button_label, width = 10, command =(lambda i = i:func_button(i,list_1.index(i))))
        button_1.place(x = 200, y = new)
    file.close()

def back_func(i):
        i.pack_forget()
        main_theme()

def confirm_subject(subject, fees, classes):
    file = open(r"C:\Users\samue\Desktop\samuel_dates.txt", "a")
    file.write(","+subject+" "+fees+" "+classes)
    file = open(r"C:\Users\samue\Desktop\samuel_dates.txt", "r")
    list_1 = (file.read()).split(",")
    file.close()

    loc = r"C:\Users\samue\Desktop\recordbookfinal.xls"
    rb = xlrd.open_workbook(loc)
    wb = copy(rb)
    sheet_1 = wb.add_sheet(subject)
    
    #sheet_edited = rb.sheet_by_index(list_1.index(subject))
    #sheet_edited.cell_value(0,0)

    sheet_written = wb.get_sheet(list_1.index(subject+" "+fees+" "+classes))
    
    sheet_written.write(3,4,subject)
    sheet_written.write(4,4,"S.NO")
    sheet_written.write(4,5,"DATE")
    sheet_written.write(4,6,"FEES")

    

    wb.save(r"C:\Users\samue\Desktop\recordbookfinal.xls")
    
   

def add_subjects(canvas_1):

    canvas_2 = Canvas(root)
        
    for i in root.winfo_children():
        if isinstance(i, Toplevel):
            i.destroy()
            
    canvas_1.pack_forget()

    canvas_2.pack(fill = BOTH, expand = True)

    subject_var = StringVar()
    classes_var = StringVar()
    fees_var = StringVar()
    

    label_sub_entry = Label(canvas_2, text = "Enter subject: ", font = main_label)
    label_sub_entry.place(x = 85, y = 65)

    label_sub_classes = Label(canvas_2,text = "Enter classes: ", font = main_label)
    label_sub_classes.place(x = 85, y = 165)
 
    label_fees_entry = Label(canvas_2, text = "Enter fees: ", font = main_label)
    label_fees_entry.place(x = 110, y = 265)
    
    
    entry_sub = Entry(canvas_2, text = subject_var)
    entry_sub.place(x = 250, y = 73)

    entry_classes = Entry(canvas_2, text = classes_var)
    entry_classes.place(x = 250, y = 173)
    
    entry_fees = Entry(canvas_2, text = fees_var)
    entry_fees.place(x = 250, y = 273)

    back_button = Button(canvas_2, text = "←", font = button_label, command = lambda: back_func(canvas_2))
    back_button.place(x= 10, y = 10)

    enter_button = Button(canvas_2, text = "Confirm", font = button_label, command = lambda: confirm_subject(subject_var.get(),fees_var.get(),classes_var.get()))
    enter_button.place(x = 220, y = 400)
       

def main_theme():
    
    canvas_1 = Canvas(root)
    canvas_1.pack(fill = BOTH, expand = True)
    
    label = Label(canvas_1, text = "Hello Samuel, which tuitions do u have today?", font = main_label)
    label.place(x = 12, y = 100)

    button_creating = Button(canvas_1, text = "+", font = main_label, command = lambda: add_subjects(canvas_1))
    button_creating.place(x = 450,y = 450)

    button_creator(canvas_1)


main_theme()

root.mainloop()
