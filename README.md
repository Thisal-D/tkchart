<img src="https://drive.google.com/uc?export=view&id=16Y00GIKEpmC4t3gAlUv7IJutE4yzFszo" style="margin-left: auto;margin-right: auto;display: block; max-width:100%">
<img src="https://drive.google.com/uc?export=view&id=1YqYcKm0ear9j2NB2BtOlWTvajubi6ZTH" style="margin-left: auto;margin-right: auto;display: block;  max-width:100%">

<hr>

# tkchart - 1.0.5
<hr>
<br>

#### you need to install package first
> pip install tkchart

#### you need to import package 
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
    ``x_data_min_max`` : touple(min:int ,max:int) <br>
    ``y_values_decimals`` : int<br>
    ``x_values_decimals`` : int<br>

    ``sections_color`` : str<br>
    ``y_values_color`` : str<br>
    ``x_values_color`` : str<br>
    ``y_data_text_color`` : str<br>
    ``x_data_text_color`` : str<br>
    ``bg_color`` : str<br>
    ``chart_color`` : str<br>
    ``bar_color`` : str<br>

    ``x_y_data_font`` : tuple<br>
    ``x_y_values_font`` : tuple<br>
    ``line_width_auto`` : bool<br>
    ``line_width`` : int<br>


- ##  Methods
    
    #### ``1. configure``: use to change LineChart attributes
    support **kwargs
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
    x_data_min_max 
    y_values_decimals
    x_values_decimals
    sections_color
    y_values_color
    x_values_color 
    y_data_text_color 
    x_data_text_color 
    bg_color
    chart_color 
    bar_color 
    x_y_data_font
    x_y_values_font
    line_width_auto
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

    #### ``6. place_forget`` : use to place forget the chart<br>
    #### ``7. pack_forget`` : use to pack forget the chart<br>
    #### ``8. grid_forget`` : use to grid forget the chart<br>
    #### ``9. place_back`` : use to place chart in the old location after place forget<br>
    #### ``10. pack_back`` : use to pack chart in the old location after pack forget<br>
    #### ``11. grid_back`` : use to grid chart in the old location after grid forget<br>
    #### ``12. hide_all`` : use to hide all the lines<br>
    support **kwargs
    ```
    state: Bool
    ```
    #### ``13. hide`` : use hide a specific line<br>
    support **kwargs
    ```
    line: tkchart.Line
    state: bool
    ```
    

```
linechart = tkchart.LineChart(master=root,
                            width=1000, 
                            height=600,
                            bar_size=5
                            )
```

![Example Image](https://drive.google.com/uc?export=view&id=10xbpwAUI5vNxfUMM9rUbd4B6va56Zmj6)




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

![Example Image](https://drive.google.com/uc?export=view&id=1jt8JeAIU9HqimmCsL-3sodXmjlNYhbYg)




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
                            x_data_min_max=(20,60),
                            y_data_max=1000,
                            x_values_decimals=4,
                            y_values_decimals=5,
                            )
```

![Example Image](https://drive.google.com/uc?export=view&id=1WOYWlDMJKIF5_HDzocOPdl6oQZJLuY0H)




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
                            x_data_min_max=(20,60),
                            y_data_max=1000,
                            x_values_decimals=4,
                            y_values_decimals=5,
                            
                            sections_color="#ffffff",
                            y_values_color="#ffffff",
                            x_values_color="#ffffff",
                            x_data_text_color="#00ffff",
                            y_data_text_color="#ff00ff",
                            bg_color="#202020",
                            chart_color="#101010",
                            bar_color="#909090"
                            )
```

![Example Image](https://drive.google.com/uc?export=view&id=11TMakOOD9XXbrRXGAdxscmPhEeRARXLz)


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
                            x_data_min_max=(20,60),
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
![Example Image](https://drive.google.com/uc?export=view&id=1ZvjEkmt_L-l2Pi1GzdmS9vuMujb1tLH5)



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

![Example Image](https://drive.google.com/uc?export=view&id=1zPR4mIfZmcP6zyA8Sd2JCmHdgbilv7Fe)



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

root.mainloop()
```
output:

https://github.com/Thisal-D/tkchart/assets/93121062/70d53841-86aa-48fa-9e89-6d2359d550a5



<br>
<br>

## For more details 

##  Pypi.org   :   <a href="https://pypi.org/project/tkchart/"><i>tkchart</i></a>

<br>
<br>

### Special thanks to <a href="https://github.com/childeyouyu" target="_blank">childeyouyu</a> for valuable ideas and support in the development of this project. 
