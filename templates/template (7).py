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
                          )         
chart.pack()

#creating a line
line1 = tkchart.Line(master=chart,
                    size=3,
                    point_highlight="enabled",
                    point_highlight_size=10,
                    fill="enabled",
                    style="normal")




data = [x for x in range(0,100)]
#dipslay data (random)
def loop():
    chart.show_data(line=line1, data=random.choices(data, k=1))
    
    root.after(500, loop)
loop()

root.mainloop()