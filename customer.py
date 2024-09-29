from tkinter import *
from PIL import ImageTk,Image
from PIL import Image,ImageDraw,ImageFont
from tkinter import messagebox
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import ttk
import os

#--------------------------view customer list------------------------------

def view():
    con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
    cursor=con.cursor()
    cursor.execute(f"select * from customer")
        
    result_set=cursor.fetchall()
    if len(result_set)!=0:
        cust_list.delete(*cust_list.get_children())
        for row in result_set:
            cust_list.insert('',END,values=row)
    else:
        MessageBox.showinfo("Status","No record Found")
    cursor.execute("commit")
    con.close()

    
root=Tk()
root.geometry("2050x900+0+0")
root.title("View Customer List")
root.config(background='#60F4EE')



data_frame=Frame(root,relief="groove",bg="black",bd=5)
data_frame.place(x=230,y=20,width=1050,height=750)

search_frame=Frame(data_frame,bg='#60F4EE',bd=5)
search_frame.pack(side="top",fill="x")
    

view_btn=Button(search_frame,text="View List",font=("courier new",15,"bold"),\
                fg='white',bg='black',bd=5,width=12,command=view)
view_btn.pack(side="top",fill="x")


    
y_scroll=ttk.Scrollbar(data_frame,orient=VERTICAL)
x_scroll=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
cust_list=ttk.Treeview(data_frame,columns=("Customer ID","Name","Phone","Bill No","Total Bill")\
                        ,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
y_scroll.config(command=cust_list.yview)
x_scroll.config(command=cust_list.xview)
y_scroll.pack(side=RIGHT,fill="y")
x_scroll.pack(side=BOTTOM,fill="x")

    
cust_list.heading("Customer ID",text="Customer ID")
cust_list.heading("Name",text="Name")
cust_list.heading("Phone",text="Phone")
cust_list.heading("Bill No",text="Bill No")
cust_list.heading("Total Bill",text="Total Bill")

cust_list.pack(fill="both",expand=True)
cust_list["show"]='headings'    

root.mainloop()
