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
                            axis_size=5,
                            
                            y_axis_section_count=5,
                            x_axis_section_count=5,
                            y_axis_label_count=5,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=[x for x in range(20,60)],
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
                            
                            data_font_style = ("Arial", 15,"bold"),
                            axis_font_style = ("Arial", 10,"bold"),
                            )
#place LineChart
linechart.place(x=50 ,y=150)


#Create Line
line1 = tkchart.Line(master=linechart,
                color="#0000ff",
                size=3)
#Create Line
line2 = tkchart.Line(master=linechart,
                color="#00ff00",
                size=3)

displayed = 0
max_support = 50 #60-50
data = [0,100,200,300,400,500,600,700,800,900,1000]

def loop():
    linechart.show_data(data=[random.choice(data)], line=line1)
    linechart.show_data(data=[random.choice(data)], line=line2)
    root.after(250,loop)
#calling to loop
loop()



def place_forget():
    linechart.place_forget()
def place_back():
    linechart.place_back()
def hide_all(state:bool):
    linechart.hide_all(state)
    
def hide_line_1():
    linechart.hide(line=line1,state=True)
def show_line_1():
    linechart.hide(line=line1,state=False)

def hide_line_2():
    linechart.hide(line=line2,state=True)
def show_line_2():
    linechart.hide(line=line2,state=False)
    


tkinter.Button(text="place_foget", command=place_forget).place(x=100, y=600)
tkinter.Button(text="place_back", command=place_back).place(x=250, y=600)

tkinter.Button(text="hide_all(True)", command=lambda :hide_all(True) ).place(x=100, y=630)
tkinter.Button(text="hide_all(False)", command=lambda :hide_all(False) ).place(x=250, y=630)


tkinter.Button(text="hide line 1", command=hide_line_1) .place(x=100, y=660)
tkinter.Button(text="show line 1", command=show_line_1) .place(x=250, y=660)

tkinter.Button(text="hide line 2", command=hide_line_2).place(x=100, y=690)
tkinter.Button(text="show line 2", command=show_line_2).place(x=250, y=690)
root.mainloop()