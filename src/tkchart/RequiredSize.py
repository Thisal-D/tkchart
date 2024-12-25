import tkinter

def RequiredWidth(text="" ,font=None):
    label = tkinter.Label(font=font)
    label.config(text=str(text) +"")
    return label.winfo_reqwidth()


def RequiredHeight(text="" ,font=None):
    label = tkinter.Label(font=font)
    label.config(text=str(text) +"")
    return label.winfo_reqheight()