import tkinter as tk
import tkchart
import random

#root
root = tk.Tk()
root.configure(bg="#151515")
root.geometry("700x400+500+300")


#creating a chart
chart = tkchart.LineChart(master=root,
                          x_axis_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                          y_axis_values = (0,100))         
chart.pack()

#creating a line
line1 = tkchart.Line(master=chart,
                    size=3,
                    color="#ef8ccb",
                    style="normal",
                    fill="enabled",
                    fill_color="#b46d9a")

line2 = tkchart.Line(master=chart,
                    style="dashed",
                    size=3,
                    style_type=(10,5),
                    )

line3 = tkchart.Line(master=chart,
                    style="dotted",
                    style_type=(6,10),
                    color="#22eb48"
                    )

data = [x for x in range(0,100)]
#dipslay data (random)
def loop():
    chart.show_data(line=line1, data=random.choices(data, k=1))
    chart.show_data(line=line2, data=random.choices(data, k=1))
    chart.show_data(line=line3, data=random.choices(data, k=1))
    
    root.after(500, loop)
loop()

root.mainloop()