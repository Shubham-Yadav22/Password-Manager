# Importing Modules
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    len_of_password = random.randint(0, 20)
    nr_symbols = random.randint(0, 10)
    nr_char = random.randint(0, 10)
    nr_numbers = random.randint(0, 10)

    password_letters = [random.choice(letters) for _ in range(nr_char)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_numbers + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    passw_en.insert(0, password)

    # Copying at clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Function to save password
def write():

    new_data = {
       Web_en.get() :  {
                "email": Email_en.get(),
                "password": passw_en.get()
       }
    }

    if len(Web_en.get()) == 0 or len(passw_en.get()) == 0 or len(Email_en.get()) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave any field empty")

    else:
        try:
            with open("data.json", "r") as f:
                # Read old data from file
                data = json.load(f)
        except:
            with open("data.json","w") as f:
                # Writing data for the first time
                json.dump(new_data,f,indent=4)
        else:
            with open("data.json", "w") as f:
                # Updating old data
                data.update(new_data)
                # Saving updated data
                json.dump(data, f, indent=4)


# Function to delete the entry
def clear_entry():
    Web_en.delete(0, END)
    passw_en.delete(0, END)
    Web_en.focus()

# Function to search in the file
def search():
    search_element = Web_en.get()
    try :
        with open("data.json") as f:
            data = json.load(f)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found. ")

    else :
        if search_element in data:
            email = data[search_element]["email"]
            password = data[search_element]["password"]
            messagebox.showinfo(title=search_element,message=f"Email: {email}\n Password: {password}")

        else :
            messagebox.showinfo(title="Error" ,message=f"No details for {search_element} exists ." )




# ---------------------------- UI SETUP ------------------------------- #
# setting up the window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)

# Inserting the logo
img = PhotoImage(file="logo1.png")

canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Labels
Web = Label(text="Website:")
Web.grid(row=1, column=0)

Email = Label(text="Email:")
Email.grid(row=2, column=0)

passw = Label(text="Password:")
passw.grid(row=3, column=0)

# Entries
Web_en = Entry(width=32)
Web_en.grid(column=1, row=1)
Web_en.focus()

Email_en = Entry(width=45)
Email_en.grid(column=1, row=2, columnspan=2)
Email_en.insert(0, "432shobhit@gmail.com")

passw_en = Entry(width=31)
passw_en.grid(column=1, row=3, columnspan=1)

# Buttons
Generate = Button(text="Generate", width=10, command=generate_password)
Generate.grid(row=3, column=2)

Add = Button(text="Add", width=26, command=lambda: [write(), clear_entry()])
Add.grid(row=4, column=1)

Search  = Button(text="Search", width=10 , command=search)
Search.grid(column=2,row=1,)

# Mainloop
window.mainloop()
