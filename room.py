from multiprocessing import parent_process
from tkinter import *
import random as rand
from turtle import bgcolor, width
from PIL import Image,ImageTk
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
        
        #===========================variable==============
        self.var_conatact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        lbl_title=Label(self.root,text="Room Booking Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        img2=Image.open(r"C:\Users\kity\hotel management system\hotel\image\golden-hotel-logo-free-graphics-free-vector-thumb.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
       
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("arial",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)
#=====================================label and entry=============
        lbl_cus_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cus_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_conatact,font=("arial",13,"bold"),width=20)
        enty_contact.grid(row=0,column=1,sticky=W)
        #Featch data button
        btnFetchcData=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=10)
        btnFetchcData.place(x=340,y=4)
#=========================Check in date==================
        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_in Date",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_out Date",padx=2,pady=6)
        check_out.grid(row=2,column=0,sticky=W)
        txtcheck_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txtcheck_out.grid(row=2,column=1)

#==========================roomtype==============
        label_roomtype=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_roomtype.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
        my_cursor=conn.cursor()
        my_cursor.execute("Select roomtype from details") 
        ide=my_cursor.fetchall()
        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
#========================Available room=============
        lblRoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Available Room",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)     
        #txtRoomAvailable.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
        my_cursor=conn.cursor()
        my_cursor.execute("Select roomno from details") 
        rows=my_cursor.fetchall()

        combo_RoomAvailable=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomAvailable["value"]=rows
        combo_RoomAvailable.current(0)
        combo_RoomAvailable.grid(row=4,column=1)


  #meal      
        lblmeals=Label(labelframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblmeals.grid(row=5,column=0,sticky=W)
        
        txtmeal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=27,state="readonly")
        txtmeal["value"]=("Breakfast","Lunch","Dinner")
        txtmeal.current(0)
        txtmeal.grid(row=5,column=1)
#no of days
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="No of Days",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)     
        txtNoOfDays.grid(row=6,column=1)
#Paid Tax
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Paid Tax",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)     
        txtNoOfDays.grid(row=7,column=1)
#Sub Total
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)     
        txtNoOfDays.grid(row=8,column=1)
#total Cost
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)     
        txtIdNumber.grid(row=9,column=1)
