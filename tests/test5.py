import tkinter
import tkchart
import random #for get random value

#create root 
root = tkinter.Tk()
root.minsize(1200,800)

#create LineChart
linechart = tkchart.LineChart(master=root, 
                            width=1000, 
                            height=400,
                            bar_size=5,
                            
                            y_sections_count=5,
                            x_sections_count=5,
                            y_labels_count=5,
                            x_labels_count=5,
                            
                            y_data="GB",
                            x_data="S",
                            x_data_min_max=(20,60),
                            y_data_max=1000,
                            x_values_decimals=4,
                            y_values_decimals=5,
                            
                            sections_color="#707070",
                            y_values_color="#bbbbbb",
                            x_values_color="#bbbbbb",
                            x_data_color="#00ff00",
                            y_data_color="#00ff00",
                            bg_color="#202020",
                            chart_color="#101010",
                            bar_color="#cccccc",
                            
                            x_y_data_font = ("Arial", 15,"bold"),
                            x_y_values_font = ("Arial", 10,"bold"),
                            )
#place LineChart
linechart.place(x=50 ,y=150)


#Create Line
line = tkchart.Line(master=linechart,
                color="#cccccc",
                size=3)

displayed = 0
max_support = 50 #60-50
data = [0,100,200,300,400,500,600,700,800,900,1000]
start = (20,60)
def loop():
    global displayed
    global start
    linechart.show_data(data=[random.choice(data)], line=line)
    displayed+=1
    if displayed>40:
        start = (start[0]+1,start[1]+1)
        linechart.configure(x_data_min_max=((start[0],start[1])))
    root.after(250,loop)
#calling to loop
loop()

def place_forget():
    linechart.place_forget()
def place_back():
    linechart.place_back()
def hide_all(state:bool):
    linechart.hide_all(state)

tkinter.Button(text="place_foget", command=place_forget).place(x=100, y=600)
tkinter.Button(text="place_back", command=place_back).place(x=100, y=630)

tkinter.Button(text="hide_all(True)", command=lambda :hide_all(True) ).place(x=100, y=660)
tkinter.Button(text="hide_all(False)", command=lambda :hide_all(False) ).place(x=100, y=690)


root.mainloop()