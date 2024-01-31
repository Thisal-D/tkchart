import tkinter
import customtkinter
import tkchart
import random
import os
import time

root = customtkinter.CTk()
root.configure(bg="#202020")

root.minsize(1000,900)

chart = tkchart.LineChart(root, width=950, height=250,y_axis_max_value=1000, x_axis_values=[x for x in range(80,100)],
                            y_axis_data="GB" ,x_axis_data="S" ,y_axis_precision=5)
                       
chart.place(x=0, y=0)

chart.configure(x_axis_data_font_color="#000000", y_axis_data_font_color="#ff00ff",
                x_axis_font_color="#00ffff", y_axis_font_color="#ff00ff",
                y_axis_label_count=10)



line = tkchart.Line(master=chart, color="#ff0000", size=1)
line2 = tkchart.Line(master=chart, color="#00ff00", size=1)

data=[x for x in range(1,1001)]
def display():
    chart.show_data(line=line,  data=random.choices(data,k=1))
    root.after(1000, display)
display()

def display2():
    chart.show_data(line=line2, data=random.choices(data,k=1))
    root.after(2000, display2) 
display2()

root.mainloop()