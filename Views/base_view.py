from tkinter import ttk
from tkinter import *

class BaseView:
    def __init__(self, window):
        self.window = window

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def on_selection_clear(self,event):
        event.widget.selection_clear()

    def create_dropdown(self, frame, state, row, column, columnspan, padx, binding_func, values=None):
        dropdown = ttk.Combobox(frame, state=state)
        dropdown.bind('<<ComboboxSelected>>', binding_func)
        dropdown['values'] = values
        dropdown.grid(row=row, column=column, columnspan=columnspan, padx=padx)
        return dropdown

    def create_button(self, frame, text, command, state, row, column, pady, columnspan=1, sticky=None ):
        button = Button(frame, text=text, command=command, state=state)
        button.grid(row=row, column=column,columnspan=columnspan, pady=pady, sticky=sticky)
        return button

    def create_label(self, frame, text, row, column, padx, columnspan, sticky, font=None, bg=None):
        label = Label(frame, text=text, font=font, bg=bg,)
        label.grid(row=row, column=column, padx=padx, columnspan=columnspan, sticky=sticky)
        return label
    
    def format_dropdown_values(self, dict_values):
        return [key for key in dict_values.keys()]