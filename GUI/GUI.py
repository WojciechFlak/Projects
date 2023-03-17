import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('500x500')

def funct():
    print("anything")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Task App")
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Save task", command=funct())
button.pack()

root.mainloop()