from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import font
from turtle import title
from PIL import ImageTk,Image
import tkinter
from student import Student
from student1 import Student1
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from time import strftime
from datetime import datetime


class Face_Recognition_System1:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Student Attendence System")

        #background image
        img=Image.open(r"D:\Face Detection Based Attendence System\images\bg1.jpg")
        img=img.resize((1530,710),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title
        title_lbl=Label(bg_img,text="Face Recoginition Based Student Attendence System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #------------time--------------
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #student button
        img4=Image.open(r"D:\Face Detection Based Attendence System\images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=300,width=220,height=40)


        


        #attendance button
        img6=Image.open(r"D:\Face Detection Based Attendence System\images\attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b2.place(x=800,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_1.place(x=800,y=300,width=220,height=40)


        


        #developers button
        img9=Image.open(r"D:\Face Detection Based Attendence System\images\developers.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b2=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.developer_data)
        b2.place(x=500,y=380,width=220,height=220)

        b2_1=Button(bg_img,text="Developers",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_1.place(x=500,y=580,width=220,height=40)


        #exit button
        img10=Image.open(r"D:\Face Detection Based Attendence System\images\exit.png")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b2=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.iExit)
        b2.place(x=800,y=380,width=220,height=220)

        b2_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_1.place(x=800,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    #--------------------function buttons----------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student1(self.new_window)       


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window) 

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 


    


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System1(root)
    root.mainloop()        
