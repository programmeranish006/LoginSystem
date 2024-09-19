from tkinter import *
from tkinter import messagebox
import os


def login():
    user = username.get()
    code = password.get()

    if user == "Anish" and code == "123":
        print("Login successful!")

        root = Toplevel(screen)
        root.title("Bill")
        root.geometry("1280x720+150+80")

        # Create and display the success label
        success_label = Label(root, text="Login successful!", font=("Arial", 20))
        success_label.pack(pady=20)


       

        # Add other functionality for the 'Bill' window here

    elif user == "" and code == "":
        messagebox.showerror("Invalid", "Please enter username and Password")
    elif user == "":
        messagebox.showerror("Invalid", "Username is mandatory")
    elif code == "":
        messagebox.showerror("Invalid", "Password is required")
    elif user != "Anish" or code != "123":
        messagebox.showerror("Invalid", "Incorrect Username or Password!")
    elif user != "Anish":
        messagebox.showerror("Invalid", "Please enter a valid Username")
    elif code != "123":
        messagebox.showerror("Invalid", "Password is incorrect!")


    


def main_screen():


    global screen
    global username
    global password
    
    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")

    # Icon (adjust the path as needed)
    image_icon = PhotoImage(file=r"C:\Users\NJ521WS\OneDrive\画像\Camera Roll\lock.png")
    screen.iconphoto(False, image_icon)
    
    screen.title("Login system")


    lblTitle=Label(text="Login System",font=("arial",50,'bold'),fg="blue",bg="#d7dae2")
    lblTitle.pack(pady=50)


    bordercolor=Frame(screen,bg="Black",width=800,height=400)
    bordercolor.pack()

    mainframe=Frame(bordercolor,bg="#d7dae2",width=800,height=400)
    mainframe.pack(padx=20,pady=20)

    Label(mainframe, text="Username", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="Password", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)
    
    username=StringVar()
    password=StringVar()

    entry_username=Entry(mainframe,textvariable=username,width=12,bd=2,font=("arial",30))
    entry_username.place(x=400,y=50)
    entry_password=Entry(mainframe,textvariable=password,width=12,bd=2,font=("arial",30),show="*")
    entry_password.place(x=400,y=150)

    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    Button(mainframe, text="Login", height="2", width=23, bg="#ed3833", fg="White", bd=0, command=login).place(x=100, y=250)

    Button(mainframe,text="Reset",height="2",width=23,bg="#1089ff",fg="White",bd=0,command=reset).place(x=300,y=250)
    Button(mainframe,text="Back",height="2",width=23,bg="#00bd56",fg="White",bd=0,command=screen.destroy).place(x=500,y=250)
        





    

    screen.mainloop()
    

    

    # Add other widgets or functionality here

    screen.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main_screen()
