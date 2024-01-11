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

![1](https://github.com/Thisal-D/tkchart/assets/93121062/9c68422b-c3fd-4d0c-84e2-41ce23e84849)


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
![2](https://github.com/Thisal-D/tkchart/assets/93121062/5be7c60a-aa7c-4cad-8985-ab0c93d7855a)


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
![3](https://github.com/Thisal-D/tkchart/assets/93121062/1413e734-f980-4f21-92db-14f080c571e3)

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
![4](https://github.com/Thisal-D/tkchart/assets/93121062/c854c38a-cab6-4c77-a02a-2b8482b2cb41)


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

![5](https://github.com/Thisal-D/tkchart/assets/93121062/8d9866c9-362e-4b5e-96bf-d923993b1ee4)



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
![6](https://github.com/Thisal-D/tkchart/assets/93121062/25f73428-2071-4826-9961-b8e78808f698)



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



    


    


    

    
