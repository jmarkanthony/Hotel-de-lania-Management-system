from ast import Return
from optparse import Values
from tkinter import*
from atexit import register
from cProfile import label
from cgitb import text
import imp
from logging import root
import re
from tkinter import RIDGE, Button, Entry, Frame, Label, StringVar, Toplevel, font, ttk
from tkinter.tix import Tk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql
from hot import HotelManagementSystem


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
     
        self.bg=ImageTk.PhotoImage(file=r"C:\\Users\\kity\Desktop\\Restaurant Management System\\Images\\loginimage.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=140,width=340,height=450)

        img1=Image.open(r"C:\\Users\\kity\Desktop\\Restaurant Management System\\Images\\user-login-icon-29.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=175,width=100,height=100)

        get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=125)
      #label

        username=lbl=Label(frame,text="User Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=120,y=180)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=205,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=120,y=245)

        self.txtpass=Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=280,width=270)
      
        img2=Image.open(r"C:\\Users\\kity\Desktop\\Restaurant Management System\\Images\\login logo\\copy.png")
        img2=img2.resize((20,20),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg2.place(x=600,y=323,width=20,height=20)

        img3=Image.open(r"C:\\Users\\kity\Desktop\\Restaurant Management System\\Images\\af6816ec67ec51da6b275a4aa08d236c-lock-circle-icon.png")
        img3=img3.resize((20,20),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=600,y=395,width=30,height=20)
     #loginbutton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=330,width=120,height=35)
    #registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.rigester_window, font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=5,y=390,width=160)
    #forgetpassword
        forgotbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=5,y=410,width=160) 

        viewbtn=Button(frame,text="View logins",command=self.view_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        viewbtn.place(x=170,y=390,width=160)     
    
    def rigester_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
      if self.txtuser.get()=="" or self.txtpass.get()=="":
          messagebox.showerror("error","all field required")
      elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
          messagebox.showinfo("Success","Welcome to Restaurant Management System")
      else:
         conn=mysql.connector.connect(host="localhost",user="root",password="Csu1234!",database="geeksforgeeks")
         my_cursor=conn.cursor()
         my_cursor.execute("Select * from register where email=%s and password=%s", (
                                                                                    self.txtuser.get(),   
                                                                                    self.txtpass.get()   
                                                                                    ))
         Row=my_cursor.fetchone()
         if Row!=None:
                    messagebox.showerror("Error","Invalid Username & password")
         else:
            open_main=messagebox.askyesno("YesNo","Access only admin")
            if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
            else:
                if not open_main:
                    return 
                    #reset password
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select th security question ",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the asnwer ",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the new password ",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Csu1234!",database="geeksforgeeks")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s and securityQ=%s and securityA=%s")
            vlue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,vlue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)
                self.root2.destroy()
                    #=======================forgot password
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
             conn=mysql.connector.connect(host="localhost",user="root",password="Csu1234!",database="geeksforgeeks")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s")
             value=(self.txtuser.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             #print(row)

             if row==None:
                messagebox.showerror("My Error","Please enter a valid user name")
             else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",12,"bold"),fg="red",bg="black")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",10,"bold"),bg="white",fg="black") 
                security_Q.place(x=50,y=80)
        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("Times new roman",10,"bold"),state="readonly")  
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)     
        

                security_A=Label(self.root2,text="Security Answer",font=("Times new roman",10,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("Times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("Times new roman",10,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("Times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)


    def view_window(self):
                self.root3=Toplevel()
                self.root3.title("View Logins")
                self.root3.geometry("600x600+610+170")    

                table_frameleft=LabelFrame(self.root3,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"))
                table_frameleft.place(x=5,y=10,width=500,height=500)

        
        
                scroll_x=ttk.Scrollbar(table_frameleft,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frameleft,orient=VERTICAL)

                self.room_Table=ttk.Treeview(table_frameleft,columns=("fname","lname","contact","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)        
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.room_Table.xview)
                scroll_y.config(command=self.room_Table.yview)

                self.room_Table.heading("fname",text="First Name")
                self.room_Table.heading("lname",text="Last Name")
                self.room_Table.heading("contact",text="Contact No")
                self.room_Table.heading("email",text="Email")
       

                self.room_Table["show"]="headings"
        
                self.room_Table.column("fname",width=50)
                self.room_Table.column("lname",width=50)
                self.room_Table.column("contact",width=50)   
                self.room_Table.column("email",width=50) 
                self.room_Table.pack(fill=BOTH,expand=1)
                self.fetch_data() 

                logoutbtn=Button(self.root3,text="Back",command=self.log_out,font=("times new roman",15,"bold"),fg="white",bg="green")
                logoutbtn.place(x=520,y=250)
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from register") 
        rows=my_cursor.fetchall()
        if len(rows)!=0:
             self.room_Table.delete(*self.room_Table.get_children())
             for i in rows:
                 self.room_Table.insert("",END,values=i)
             conn.commit()
        conn.close()
    def log_out(self):
        self.root3.destroy()
                
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\\Users\\kity\Desktop\\Restaurant Management System\\Images\\Tatang_Filipino_Food.0.jpg")
        bg=Label(self.root,image=self.bg)
        bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file=r"C:\\Users\\kity\\hotel management system\\hotel\\image\\354888596.jpg")
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
        b2=Button(frame,image=self.photoimage1,command=self.log_out1,borderwidth=0,cursor="hand2")
        b2.place(x=260,y=300,width=200)

# ######################################function declaration#########################################
    
    def log_out1(self):
        self.root.destroy()
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









    






if __name__== "__main__":
    main()
