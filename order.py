from tkinter import *
from PIL import ImageTk,Image
from PIL import Image,ImageDraw,ImageFont
from tkinter import messagebox
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import ttk
import random



def welcome():
    textarea.delete("1.0",END)
    textarea.insert(END,"\t\tWelcome To The Restaurant")
    textarea.insert(END,f"\n\nBill No: {bill_no.get()}")
    textarea.insert(END,f'\t\t\t\tCustomer Name: {c_name.get()}')
    textarea.insert(END,f'\nPhone: {c_phone.get()}')
    textarea.insert(END,"\n=========================================================\n")
    textarea.insert(END,'\tProduct\t\tQuantity\t\tPrice')
    textarea.insert(END,"\n=========================================================\n")
    textarea.configure(font=('courier new', 15,'bold'))
    #pname_combo.focus()
    
def add():
    
    if pname_combo.get()=='':
        Messagebox.showerror("Error","Item canot be entry")
    else:
        
        amt=rate.get()*qty.get()
        prices.append(amt)
        textarea.insert(END,f'\n\t{product.get()}\t\t{qty.get()}\t\t{amt}')
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        query=f"INSERT INTO bill(item_name,quantity,price,bill_no)values('{product.get()}',{qty.get()},\
{rate.get()},{n})"
        cursor.execute(query)
        con.commit()
        
        product.set('')
        qty.set('')
        rate.set('')
        pname_combo.focus()
        
def bill():
    textarea.insert(END,"\n=========================================================\n")
    textarea.insert(END,f'\t\t\tTotal Bill Amount:\t\t{sum(prices)}')
    textarea.insert(END,"\n=========================================================\n")
#-----------------------------------------storing in Database-----------------------------
    con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
    cursor=con.cursor()
    query=f"INSERT INTO customer(cust_name,cust_phone,bill_no,tot_bill)\
    values('{c_name.get()}','{c_phone.get()}',{n},{sum(prices)})"
    cursor.execute(query)
    con.commit()
    con.close()
    
def clear():
    c_name.set('')
    c_phone.set('')
    product.set('')
    qty.set('')
    rate.set('')
    cname_entry.focus()
    textarea.delete("1.0",END)
    amt=0

def pricelist():
    
    def view():
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"select item_name,price from menu")
                    
        result_set=cursor.fetchall()
        if len(result_set)!=0:
            price_list.delete(*price_list.get_children())
            for row in result_set:
                price_list.insert('',END,values=row)
         
        else:
            MessageBox.showinfo("Status","No record Found")
        cursor.execute("commit")
        con.close()

    
    window=Toplevel(root)
    window.geometry("2050x900+0+0")
    window.title("Price List")
    window.config(background='#60F4EE')

    data_frame=Frame(window,relief="groove",bg="black",bd=5)
    data_frame.place(x=150,y=20,width=1230,height=750)

    search_frame=Frame(data_frame,bg='#60F4EE',bd=5)
    search_frame.pack(side="top",fill="x")

    view_btn=Button(search_frame,text="View Price",font=("courier new",15,"bold"),\
                    fg='white',bg='black',bd=5,width=12,command=view)
    view_btn.pack(side="top",fill="x")


        
    y_scroll=ttk.Scrollbar(data_frame,orient=VERTICAL)
    x_scroll=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
    price_list=ttk.Treeview(data_frame,columns=("Item Name","Price")\
                          ,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=price_list.yview)
    x_scroll.config(command=price_list.xview)
    y_scroll.pack(side=RIGHT,fill="y")
    x_scroll.pack(side=BOTTOM,fill="x")

    price_list.heading("Item Name",text="Item Name")
    price_list.heading("Price",text="Price")             
    price_list.pack(fill="both",expand=True)
    price_list["show"]='headings'

    window.mainloop()

#---------------------------------------------------------------------------


root=Tk()
root.geometry("2050x900+0+0")
root.title("Place order")

img_resize=Image.open(r'C:\Users\laksh\HTML website creation\bg3.jpg').resize((1535,800))
pic=ImageTk.PhotoImage(img_resize)
label=Label(root,image=pic)
label.place(x=0)

title=Label(root,text='Billing Area',fg='black',bg='#60F4EE',font=('courier new',35,'bold'))
title.pack(side='top')

frame=LabelFrame(root,bg='black')
frame.place(x=90,y=70,width=1350,height=670)

order_frame=LabelFrame(frame,bg="#0DECE4",font=("courier new",15,"bold"),relief="ridge",bd=5)
order_frame.place(x=20,y=20,width=1307,height=630)

#-------------------------------------------Variables--------------------------------------------
prices=[]
amt=0

