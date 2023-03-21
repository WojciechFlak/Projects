import customtkinter

# from Python_app import App


def main_page():
    def save_position():
        if len(entry1.get()) == 0 or len(entry2.get()) == 0:
            info.configure(text="Please provide valid data. Unable do save.")
            entry1.delete(0, customtkinter.END)
            entry2.delete(0, customtkinter.END)
        else:
            info.configure(text="Saved successfully")

    def show_5():
        pass

    main_frame = customtkinter.CTkFrame(master=root)
    main_frame.pack(pady=20, padx=60, fill="both", expand=True)

    customtkinter.CTkLabel(main_frame, text="Enter Task to be done:").pack()
    entry1 = customtkinter.CTkEntry(master=main_frame)
    entry1.pack()

    customtkinter.CTkLabel(main_frame, text="Enter deadline:").pack()
    entry2 = customtkinter.CTkEntry(master=main_frame)
    entry2.pack()

    info = customtkinter.CTkLabel(main_frame, text="")
    info.pack()

    button1 = customtkinter.CTkButton(master=main_frame, text="Save task", command=save_position)
    button1.pack()

    button2 = customtkinter.CTkButton(master=main_frame, text="5 most important", command=show_5)
    button2.pack(side='left', padx=20)

    button3 = customtkinter.CTkButton(master=main_frame, text="Show all",
                                      command=lambda: [main_frame.destroy(), frame1()])
    button3.pack(side='right', padx=20)


def frame1():

    def delete_position():
        pass

    frame1 = customtkinter.CTkFrame(root)
    frame1.pack(pady=20, padx=60, fill="both", expand=True)

    button1 = customtkinter.CTkButton(master=frame1, text="Main page",
                                      command=lambda: [frame1.pack_forget(), main_page()])
    button1.pack(side='left', padx=20)

    button2 = customtkinter.CTkButton(master=frame1, text="Delete position",
                                      command=delete_position)
    button2.pack(side='right', padx=20)



customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('700x280')
root.title('Task App')
root.resizable(False, False)
root.attributes('-alpha', 0.95)

main_page()

root.mainloop()
