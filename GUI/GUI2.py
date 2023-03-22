import customtkinter
from tkinter import ttk




class App_GUI:


    def __init__(self, master):
        self.master = master
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        self.master.geometry('700x280')
        self.master.title('Task App')
        self.master.resizable(False, False)
        self.master.attributes('-alpha', 0.95)

        self.main_page()


    def main_page(self):


        def save_position():
            if len(entry1.get()) == 0 or len(entry2.get()) == 0:
                info.configure(text="Please provide valid data. Unable do save.")
                entry1.delete(0, customtkinter.END)
                entry2.delete(0, customtkinter.END)
            else:
                info.configure(text="Saved successfully")
                return [entry_1.get(), entry_2.get()]

        entry_1 = customtkinter.StringVar()
        entry_2 = customtkinter.StringVar()

        main_frame = customtkinter.CTkFrame(master=self.master)
        main_frame.pack(pady=20, padx=60, fill="both", expand=True)

        customtkinter.CTkLabel(main_frame, text="Enter Task to be done:").pack()
        entry1 = customtkinter.CTkEntry(master=main_frame, textvariable=entry_1)
        entry1.pack()

        customtkinter.CTkLabel(main_frame, text="Enter deadline:").pack()
        entry2 = customtkinter.CTkEntry(master=main_frame, textvariable=entry_2)
        entry2.pack()

        # entry_1.trace('w', entry_1.get())
        # entry_2.trace('w', entry_2.get())

        info = customtkinter.CTkLabel(main_frame, text="")
        info.pack()

        button1 = customtkinter.CTkButton(master=main_frame, text="Save task", command=save_position)
        button1.pack()

        button2 = customtkinter.CTkButton(master=main_frame, text="5 most important",
                                          command=lambda: [main_frame.destroy(), self.frame_5()])
        button2.pack(side='left', padx=20)

        button3 = customtkinter.CTkButton(master=main_frame, text="Show all",
                                          command=lambda: [main_frame.destroy(), self.frame_all()])
        button3.pack(side='right', padx=20)


    def frame_all(self):

        def delete_position():
            item = tree.selection()
            try:
                tree.delete(item)
            except:
                pass

            #TODO: add delete funct in db

        frame_all = customtkinter.CTkFrame(self.master)
        frame_all.pack(pady=20, padx=60, fill="both", expand=True)

        tree = ttk.Treeview(frame_all, columns=('c1','c2','c3'), show='headings')
        tree.column('#1', anchor=customtkinter.CENTER)
        tree.heading('#1', text='ID')
        tree.column('#2', anchor=customtkinter.CENTER)
        tree.heading('#2', text='TASK')
        tree.column('#3', anchor=customtkinter.CENTER)
        tree.heading('#3', text='DEADLINE')
        tree.insert('', customtkinter.END, values=(2,3,4))
        tree.insert('', customtkinter.END, values=(2,3,4))
        tree.pack()

        button1 = customtkinter.CTkButton(master=frame_all, text="Main page",
                                          command=lambda: [frame_all.pack_forget(), self.main_page()])
        button1.pack(side='left', padx=20)

        button2 = customtkinter.CTkButton(master=frame_all, text="Delete position",
                                          command=delete_position)
        button2.pack(side='right', padx=20)

    def frame_5(self):
        def delete_position():
            item = tree.selection()
            try:
                tree.delete(item)
            except:
                pass
            # TODO: add delete funct in db

        frame_5 = customtkinter.CTkFrame(self.master)
        frame_5.pack(pady=20, padx=60, fill="both", expand=True)

        tree = ttk.Treeview(frame_5, columns=('c1', 'c2', 'c3'), show='headings')
        tree.column('#1', anchor=customtkinter.CENTER)
        tree.heading('#1', text='ID')
        tree.column('#2', anchor=customtkinter.CENTER)
        tree.heading('#2', text='TASK')
        tree.column('#3', anchor=customtkinter.CENTER)
        tree.heading('#3', text='DEADLINE')
        tree.insert('', customtkinter.END, values=(2, 3, 4))
        tree.insert('', customtkinter.END, values=(2, 3, 4))
        tree.pack()

        button1 = customtkinter.CTkButton(master=frame_5, text="Main page",
                                          command=lambda: [frame_5.pack_forget(), self.main_page()])
        button1.pack(side='left', padx=20)

        button2 = customtkinter.CTkButton(master=frame_5, text="Delete position",
                                          command=delete_position)
        button2.pack(side='right', padx=20)


if __name__ == '__main__':

    root = customtkinter.CTk()
    app_gui = App_GUI(root)
    print(possitions)
    root.mainloop()
