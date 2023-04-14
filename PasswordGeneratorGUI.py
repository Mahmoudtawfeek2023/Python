import random
import string
import os
import datetime
import tkinter as tk
from tkinter import messagebox

# Function to generate strong password with given length
def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    # Combine all character sets
    all_chars = lowercase + uppercase + digits + symbols
    # Shuffle all characters
    shuffled_chars = random.sample(all_chars, len(all_chars))
    # Take first 'length' characters from shuffled characters
    password = ''.join(shuffled_chars[:length])
    return password

# Function to save password to file
def save_password_to_file(password):
    current_dir = os.getcwd()
    password_folder_path = os.path.join(current_dir, "password_generator")
    if not os.path.exists(password_folder_path):
        os.makedirs(password_folder_path)
    password_file_path = os.path.join(password_folder_path, "passwords.txt")
    with open(password_file_path, "a") as f:
        f.write(f"{datetime.datetime.now()}: {password}\n")

# Function to handle password generation and saving
def generate_password_and_save(length, repeat_days):
    # Generate password with given length
    password = generate_password(length)
    print(f"Generated password: {password}")
    # Save password to file
    save_password_to_file(password)
    # Set next password generation date
    next_gen_date = datetime.datetime.now() + datetime.timedelta(days=repeat_days)
    with open("next_gen_date.txt", "w") as f:
        f.write(str(next_gen_date))

# Function to check if password generation should be repeated based on repeat_days
def check_repeat():
    if os.path.exists("next_gen_date.txt"):
        with open("next_gen_date.txt", "r") as f:
            next_gen_date = datetime.datetime.strptime(f.read().strip(), '%Y-%m-%d %H:%M:%S.%f')
            if datetime.datetime.now() < next_gen_date:
                return False
    return True

# Function to handle password generation button click event
def generate_password_clicked():
    try:
        length = int(length_entry.get())
        if length < 9:
            raise ValueError("Password length must be 9 or greater.")
        repeat_days = int(repeat_entry.get())
        if repeat_days <= 0:
            raise ValueError("Repeat days must be greater than 0.")
        if check_repeat():
            generate_password_and_save(length, repeat_days)
            messagebox.showinfo("Password Generated", "Password generated and saved successfully.")
        else:
            messagebox.showinfo("Cannot Generate Password", f"Password generation can only be repeated after {repeat_days} days.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        
# Create GUI window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")

# Create password length label and entry
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Create repeat days label and entry
repeat_label = tk.Label(window, text="Repeat Every (days):")
repeat_label.pack()
repeat_entry = tk.Entry(window)
repeat_entry.pack()

# Create generate password button
generate_button = tk.Button(window, text="Generate Password", command=generate_password_clicked)
generate_button.pack()

# Run GUI main loop
window.mainloop()
