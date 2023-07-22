import tkinter
from tkinter import PhotoImage
from tkinter import StringVar
from tkinter import OptionMenu
from tkinter import Text
from tkinter import Entry
from tkinter import ttk

import mysql.connector
import random
import csv
database=mysql.connector.connect(host="localhost",user="root",charset="utf8",password="1234",database="QUESTIONNAIRE")

def login():
    def login_check():
        a=username_textbox.get("1.0","end-1c")
        b=password_textbox.get("1.0","end-1c")        
        cursor_object=database.cursor()
        query_1 ="select * from teacher_table"
        cursor_object.execute(query_1)
        m=cursor_object.fetchall()
        for i in m:            
            if i[1]==a and i[2]==int(b):
                menu()
                break
        else:
            l_2=tkinter.Label(login_menu,text="INVALID USERNAME OR PASSWORD",font=("times new roman",10),fg="red").place(x=80,y=250)
    login_menu=tkinter.Tk()
    login_menu.geometry("400x400")
    login_menu.title("QUESTIONNAIRE")
    global img
    img=PhotoImage(file='APP PHOTO.PNG')
    background=tkinter.Label(login_menu,font=("times new roman",50),image=img)
    background.place(x=0,y=0)
    l_1=tkinter.Label(login_menu,text="WELCOME TO QUESTIONNAIRE",font=("times new roman",20),fg="black",bg="yellow").pack()
    username_label=tkinter.Label(login_menu,text="USERNAME",font=("times new roman",15),fg="black",bg="yellow").place(x=0,y=65)
    password_label=tkinter.Label(login_menu,text="PASSWORD",font=("times new roman",15),fg="black",bg="yellow").place(x=0,y=115)
    username_textbox=Text(login_menu,width=15,height=1.3)
    username_textbox.place(x=125,y=70)
    password_textbox=Text(login_menu,width=15,height=1.3)
    password_textbox.place(x=125,y=120)
    login_button=tkinter.Button(login_menu,text="LOGIN",font=("times new roman",12),fg="black",bg="pink",command=login_check).place(x=0,y=180)
    create_account_button=tkinter.Button(login_menu,text="CREATE ACCOUNT",font=("times new roman",12),fg="black",bg="pink",command=create_account).place(x=80,y=180)
def menu():
    menu=tkinter.Toplevel()
    menu.geometry("400x400")
    menu.title("QUESTIONNAIRE")
    global img1
    img1=PhotoImage(file='APP PHOTO1.PNG')
    background=tkinter.Label(menu,font=("times new roman",50),image=img)
    background.place(x=0,y=0)
    add_question_button=tkinter.Button(menu,text="ADD QUESTION",font=("times new roman",20),fg="black",bg="pink",command=add_question_fun).place(x=90,y=30)
    delete_question_button=tkinter.Button(menu,text="DELETE QUESTION",font=("times new roman",20),fg="black",bg="pink",command=delete_question).place(x=70,y=120)
    view_question_bank_button=tkinter.Button(menu,text="VIEW QUESTION BANK",font=("times new roman",20),fg="black",bg="pink",command=question_viewing).place(x=45,y=200)
    create_question_button=tkinter.Button(menu,text="CREATE QUESTION PAPER",font=("times new roman",20),fg="black",bg="pink",command=create_question_paper_fun).place(x=25,y=280)
    
def create_account():
    def creation():
         j=username_textbox.get("1.0","end-1c")
         k=password_textbox.get("1.0","end-1c")
         cursor_object=database.cursor()
         query_2 ="select * from teacher_table"
         cursor_object.execute(query_2)
         m=cursor_object.fetchall()
        
         n=0
         for x in m:
             r=x[0]
             if x[1]==j:                
                 l_3=tkinter.Label(create_account_window,text="USERNAME ALREADY EXISTS PLEASE SELECT \n ANOTHER USERNAME",font=("times new roman",10),fg="red")
                 l_3.place(x=50,y=220)
                 n=1
         if n!=1:
            cursor_object.execute("insert into teacher_table values(%s,%s,%s)",(r+1,j,k))
            database.commit()
            l7=tkinter.Label(create_account_window,text="YOUR ACCOUNT HAS BEEN CREATED",font=("times new roman",10),fg="green").place(x=70,y=280)
            go_back_button=tkinter.Button(create_account_window,text="GO BACK",font=("times new roman",12),fg="black",bg="pink",command=create_account_window.destroy).place(x=140,y=330)
           
         
    create_account_window=tkinter.Toplevel()
    create_account_window.geometry("400x400")
    create_account_window.title("QUESTIONNAIRE")
    global img2
    img2=PhotoImage(file='APP PHOTO2.PNG')
    background=tkinter.Label(create_account_window,font=("times new roman",50),image=img2)
    background.place(x=0,y=0)
    l_3=tkinter.Label(create_account_window,text="CREATE ACCOUNT",font=("times new roman",20),fg="black",bg="yellow").pack()
    username_label=tkinter.Label(create_account_window,text="CREATE USERNAME",font=("times new roman",15),fg="black",bg="yellow").place(x=0,y=65)
    password_label=tkinter.Label(create_account_window,text="CREATE PASSWORD",font=("times new roman",15),fg="black",bg="yellow").place(x=0,y=115)
    username_textbox=Text(create_account_window,width=15,height=1.3)
    username_textbox.place(x=210,y=70)
    password_textbox=Text(create_account_window,width=15,height=1.3)
    password_textbox.place(x=210,y=120)
    create_account_button=tkinter.Button(create_account_window,text="CREATE ACCOUNT",font=("times new roman",12),fg="black",bg="pink",command=creation).place(x=0,y=180)