c_name=StringVar()
c_phone=StringVar()
bill_no=StringVar()
n=random.randint(1000,10000)
bill_no.set(str(n))
product=StringVar()
qty=IntVar()
rate=IntVar()
#-------------------------------------customer frame-------------------------------------
customer_frame=LabelFrame(order_frame,text="Customer Detail",bg="black",fg="white",font=("courier new",15,"bold"))
customer_frame.place(x=5,y=5,relwidth=0.993)

cname_lbl=Label(customer_frame,text="Customer Name:",bg="black",fg="white",font=("courier new",15,"bold"))
cname_lbl.grid(row=0,column=0,padx=10,pady=10)
cname_entry=Entry(customer_frame,font=("courier new",15,"bold"),textvariable=c_name)
cname_entry.grid(row=0,column=1,padx=10,pady=10)

cphone_lbl=Label(customer_frame,text="Customer Phone:",bg="black",fg="white",font=("courier new",15,"bold"))
cphone_lbl.grid(row=0,column=2,padx=10,pady=10)
cphone_entry=Entry(customer_frame,font=("courier new",15,"bold"),textvariable=c_phone)
cphone_entry.grid(row=0,column=3,padx=10,pady=10)
ok_btn=Button(customer_frame,text="OK",bg="white",fg="black",relief=GROOVE,bd=3,\
              font=("courier new",12,"bold"),width=12,command=welcome)
ok_btn.grid(row=0,column=4,padx=10,pady=10)

#-------------------------------------product frame-------------------------------------

detail_frame=LabelFrame(order_frame,text="Product Detail",bg="black",fg="white",\
                        font=("courier new",15,"bold"),relief="ridge",bd=5)
detail_frame.place(x=5,y=120,width=480,height=480)

pname_lbl=Label(detail_frame,text="Product:",bg="black",fg="white",font=("courier new",15,"bold"))
pname_lbl.grid(row=0,column=0,padx=10,pady=20)
pname_combo=ttk.Combobox(detail_frame,font=("courier new",15,"bold"),textvariable=product)
con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
cursor=con.cursor()
cursor.execute("select item_name from menu")
result_set=cursor.fetchall()
item=[]
b_list=[]
for item in result_set:
    b_list.append(item[0])
pname_combo['values']=b_list
con.commit()
con.close()
pname_combo.grid(row=0,column=1,padx=10,pady=20)

prate_lbl=Label(detail_frame,text="Rate:",bg="black",fg="white",font=("courier new",15,"bold"))
prate_lbl.grid(row=1,column=0,padx=10,pady=20)
prate_entry=Entry(detail_frame,font=("courier new",15,"bold"),relief=SUNKEN,textvariable=rate)
prate_entry.grid(row=1,column=1,padx=10,pady=20)

pqty_lbl=Label(detail_frame,text="Quantity:",bg="black",fg="white",font=("courier new",15,"bold"))
pqty_lbl.grid(row=2,column=0,padx=10,pady=20)
pqty_entry=Entry(detail_frame,font=("courier new",15,"bold"),relief=SUNKEN,textvariable=qty)
pqty_entry.grid(row=2,column=1,padx=10,pady=20)

#-------------------------------------product buttons-------------------------------------
button_frame=Frame(detail_frame,bg="black",bd=5)
button_frame.place(x=50,y=250,width=330,height=150)

add_btn=Button(button_frame,text="Add Item",bg="white",fg="black",relief=GROOVE,\
               font=("courier new",12,"bold"),width=12,command=add)
add_btn.grid(row=3,column=0,padx=20,pady=20)

bill_btn=Button(button_frame,text="Generate Bill",bg="white",relief=GROOVE,fg="black",\
                font=("courier new",12,"bold"),width=14,command=bill)
bill_btn.grid(row=3,column=1,padx=10,pady=20)

remove_btn=Button(button_frame,text="Clear",bg="white",fg="black",relief=GROOVE,\
                  font=("courier new",12,"bold"),width=12,command=clear)
remove_btn.grid(row=4,column=0,padx=20,pady=20)

pricelist_btn=Button(button_frame,text="Price List",bg="white",fg="black",relief=GROOVE,\
                font=("courier new",12,"bold"),width=14,command=pricelist)
pricelist_btn.grid(row=4,column=1,padx=10,pady=20)

#-----------------------------------------Bill Area-------------------------------------------

billarea_frame=Frame(order_frame,bg="white",relief="ridge",bd=5)
billarea_frame.place(x=520,y=120,width=750,height=480)
bill_title=Label(billarea_frame,text="Bill Area",font=("courier new",20,"bold"),relief=GROOVE, bd=7)
bill_title.pack(fill="x")
scroll_y=Scrollbar(billarea_frame,orient=VERTICAL)
textarea=Text(billarea_frame,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()

cname_entry.focus()


root.mainloop()

