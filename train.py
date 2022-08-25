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
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detection Based Student Attendence System")


        title_lbl=Label(self.root,text="Train data set",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_left=Image.open(r"D:\Face Detection Based Attendence System\images\train data.jpg")
        img_left=img_left.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(self.root,image=self.photoimg_left)
        bg_img.place(x=0,y=55,width=1530,height=325)

        b1_1=Button(self.root,text="Train data",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=0,y=380,width=1530,height=40)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[-1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(13)
        ids=np.array(ids)


        #------------------------train the classifier and save ----------------------
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.save("classifier.yml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !!")








if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()   