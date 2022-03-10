from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def userRegister():

    userName1 = userName.get()
    mobileNum1 = mobileNum.get()
    emailAddress1 = emailAddress.get()
    userAddress1 = userAddress.get()
    userPassword1 = userPassword.get()

    if userName1 != "" and mobileNum1 != "" and emailAddress1 != "" and userAddress1 != "" and userPassword1 != "" :
        insert_Data = "Insert into user1 (user_name,user_mobile,user_email, user_address, role_id) value (%s,%s,%s,%s,%s)"
        value = (userName1, mobileNum1, emailAddress1, userAddress1, 1)
        cur.execute(insert_Data, value)
        con.commit()
        messagebox.showinfo("Info", "Record Inserted")
    else:
        messagebox.showinfo("Info", "Enter Valid Records")
    
    print(bookDescription)
    print(bookTitle)
    print(bookCategory)
    print(bookAuthorName)
    print(bookPublication)
    print(bookPrice)
    print(bookISBN)


    root.destroy()
    
def addBook(): 
    
    global userName, mobileNum, emailAddress, userAddress, userPassword, bookInfo6, bookInfo7, Canvas1, con, cur, bookTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "S@nde780yepuri"
    mydatabase = "libpos"

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
        
    # Book ISBN
    lb1 = Label(labelFrame,text="User Name : ",bg='#F8F9F9', fg='black')
    lb1.place(relx=0.05,rely=0.02, relheight=0.08)
        
    userName = Entry(labelFrame)
    userName.place(relx=0.3,rely=0.02, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="User Mobile : ",bg='#F8F9F9', fg='black')
    lb2.place(relx=0.05,rely=0.15, relheight=0.08)
        
    mobileNum = Entry(labelFrame)
    mobileNum.place(relx=0.3,rely=0.15, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="User Email : ",bg='#F8F9F9', fg='black')
    lb3.place(relx=0.05,rely=0.30, relheight=0.08)
        
    emailAddress = Entry(labelFrame)
    emailAddress.place(relx=0.3,rely=0.30, relwidth=0.62, relheight=0.08)
        
    # Book Category
    lb4 = Label(labelFrame,text="User Address",bg='#F8F9F9', fg='black')
    lb4.place(relx=0.05,rely=0.45, relheight=0.08)

    userAddress = Entry(labelFrame)
    userAddress.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)

    # Book Category
    lb4 = Label(labelFrame,text="User Password",bg='#F8F9F9', fg='black')
    lb4.place(relx=0.05,rely=0.60, relheight=0.08)

    userPassword = Entry(labelFrame)
    userPassword.place(relx=0.3,rely=0.60, relwidth=0.62, relheight=0.08)

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#82E0AA', fg='black',command=userRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#EC7063', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
