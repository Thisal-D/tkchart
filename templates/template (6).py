import tkinter as tk
import tkchart
import random

#root
root = tk.Tk()
root.geometry("700x400+500+300")
root.configure(bg="#151515")

#creating a chart
chart = tkchart.LineChart(master=root,
                          x_axis_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                          y_axis_values = (0,100),
                          y_axis_label_count=10,
                          x_axis_section_count=10,
                          y_axis_section_count=10,
                          x_axis_section_color="#5d6db6",
                          y_axis_section_color="#5d6db6",
                          data_font_style=("arial", 10, "bold"),
                          axis_font_style=("arial", 9, "italic"),
                          x_axis_font_color="#efefef",
                          y_axis_font_color="#efefef",
                          axis_color="#5d6db6",
                          x_axis_data_font_color="#efefef",
                          y_axis_data_font_color="#efefef",
                          y_space=20,
                          x_space=20,
                          )         
chart.pack()

#creating a line
line1 = tkchart.Line(master=chart,
                    size=3,
                    style="normal",
                    fill_color="#5d6db6",
                    fill="enabled")




data = [x for x in range(0,100)]
#dipslay data (random)
def loop():
    chart.show_data(line=line1, data=random.choices(data, k=1))
    
    root.after(500, loop)
loop()

root.mainloop()