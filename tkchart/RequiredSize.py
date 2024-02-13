import tkinter

def RequiredWidth(text="" ,font=None):
    required_width = 0
    label = tkinter.Label(font=font)
    label.config(text=str(text) +"")
    return label.winfo_reqwidth()


def RequiredHeight(text="" ,font=None):
    required_height = 0
    label = tkinter.Label(font=font)
    label.config(text=str(text) +"")
    return label.winfo_reqheight()