def add_question_fun():
    def question_addition():
        q=question_textbox.get("1.0","end-1c")
        a=option_a_textbox.get("1.0","end-1c")
        b=option_b_textbox.get("1.0","end-1c")
        c=option_c_textbox.get("1.0","end-1c")
        d=option_d_textbox.get("1.0","end-1c")
        e=subject_var.get()
        f=correct_option_var.get()
        print(e)
        if e=='MATHEMATICS':
            cursor_object=database.cursor()
            query_2 ="select * from question_table_mathamatics"
            cursor_object.execute(query_2)
            m=cursor_object.fetchall()
            for i in m:
                x=i[0]
            cursor_object.execute("insert into question_table_mathamatics values(%s,%s,%s,%s,%s,%s,%s)",(x+1,q,"A."+a,"B."+b,"C."+c,"D."+d,f))
            database.commit()
            l_9=tkinter.Label(add_question_window,text="YOUR QUESTION HAS BEEN ADDED",font=("times new roman",15),fg="green").place(x=120,y=420)
            c=tkinter.Button(add_question_window,text="EXIT",font=("times new roman",12),fg="black",bg="pink",command=add_question_window.destroy).place(x=0,y=460)        
    add_question_window=tkinter.Toplevel()
    add_question_window.geometry("500x500")
    add_question_window.title("QUESTIONNAIRE")
    global img3
    img3=PhotoImage(file='APP PHOTO3.PNG')
    background=tkinter.Label(add_question_window,font=("times new roman",50),image=img3)
    background.place(x=0,y=0)
    l_8=tkinter.Label(add_question_window,text="ADD QUESTION",font=("times new roman",20),fg="black",bg="yellow")
    l_8.place(x=140,y=0)
    subject_label=tkinter.Label(add_question_window,text="SELECT SUBJECT",font=("times new roman",15),fg="black",bg="yellow")
    subject_label.place(x=0,y=60)
    subject_var=StringVar()
    subject_var.set("       ")
    subject_menu=OptionMenu(add_question_window,subject_var,"MATHEMATICS","PHYSICS","CHEMISTRY")
    subject_menu.place(x=190,y=60)
    question_lable=tkinter.Label(add_question_window,text="ENTER QUESTION",font=("times new roman",15),fg="black",bg="yellow").place(x=0,y=100)
    question_textbox=Text(add_question_window,width=35,height=7)
    question_textbox.place(x=190,y=100)
    option_a_label=tkinter.Label(add_question_window,text="OPTION A",font=("times new roman",15),fg="black",bg="yellow")
    option_a_label.place(x=0,y=230)
    option_b_label=tkinter.Label(add_question_window,text="OPTION B",font=("times new roman",15),fg="black",bg="yellow")
    option_b_label.place(x=0,y=260)
    option_c_label=tkinter.Label(add_question_window,text="OPTION C",font=("times new roman",15),fg="black",bg="yellow")
    option_c_label.place(x=0,y=290)
    option_d_label=tkinter.Label(add_question_window,text="OPTION D",font=("times new roman",15),fg="black",bg="yellow")
    option_d_label.place(x=0,y=320)
    correct_option_label=tkinter.Label(add_question_window,text="CORRECT OPTION",font=("times new roman",15),fg="black",bg="yellow").place(x=0,y=350)
    correct_option_var=StringVar()
    correct_option_var.set("       ")
    correct_option_menu=OptionMenu(add_question_window,correct_option_var,"A","B","C","D")
    correct_option_menu.place(x=190,y=350)
    option_a_textbox=Text(add_question_window,width=15,height=1.3)
    option_b_textbox=Text(add_question_window,width=15,height=1.3)
    option_c_textbox=Text(add_question_window,width=15,height=1.3)
    option_d_textbox=Text(add_question_window,width=15,height=1.3)
    option_a_textbox.place(x=190,y=230)
    option_b_textbox.place(x=190,y=260)
    option_c_textbox.place(x=190,y=290)
    option_d_textbox.place(x=190,y=320)
    submit_button=tkinter.Button(add_question_window,text="SUBMIT",font=("times new roman",12),fg="black",bg="pink",command=question_addition).place(x=0,y=400)
