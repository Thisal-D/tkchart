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


# 1 . Create LineChart 
Create a LineChart

   

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
    ``y_values_color`` : str<br>
    ``x_values_color`` : str<br>
    ``y_data_color`` : str<br>
    ``x_data_color`` : str<br>
    ``bg_color`` : str<br>
    ``chart_color`` : str<br>
    ``bar_color`` : str<br>

    ``x_y_data_font`` : tuple<br>
    ``x_y_values_font`` : tuple<br>

    ``line_width`` : int<br>


- ##  Methods
    
    #### ``1. configure``: use to change LineChart attributes
    ```
    width 
    height 
    bar_size 
    y_sections_count 
    x_sections_count 
    y_labels_count 
    x_labels_count
    y_data 
    x_data 
    y_data_max 
    x_data_max 
    y_values_decimals
    x_values_decimals
    sections_color
    y_values_color
    x_values_color 
    y_data_color 
    x_data_color 
    bg_color
    chart_color 
    bar_color 
    x_y_data_font
    x_y_values_font
    line_width
    ```

    
    #### ``2. show_data`` : use to display data. <br>
    support **kwargs
    ```
    data
    line
    ```
    

    #### ``3. place`` : use to place <font color="red"> same as tkinter place method..!</font><br>
    support **kwargs
    ```
    x
    y
    rely
    relx
    anchor
    ```
    #### ``4. pack`` : use to pack. <font color="red"> same as tkinter pack method..! </font><br>
    support **kwargs
    ```
    pady
    padx
    before
    after
    side
    ipadx
    ipady
    ancho
    ```
    #### ``5. grid`` : use to grid. <font color="red"> same as tkinter grid method..! </font><br>
    support **kwargs
    ```
    column
    columnspan
    ipadx
    ipady
    padx
    pady
    row
    rowspan
    sticky
    ```
    

```
linechart = tkchart.LineChart(master=root,
                            width=1000, 
                            height=600,
                            bar_size=5
                            )
```

![1](https://github.com/Thisal-D/tkchart/assets/93121062/866228f8-1d2e-4486-9615-6383582c52ca)


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
![2](https://github.com/Thisal-D/tkchart/assets/93121062/203494d5-7a2a-4435-9f4d-02aa17782fbc)


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
![3](https://github.com/Thisal-D/tkchart/assets/93121062/f7789d90-250c-4c18-b1ee-dac2eb02ea89)


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
                            y_values_color="#ffffff",
                            x_values_color="#ffffff",
                            x_data_color="#00ffff",
                            y_data_color="#ff00ff",
                            bg_color="#202020",
                            chart_color="#101010",
                            bar_color="#909090"
                            )
```

![4](https://github.com/Thisal-D/tkchart/assets/93121062/2844b8d8-b76c-4a9b-8cf9-11220d12d8a5)

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
                            y_values_color="#bbbbbb",
                            x_values_color="#bbbbbb",
                            x_data_color="#00ffff",
                            y_data_color="#ff00ff",
                            bg_color="#202020",
                            chart_color="#101010",
                            bar_color="#cccccc",
                            
                            x_y_data_font = ("Arial", 15,"bold"),
                            x_y_values_font = ("Arial", 10,"bold")
                            )
```

![5](https://github.com/Thisal-D/tkchart/assets/93121062/48cb095a-199d-450d-b50b-26f8e1c7db50)


<br>
<br>

# 1 . Create Line 
Create a Line

   

### ``line = tkchart.Line()``

- ##  Attributes & Types

    ``master`` : tkchart.LineChart<br>
    ``color`` : str<br>
    ``size`` : int<br>


- ##  Methods
    
    #### ``1. configure``: use to change Line attributes
    ```
    size 
    color 
    ```
```
line = tkchart.Line(master=linechart,
                color="#ffff00",
                size=5)

```
![6](https://github.com/Thisal-D/tkchart/assets/93121062/b8d83e78-e98b-4bfa-8947-206bc53a892e)



`` line_width `` <font color="Red" >is not a attributes of Line. Its a attribute of LineChart object..! </font>


<br>
<br>

# 1 . Display Data
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


https://github.com/Thisal-D/tkchart/assets/93121062/10b569b0-1b4c-4a92-a000-de5d01c92607

