from cgitb import text
from tkinter import*
from tkinter import ttk
from turtle import title, width
from PIL import ImageTk,Image
from tkinter import messagebox
from click import command
import mysql.connector
import cv2
import csv


class Student:
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
        

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #buttoms frames
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        takephoto_btn=Button(btn_frame1,command=self.generate_dataset,text="take photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=0,column=0)

        updatephoto_btn=Button(btn_frame1,text="update photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=0,column=1)


        

        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"D:\Face Detection Based Attendence System\images\bg1.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        bg_img=Label(right_frame,image=self.photoimg_right)
        bg_img.place(x=5,y=0,width=720,height=130)

         #-------------search system--------------
        
        
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label (search_frame,text="search by:",font=("times new roman",13,"bold"))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("times new roman",12,"bold"),state="read only")
        search_combo["values"]=("select option","roll","phone","Dept")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="search",width=6,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,command=self.fetch_data,text="showall",width=6,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        save_btn=Button(search_frame,text="save",command=self.save_csv,width=6,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=5,padx=4)
        


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


    def add_data(self):
        if self.var_dep.get()=="Select Department"or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are requied",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sumanth09",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_id.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been addes succesful",parent=self.root)      
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)   

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
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]) 

    #--------update function----------
    def update_data(self):
        if self.var_dep.get()=="Select Department"or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are requied",parent=self.root)

        else:
            try:
                upadate=messagebox.askyesno("update","do you want to update this student details",parent=self.root)
                if upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sumanth09",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,name=%s,divison=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where studentid=%s",(

                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                    self.var_id.get()
                                                                                                                                                                ))
                else:
                    if not upadate:
                        return
                messagebox.showinfo("success","student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)

    #---------------delete function---------------
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","student id must be requried",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sumanth09",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where studentid=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)

    #-----------reset---------------
    def reset_data(self):
        self.var_dep.set("select department")
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_semester.set("Select semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("select division")
        self.var_roll.set("select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #--------------------search data----------------
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sumanth09",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close() 

            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)  



    #----------------save data-------------
    def save_csv(self):
        with open("sample.csv", "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')
        
            for row_id in self.student_table.get_children():
                row = self.student_table.item(row_id)['values']
                print('save row:', row)
                csvwriter.writerow(row)

    #--------------------generate data set or take photo samples--------------------
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department"or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are requied",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sumanth09",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,name=%s,divison=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where studentid=%s",(

                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                    self.var_id.get()==id+1
                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 
             


                 #--------------------------load predifined data on face frontals from opencv----------------

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed !!!")     
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)   









    



        

        










        




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()            