def delete_question():
    def delition():
        a=question_id_textbox.get("1.0","end-1c")
        b=subject_var.get()
        cursor_object=database.cursor()
        
        if b=='MATHEMATICS':
            cursor_object.execute("delete from question_table_mathamatics where question_id=%s",(int(a),))
            database.commit()
            l_10=tkinter.Label(delete_question_window,text="THE QUESTION HAS BEEN DELETED",font=("times new roman",15),fg="green").place(x=40,y=200)
            go_back_2=tkinter.Button(delete_question_window,text="GO BACK",font=("times new roman",12),fg="black",bg="pink",command=delete_question_window.destroy).place(x=10,y=250)        
    delete_question_window=tkinter.Toplevel()
    delete_question_window.geometry("400x400")
    delete_question_window.title("QUESTIONNAIRE")
    global img4
    img4=PhotoImage(file='APP PHOTO4.PNG')
    background=tkinter.Label(delete_question_window,font=("times new roman",50),image=img4)
    background.place(x=0,y=0)
    l_9=tkinter.Label(delete_question_window,text="DELETE QUESTION",font=("times new roman",20),fg="black",bg="yellow").place(x=70,y=0)
    subject_label=tkinter.Label(delete_question_window,text="SELECT SUBJECT",font=("times new roman",15),fg="black",bg="yellow")
    subject_label.place(x=0,y=60)
    subject_var=StringVar()
    subject_var.set("       ")
    subject_menu=OptionMenu(delete_question_window,subject_var,"MATHEMATICS","PHYSICS","CHEMISTRY")
    subject_menu.place(x=210,y=60)
    question_id_label=tkinter.Label(delete_question_window,text="ENTER QUESTION ID",font=("times new roman",15),fg="black",bg="yellow").place(x=0,y=100)
    question_id_textbox=Text(delete_question_window,width=4,height=1.3)
    question_id_textbox.place(x=210,y=100)
    delete_button=tkinter.Button(delete_question_window,text="DELETE",font=("times new roman",12),fg="black",bg="pink",command=delition).place(x=10,y=150)
def create_question_paper_fun():
    def create():
         
         a=exam_name_textbox.get("1.0","end-1c")
         b=subject_var.get()
         c=total_question_textbox.get("1.0","end-1c")
         cursor_object=database.cursor()
         if b=='MATHEMATICS':
          query_2 ="select * from question_table_mathamatics"
          cursor_object.execute(query_2)
          m=cursor_object.fetchall()
          k=random.sample(range(1,5),int(c))
          a1=a+".txt"
          a2=a+"solution.csv"
          g=open(a2,'w')
          wr=csv.writer(g)
          q=a+" solution"
          wr.writerow([q])
          wr.writerow(["question_ID","solution"])
          f=open(a1,'w')
          f.write(a.upper()+"\n\n\n")
          for x in k:
              for i in m:
                  if i[0]==x:
                      v=["question_ID: "+str(i[0])+"\n",i[1]+"\n",i[2]+"\n",i[3]+"\n",i[4]+"\n",i[5]+"\n","\n\n"]
                      f.writelines(v)
                      wr.writerow([str(i[0]),i[6]])
                     
          f.close()            
          g.close()
         create_window=tkinter.Toplevel()
         create_window.geometry("400x400")
         create_window.title("QUESTIONNAIRE")
         create_window.configure(bg='light blue')
         global img7
         img7=PhotoImage(file='APP PHOTO7.PNG')
         background=tkinter.Label(create_question_paper_window,font=("times new roman",50),image=img5)
         background.place(x=0,y=0)
         l_11=tkinter.Label(create_window,text="YOUR QUESTION PAPER AND SOLUTION",font=("times new roman",15),fg="black",bg="light blue").place(x=0,y=0)
         l_14=tkinter.Label(create_window,text="SHEET HAVE BEEN DOWLOADED TO YOUR DEVICE",font=("times new roman",15),fg="black",bg="light blue").place(x=0,y=20)
         l_15=tkinter.Label(create_window,text="YOUR DEVICE",font=("times new roman",15),fg="black",bg="light blue").place(x=0,y=40)
         l_12=tkinter.Label(create_window,text="QUESTION PAPER: "+a1,font=("times new roman",15),fg="black",bg="light blue").place(x=0,y=80)
         l_12=tkinter.Label(create_window,text="SOLUTION SHEET: "+a2,font=("times new roman",15),fg="black",bg="light blue").place(x=0,y=120)
         exit_button=tkinter.Button(create_window,text="EXIT",font=("times new roman",12),fg="black",bg="pink",command=create_window.destroy).place(x=10,y=170)
    create_question_paper_window=tkinter.Toplevel()
    create_question_paper_window.geometry("400x400")
    create_question_paper_window.title("QUESTIONNAIRE")
    global img5
    img5=PhotoImage(file='APP PHOTO5.PNG')
    background=tkinter.Label(create_question_paper_window,font=("times new roman",50),image=img5)
    background.place(x=0,y=0)
    l_10=tkinter.Label(create_question_paper_window,text="CREATE QUESTION PAPER",font=("times new roman",20),fg="black",bg="yellow").place(x=25,y=0)
    subject_label=tkinter.Label(create_question_paper_window,text="SELECT SUBJECT",font=("times new roman",15),fg="black",bg="yellow")
    subject_label.place(x=0,y=60)
    subject_var=StringVar()
    subject_var.set("       ")
    subject_menu=OptionMenu(create_question_paper_window,subject_var,"MATHEMATICS","PHYSICS","CHEMISTRY")
    subject_menu.place(x=210,y=60)
    exam_name_label=tkinter.Label(create_question_paper_window,text="EXAM NAME",font=("times new roman",15),fg="black",bg="yellow").place(x=0,y=100)
    exam_name_textbox=Text(create_question_paper_window,width=23,height=1.3)
    exam_name_textbox.place(x=210,y=100)
    total_question_label=tkinter.Label(create_question_paper_window,text="TOTAL QUESTIONS",font=("times new roman",15),fg="black",bg="yellow").place(x=0,y=140)
    total_question_textbox=Text(create_question_paper_window,width=4,height=1.3)
    total_question_textbox.place(x=210,y=140)
    create_question_button=tkinter.Button(create_question_paper_window,text="CREATE QUESTION PAPER",font=("times new roman",12),fg="black",bg="pink",command=create).place(x=10,y=190)
