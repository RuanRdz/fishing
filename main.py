from dotenv import load_dotenv
from tkinter import *
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.label = customtkinter.CTkLabel(self, text="CTkLabel", fg_color="transparent")
        self.label.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        self.entry = customtkinter.CTkEntry(self, placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        #self.entry.bind("<Return>", self.search_event)

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("checkbox_frame_1:", self.checkbox_frame_1.get())
        print("checkbox_frame_2:", self.checkbox_frame_2.get())

app = App()
app.mainloop()