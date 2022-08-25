from atexit import register
from tkinter import *
from tkinter import ttk
from turtle import left, width
from PIL import Image,ImageTk
from matplotlib.pyplot import text  
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detection Based Attendence System")

        #------------variables-----------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        img=Image.open(r"D:\Face Detection Based Attendence System\images\bg.jpg")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)


        #------------left image-------------
        self.bg1=ImageTk.PhotoImage(file=r"D:\Face Detection Based Attendence System\images\bg.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #----------main frame-------------
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)


        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #---------label and entry------------

        #-----------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)


        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=370,y=130,width=250)

        #-----------row2
        fname=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=170)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact_entry.place(x=50,y=200,width=250)

        fname=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=370,y=170)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email_entry.place(x=370,y=200,width=250)

        #-------------row3
        fname=Label(frame,text="select secutity question",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=240)

        self.combo_security=ttk.Combobox(frame,textvariable=self.var_securityq,font=("time new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","your birthday","place of brith","pet name")
        self.combo_security.place(x=50,y=270,width=250)

        fname=Label(frame,text="secutity answer",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=370,y=240)

        self.security_entry=ttk.Entry(frame,textvariable=self.var_securitya,font=("times new roman",15,"bold"))
        self.security_entry.place(x=370,y=270,width=250)

        #------------row4
        fname=Label(frame,text="password",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=310)

        self.password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.password_entry.place(x=50,y=340,width=250)


        fname=Label(frame,text="confirm password",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=370,y=310)

        self.security_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.security_entry.place(x=370,y=340,width=250)

        #------------checkbox------------
        self.var_check=IntVar()
        checkbox=Checkbutton(frame,variable=self.var_check,text="I Agree The terms and conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbox.place(x=50,y=380 )

        #----------buttons-----------
        img=Image.open(r"D:\Face Detection Based Attendence System\images\register.png")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1= Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)


        img1=Image.open(r"D:\Face Detection Based Attendence System\images\log.png")
        img1=img1.resize((200,45),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1= Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=330,y=420,width=200)


    #------------function declaration------------

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="Select":
            messagebox.showerror("Erro","All fields are requried")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sumanth09",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityq.get(),
                                                                                    self.var_securitya.get(),
                                                                                    self.var_pass.get()

                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Succesfully")





    




if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()