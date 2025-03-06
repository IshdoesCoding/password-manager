from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    #password = ""

    #for letters in password_list:
        #password += letters

    print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #




def save():

    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title = "oops", message=" Don't leave any field empty!")
    else:
        try:
            with open('data.json', 'r') as file:
                #Read old data
                data = json.load(file)
                #update old data
        except FileNotFoundError:
            with open('data.json', 'w') as file:

                #saving updated data
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


#------------------------------ Search ----------------------------------#

def search():

    website = website_input.get()

    try:
        with open("data.json", "r") as file:
            data_dict = json.load(file)
            if website in data_dict:
                messagebox.showinfo(title = website, message = f" Your info: \n email: {data_dict[website]['email']}, \n password: {data_dict[website]['password']}")
            else:
                messagebox.showwarning(title="Error", message="no details for file")
    except FileNotFoundError:
        messagebox.showwarning(title= "Error", message= "file not found")


# ---------------------------- UI SETUP ------------------------------- #


#window

window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)


#canvas

canvas = Canvas(width = 200, height= 200 )
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(column= 1, row = 0,)

#label

website = Label(text="Website: ")
website.grid(column= 0 , row = 1)

email_U = Label(text = "Email/Username: ")
email_U.grid(column= 0 , row = 2)

password = Label(text = "Password: ")
password.grid(column= 0, row = 3)

#Buttons
generate_password = Button(text = "Generate Password: ", command = generate_password)
generate_password.grid(column= 2, row = 3)

add = Button(text = "Add", width = 36, command = save)
add.grid(column= 1 , row = 4, columnspan = 2)

search = Button(text="Search", width = 13, command = search )
search.grid(column = 2, row = 1)

#inputs

website_input = Entry( width= 35)
website_input.grid(column= 1, row = 1, columnspan = 1)
website_input.focus()

email_user_input = Entry( width = 35)
email_user_input.grid(column= 1, row = 2, columnspan = 1)
email_user_input.insert(0, 'ishmamabtahi17@gmail.com')


password_input = Entry(width = 21)
password_input.grid(column= 1 , row = 3)










window.mainloop()

