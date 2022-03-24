from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def userRegister(userId):
    userName1 = userName.get()
    mobileNum1 = mobileNum.get()
    emailAddress1 = emailAddress.get()
    userAddress1 = userAddress.get()
    userPassword1 = userPassword.get()
    print(userId)
    if userId > 0:
        role_id = 1
    else:
        role_id = 2
    if userName1 != "" and mobileNum1 != "" and emailAddress1 != "" and userAddress1 != "" and userPassword1 != "" :
        insert_Data = "Insert into user (user_name,user_mobile,user_email, user_address,user_password, role_id) value (%s,%s,%s,%s,%s,%s)"
        value = (userName1, mobileNum1, emailAddress1, userAddress1, userPassword1, role_id)
        cur.execute(insert_Data, value)
        con.commit()
        messagebox.showinfo("Info", "Record Inserted")
        if userId > 0:
          cur.execute("select * from user where user_name=%s", userName1)
          op = cur.fetchone()
          insert_junctionTable = "Insert into userContacts(parent_user_id, contact_user_id) value (%s, %s)"
          value = (userId, op[0])
          cur.execute(insert_junctionTable, value)
          con.commit()
        messagebox.showinfo("Info", "Junction table Inserted")
    else:
        messagebox.showinfo("Info", "Enter Valid Records")


    root.destroy()
    
def addUser(args): 

    print(args)
    global userName, mobileNum, emailAddress, userAddress, userPassword, Canvas1, con, cur, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "S@nde780yepuri"
    mydatabase = "CMS_db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#F8F9F9")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#F8F9F9",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="ADD A USER",bg='#F8F9F9', fg='black', font=15)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='#F8F9F9')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #User Name
    lb1 = Label(labelFrame,text="User Name : ",bg='#F8F9F9', fg='black')
    lb1.place(relx=0.05,rely=0.02, relheight=0.08)
        
    userName = Entry(labelFrame)
    userName.place(relx=0.3,rely=0.02, relwidth=0.62, relheight=0.08)
        
    # Mobile
    lb2 = Label(labelFrame,text="User Mobile : ",bg='#F8F9F9', fg='black')
    lb2.place(relx=0.05,rely=0.15, relheight=0.08)
        
    mobileNum = Entry(labelFrame)
    mobileNum.place(relx=0.3,rely=0.15, relwidth=0.62, relheight=0.08)
        
    # User Email
    lb3 = Label(labelFrame,text="User Email : ",bg='#F8F9F9', fg='black')
    lb3.place(relx=0.05,rely=0.30, relheight=0.08)
        
    emailAddress = Entry(labelFrame)
    emailAddress.place(relx=0.3,rely=0.30, relwidth=0.62, relheight=0.08)
        
    # User Address
    lb4 = Label(labelFrame,text="User Address",bg='#F8F9F9', fg='black')
    lb4.place(relx=0.05,rely=0.45, relheight=0.08)

    userAddress = Entry(labelFrame)
    userAddress.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)

    # User Password
    lb4 = Label(labelFrame,text="User Password",bg='#F8F9F9', fg='black')
    lb4.place(relx=0.05,rely=0.60, relheight=0.08)

    userPassword = Entry(labelFrame)
    userPassword.place(relx=0.3,rely=0.60, relwidth=0.62, relheight=0.08)

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#82E0AA', fg='black',command = lambda: userRegister(args))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#EC7063', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
