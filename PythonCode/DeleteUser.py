from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "S@nde780yepuri"
mydatabase="libpos"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()




def deleteUser():

    userName = userInfo.get()
    getUserId = "select * from User1 where user_name = '%s'" % userName
    deleteByUserName = "Delete from User2 where user_name = '%s'" % userName
    

    try:
        cur.execute(getUserId)
        result = cur.fetchone()
        deleteJuntionTableRecords = "Delete from userContacts2 where parent_user_id = '%s'" % result[0]
        cur.execute(deleteJuntionTableRecords)
        cur.execute(deleteByUserName)
        con.commit()
        messagebox.showinfo("Information", "Record Deleted")
    except:
        messagebox.showinfo("Please check Book ID")

    print(deleteByUserName)

    root.destroy()
    
def delete(): 
    
    global userInfo,Canvas1,con,cur,root
    
    root = Tk()
    root.title("Delete")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#FDFEFE")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FDFEFE",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete A Existing User", bg='#FDFEFE', fg='black', font=15)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='#FDFEFE')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Enter user name: ", bg='#FDFEFE', fg='black')
    lb1.place(relx=0.05,rely=0.5)
        
    userInfo = Entry(labelFrame)
    userInfo.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Delete",bg='#d1ccc0', fg='black',command=deleteUser)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
