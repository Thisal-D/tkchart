import tkinter as tk
import tkchart
import random

#root
root = tk.Tk()
root.geometry("700x400+500+300")
root.configure(bg="#151515")

#creating a chart
chart = tkchart.LineChart(master=root,
                          x_axis_values = ("100\nS", "200\nS", "300\nS", "400\nS", "500\nS", "600\nS", "700\nS", "800\nS", "900\nS"),
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
                          x_axis_data="Seconds\n(s)",
                          x_axis_data_position="side",
                          y_axis_data_position="top",
                          
                        
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