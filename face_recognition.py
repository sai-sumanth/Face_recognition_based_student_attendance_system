from cgitb import text
from tkinter import*
from tkinter import ttk
from turtle import title, width
from PIL import ImageTk,Image
from tkinter import messagebox
from click import command
import mysql.connector
import cv2
import os
from mysqlx import View
import numpy as np
import time
import csv
from time import strftime
from datetime import datetime


class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detection Based Student Attendence System")


        #-----------variables-----------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()


        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #first image
        img_left=Image.open(r"D:\Face Detection Based Attendence System\images\train data.jpg")
        img_left=img_left.resize((650,700),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(self.root,image=self.photoimg_left)
        bg_img.place(x=0,y=55,width=650,height=700)

        #second image
        img_left1=Image.open(r"D:\Face Detection Based Attendence System\images\train data.jpg")
        img_left1=img_left1.resize((950,700),Image.ANTIALIAS)
        self.photoimg_left1=ImageTk.PhotoImage(img_left1)

        bg_img=Label(self.root,image=self.photoimg_left1)
        bg_img.place(x=650,y=55,width=950,height=700)


        #button
        b1_1=Button(bg_img,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=350,y=620,width=200,height=40)
    #-----------------------attendence-----------------------------

    def mark_attendance(self,i,r,n,d):
        with open("att.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            date1=datetime.now()
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list)and(n not in name_list)and(d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                self.var_id=i
                self.var_roll=r
                self.var_name=n
                self.var_dept=d
                self.var_time=dtString
                self.var_date=d1
                conn=mysql.connector.connect(host="localhost",username="root",password="sumanth09",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_id,
                                                                                                                    self.var_roll,
                                                                                                                    self.var_name,
                                                                                                                    self.var_dept,
                                                                                                                    self.var_time,
                                                                                                                    self.var_date
                                                                                                                ))
                conn.commit()
                conn.close()       


     #----------------face recognition---------------
   
    def face_recog(self):
        def draw_boundray(img,classifer,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifer.detectMultiScale(gray_image,scaleFactor,minNeighbors)


            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,confidence=clf.predict(gray_image[y:y+h,x:x+w])

                conn=mysql.connector.connect(host="localhost",username="root",password="sumanth09",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where studentid="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where studentid="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)


                my_cursor.execute("select Dept from student where studentid="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select studentid from student where studentid="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confidence<50:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
 
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.yml")
            

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

        






if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()   