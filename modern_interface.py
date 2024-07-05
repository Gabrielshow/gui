# Install customtkinter

import customtkinter

customtkinter.set_appearance_mode("dark")  #you can also change this "System"
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")
    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=50, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButon(master=frmae, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

root.mainloop()
                        