def question_viewing():
         def viewing():
             a=subject_var.get()
             viewing_window=tkinter.Toplevel()
             viewing_window.geometry("800x800")
             viewing_window.title("QUESTIONNAIRE")
             trv=ttk.Treeview(viewing_window)
             #trv.grid(row=1,column=1,padx=20,pady=20)
             trv['columns']=("1","2","3","4","5","6","7")
             trv.pack()
             trv['show']='headings'
             z=ttk.Style(viewing_window)
             z.theme_use("clam")
             trv.column("1", width = 100, anchor ='c')
             trv.column("2", width = 500, anchor ='c')
             trv.column("3", width = 100, anchor ='c')
             trv.column("4", width = 100, anchor ='c')
             trv.column("5", width = 100, anchor ='c')
             trv.column("6", width = 100, anchor ='c')
             trv.column("7", width = 100, anchor ='c')
             
             trv.heading("1", text ="QUESTION_ID")
             trv.heading("2", text ="QUESTION")
             trv.heading("3", text ="OPTION A")
             trv.heading("4", text ="OPTION B")
             trv.heading("5", text ="OPTION C")
             trv.heading("6", text ="OPTION D")
             trv.heading("7", text ="CORRECT OPTION")
             cursor_object=database.cursor()
             if a=='MATHEMATICS':
                 query_4 ="select * from question_table_mathamatics"
                 cursor_object.execute(query_4)
                 m=cursor_object.fetchall()
                 i=0
                 for t in m:
                     trv.insert("",i,values=(t[0],t[1],t[2],t[3],t[4],t[5],t[6]))
                     i=i+1
              
         question_viewing_window=tkinter.Toplevel()
         question_viewing_window.geometry("400x400")
         question_viewing_window.title("QUESTIONNAIRE")         
         global img7
         img7=PhotoImage(file='APP PHOTO7.PNG')
         background=tkinter.Label(question_viewing_window,font=("times new roman",50),image=img7)
         background.place(x=0,y=0)
         l_12=tkinter.Label(question_viewing_window,text="QUESTION BANK",font=("times new roman",20),fg="black",bg="yellow").place(x=80,y=0)
         subject_label=tkinter.Label(question_viewing_window,text="SELECT SUBJECT",font=("times new roman",15),fg="black",bg="yellow")
         subject_label.place(x=0,y=60)
         subject_var=StringVar()
         subject_var.set("       ")
         subject_menu=OptionMenu(question_viewing_window,subject_var,"MATHEMATICS","PHYSICS","CHEMISTRY")
         subject_menu.place(x=210,y=60)
         view_question_bank_button=tkinter.Button(question_viewing_window,text="VIEW QUESTION BANK",font=("times new roman",12),fg="black",bg="pink",command=viewing).place(x=110,y=150)
    
     
    
    
#__MAIN__

login()
















