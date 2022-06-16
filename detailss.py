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


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
        
        self.var_floor=StringVar()
        self.var_roomno=StringVar()
        self.var_roomtype=StringVar()
       

        
        lbl_title=Label(self.root,text="Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        img2=Image.open(r"C:\Users\kity\hotel management system\hotel\image\golden-hotel-logo-free-graphics-free-vector-thumb.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
       
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"))
        labelframeleft.place(x=5,y=50,width=540,height=350)
#floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",13,"bold"),width=29)
        enty_floor.grid(row=0,column=1,sticky=W)
#roomno
        lbl_roomno=Label(labelframeleft,font=("arial",12,"bold"),text="Room No",padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W)
       
        txt_roomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno,font=("arial",13,"bold"),width=29)     
        txt_roomno.grid(row=1,column=1)
#roomtype
        label_roomtype=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_roomtype.grid(row=3,column=0,sticky=W)
        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_roomtype["value"]=("Single","Double","Laxary")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)
#button
#bttns      
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_Delete=Button(btn_frame,text="Delete",command=self.nDELETE,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_Delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_reset.grid(row=0,column=3,padx=1)
        #==========================right side image===========

       #arch================
        
        table_frameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"))
        table_frameleft.place(x=600,y=55,width=600,height=350)

        
        
        scroll_x=ttk.Scrollbar(table_frameleft,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frameleft,orient=VERTICAL)

        self.room_Table=ttk.Treeview(table_frameleft,columns=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("floor",text="floor")
        self.room_Table.heading("roomno",text="Room No")
        self.room_Table.heading("roomtype",text="Room Type")
       

        self.room_Table["show"]="headings"
        
        self.room_Table.column("floor",width=100)
        self.room_Table.column("roomno",width=100)
        self.room_Table.column("roomtype",width=100)     
        self.room_Table.pack(fill=BOTH,expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
#add data
    def add_data(self):
        if self.var_floor.get()==""or self.var_roomno.get()=="":  
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
                try:
                       conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
                       my_cursor=conn.cursor()
                       my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                   self.var_floor.get(),
                                                                                   self.var_roomno.get(),           
                                                                                   self.var_roomtype.get()                                                                            
                                                                                ))
                       conn.commit()
                       self.fetch_data()
                       conn.close()
                       messagebox.showinfo("Success","No Room has been added",parent=self.root)
                except Exception as es:
                       messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

     #fetch data                    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from details") 
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

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])
        
       

   #update
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        else:                   
            conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,roomtype=%s where roomno=%s ",(                                                                                                   
                                                                                          self.var_floor.get(),             
                                                                                          self.var_roomtype.get(),
                                                                                          self.var_roomno.get()                                                                        
                                                                                         ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room has been updated successfully",parent=self.root)

 #delete
    def nDELETE(self):
           nDELETE=messagebox.askyesno("Hotel System","Do you want to delete this customer",parent=self.root)
           if nDELETE>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="Csu1234!",database="geeksforgeeks")
               my_cursor=conn.cursor()
               query="delete from details where roomno=%s"
               value=(self.var_roomno.get(),)
               my_cursor.execute(query,value)
           else:
               if not nDELETE:
                       return
           conn.commit()
           self.fetch_data()
           conn.close()  
    def reset(self):
           self.var_floor.set("")
           self.var_roomno.set("")
           self.var_roomtype.set("")
           
              
                   
   
        

if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()