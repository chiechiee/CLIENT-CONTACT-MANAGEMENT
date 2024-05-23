import tkinter as tk

def add_contact():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    
  
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    status_label.config(text="Contact added successfully!")


root = tk.Tk()
root.title("Welcome to Your Contact Manager")


tk.Label(root, text="Your Name:").grid(row=0, column=0, sticky=tk.E)
tk.Label(root, text="Your Email:").grid(row=1, column=0, sticky=tk.E)
tk.Label(root, text="Your Phone:").grid(row=2, column=0, sticky=tk.E)


name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1)


add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=1)


status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=2)

root.mainloop()