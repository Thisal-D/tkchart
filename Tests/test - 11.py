import tkchart
import tkinter

import random
root = tkinter.Tk()
root.geometry("1920x1000")
chart = tkchart.LineChart(master=root, width=1011, height=600, y_axis_label_count=20,
                          x_axis_values=[x for x in range(1,21)], y_axis_max_value=1000, x_axis_section_count=5,
                          y_axis_section_count=5)
chart.pack()

line1 = tkchart.Line(master=chart ,color="blue", size=3)
line2 = tkchart.Line(master=chart ,color="yellow", size=3)
line3 = tkchart.Line(master=chart ,color="red", size=3)
line4 = tkchart.Line(master=chart ,color="white", size=3)
line5 = tkchart.Line(master=chart ,color="orange", size=3)



lines = [line1, line2, line3, line4, line5]

tkinter.Button(master=root, bg="orange", width=2, command=lambda :chart.hide(line=line5,state=True)).pack(side="right")
tkinter.Button(master=root, bg="white", width=2, command=lambda :chart.hide(line=line4,state=True)).pack(side="right")
tkinter.Button(master=root, bg="red", width=2, command=lambda :chart.hide(line=line3,state=True)).pack(side="right")
tkinter.Button(master=root, bg="yellow", width=2, command=lambda :chart.hide(line=line2,state=True)).pack(side="right")
tkinter.Button(master=root, bg="blue", width=2, command=lambda :chart.hide(line=line1,state=True)).pack(side="right")
tkinter.Label(master=root, text="Hide").pack(side="right")



tkinter.Label(master=root, text="Show").pack(side="left")
tkinter.Button(master=root, bg="blue", width=2, command=lambda :chart.hide(line=line1,state=False)).pack(side="left")
tkinter.Button(master=root, bg="yellow", width=2,  command=lambda :chart.hide(line=line2,state=False)).pack(side="left")
tkinter.Button(master=root, bg="red", width=2, command=lambda :chart.hide(line=line3,state=False)).pack(side="left")
tkinter.Button(master=root, bg="white", width=2, command=lambda :chart.hide(line=line4,state=False)).pack(side="left")
tkinter.Button(master=root, bg="orange", width=2, command=lambda :chart.hide(line=line5,state=False)).pack(side="left")



data = [[i for i in range(0,201)],
        [i for i in range(201,401)],
        [i for i in range(401,601)],
        [i for i in range(601,801)],
        [i for i in range(801,1001)],
        ]

def loop():
    global index
    for i,line in enumerate(lines):
        chart.show_data(line=line, data=random.choices(data[i],k=1))

    root.after(500,loop)
loop()


root.mainloop()