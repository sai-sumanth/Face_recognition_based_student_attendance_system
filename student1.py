from cgitb import text
from tkinter import*
from tkinter import ttk
from turtle import title, width
from PIL import ImageTk,Image
from tkinter import messagebox
from click import command
import mysql.connector
import cv2


class Student1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detection Based Student Attendence System")

        #----------------variables--------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #background image
        img=Image.open(r"D:\Face Detection Based Attendence System\images\bg1.jpg")
        img=img.resize((1530,710),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title
        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open(r"D:\Face Detection Based Attendence System\images\bg1.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(left_frame,image=self.photoimg_left)
        bg_img.place(x=5,y=0,width=720,height=130)

        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)

        #department
        dep_label=Label (current_course_frame,text="Department",font=("times new roman",13,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("select department","cse","ece","civil","mech")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label=Label (current_course_frame,text="Section",font=("times new roman",13,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only")
        course_combo["values"]=("select section","a","b","c","d")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label (current_course_frame,text="year",font=("times new roman",13,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only")
        year_combo["values"]=("select year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #semester
        sem_label=Label (current_course_frame,text="semester",font=("times new roman",13,"bold"))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only")
        sem_combo["values"]=("select semester","1","2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        #student id
        studentid_label=Label (class_student_frame,text="student id",font=("times new roman",13,"bold"))
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student name
        studentname_label=Label (class_student_frame,text="student name",font=("times new roman",13,"bold"))
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        classdiv_label=Label (class_student_frame,text="class division",font=("times new roman",13,"bold"))
        classdiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only")
        div_combo["values"]=("select ","a","b","c","d")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #gender
        studentgender_label=Label (class_student_frame,text="student gender",font=("times new roman",13,"bold"))
        studentgender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)


        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only")
        gender_combo["values"]=("select ","male","female","other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #dob
        studentdob_label=Label (class_student_frame,text="student dob",font=("times new roman",13,"bold"))
        studentdob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        studentdob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        studentdob_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #email
        studentemail_label=Label (class_student_frame,text="student email",font=("times new roman",13,"bold"))
        studentemail_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentemail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        studentemail_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #phone no
        studentph_label=Label (class_student_frame,text="student phone",font=("times new roman",13,"bold"))
        studentph_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentph_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        studentph_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #address
        studentname_label=Label (class_student_frame,text="student address",font=("times new roman",13,"bold"))
        studentname_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #teacher name 
        studenttname_label=Label (class_student_frame,text="teacher name",font=("times new roman",13,"bold"))
        studenttname_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studenttname_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        studenttname_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #roll no 
        studentroll_label=Label (class_student_frame,text="roll no",font=("times new roman",13,"bold"))
        studentroll_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        studenttname_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        studenttname_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        

        


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"D:\Face Detection Based Attendence System\images\bg1.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        bg_img=Label(right_frame,image=self.photoimg_right)
        bg_img.place(x=5,y=0,width=720,height=130)

        

        #-----table frame-----
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="photosamplestatud")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    
    #--------------function declaration--------------


    
     #------------fetch data----------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sumanth09",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                 self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    


    #---------get cursor--------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]), 
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]) 

    
        










        




if __name__ == "__main__":
    root=Tk()
    obj=Student1(root)
    root.mainloop()            