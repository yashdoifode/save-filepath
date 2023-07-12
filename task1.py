from tkinter import *
from tkinter import filedialog
import mysql.connector 
import mysql.connector as conn

database = conn.connect(host='localhost',user='root',password='@yash2002',database='filepath')


base=Tk()
base.geometry('400x400')

myfile = filedialog.askdirectory()

def mysql():
    curs=database.cursor()
    s = "INSERT INTO path (filepath) VALUES(%s)"
    B1=(myfile,)
    curs.execute(s,B1)
    database.commit()
    label=Label(text=myfile,foreground="red")
    label.place(x=150,y=150)
    print("done")

label=Label(text=myfile,foreground="red")
label.place(x=150,y=150)    
b2 = Button(base,text="Save Path",command=mysql)
b2.place(x=150,y=300)    



base.mainloop()
