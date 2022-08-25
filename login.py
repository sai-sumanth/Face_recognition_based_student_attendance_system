from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from matplotlib.pyplot import text  
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
from main1 import Face_Recognition_System1

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Student Attendence System")

        img=Image.open(r"D:\Face Detection Based Attendence System\images\bg.jpg")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"D:\Face Detection Based Attendence System\images\loginlogo.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started ",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)


        #label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button
        registerbtn=Button(frame,text="New user Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black")
        registerbtn.place(x=15,y=350,width=160)

        #forgetpassword button
        #forgetbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black")
        #forgetbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields are required")
        elif self.txtuser.get()=="sai" and self.txtpass.get()=="sai123":
            #messagebox.showinfo("Success","Welcome to face recognition based attendance system")
            open_main=messagebox.askyesno("YesNo","Access only Authority Person")
            if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window) 
            else:
                if not open_main:
                    return
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sumanth09",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()

                                                                                     ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System1(self.new_window) 
                
            conn.commit()
            conn.close() 
    


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

        

        #------------row3
        fname=Label(frame,text="password",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=240)

        self.password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.password_entry.place(x=50,y=270,width=250)


        fname=Label(frame,text="confirm password",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=370,y=240)

        self.security_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.security_entry.place(x=370,y=270,width=250)

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


    


    #------------function declaration------------

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" :
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
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_pass.get()

                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Succesfully")



if __name__=="__main__":
    main()