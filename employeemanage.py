import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import re
import sqlite3
mydb=sqlite3.connect('batch4pm.db')
#print("database created successfully..")
#print(mydb)
crsr=mydb.cursor()
window=Tk()
window.title('Registration Form')
window.maxsize(800,500)
window.configure(bg='grey')
window.geometry('800x500')
lbl11=Label(window,text='REGISTRATION FORM',bg='grey',fg='black',width=16)
lbl11.grid(row=0,column=1,padx=7,pady=7)
lbl11.config(font=('bold',10))
lbl1=Label(window,text='ID:',bg='grey',fg='black')
lbl1.grid(row=2,column=0,padx=7,pady=7)
e1=Entry(window,bg='white')
e1.grid(row=2,column=2)
lbl2=Label(window,text='NAME:',bg='grey',fg='black')
lbl2.grid(row=4,column=0,padx=7,pady=7)

e2=Entry(window,bg='white')
e2.grid(row=4,column=2)

lbl3=Label(window,text='EMAIL:',bg='grey',fg='black')
lbl3.grid(row=5,column=0,padx=7,pady=7)

e3=Entry(window,bg='white')
e3.grid(row=5,column=2)
lbl4=Label(window,text='GENDER:',bg='grey',fg='black')
lbl4.grid(row=7,column=0)
selected=StringVar()
rad1=Radiobutton(window,text="MALE",value='MALE',var=selected)
rad1.grid(row=7,column=2,padx=7,pady=7)
rad1.place(x=260,y=144)
rad2=Radiobutton(window,text='FEMALE',value='FEMALE',var=selected)
rad2.grid(row=7,column=3,padx=7,pady=7)
rad2.place(x=338,y=144)
lbl5=Label(window,text='AGE:',bg='grey',fg='black')
lbl5.grid(row=8,column=0,padx=7,pady=7)

e5=Entry(window,bg='white')
e5.grid(row=8,column=2)
lbl6=Label(window,text='QUALIFICATION:',bg='grey',fg='black')
lbl6.grid(row=9,column=0,padx=7,pady=7)

e6=Entry(window,bg='white')
e6.grid(row=9,column=2)
lbl7=Label(window,text='DEPARTMENT:',bg='grey',fg='black')
lbl7.grid(row=10,column=0,padx=7,pady=7)


e7=Entry(window,bg='white')
e7.grid(row=10,column=2)

lbl8=Label(window,text='ROLE:',bg='grey',fg='black')
lbl8.grid(row=11,column=0,padx=7,pady=7)

e8=Entry(window,bg='white')
e8.grid(row=11,column=2)
lbl9=Label(window,text='PHONE NUMBER:',bg='grey',fg='black')
lbl9.grid(row=12,column=0,padx=7,pady=7)

e9=Entry(window,bg='white')
e9.grid(row=12,column=2)
def id_value(event=None):

        
                x=e1.get()
                e1.focus()
                c=r'^[0-9]+$'
                if re.search(c,x):
                        
                
                        e2.focus()

                else:
                        messagebox.showerror('ERROR','Invalid ID')
                        e1.delete(0,END)
                        e1.focus()

def namevalue(event=None):

        
                x=e2.get()
                e2.focus()
                a=r'^[a-zA-Z\s]+$'
                if re.search(a,x):
                        
                
                        e3.focus()

                else:
                        messagebox.showerror('ERROR','Invalid name')
                        e2.delete(0,END)
                        e2.focus()
def emailvalue(event=None):                       
                x2=e3.get()
                b=r'@gmail.com$'
                if re.search(b,x2):
                     e5.focus()
                else:
                        messagebox.showerror('ERROR','Invalid Email')
                        e3.delete(0,END)
                        e3.focus()
def age_value(event=None):

        
                x=e5.get()
                e5.focus()
                c=r'^[0-9]{2}+$'
                if re.search(c,x):
                        
                
                        e6.focus()

                else:
                        messagebox.showerror('ERROR','Invalid Age')
                        e5.delete(0,END)
                        e5.focus()


def mobilevalue(event=None):
                x3=e9.get()
                c=r'^[0-9]{10}+$'
                if re.search(c,x3):
                        e9.focus()
                else:
                        messagebox.showerror('ERROR','invalid mobile number')
                        e9.delete(0,END)
                        e9.focus()
def qualificationvalue(event=None):

        
                x=e6.get()
                e6.focus()
                a=r'^[a-zA-Z\s._]+$'
                if re.search(a,x):
                        
                
                        e7.focus()

                else:
                        messagebox.showerror('ERROR','Invalid Qualification name')
                        e6.delete(0,END)
                        e6.focus()
