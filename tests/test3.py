import tkinter as tk
import tkchart as tkc


root = tk.Tk()
root.minsize(1920,1000)

def width1400():
    chart.configure(width=1400)
def width700():
    chart.configure(width=700)
    
def height900():
    chart.configure(height=900)
def height500():
    chart.configure(height=500)
    
def barsize10():
    chart.configure(bar_size=10)
def barsize5():
    chart.configure(bar_size=5)
    
def ylabelcount20():
    chart.configure(y_labels_count=20)
def ylabelcount10():
    chart.configure(y_labels_count=10)
    
def xlabelcount20():
    chart.configure(x_labels_count=20)
def xlabelcount10():
    chart.configure(x_labels_count=10)
    
def ysectionscount20():
    chart.configure(y_sections_count=20)
def ysectionscount10():
    chart.configure(y_sections_count=10)
    
def xsectionscount10():
    chart.configure(x_sections_count=10)
def xsectionscount20():
    chart.configure(x_sections_count=20)
    
def ydecimals4():
    chart.configure(y_values_decimals=4)
def ydecimals0():
    chart.configure(y_values_decimals=0)
    
def xdecimals4():
    chart.configure(x_values_decimals=4)
def xdecimals0():
    chart.configure(x_values_decimals=0)
    
def linewidth50():
    chart.configure(line_width=50)
def linewidth100():
    chart.configure(line_width=100)
    
    
tk.Button(text="Width to 1400", command=width1400).place(x=1) 
tk.Button(text="Width to  700", command=width700).place(x=150)

tk.Button(text="height to 1000", command=height900).place(x=1, y=30)
tk.Button(text="height to 500",command=height500).place(x=150, y=30) 

tk.Button(text="bar size to 10",command=barsize10).place(x=1, y=60)
tk.Button(text="bar size to 5",command=barsize5).place(x=150, y=60) 

tk.Button(text="y_labels to 10",command=ylabelcount10).place(x=1, y=90)
tk.Button(text="y_labels to 20",command=ylabelcount20).place(x=150, y=90) 

tk.Button(text="x_labels to 10",command=xlabelcount10).place(x=1, y=120)
tk.Button(text="x_labels to 20",command=xlabelcount20).place(x=150, y=120) 

tk.Button(text="y_sections to 10",command=ysectionscount10).place(x=1, y=150)
tk.Button(text="y_sections to 20",command=ysectionscount20).place(x=150, y=150) 

tk.Button(text="x_sections to 10",command=xsectionscount10).place(x=1, y=180)
tk.Button(text="x_sections to 20",command=xsectionscount20).place(x=150, y=180) 

tk.Button(text="y decimals to 4",command=ydecimals4).place(x=1, y=210)
tk.Button(text="y decimals to 0",command=ydecimals0).place(x=150, y=210) 

tk.Button(text="x decimals to 4",command=xdecimals4).place(x=1, y=240)
tk.Button(text="x decimals to 0",command=xdecimals0).place(x=150, y=240) 

tk.Button(text="line width to 50",command=linewidth50).place(x=1, y=270)
tk.Button(text="line width to 100",command=linewidth100).place(x=150, y=270) 


## check this out this
chart = tkc.LineChart(root ,x_data_min_max=(0,50))        
chart.place(x=400, y=0)


line = tkc.Line(master=chart)

line2 = tkc.Line(master=chart)


data=[x for x in range(1,1001)]
datas = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
index = 0
import random
def display():
    global index
    chart.show_data(line=line, data=random.choices(datas,k=1))
    index+=1
    if index>= len(datas):
        index =0
    root.after(100, display)
display()


root.mainloop()