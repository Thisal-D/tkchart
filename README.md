# tkchart
<hr>
<br>

#### you need to import package first

> import tkchart

## Mainly there are 2 objects. 
>  - LineChart 
>  - Line 

## To display data using LineChart you need to do 3 main tasks
> 1. Create LineChart
> 2. Create Line
> 3. Display data
<br>


- ## 1 . Create LineChart 
    - Create a LineChart

   

    ### ``linechart = tkchart.LineChart()``

    - ##  Attributes & Types
    
    ``master`` : tkinter.widget (Frame, Canvas, Tk)<br>
    ``width`` : int<br>
    ``height`` : int<br>
    ``bar_size`` : int<br>

    ``y_sections_count`` : int<br>
    ``x_sections_count`` : int<br>
    ``y_labels_count`` : int<br>
    ``x_labels_count`` : int<br>
    
    ``y_data`` : str ,int, float<br>
    ``x_data`` : str ,int, float<br>
    ``y_data_max`` : int ,float<br>
    ``x_data_max`` : int ,float<br>
    ``y_values_decimals`` : int<br>
    ``x_values_decimals`` : int<br>

    ``sections_color`` : str<br>
    ``y_values_text_color`` : str<br>
    ``x_values_text_color`` : str<br>
    ``y_data_text_color`` : str<br>
    ``x_data_text_color`` : str<br>
    ``bg_color`` : str<br>
    ``chart_color`` : str<br>
    ``bar_color`` : str<br>
    
    ``x_y_data_font`` : tuple<br>
    ``x_y_values_font`` : tuple<br>

    ``line_width`` : int<br>

    

```
linechart = tkchart.LineChart(master=root,
                            width=1000, 
                            height=600,
                            bar_size=5
                            )
```

<img src="1.png">

```
linechart = tkchart.LineChart(master=root, 
                            width=1000, 
                            height=600,
                            bar_size=5,

                            y_sections_count=5,
                            x_sections_count=5,
                            y_labels_count=5,
                            x_labels_count=5
                            )
```
<img src="2.png">

```
linechart = tkchart.LineChart(master=root, width=1000, 
                            height=600,
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
                            )
```
<img src="3.png">

```

linechart = tkchart.LineChart(master=root, width=1000, 
                            height=600,
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
                            
                            sections_color="#ffffff",
                            y_values_text_color="#ffffff",
                            x_values_text_color="#ffffff",
                            x_data_text_color="#00ffff",
                            y_data_text_color="#ff00ff",
                            bg_color="#202020",
                            chart_color="#101010",
                            bar_color="#909090"
                            )
```
<img src="4.png">

```

linechart = tkchart.LineChart(master=root, 
                            width=1000, 
                            height=600,
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
                            
                            sections_color="#505050",
                            y_values_text_color="#bbbbbb",
                            x_values_text_color="#bbbbbb",
                            x_data_color="#00ffff",
                            y_data_color="#ff00ff",
                            bg_color="#202020",
                            chart_color="#101010",
                            bar_color="#cccccc",
                            
                            x_y_data_font = ("Arial", 15,"bold"),
                            x_y_values_font = ("Arial", 10,"bold")
                            )
```

<img src="5.png">


- ## 1 . Create Line 
    - Create a Line

   

    ### ``line = tkchart.Line()``

    - ##  Attributes & Types
    
    ``master`` : tkchart.LineChart<br>
    ``color`` : str<br>
    ``size`` : int<br>

```
line = tkchart.Line(master=linechart,
                color="#ffff00",
                size=5)

```
<img src="6.png">


`` line_width `` <font color="Red" >is not a attributes of Line. Its a attribute of LineChart object..! </font>


- ## 1 . Display Data
```
import tkinter
import tkchart
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
                            y_values_text_color="#bbbbbb",
                            x_values_text_color="#bbbbbb",
                            x_data_color="#00ff00",
                            y_data_color="#00ff00",
                            bg_color="#202020",
                            chart_color="#101010",
                            bar_color="#cccccc",
                            
                            x_y_data_font = ("Arial", 15,"bold"),
                            x_y_values_font = ("Arial", 10,"bold"),
                            
                            line_width=100)
#place LineChart
linechart.place(x=0 ,y=0)


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
```



    


    


    

    