from tkinter import *
from PIL import ImageTk,Image
from PIL import Image,ImageDraw,ImageFont
from tkinter import messagebox
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import ttk
import os
import menu

root=Tk()


#---------------------------------------add menu item-----------------------------------------

def addmenuwindow():

    itemid=StringVar()
    itemname=StringVar()
    category=StringVar()
    itemtype=StringVar()
    price=StringVar()
    
    
    def add():
        
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"insert into menu values({itemid.get()},'{itemname.get()}','{category.get()}',\
'{itemtype.get()}','{price.get()}')")
        cursor.execute("commit")
        con.close()
    def delete():
        
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"delete from menu where item_id=({itemid_entry.get()}) or item_name=('{itemname_entry.get()}')")
        cursor.execute("commit")
        con.close()
        
    def clear():
        itemid.set("")
        itemname.set("")
        category.set("")
        itemtype.set("")
        price.set("")


    menu_win=Toplevel(root)
    menu_win.geometry("542x390+200+200")
    menu_win.title("Add Menu")
    newmenu_frame=LabelFrame(menu_win,bg="#0DECE4",font=("Arial",15,"bold"),relief="ridge",bd=5)
    newmenu_frame.place(x=20,y=20,width=500,height=350)

    itemid_lbl=Label(newmenu_frame,text="Item ID:",font=("courier new",15,'bold'),bg="#0DECE4",fg="black")
    itemid_entry=Entry(newmenu_frame,textvariable=itemid,font=("courier new",12,'bold'))
    itemname_lbl=Label(newmenu_frame,text="Item Name:",font=("courier new",15,'bold'),bg="#0DECE4",fg="black")
    itemname_entry=Entry(newmenu_frame,textvariable=itemname,font=("courier new",12,'bold'))
    itemcategory_lbl=Label(newmenu_frame,text="Category:",font=("courier new",15,'bold'),bg="#0DECE4",fg="black")
    itemcategory_combo=ttk.Combobox(newmenu_frame,textvariable=category,font=("courier new",12,'bold'))
    itemcategory_combo['values']=('starter','Beverages','Main cource')
    itemtype_lbl=Label(newmenu_frame,text="Type:",font=("courier new",15,'bold'),bg="#0DECE4",fg="black")
    itemtype_combo=ttk.Combobox(newmenu_frame,textvariable=itemtype,font=("courier new",12,'bold'))
    itemtype_combo['values']=('Veg','non veg')
    price_lbl=Label(newmenu_frame,text="Price:",font=("courier new",15,'bold'),bg="#0DECE4",fg="black")
    price_entry=Entry(newmenu_frame,textvariable=price,font=("courier new",12,'bold'))
    
    
    add_btn=Button(newmenu_frame,text="Add",font=("courier new",15,'bold'),\
    bd=5,fg="white",bg="black",width=6,command=add)
    delete_btn=Button(newmenu_frame,text="Delete",font=("courier new",15,'bold'),\
    bd=5,fg="white",bg="black",width=6,command=delete)
    clear_btn=Button(newmenu_frame,text="Clear",font=("courier new",15,'bold'),\
    bd=5,fg="white",bg="black",width=6,command=clear)
    
    itemid_lbl.grid(row=0,column=0,padx=10,pady=10)
    itemid_entry.grid(row=0,column=1,padx=10,pady=10)
    itemname_lbl.grid(row=1,column=0,padx=10,pady=10)
    itemname_entry.grid(row=1,column=1,padx=10,pady=10)
    itemcategory_lbl.grid(row=2,column=0,padx=10,pady=10)
    itemcategory_combo.grid(row=2,column=1,padx=10,pady=10)
    itemtype_lbl.grid(row=3,column=0,padx=10,pady=10)
    itemtype_combo.grid(row=3,column=1,padx=10,pady=10)
    price_lbl.grid(row=4,column=0,padx=10,pady=10)
    price_entry.grid(row=4,column=1,padx=10,pady=10)
    
    add_btn.grid(row=5,column=0,padx=5,pady=5)
    delete_btn.grid(row=5,column=1,padx=5,pady=5)
    clear_btn.grid(row=5,column=2,padx=5,pady=5)    

#---------------------------------------view menu--------------------------------------

def viewmenu():
    menu.display()

#-------------------------------------------order---------------------------------------
def order():
    os.system("python order.py")

#---------------------------------employee window open------------------------------------

def employee_win():
    os.system("python employee.py")

#---------------------------------table window open------------------------------------

def table_win():
    os.system("python table.py")

#---------------------------------------view menu--------------------------------------
def viewcust():
    import customer

#-----------------------------------over------------------------------------------

root.title('Restaurant Management System')
root.iconbitmap('C:\\Users\\laksh\\tkinter\\project\\restaurant.ico')
root.geometry('2050x900+0+0')

img_resize=Image.open(r'C:\Users\laksh\HTML website creation\bg3.jpg').resize((1535,800))
pic=ImageTk.PhotoImage(img_resize)
label=Label(root,image=pic)
label.place(x=0)

title=Label(root,text='Restaurant Management System',fg='black',bg='#60F4EE',font=('courier new',40,'bold'))
title.pack(side='top')


frame=LabelFrame(root,bg='black')
frame.place(x=0,y=100,width=1535,height=75)


mb=Menubutton(frame,text="Menu",font=("courier new",25,"bold"),\
                cursor="hand2",bg="#0DECE4",fg="black")
mb.menu=Menu(mb)
mb['menu']=mb.menu
mb.menu.add_command(label='View Menu',font=("courier new",25,"bold"),command=viewmenu)
mb.menu.add_command(label='Add Menu Item',font=("courier new",25,"bold"),command=addmenuwindow)
mb.config(fg='black',bg='#0DECE4')
mb.place(x=350,y=15,height=40,width=180)


order=Button(frame,text="Order",font=("courier new",25,"bold"),\
                   cursor="hand2",bg='#0DECE4',fg="black",command=order)
order.place(x=550,y=15,height=40,width=180)


cb=Menubutton(frame,text="Customer",font=("courier new",25,"bold"),\
                cursor="hand2",bg="#0DECE4",fg="black")
cb.menu=Menu(cb)
cb['menu']=cb.menu
cb.menu.add_command(label='Customer List',font=("courier new",25,"bold"),command=viewcust)
cb.config(fg='black',bg='#0DECE4')
cb.place(x=750,y=15,height=40,width=210)


Exit=Button(frame,text="Exit",font=("courier new",25,"bold"),\
                   cursor="hand2",bg="#0DECE4",fg="black",command=root.destroy)
Exit.place(x=980,y=15,height=40,width=180)

waiter_btn=PhotoImage(file=r'C:\Users\laksh\tkinter\project\waiter.png')
waiter=Button(root,image=waiter_btn,font=("courier new",25,"bold"),\
                   cursor="hand2",bg='black',fg="black",command=employee_win)
waiter.place(x=300,y=350,height=300,width=300)

table_btn=PhotoImage(file=r'C:\Users\laksh\tkinter\project\table.png')
table=Button(root,image=table_btn,font=("courier new",25,"bold"),\
                   cursor="hand2",bg='black',fg="#0DECE4",command=table_win)
table.place(x=900,y=350,height=300,width=300)



root.mainloop()
