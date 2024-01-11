import tkinter
import tkchart as tkchart
import random #for get random value

#create root 
root = tkinter.Tk()
root.minsize(1200,500)

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
                            x_data_max=60,
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
                            
                            line_width=100)
#place LineChart
linechart.place(x=50 ,y=50)


#Create Line
line = tkchart.Line(master=linechart,
                color="#cccccc",
                size=3)

data = [0,100,200,300,400,500,600,700,800,900,1000]
def loop():
    linechart.show_data(data=[random.choice(data)], line=line)
    root.after(250,loop)
#calling to loop
loop()

root.mainloop()