def departmentvalue(event=None):
                x4=e7.get()
                a=r'^[a-zA-Z\s._]+$'
                if re.search(a,x4):
                        e8.focus()
                else:
                        messagebox.showerror('ERROR','invalid department Name')
                        e7.delete(0,END)
                        e7.focus()
def rolevalue(event=None):

        
                x=e8.get()
                e8.focus()
                a=r'^[a-zA-Z\s_]+$'
                if re.search(a,x):
                        
                
                        e9.focus()

                else:
                        messagebox.showerror('ERROR','Invalid Role')
                        e8.delete(0,END)
                        e8.focus()
           
e1.bind('<Return>',id_value)
e2.bind('<Return>',namevalue)
e3.bind('<Return>',emailvalue)
e6.bind('<Return>',qualificationvalue)
e5.bind('<Return>',age_value)
e7.bind('<Return>',departmentvalue)
e8.bind('<Return>',rolevalue)
e9.bind('<Return>',mobilevalue)


#crsr.execute("create table employee(id integer,name text,email text,gender text,age integer,qualification text,department text,role text,phone_number bigint)")
#print("table created...")
#crsr.execute('drop table employee')

def add_register():
    
    id=e1.get()
    name=e2.get()
    gender=selected.get()
    email=e3.get()
    age=e5.get()
    qualification=e6.get()
    department=e7.get()
    role=e8.get()
    phone_number=e9.get()

    if id!="" and name!="" and gender!=""and email!="" and age!="" and qualification!="" and department!="" and role!="" and phone_number!="":
        crsr.execute("insert into employee(id,name,email,gender,age,qualification,department,role,phone_number)values(?,?,?,?,?,?,?,?,?)",(id,name,email,gender,age,qualification,department,role,phone_number))
        mydb.commit()
   
        messagebox.showinfo('INFO','Registration successfully ') 
    else:
        messagebox.showwarning('WARNING','please Fullfill requiered field')
    
btn=Button(window,text='Register',bg='green',fg='white',command=add_register)
btn.grid(row=13,column=1,padx=7,pady=7)
lbl10=Label(window,text='Enter ID:',bg='grey',fg='black')
lbl10.grid(row=2,column=3,padx=7,pady=7)

e10=Entry(window,bg='white')
e10.grid(row=2,column=4)


t1=scrolledtext.ScrolledText(window,width=38,height=20)
t1.grid(row=0,column=0)
t1.place(x=426,y=70)
def view_register():
    t1.delete(1.0,END)
    try:    
        x=e10.get()
        crsr.execute('select *from employee where id=?',(x,))
        x1=crsr.fetchone()
        for i in range(len(x1)):
            if i==0:
                t1.insert(END,('ID:',  x1[i]))
                t1.insert(END,'\n')
            # ll1.insert(END,x1[i])
            elif i==1:
                t1.insert(END,('NAME:',        x1[i]))
                t1.insert(END,'\n')
            elif i==2:
                t1.insert(END,('EMAIL:',        x1[i]))
                t1.insert(END,'\n')
            elif i==3:
                t1.insert(END,('GENDER:',      x1[i]))
                t1.insert(END,'\n')
            elif i==4:
                t1.insert(END,('AGE:',      x1[i]))  
                t1.insert(END,'\n')          
            elif i==5:
                t1.insert(END,('QUALIFICATION:',       x1[i]))
                t1.insert(END,'\n')
            elif i==6:
                t1.insert(END,('DEPARTMENT:',      x1[i]))
                t1.insert(END,'\n')
            elif i==7:
                t1.insert(END,('ROLE:',        x1[i]))
                t1.insert(END,'\n')
            elif i==8:
                t1.insert(END,('PHONE_NUMBER:',        x1[i]))
                t1.insert(END,'\n')
            e10.delete(0,END)     
    except:
            messagebox.showwarning('Warning','id not found')
            e10.delete(0,END)
    

