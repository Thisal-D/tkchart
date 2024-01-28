import tkinter
import customtkinter
import tkchart

import os
import time

root = customtkinter.CTk()
root.configure(bg="#202020")

root.minsize(1000,900)

chart = tkchart.LineChart(root, width=950, height=250,y_data_max=1000,x_data_min_max=(50,100),x_values_decimals=5 ,y_data="GB" ,x_data="S" ,y_values_decimals=5)
                        
                        
chart.place(x=0, y=0)

chart.configure(x_data_color="#000000", y_data_color="#ff00ff",
                x_values_color="#00ffff", y_values_color="#ff00ff",
                y_labels_count=10, x_labels_count=10)



line = tkchart.Line(master=chart, color="#ff0000", size=1)

line2 = tkchart.Line(master=chart, color="#00ff00", size=1)

import random
data=[x for x in range(1,1001)]
datas = [0,1000,0,1000,0,1000,0,1000,0,1000]

index = 0
def display():
    global index
    chart.show_data(line=line, data=[datas[index]])
    index+=1
    if index>= len(datas):
        index =0
    root.after(500, display)
display()

i =  1
def display2():
    global speed
    global i
    chart.show_data(line=line2, data=random.choices(data,k=1))
    i = i+1
    root.after(500, display2)
    
display2()

root.mainloop()