from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddUser import *
from DeleteUser import *
from showAllRecord import *

# Add your own database name and password here to reflect in the code
mypass = "S@nde780yepuri"
mydatabase="CMS_db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()


def mainmenu():
    root = Tk()
    root.title("Admin_View")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Take n greater than 0.25 and less than 5
    same = True
    n = 0.25

    # Adding a background image
    background_image = Image.open("CMS-Home-Image.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth * n)
    if same:
        newImageSizeHeight = int(imageSizeHeight * n)
    else:
        newImageSizeHeight = int(imageSizeHeight / n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FDFEFE", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Wizards At Work \nContact Management System", bg='#FDFEFE', fg='#17202A',
                         font='40')
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="Add a new user ", bg='#AED6F1', fg='black', command=lambda: addUser(0))
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Delete a User", bg='#AED6F1', fg='black', command=lambda: delete(0))
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
    

    root.mainloop()
