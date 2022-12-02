import tkinter as tk

def RequredWidth(text="" ,font=None):
    requred_width = 0
    label = tk.Label(font=font)
    label.config(text=str(text) +"      ")
    requred_width = label.winfo_reqwidth()
    return requred_width

def RequredHeight(text="" ,font=None):
    requred_height = 0
    label = tk.Label(font=font)
    label.config(text=str(text) +"      ")
    requred_height = label.winfo_reqheight()
    return requred_height