from ast import Return
import email
from sre_parse import State
import ssl
from tabnanny import check
from tkinter import *
from tkinter import ttk
from tkinter.tix import Select
from turtle import left
from PIL import Image,ImageTk
from tkinter import messagebox
from django.http import QueryDict
import mysql.connector



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\\Users\\kity\Desktop\\Restaurant Management System\\Images\\Tatang_Filipino_Food.0.jpg")
        bg=Label(self.root,image=self.bg)
        bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file=r"C:\\Users\\kity\\hotel management system\hotel\image\354888596.jpg")
        left__lbl=Label(self.root,image=self.bg1)
        left__lbl.place(x=200,y=150,width=470,height=400)
#############################################variables#########################################
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        frame=Frame(self.root,bg="white")
        frame.place(x=670,y=150,width=470,height=400)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)


        fname=Label(frame,text="First Name",font=("times new roman",10,"bold"),bg="white")
        fname.place(x=90,y=70)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",10,"bold"))
        self.fname_entry.place(x=50,y=100,width=150)
        

        l_name=Label(frame,text="Last Name",font=("times new roman",10,"bold"),bg="white",fg="black")
        l_name.place(x=320,y=70)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",10))
        self.txt_lname.place(x=280,y=100,width=150)

        contact=Label(frame,text="Contact No",font=("times new roman",10,"bold"),bg="white",fg="black")
        contact.place(x=90,y=130)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",10))
        self.txt_contact.place(x=50,y=150,width=150)

        email=Label(frame,text="Email",font=("times new roman",10,"bold"),bg="white",fg="black") 
        email.place(x=330,y=130)  

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",10))
        self.txt_email.place(x=280,y=150,width=150)

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",10,"bold"),bg="white",fg="black") 
        security_Q.place(x=50,y=180)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Times new roman",10,"bold"),state="readonly")  
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=200,width=150)
        self.combo_security_Q.current(0)     
        

        security_A=Label(frame,text="Security Answer",font=("Times new roman",10,"bold"),bg="white",fg="black")
        security_A.place(x=300,y=180)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("Times new roman",10))
        self.txt_security.place(x=280,y=200,width=150)

        pswd=Label(frame,text="Password",font=("Times new roman",10,"bold"),bg="white",fg="black")
        pswd.place(x=90,y=230)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",10))
        self.txt_pswd.place(x=50,y=250,width=150)

        confirm_pswd=Label(frame,text="Confirm Password",font=("Times new roman",10,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=290,y=230)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",10))
        self.txt_confirm_pswd.place(x=280,y=250,width=150)
        
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Forms & Condition",font=("Times new roman",10,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=270)

        img=Image.open(r"C:\Users\kity\Desktop\Restaurant Management System\Images\login logo\Register.jpg")
        img=img.resize((100,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register__data,borderwidth=0,cursor="hand2")
        b1.place(x=20,y=300,width=200)

        img1=Image.open(r"C:\Users\kity\Desktop\Restaurant Management System\Images\login.jpg")
        img1=img1.resize((100,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b2.place(x=260,y=300,width=200)

# ######################################function declaration#########################################
    
    def register__data(self):
        if self.var_fname.get()=="" or self.var_email.get=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fileds are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be the same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Csu1234!",database="geeksforgeeks")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            Row=my_cursor.fetchone()
            if Row!=None:
                messagebox("Error","User already exist,please anothert email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(                                                                                     
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get(),                                                                   
                                                                                                                                                              
                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","register successfully")
 
    



if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()





 

        