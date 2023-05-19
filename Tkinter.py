#import tkinter as tk
#root = tk.Tk()
#root.geometry("800x400") #width x height
#label1= tk.Label(root, text="Store your data")
#label1.place(x=50, y=10)
#tk.Entry().place(x=50, y=30)
#root.mainloop()

import tkinter as tk
root = tk.Tk()
root.geometry("500x500") #width x height
root.resizable(True, True)
root.configure(bg="blue")
root.title("Sign up")
user = tk.StringVar()
passwd = tk.StringVar()
def print_user_pwd():
    output.configure(text=f"{user.get()}, is my username and {passwd.get()} is my password")
    print(f"{user.get()}, is my username and {passwd.get()} is my password" )
tk.Label(root, text="Please sign up").grid(row=0, column=0, pady=15, padx=15)
tk.Label(root, text="Username", width=15).grid(row=1, column=0, pady=15, padx=15)
tk.Entry(root, width=15, textvariable=user).grid(row=1, column=1, pady=15, padx=15)
tk.Label(root, text="Password", width=15).grid(row=2, column=0, pady=15, padx=15)
tk.Entry(root, show="*", textvariable=passwd).grid(row=2, column=1, pady=15, padx=15)
tk.Button(root, text="Click me", width=15, command=print_user_pwd).grid(row=3, column=1, pady=15, padx=15)
output = tk.Label(root, text="result")
output.grid(row=4, column=0, columnspan=1)
root.mainloop()

