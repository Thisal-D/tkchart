
<div align="center"><h1> tkchart</h1> </div>

<div align="center">
<img src="https://drive.google.com/uc?export=view&id=16Y00GIKEpmC4t3gAlUv7IJutE4yzFszo">
<img src="https://drive.google.com/uc?export=view&id=1kMVifs_1oLZPyQkX4mHGyPWThbqj8nNU">
</div>


### <li>tkchart Library is a Python library that simplifies the process of creating line charts in tkinter and customtkinter GUI applications.</li>

## Examples
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1F_elYaMgKzVMNLgDjBN6B7P4EX9X43YV"></div>


## tkchart - 1.0.6
<hr>
<br>

#### you need to install & import package first
> installation
>> pip install tkchart

> importing
>> import tkchart

## Mainly there are 2 objects. 
>  - LineChart 
>  - Line 

## To display data using LineChart you need to do 3 main tasks
> 1. Create LineChart
> 2. Create Line
> 3. Display data

<br>
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
    ``x_data_min_max`` : touple(min ,max) <br>
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
    y_data_color 
    x_data_color 
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
                            width=800, 
                            height=400,
                            bar_size=5
                        )
```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1BA-C3w22rGLmhMK-aMN9aprntyEytbSO"></div>
<br>
<br>

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            bar_size=5,
                            
                            
                            y_sections_count=5,
                            x_sections_count=5,
                            y_labels_count=5,
                            x_labels_count=5,
                        )
```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1eoJ64dn19Tqpwl5-rev_yW_N8rLMTTIM"></div>
<br>
<br>

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
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
                            y_values_decimals=5
                        )
```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1PzJiQgRmBPUJSdBPu57O9EJLvATt-BLb"></div>
<br>
<br>

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
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
                            
                            sections_color="#404040",
                            y_values_color="#707070",
                            x_values_color="#707070",
                            x_data_color="lightblue",
                            y_data_color="lightblue",
                            bg_color="#202020",
                            chart_color="#202020",
                            bar_color="#707070"
                            )
```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1bVgBSVc2SVkwY8B1yaJpoxq0tfv88GGU"></div>
<br>
<br>

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
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
                            
                            sections_color="#404040",
                            y_values_color="#707070",
                            x_values_color="#707070",
                            x_data_color="lightblue",
                            y_data_color="lightblue",
                            bg_color="#202020",
                            chart_color="#202020",
                            bar_color="#707070",
                            
                            x_y_data_font = ("Arial", 15,"bold"),
                            x_y_values_font = ("Arial", 10,"bold")
                            )
```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1we8KgY7vNk2i05pnDSpzxh7j0lnWyD4c"></div>
<br>
<br>
<br>
<br>

# 2 . Create Line 
Create a Line

### ``line = tkchart.Line()``

- ##  Attributes & Types

    ``master`` : tkchart.LineChart<br>
    ``color`` : str<br>
    ``size`` : int<br>
    ``mode`` : str<br>
    ``mode_style`` : tuple<br>


- ##  Methods
    
    #### ``1. configure``: use to change Line attributes
    ```
    size 
    color 
    mode
    mode_style
    ```
```
line = tkchart.Line(master=linechart,
                color="lightblue",
                size=2,
                mode="dash",
                mode_style=(4,10))

```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1_--eXTjWu5trc9gN_r1h3iq4mZtSZds6"></div>
<br>
<br>
<br>
<br>

# 3 . Display Data
```
import tkchart
import customtkinter


root = customtkinter.CTk()
root.geometry("1048x599+442+239")

linechart = tkchart.LineChart(master=root,
                            width=800, 
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
                            
                            sections_color="#404040",
                            y_values_color="#707070",
                            x_values_color="#707070",
                            x_data_color="lightblue",
                            y_data_color="lightblue",
                            bg_color="#202020",
                            chart_color="#202020",
                            bar_color="#707070",
                            
                            x_y_data_font = ("Arial", 15,"bold"),
                            x_y_values_font = ("Arial", 10,"bold")
                            )


linechart.pack(pady=100)


line = tkchart.Line(master=linechart,
                color="lightblue",
                size=2,
                mode="dash",
                mode_style=(4,10))


import random
data = [0,100,200,300,400,500,600,700,800,900,1000]
def loop():
    linechart.show_data(data=[random.choice(data)], line=line)
    root.after(250,loop)
#calling to loop
loop()
root.mainloop()
```
## output
### click to play
> [![Watch the video](https://drive.google.com/uc?export=view&id=1qufx4vqtCjsXwLvcZmbvqxSwJnZEldqZ)](https://drive.google.com/file/d/1qufx4vqtCjsXwLvcZmbvqxSwJnZEldqZ/view?usp=drive_link)


<br>
<br>
<br>
<br>


## Examples
>> 1. <div align="center"><img src="https://drive.google.com/uc?export=view&id=1_fLJaHHxNYf8Hviu_I7HKIst_l2m5_A0"></div>

> 2. <div align="center"><img src="https://drive.google.com/uc?export=view&id=1HoYA0oDPnEW6l7ALNTO8GwPzewXIutU-"></div>

> 3. <div align="center"><img src="https://drive.google.com/uc?export=view&id=1Q5Y8vw4Inh6Ne6WckfBDt_PRYpbgWpiI"></div>

> 4. <div align="center"><img src="https://drive.google.com/uc?export=view&id=10lmTzrQ29Tynx3zjZOHCyW3f5qXdjPMr"></div>

> 5. <div align="center"><img src="https://drive.google.com/uc?export=view&id=1tdo37nq3Hcv2roTOA80qsME9P185F7r1"></div>

> 6. <div align="center"><img src="https://drive.google.com/uc?export=view&id=1_vTP7DIsEdd4gU5hQOYeWF5FVYfilCvG"></div>





## go to GitHub
>  Github.com   :   <a href="https://github.com/Thisal-D/tkchart"><i>tkchart<i></a>