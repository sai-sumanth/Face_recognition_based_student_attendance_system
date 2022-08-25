from cgitb import text
from tkinter import*
from tkinter import ttk
from turtle import title, width
from PIL import ImageTk,Image
from tkinter import messagebox
from click import command
from matplotlib.pyplot import fill
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detection Based Student Attendence System")

        #--------------variables-----------------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        #background image
        img=Image.open(r"D:\Face Detection Based Attendence System\images\bg.jpg")
        img=img.resize((1530,710),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=130,width=1530,height=710)

         #title
        title_lbl=Label(bg_img,text="Attendance Management System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"D:\Face Detection Based Attendence System\images\bg.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(left_frame,image=self.photoimg_left)
        bg_img.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #--------------------label entry---------

        #attendance id
        attendanceid_label=Label (left_inside_frame,text="Attendance id",font=("times new roman",13,"bold"))
        attendanceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceid_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        name_label=Label (left_inside_frame,text="Roll",font=("times new roman",13,"bold"))
        name_label.grid(row=0,column=2,padx=4,pady=8)

        name_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        name_entry.grid(row=0,column=3,pady=8)

        #name
        date_label=Label (left_inside_frame,text="Name",font=("times new roman",13,"bold"))
        date_label.grid(row=1,column=0)

        date_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        date_entry.grid(row=1,column=1,pady=8)


        #department
        dept_label=Label (left_inside_frame,text="Department",font=("times new roman",13,"bold"))
        dept_label.grid(row=1,column=2)

        dept_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        dept_entry.grid(row=1,column=3,pady=8)

        #time
        time_label=Label (left_inside_frame,text="Time",font=("times new roman",13,"bold"))
        time_label.grid(row=2,column=0)

        time_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,pady=8)

        #date
        date_label=Label (left_inside_frame,text="Date",font=("times new roman",13,"bold"))
        date_label.grid(row=2,column=2)

        date_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,pady=8)


        #attendance
        attendance_label=Label (left_inside_frame,text="Attendance Status",font=("times new roman",13,"bold"))
        attendance_label.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)


        #buttoms frames
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=70)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2)


        




        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=715,height=445)

        #-------------scroll bar--------------

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #------------------fetch data--------------
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


    









if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()            