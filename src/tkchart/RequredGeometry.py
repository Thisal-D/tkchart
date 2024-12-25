import tkinter

def RequredWidth(text="" ,font=None):
    requred_width = 0
    label = tkinter.Label(font=font)
    label.config(text=str(text) +"")
    return label.winfo_reqwidth()


def RequredHeight(text="" ,font=None):
    requred_height = 0
    label = tkinter.Label(font=font)
    label.config(text=str(text) +"")
    return label.winfo_reqheight()