#==============================================Bill buton
        btnBill=Button(labelframeleft,command=self.total,text="Bill",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

#bttns      
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_Delete=Button(btn_frame,text="Delete",command=self.nDELETE,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_Delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_reset.grid(row=0,column=3,padx=1)
        #==========================right side image===========

        img3=Image.open(r"C:\Users\kity\hotel management system\hotel\image\85fbc30af4836b834a1ed4af61dde6d6.webp")
        img3=img3.resize((550,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=550,height=300)
#=========================================table frame search================
        
        table_frameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"))
        table_frameleft.place(x=435,y=280,width=860,height=260)

        lblSearchby=Label(table_frameleft,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchby.grid(row=0,column=0,sticky=W)
        
        self.serch_var=StringVar()
        combo_search=ttk.Combobox(table_frameleft,textvariable=self.serch_var ,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_frameleft,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)     
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(table_frameleft,command=self.search,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btn_showall=Button(table_frameleft,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_showall.grid(row=0,column=4,padx=1)

          #============================show data table===================

        details_table=Frame(table_frameleft,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_Table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","Room","meal", "noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact",text="Contact")
        self.room_Table.heading("checkin",text="Check-in(d/m/Y)")
        self.room_Table.heading("checkout",text="Check-out(d/m/Y")
        self.room_Table.heading("roomtype",text="Room Type")
        self.room_Table.heading("Room",text="Room No")
        self.room_Table.heading("meal",text="Meal")
        self.room_Table.heading("noOfdays",text="NoOfDays")
       

        self.room_Table["show"]="headings"
        
        self.room_Table.column("contact",width=100)
        self.room_Table.column("checkin",width=100)
        self.room_Table.column("checkout",width=100)
        self.room_Table.column("roomtype",width=100)
        self.room_Table.column("Room",width=100)
        self.room_Table.column("meal",width=100)
        self.room_Table.column("noOfdays",width=100)     
        self.room_Table.pack(fill=BOTH,expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
#add data
    def add_data(self):
        if self.var_conatact.get()==""or self.var_checkin.get()=="":  
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
                try:
                       conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
                       my_cursor=conn.cursor()
                       my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_conatact.get(),
                                                                                                self.var_checkin.get(),             
                                                                                                self.var_checkout.get(),
                                                                                                self.var_roomtype.get(),
                                                                                                self.var_roomavailable.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_noofdays.get()       
                                                                                         ))
                       conn.commit()
                       self.fetch_data()
                       conn.close()
                       messagebox.showinfo("Success","Room Booked",parent=self.root)
                except Exception as es:
                       messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

     #fetch data                    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from room") 
        rows=my_cursor.fetchall()
        if len(rows)!=0:
             self.room_Table.delete(*self.room_Table.get_children())
             for i in rows:
                 self.room_Table.insert("",END,values=i)
             conn.commit()
        conn.close()
#getcuersor
    def get_cuersor(self,event=""):
        cusrsor_row=self.room_Table.focus()
        content=self.room_Table.item(cusrsor_row)
        row=content["values"]

        self.var_conatact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

   #update
    def update(self):
        if self.var_conatact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:                   
            conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,Room=%s,meal=%s,noOfdays=%s where contact=%s",(                                                                                                   
                                                                                                                                                                        self.var_checkin.get(),             
                                                                                                                                                                        self.var_checkout.get(),
                                                                                                                                                                        self.var_roomtype.get(),
                                                                                                                                                                        self.var_roomavailable.get(),
                                                                                                                                                                        self.var_meal.get(),
                                                                                                                                                                        self.var_noofdays.get(),
                                                                                                                                                                        self.var_conatact.get()
                                                                                                                                                                           
                                                                                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

 #delete
    def nDELETE(self):
           nDELETE=messagebox.askyesno("Hotel System","Do you want to delete this customer",parent=self.root)
           if nDELETE>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
               my_cursor=conn.cursor()
               query="delete from room where contact=%s"
               value=(self.var_conatact.get(),)
               my_cursor.execute(query,value)
           else:
               if not nDELETE:
                       return
           conn.commit()
           self.fetch_data()
           conn.close()  
    def reset(self):
           self.var_conatact.set("")
           self.var_checkin.set("")
           self.var_checkout.set("")
           self.var_roomtype.set("")
           self.var_roomavailable.set("")
           self.var_meal.set("")
           self.var_noofdays.set("")   
           self.var_paidtax.set("")
           self.var_actualtotal.set("")
           self.var_total.set("")
              
                   
             
    #=======================All data fetch====================    
    def fetch_contact(self):
        if self.var_conatact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_conatact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
              messagebox.showerror("Error","This number not Found",parent=self.root)
            else:
              conn.commit()
              conn.close()



              showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
              showDataframe.place(x=450,y=55,width=300,height=180)  
#name
              lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
              lblName.place(x=0,y=0)

              lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl2.place(x=90,y=0)
#gender         
              conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
              my_cursor=conn.cursor()
              query=("select Gender from customer where Mobile=%s")
              value=(self.var_conatact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              
              lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
              lblGender.place(x=0,y=30)

              lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl3.place(x=90,y=30)
#EMail
              conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
              my_cursor=conn.cursor()
              query=("select Email from customer where Mobile=%s")
              value=(self.var_conatact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              
              lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
              lblEmail.place(x=0,y=60)

              lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl4.place(x=90,y=60)
              
#nationality
              conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
              my_cursor=conn.cursor()
              query=("select Nationality from customer where Mobile=%s")
              value=(self.var_conatact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              
              lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
              lblNationality.place(x=0,y=90)

              lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl5.place(x=90,y=90)
 #address             
              conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
              my_cursor=conn.cursor()
              query=("select Address from customer where Mobile=%s")
              value=(self.var_conatact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              
              lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
              lblAddress.place(x=0,y=120)

              lbl1=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl1.place(x=90,y=120)
#search
    def search(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
           my_cursor=conn.cursor()

           my_cursor.execute("Select * from room where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
           rows=my_cursor.fetchall()
           if len (rows)!=0:
                self.room_Table.delete(*self.room_Table.get_children())
                for i in rows:
                    self.room_Table.insert("",END,values=i)
                conn.commit()
           conn.close()
#total
   
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Laxary"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.9))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)
          
             
        
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.9))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)
        

if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