btn=Button(window,text='View',bg='blue',fg='white',command=view_register)
btn.grid(row=2,column=5,padx=7,pady=7)
lbl12=Label(window,text='Enter ID:',bg='grey',fg='black')
lbl12.grid(row=16,column=0,padx=7,pady=7)
def search():
    try:    
        x=e12.get()
        crsr.execute('select *from employee where id=?',(x,))
        x1=crsr.fetchone()
        for i in range(len(x1)):
            if i==0:
                e1.insert(END,(x1[i]))
            # ll1.insert(END,x1[i])
            elif i==1:
                e2.insert(END,(x1[i]))
            elif i==2:
                e3.insert(END,(x1[i]))
            elif i==3:
                selected.set(x1[i])
            elif i==4:
                e5.insert(END,(x1[i]))            
            elif i==5:
                e6.insert(END,(x1[i]))
            elif i==6:
                e7.insert(END,(x1[i]))
            elif i==7:
                e8.insert(END,(x1[i]))
            elif i==8:
                e9.insert(END,(x1[i])) 
        
    except:
            messagebox.showwarning('Warning',' id not found')


e12=Entry(window,bg='white')
e12.grid(row=16,column=1)

btn3=Button(window,text='search',bg='blue',fg='white',command=search)
btn3.grid(row=16,column=2,padx=7,pady=7)
btn3.place(x=255,y=385)
def add_update():
    id=e1.get()
    name=e2.get()
    email=e3.get()
    gender=selected.get()
    age=e5.get()
    qualification=e6.get()
    department=e7.get()
    role=e8.get()
    phone_number=e9.get()
    if id!="":
        crsr.execute("update employee set name=?, email=? ,gender=? ,age=? ,qualification=?, department=? ,role=?, phone_number= ? where id= ? ",
        (name,email,gender,age,qualification,department,role,phone_number,id))

       
        mydb.commit()
        messagebox.showinfo('INFO','updated successfully')
        e12.delete(0,END)

    else:
                  messagebox.showwarning('WARNING','please search to select the contact')             
btn2=Button(window,text='update',bg='blue',fg='white',command=add_update)
btn2.grid(row=17,column=0,padx=7,pady=7)
def delete_emp():
    name=e2.get()
    id=e1.get()
    if id!="":
        crsr.execute("delete from employee where id=?",(id,))
        mydb.commit()
        messagebox.showinfo('INFO',f'The details of employee {name}  deleted successfully')
    else:
         messagebox.showwarning('WARNING','please search to select the contact')              

btn4=Button(window,text='delete',bg='red',fg='white',command=delete_emp)
btn4.grid(row=17,column=1,padx=7,pady=7)
def clear_emp():
     e1.delete(0,END)
     e2.delete(0,END)
     e3.delete(0,END)
     selected.set('')
     e5.delete(0,END)
     e6.delete(0,END)
     e7.delete(0,END)
     e8.delete(0,END)
     e9.delete(0,END)
     e12.delete(0,END)
     t1.delete(1.0,END)
btn5=Button(window,text='Clear All',bg='blue',fg='white',command=clear_emp)
btn5.grid(row=17,column=2,padx=7,pady=7)
def view_all():
    crsr.execute('select *from employee' )
    y=crsr.fetchall()
    t1.delete(1.0,END)
    for x1 in y:
        #  x1=crsr.fetchone()
        for i in range(len(x1)):
            if i==0:
                t1.insert(END,('ID:',  x1[i]))
                t1.insert(END,'\n')
            # ll1.insert(END,x1[i])
            elif i==1:
                t1.insert(END,('NAME:',        x1[i]))
                t1.insert(END,'\n')
            elif i==2:
                t1.insert(END,('EMAIL:',        x1[i]))
                t1.insert(END,'\n')
            elif i==3:
                t1.insert(END,('GENDER:',      x1[i]))
                t1.insert(END,'\n')
            elif i==4:
                t1.insert(END,('AGE:',      x1[i]))  
                t1.insert(END,'\n')          
            elif i==5:
                t1.insert(END,('QUALIFICATION:',       x1[i]))
                t1.insert(END,'\n')
            elif i==6:
                t1.insert(END,('DEPARTMENT:',      x1[i]))
                t1.insert(END,'\n')
            elif i==7:
                t1.insert(END,('ROLE:',        x1[i]))
                t1.insert(END,'\n')
            elif i==8:
                t1.insert(END,('PHONE_NUMBER:',        x1[i]))
                t1.insert(END,'\n')
                t1.insert(END,'-------------------------------------')
                t1.insert(END,'\n')
            e10.delete(0,END)

           
btn=Button(window,text='View All',bg='blue',fg='white',command=view_all)
btn.grid(row=2,column=6,padx=7,pady=7)
btn8=Button(window,text='Exit',bg='blue',fg='white',command=window.quit)
btn8.grid(row=17,column=3)
btn8.place(x=555,y=425)
window.mainloop()