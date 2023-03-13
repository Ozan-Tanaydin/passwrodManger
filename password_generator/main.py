from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    random_password = [choice(letters) for _ in range(randint(8,10))]
    random_password.extend([choice(numbers) for _ in range(randint(2,4))])
    random_password.extend([choice(symbols) for _ in range(randint(2,4))])
    
    shuffle(random_password)
    final_pass = "".join(random_password)
    
    pyperclip.copy(text=final_pass)
    password_entry.delete(0,END)
    password_entry.insert(0, final_pass)


# ---------------------------- SEARCH ------------------------------- #

def search():

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            user_data = data[website_input.get()]
    except FileNotFoundError:
        messagebox.showerror(title="No File!", message="No file found")

    except KeyError:
        messagebox.showerror(title="Invalid Account", message="There is no record for that website")

    else:
        messagebox.showerror(title=f"website_input.get()", message=f"Email: {user_data['email']}\n Passwrod: {user_data['password']}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    mail_username = mail_username_entry.get()
    password = password_entry.get()

    new_data={website:{
        "email": mail_username,
        "password": password
        }
    }
    
    if len(website) == 0 or len(mail_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty fields", message="Please don't left any empty area")
    else:
        #messagebox.showinfo(title="Save Successful!", message="Your informaration succesfully saved")
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0,END)
            password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Passwrod Generator")
window.config(padx=20, pady=20)


#logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


#form
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=15)
website_input.grid(column=1,row=1,)
website_input.focus()

search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)


mail_username_label = Label(text="Email/Username:")
mail_username_label.grid(column=0, row=2)

mail_username_entry = Entry(width=36)
mail_username_entry.grid(column=1,row=2, columnspan=2)
mail_username_entry.insert(0, "zntnydn@gmail.com")


password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=17)
password_entry.grid(column=1,row=3, padx=0)

generate_passwrod_button = Button(text="Generate Passwrod", width=15, command=generate_password)
generate_passwrod_button.grid(column=2, row=3, padx=0)



add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
