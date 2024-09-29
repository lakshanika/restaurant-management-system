from tkinter import *
from PIL import ImageTk,Image
from PIL import Image,ImageDraw,ImageFont
from tkinter import messagebox
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import ttk


    #-----------------------------------------------view-------------------------------------------
def display():
    def search():
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"select * from menu where {search_by.get()}='{val1.get()}' ")
                    
        result_set=cursor.fetchall()
        if len(result_set)!=0:
            menu_list.delete(*menu_list.get_children())
            for row in result_set:
                menu_list.insert('',END,values=row)
         
        else:
            MessageBox.showinfo("Status","No record Found")
        cursor.execute("commit")
        con.close()

    def view():
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"select * from menu")
                    
        result_set=cursor.fetchall()
        if len(result_set)!=0:
            menu_list.delete(*menu_list.get_children())
            for row in result_set:
                menu_list.insert('',END,values=row)
         
        else:
            MessageBox.showinfo("Status","No record Found")
        cursor.execute("commit")
        con.close()


            
    root=Tk()
    root.geometry("2050x900+0+0")
    root.title("View Menu")
    root.config(background='#60F4EE')



    data_frame=Frame(root,relief="groove",bg="black",bd=5)
    data_frame.place(x=150,y=20,width=1230,height=750)

    search_frame=Frame(data_frame,bg='#60F4EE',bd=5)
    search_frame.pack(side="top",fill="x")

        
    search_by=ttk.Combobox(search_frame,font=("courier new",12,"bold"))
    search_by['values']=("Item_ID","Item_Name","Category","Item_Type","Price")
    search_by.grid(row=0,column=3,padx=2,pady=2)
    val1=Entry(search_frame)
    val1.grid(row=0,column=5,padx=2,pady=2)

    search_btn=Button(search_frame,text="Search",font=("courier new",15,"bold"),\
                      fg='white',bg='black',bd=5,width=12,command=search)
    search_btn.grid(row=0,column=6,padx=10,pady=5)
        
    view_btn=Button(search_frame,text="View All",font=("courier new",15,"bold"),\
                    fg='white',bg='black',bd=5,width=12,command=view)
    view_btn.grid(row=0,column=7,padx=10,pady=5)


        
    y_scroll=ttk.Scrollbar(data_frame,orient=VERTICAL)
    x_scroll=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
    menu_list=ttk.Treeview(data_frame,columns=("Item ID","Item Name","Category","Type","Price")\
                          ,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=menu_list.yview)
    x_scroll.config(command=menu_list.xview)
    y_scroll.pack(side=RIGHT,fill="y")
    x_scroll.pack(side=BOTTOM,fill="x")

                
    menu_list.heading("Item ID",text="Item ID")
    menu_list.heading("Item Name",text="Item Name")
    menu_list.heading("Category",text="Category")
    menu_list.heading("Type",text="Type")
    menu_list.heading("Price",text="Price")

                
    menu_list.pack(fill="both",expand=True)
    menu_list["show"]='headings'

    root.mainloop()
