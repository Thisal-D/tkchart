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
                            axis_size=5,
                            
                            y_axis_section_count=5,
                            x_axis_section_count=5,
                            y_axis_label_count=5,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            
                            x_axis_values=[x for x in range(1,21)],
                            
                            y_axis_max_value=1000,
    
                            y_axis_precision=5,
                            
                            section_color="#707070",
                            y_axis_font_color="#bbbbbb",
                            x_axis_font_color="#bbbbbb",
                            x_axis_data_font_color="#00ff00",
                            y_axis_data_font_color="#00ff00",
                            bg_color="#202020",
                            fg_color="#101010",
                            axis_color="#cccccc",
                            
                            axis_font_style = ("Arial", 15,"bold"),
                            
                            )
#place LineChart
linechart.place(x=50 ,y=50)


#Create Line
line = tkchart.Line(master=linechart,
                color="#cccccc",
                size=3)


data = [0,100,200,300,400,500,600,700,800,900,1000]

def loop():
    global displayed
    linechart.show_data(data=[random.choice(data)], line=line)
    root.after(250,loop)
loop()

root.mainloop()