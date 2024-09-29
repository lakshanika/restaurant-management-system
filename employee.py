from tkinter import *
from PIL import ImageTk,Image
from PIL import Image,ImageDraw,ImageFont
from tkinter import messagebox
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import ttk


root=Tk()
root.title('Employee')
root.iconbitmap('C:\\Users\\laksh\\tkinter\\project\\restaurant.ico')
root.geometry('2050x900+0+0')


img_resize=Image.open(r'C:\Users\laksh\HTML website creation\bg3.jpg').resize((1535,800))
pic=ImageTk.PhotoImage(img_resize)
label=Label(root,image=pic)
label.place(x=0)



def addemployee():
    
    eid=StringVar()
    ename=StringVar()
    ephone=StringVar()
    epost=StringVar()
    ejoin=StringVar()
    esalary=StringVar()
    
    
    def add():
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"insert into employee values('{id_get.get()}','{name_get.get()}','{phone_get.get()}',\
'{post_combo.get()}','{date_get.get()}','{salary_get.get()}')")
        cursor.execute("commit")
        con.close()
    def delete():
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"delete from employee where emp_id=({id_get.get()}) or name=('{name_get.get()}')")
        cursor.execute("commit")
        con.close()       
    def clear():
        eid.set('')
        ename.set('')
        ephone.set('')
        epost.set('')
        ejoin.set('')
        esalary.set('')


    emp_win=Toplevel(root)
    emp_win.geometry("590x440+200+200")
    emp_win.title("Add Employee")
    emp_frame=LabelFrame(emp_win,bg="#60F4EE",\
    font=("Arial",15,"bold"),relief="ridge",bd=5)
    emp_frame.place(x=20,y=20,width=550,height=400)
    
    e_id=Label(emp_frame,text="Employee ID:",font=("courier new",15,'bold'),bg="#60F4EE",fg="black")
    id_get=Entry(emp_frame,textvariable=eid,font=("courier new",12,'bold'))
    
    name=Label(emp_frame,text="Name:",font=("courier new",15,'bold'),bg="#60F4EE",fg="black")
    name_get=Entry(emp_frame,textvariable=ename,font=("courier new",12,'bold'))
    
    phone=Label(emp_frame,text="Phone No:",font=("courier new",15,'bold'),bg="#60F4EE",fg="black")
    phone_get=Entry(emp_frame,textvariable=ephone,font=("courier new",12,'bold'))
    
    post=Label(emp_frame,text="Post:",font=("courier new",15,'bold'),bg="#60F4EE",fg="black")
    post_combo=ttk.Combobox(emp_frame,textvariable=epost,font=("courier new",12,'bold'))
    post_combo['values']=('Chef','Manager','Waiter')

    date=Label(emp_frame,text="Joining Date:",font=("courier new",15,'bold'),bg="#60F4EE",fg="black")
    date_get=Entry(emp_frame,textvariable=ejoin,font=("courier new",12,'bold'))
    
    salary=Label(emp_frame,text="Salary:",font=("courier new",15,'bold'),bg="#60F4EE",fg="black")
    salary_get=Entry(emp_frame,textvariable=esalary,font=("courier new",12,'bold'))
    
    
    add_btn=Button(emp_frame,text="Add",font=("courier new",12,'bold'),\
    bd=5,fg="white",bg="black",width=8,command=add)

    del_btn=Button(emp_frame,text="Delete",font=("courier new",12,'bold'),\
    bd=5,fg="white",bg="black",width=8,command=delete)
    
    clear_btn=Button(emp_frame,text="Clear",font=("courier new",12,'bold'),\
    bd=5,fg="white",bg="black",width=8,command=clear)


    e_id.place(x=20,y=50)
    id_get.place(x=200,y=50)
    name.place(x=20,y=90)
    name_get.place(x=200,y=90)
    phone.place(x=20,y=130)
    phone_get.place(x=200,y=130)
    post.place(x=20,y=170)
    post_combo.place(x=200,y=170)
    date.place(x=20,y=210)
    date_get.place(x=200,y=210)
    salary.place(x=20,y=250)
    salary_get.place(x=200,y=250)
    
    add_btn.place(x=90,y=330)
    del_btn.place(x=220,y=330)
    clear_btn.place(x=350,y=330)

#-------------------------------------view employee list-----------------------------------------

def employeelist():

    def search():
        
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"select * from employee where {search_by.get()}='{val1.get()}' ")
                
        result_set=cursor.fetchall()
        if len(result_set)!=0:
           emp_list.delete(*emp_list.get_children())
           for row in result_set:
                 emp_list.insert('',END,values=row)
     
        else:
            MessageBox.showinfo("Status","No record Found")
        cursor.execute("commit")
        con.close()

    def view():
        
        con=mysql.connect(host="localhost",user="root",password="#Lakshanika2004",database="rms")
        cursor=con.cursor()
        cursor.execute(f"select * from employee")
                
        result_set=cursor.fetchall()
        if len(result_set)!=0:
           emp_list.delete(*emp_list.get_children())
           for row in result_set:
                 emp_list.insert('',END,values=row)
     
        else:
            MessageBox.showinfo("Status","No record Found")
        cursor.execute("commit")
        con.close()


        
    window=Toplevel(root)
    window.geometry("2050x900+0+0")
    window.title("View Employee List")
    window.config(background='#60F4EE')



    data_frame=Frame(window,relief="groove",bg="black",bd=5)
    data_frame.place(x=150,y=20,width=1230,height=750)

    search_frame=Frame(data_frame,bg='#60F4EE',bd=5)
    search_frame.pack(side="top",fill="x")

    
    search_by=ttk.Combobox(search_frame,font=("courier new",12,"bold"))
    search_by['values']=('Post','Joining_Date','Salary')
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
    emp_list=ttk.Treeview(data_frame,columns=("ID","Name","Phone No","Post","Joining Date","Salary")\
                            ,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=emp_list.yview)
    x_scroll.config(command=emp_list.xview)
    y_scroll.pack(side=RIGHT,fill="y")
    x_scroll.pack(side=BOTTOM,fill="x")

    
    emp_list.heading("ID",text="ID")
    emp_list.heading("Name",text="Name")
    emp_list.heading("Phone No",text="Phone No")
    emp_list.heading("Post",text="Post")
    emp_list.heading("Joining Date",text="Joining Date")
    emp_list.heading("Salary",text="Salary")
    
    emp_list.pack(fill="both",expand=True)
    emp_list["show"]='headings'
        

#--------------------------------main------------------------------------------

frame=LabelFrame(root,bg='black')
frame.place(x=0,y=100,width=1535,height=75)

btn1=Button(frame,text="Employee List",font=("courier new",25,"bold"),\
                   cursor="hand2",bg='#0DECE4',fg="black",command=employeelist)
btn1.place(x=300,y=15,height=40,width=280)

btn2=Button(frame,text="Add Employee",font=("courier new",25,"bold"),\
                   cursor="hand2",bg='#0DECE4',fg="black",command=addemployee)
btn2.place(x=650,y=15,height=40,width=280)

Exit=Button(frame,text="Exit",font=("courier new",25,"bold"),\
                   cursor="hand2",bg="#0DECE4",fg="black",command=root.destroy)
Exit.place(x=1000,y=15,height=40,width=180)

root.mainloop()
    
