import random

import customtkinter as ctk

import tkchart

root = ctk.CTk()

charts: list[tkchart.LineChart] = []
lines: list[tkchart.Line] = []

line_chart = tkchart.LineChart(
    master=root,
    x_axis_values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    y_axis_values=(0, 100),
    y_axis_label_count=10,
    width=500, height=200,
    axis_color="red", axis_size=10)
line_chart.pack()

line = tkchart.Line(master=line_chart, color="red")
line2 = tkchart.Line(master=line_chart, color="blue")
line_destroyed = False
line2_destroyed = False


def loop():
    global line2_destroyed,  line_destroyed
    if not line_destroyed:
        line_chart.show_data(line=line, data=[random.choice(range(0, 101))])
    if not line2_destroyed:
        line_chart.show_data(line=line2, data=[random.choice(range(0, 101))])

    root.after(1000, loop)


loop()

line_chart2 = tkchart.LineChart(
    master=root,
    x_axis_values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    y_axis_values=(0, 100),
    y_axis_label_count=10,
    width=500, height=200,
    axis_color="red", axis_size=10)
line_chart2.pack()

def hide(line: tkchart.Line):
    line.set_visible(False)


def show(line: tkchart.Line):
    line.set_visible(True)


def destroy1():
    global line_destroyed
    line_destroyed = True
    line.destroy()


def destroy2():
    global line2_destroyed
    line2_destroyed = True
    line2.destroy()

def hide_all():
    line_chart.set_lines_visibility(False)


def show_all():
    line_chart.set_lines_visibility(True)

def destroy_chart():
    line_chart.destroy()

def destroy_chart2():
    line_chart2.destroy()
    
def reset_chart():
    line_chart.reset()

ctk.CTkButton(master=root, text="hide line1", command=lambda: hide(line)).pack()
ctk.CTkButton(master=root, text="hide line2", command=lambda: hide(line2)).pack()
ctk.CTkButton(master=root, text="show line1", command=lambda: show(line)).pack()
ctk.CTkButton(master=root, text="show line2", command=lambda: show(line2)).pack()
ctk.CTkButton(master=root, text="show lines", command=show_all).pack()
ctk.CTkButton(master=root, text="hide lines", command=hide_all).pack()

ctk.CTkButton(master=root, text="destroy line1", command=destroy1).pack()
ctk.CTkButton(master=root, text="destroy line2", command=destroy2).pack()
ctk.CTkButton(master=root, text="destroy chart", command=destroy_chart).pack()
ctk.CTkButton(master=root, text="destroy chart2", command=destroy_chart2).pack()
ctk.CTkButton(master=root, text="reset chart", command=reset_chart).pack()


root.mainloop()
