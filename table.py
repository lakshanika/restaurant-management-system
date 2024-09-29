from tkinter import *
from PIL import ImageTk,Image
from PIL import Image,ImageDraw,ImageFont
from tkinter import messagebox
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import ttk


root=Tk()
root.title('Table Management')
root.iconbitmap('C:\\Users\\laksh\\tkinter\\project\\restaurant.ico')
root.geometry('2050x900+0+0')

img_resize=Image.open(r'C:\Users\laksh\HTML website creation\bg3.jpg').resize((1535,800))
pic=ImageTk.PhotoImage(img_resize)
label=Label(root,image=pic)
label.place(x=0)


def addtablewindow():
    table_no=StringVar()
    capacity=IntVar()
    
    
    def add():  
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"insert into tables values('{tableid_entry.get()}',{capacity_entry.get()})")
        cursor.execute("commit")
        con.close()
   
    def clear():
        table_no.set("")
        capacity.set(0)

    def delete():
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"delete from tables where table_no=('{tableid_entry.get()}')")
        cursor.execute("commit")
        con.close()
        

    table_win=Toplevel(root)
    table_win.geometry("513x293+200+200")
    table_win.title("Add Table")
    table_frame=LabelFrame(table_win,bg="#60F4EE",\
    font=("Arial",15,"bold"),relief="ridge",bd=5)
    table_frame.place(x=20,y=20,width=470,height=250)
    
    tableid_lbl=Label(table_frame,text="Table no:",font=("courier new",15,'bold'),bg="#60F4EE",fg="black")
    tableid_entry=Entry(table_frame,textvariable=table_no,font=("courier new",12,'bold'))
    
    capacity_lbl=Label(table_frame,text="Table Capacity:",font=("courier new",15,'bold'),bg="#60F4EE",fg="black")
    capacity_entry=Entry(table_frame,textvariable=capacity,font=("courier new",12,'bold'))

    add_btn=Button(table_frame,text="Add",font=("courier new",15,'bold'),\
    bd=5,fg="white",bg="black",width=6,command=add) 
    clear_btn=Button(table_frame,text="Clear",font=("courier new",15,'bold'),\
    bd=5,fg="white",bg="black",width=6,command=clear)
    delete_btn=Button(table_frame,text="Delete",font=("courier new",15,'bold'),\
    bd=5,fg="white",bg="black",width=6,command=delete)
    
    tableid_lbl.grid(row=2,column=0,padx=10,pady=10)
    tableid_entry.grid(row=2,column=1,padx=10,pady=10)
    capacity_lbl.grid(row=4,column=0,padx=10,pady=10)
    capacity_entry.grid(row=4,column=1,padx=10,pady=10)


    add_btn.place(x=70,y=170)
    clear_btn.place(x=280,y=170)
    delete_btn.place(x=180,y=170)

#--------------------------view table list------------------------------

def viewlist():

    def view():
        
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"select * from tables")
        
        result_set=cursor.fetchall()
        
        
        if len(result_set)!=0:
           table_list.delete(*table_list.get_children())
           for row in result_set:
                 table_list.insert('',END,values=row)
     
        else:
            MessageBox.showinfo("Status","No record Found")
        cursor.execute("commit")
        con.close()
    

    window=Toplevel(root)
    window.geometry("2050x900+0+0")
    window.title("View Table List")
    window.config(background='#60F4EE')



    data_frame=Frame(window,relief="groove",bg="black",bd=5)
    data_frame.place(x=230,y=20,width=1050,height=750)

    search_frame=Frame(data_frame,bg='#60F4EE',bd=5)
    search_frame.pack(side="top",fill="x")
    

    view_btn=Button(search_frame,text="View List",font=("courier new",15,"bold"),\
                    fg='white',bg='black',bd=5,width=12,command=view)
    view_btn.pack(side="top",fill="x")


    
    y_scroll=ttk.Scrollbar(data_frame,orient=VERTICAL)
    x_scroll=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
    table_list=ttk.Treeview(data_frame,columns=("Table No","Capacity")\
                            ,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=table_list.yview)
    x_scroll.config(command=table_list.xview)
    y_scroll.pack(side=RIGHT,fill="y")
    x_scroll.pack(side=BOTTOM,fill="x")

    
    table_list.heading("Table No",text="Table No")
    table_list.heading("Capacity",text="Capacity")

    table_list.pack(fill="both",expand=True)
    table_list["show"]='headings'

    

#----------------------------------main-------------------------------------------   

frame=LabelFrame(root,bg='black')
frame.place(x=0,y=100,width=1535,height=75)

btn1=Button(frame,text="Table List",font=("courier new",25,"bold"),\
                   cursor="hand2",bg='#0DECE4',fg="black",command=viewlist)
btn1.place(x=300,y=15,height=40,width=280)

btn2=Button(frame,text="Add Table",font=("courier new",25,"bold"),\
                   cursor="hand2",bg='#0DECE4',fg="black",command=addtablewindow)
btn2.place(x=650,y=15,height=40,width=280)

Exit=Button(frame,text="Exit",font=("courier new",25,"bold"),\
                   cursor="hand2",bg="#0DECE4",fg="black",command=root.destroy)
Exit.place(x=1000,y=15,height=40,width=180)

root.mainloop()
