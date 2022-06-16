
from cProfile import label
import random as rand 
from tkinter import *
from turtle import bgcolor, width
from PIL import Image,ImageTk
from mysqlx import Row
from pip import main
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Cus_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+0+0")
#====================================Variable====================================
        self.var_ref=StringVar()
        x=rand.randint(1000,9999)
        self.var_ref.set(str(x))       

        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


        lbl_title=Label(self.root,text="Add Customer Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        img2=Image.open(r"C:\Users\kity\hotel management system\hotel\image\golden-hotel-logo-free-graphics-free-vector-thumb.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)
        #==================================custref==============
        lbl_cus_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cus_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("arial",13,"bold"),width=29,state="readonly")
        enty_ref.grid(row=0,column=1)
       #========================custname=============
        cname=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)
#========================mothername==============
        lblmname=Label(labelframeleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)
#======================gender combobox        
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        
        
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
#c==========================postcode==================

        lblPostCode=Label(labelframeleft,font=("arial",12,"bold"),text="PostCode",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)     
        txtPostCode.grid(row=4,column=1)

#========================mobilenumber==================
        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)     
        txtMobile.grid(row=5,column=1)
#=======================Email==================
        lblEmail=Label(labelframeleft,font=("arial",12,"bold"),text="Email",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)     
        txtEmail.grid(row=6,column=1)
#=============================nationality==========
        
        lblNationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Filipino","American","Korean","Chinese","Other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)
#=========================idproof==============
        lblidproof=Label(labelframeleft,font=("arial",12,"bold"),text="ID Proof Type",padx=2,pady=6)
        lblidproof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Passport","Vaccination Card","Drivers Licence","Student Id","Voters Id","TIN ID","Other")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
#=========================Id number===============
        lblIdnumber=Label(labelframeleft,font=("arial",12,"bold"),text="ID Number",padx=2,pady=6)
        lblIdnumber.grid(row=9,column=0,sticky=W)
        txtIDnumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)     
        txtIDnumber.grid(row=9,column=1)
#=====================address=========
        
        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)     
        txtAddress.grid(row=10,column=1)
        

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,command=self.update,text="Update",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_Delete=Button(btn_frame,command=self.nDELETE,text="Delete",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_Delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,command=self.reset,text="Reset",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_reset.grid(row=0,column=3,padx=1)

        
#=============================tabelandsearch================
        table_frameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"))
        table_frameleft.place(x=435,y=50,width=860,height=490)

        lblSearchby=Label(table_frameleft,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchby.grid(row=0,column=0,sticky=W)
        
        self.serch_var=StringVar()
        combo_search=ttk.Combobox(table_frameleft,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_frameleft,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)     
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(table_frameleft,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btn_showall=Button(table_frameleft,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_showall.grid(row=0,column=4,padx=1)
        
        #============================show data table===================

        details_table=Frame(table_frameleft,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile",
                                             "email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Post")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()==""or self.var_mother.get()=="":  
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
                try:
                       conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
                       my_cursor=conn.cursor()
                       my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_ref.get(),
                                                                                                self.var_cust_name.get(),             
                                                                                                self.var_mother.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_id_proof.get(),
                                                                                                self.var_id_number.get(),
                                                                                                self.var_address.get()         
                                                                                         ))
                       conn.commit()
                       self.fetch_data()
                       conn.close()
                       messagebox.showinfo("Success","Customer has been added",parent=self.root)
                except Exception as es:
                       messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)           
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from customer") 
        rows=my_cursor.fetchall()
        if len(rows)!=0:
             self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
             for i in rows:
                 self.Cust_Details_Table.insert("",END,values=i)
             conn.commit()
        conn.close()

    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:                   
            conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(                                                                                                   
                                                                                                                                                                        self.var_cust_name.get(),             
                                                                                                                                                                        self.var_mother.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_post.get(),
                                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_ref.get()   
                                                                                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)
    def nDELETE(self):
           nDELETE=messagebox.askyesno("Hotel System","Do you want to delete this customer",parent=self.root)
           if nDELETE>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
               my_cursor=conn.cursor()
               query="delete from customer where Ref=%s"
               value=(self.var_ref.get(),)
               my_cursor.execute(query,value)
           else:
               if not nDELETE:
                       return
           conn.commit()
           self.fetch_data()
           conn.close()
    def reset(self):
           #self.var_ref.set(""),
           self.var_cust_name.set(""),
           self.var_mother.set(""),
           #self.var_gender.set(""),
           self.var_post.set(""),
           self.var_mobile.set(""),
           self.var_email.set(""),
           #self.var_nationality.set(""),
           #self.var_id_proof.set(""),
           self.var_id_number.set(""),
           self.var_address.set("") 
 
           
           x=rand.randint(1000,9999)
           self.var_ref.set(str(x))
    def search(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
           my_cursor=conn.cursor()

           my_cursor.execute("Select * from customer where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
           rows=my_cursor.fetchall()
           if len (rows)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
           conn.close()
             
                
if __name__=="__main__":
    root=Tk()
    obj=Cus_win(root)
    root.mainloop()
