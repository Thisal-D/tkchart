<div align="center">

<img src="https://drive.google.com/thumbnail?id=16Y00GIKEpmC4t3gAlUv7IJutE4yzFszo&sz=w900">

[![Downloads](https://static.pepy.tech/badge/tkchart)](https://pepy.tech/project/tkchart)
[![Downloads](https://static.pepy.tech/badge/tkchart/month)](https://pepy.tech/project/tkchart)
[![Downloads](https://static.pepy.tech/badge/tkchart/week)](https://pepy.tech/project/tkchart)

<img src="https://drive.google.com/thumbnail?id=1kYb8ppvWYRFHWISKEHDmIaFaV91-uPPE&sz=w180">

<div align="center"> 
   
</div>
</div>


### <li>tkchart Library is a Python library that simplifies the process of creating line charts in tkinter and customtkinter GUI applications.</li>

## Examples
<div align="center"><img src="https://drive.google.com/thumbnail?id=1F_elYaMgKzVMNLgDjBN6B7P4EX9X43YV&sz=w900"></div> 

<br>
<br>

## tkchart - 1.3.9

### You need to install & import package first
* installation
    * ``` 
        pip install tkchart 
        ```

* importing
    * ```
        import tkchart
        ```

## objects
* LineChart 
* Line 

## To display data using LineChart you need to do 3 main tasks
1. Creating a LineChart
2. Creating a Line
3. Display of data
<br>
<br>


# 1 . Creating a LineChart
 
```
linechart = tkchart.LineChart()
```
- ##  Attributes & Types & Values
    ## Master Configuration
    - master : ``tkinter | customtkinter (Frame | Canvas | Tk)``

    ## Dimensions 
    - width : ``int``
    - height : ``int``
    - axis_size : ``int``
    - x_space : ``int``
    - y_space : ``int``
    - line_width : ``int | str``
        - "auto"
        - 10
    - pointer_size : ``int``

    ## Value Configuration
    - x_axis_section_count : ``int``
    - y_axis_section_count : ``int``
    - x_axis_label_count : ``int``
    - y_axis_label_count : ``int``
    - x_axis_display_values_indices : ``tuple[int, ...]``
    - x_axis_data : ``any``
    - y_axis_data : ``any``
    - x_axis_values : ``tuple(any, ...)`` 
        - ("2020 Year", "2021 Year", "2022 Year", "2023 Year", "2024 Year")
        - (0.1, 0.2, 0.3, 0.4, 0.5)
    - y_axis_values : ``tuple(int | float, int | float)``
        - (0 ,1000)
        - (-1000, 1000)
    - y_axis_precision : ``int``
    - pointing_values_precision : ``int``
    - ~~y_axis_max_value~~ : <span style="color:red; font-weight:bold">Deprecated</span>

    ## Color Configuration
    - bg_color : ``str``
    - fg_color : ``str``
    - axis_color : ``str``
    - x_axis_font_color : ``str``
        - "#ffffff"
        - "white"
    - y_axis_font_color : ``str``
    - x_axis_data_font_color : ``str``
    - y_axis_data_font_color : ``str``
    - y_axis_section_color : ``str``
    - x_axis_section_color : ``str``
    - pointer_color : ``str``
    - ~~section_color~~ : <span style="color:red; font-weight:bold">Deprecated</span>
    
    ## Font Configuration
    - data_font_style : ``tuple[str, int, str]``
        - ("arial", 10, "bold")
        - ("arial", 20, "normal")
    - axis_font_style : ``tuple``

    ## Style Configuration
    - x_axis_data_position : ``str``
        - "top"
        - "side"
    - y_axis_data_position : ``str``
    - x_axis_section_style : ``str``
        - "normal"
        - "dashed"
    - y_axis_section_style : ``str``
    - x_axis_section_style_type : ``tuple(int, int)``
        - (50, 10)
        - (10, 10)
    - y_axis_section_style_type : ``tuple(int, int)``

    ## Data Retrieval Configuration
    - pointing_callback_function : ``function``
        - function_name(*args)
        - function_name(x ,y)
    - pointer_state : ``str``
        - "enabled"
        - "disabled"
    - pointer_lock : ``str``
        - "enabled"
        - "disabled"
    
    ## Recent Changes
    -  ~~y_axis_max_value : ``int | float``~~ <span style="color:red; font-weight:bold">Deprecated</span>
        - replaced with y_axis_values : ``tuple(int | float, int | float)``

            **_The y_axis_values parameter is a tuple where the value at index 0 represents the starting value of the Y-axis, and the value at index 1 represents the ending value of the Y-axis._**

    - ~~section_color : ``str``~~ <span style="color:red; font-weight:bold">Deprecated</span>
        - replaced with x_axis_section_color : ``str``
        - replaced with y_axis_section_color : ``str``

- ##  Methods

    - ### configure : ``use to change LineChart attributes``
        Support parameters
        - width 
        - height 
        - axis_size 
        - x_space 
        - y_space 
        - line_width 
        - pointer_size
        - x_axis_section_count 
        - y_axis_section_count 
        - x_axis_label_count
        - y_axis_label_count 
        - x_axis_display_values_indices 
        - x_axis_data 
        - y_axis_data 
        - x_axis_values 
        - y_axis_values 
        - y_axis_precision 
        - pointing_values_precision
        - bg_color 
        - fg_color
        - axis_color
        - x_axis_font_color 
        - y_axis_font_color 
        - x_axis_data_font_color 
        - y_axis_data_font_color
        - y_axis_section_color 
        - x_axis_section_color 
        - pointer_color
        - data_font_style 
        - axis_font_style
        - x_axis_data_position 
        - y_axis_data_position 
        - x_axis_section_style 
        - y_axis_section_style
        - x_axis_section_style_type 
        - y_axis_section_style_type 
        - pointing_callback_function
        - pointer_state 
        - pointer_lock 
        - ~~y_axis_max_value~~ : <span style="color:red; font-weight:bold">Removed</span>
        - ~~section_color~~ : <span style="color:red; font-weight:bold">Removed</span>
    

        
    - ### show_data : ``use to display data``
        Support parameters
        - data : ``tuple``
        - line : ``tkchart.Line``
       
    - ### place : ``use to place LineChart``
        Support parameters
        - x
        - y
        - rely
        - relx
        - anchor
       
    - ### pack : ``use to pack LineChart``
        Support parameters
        - pady
        - padx
        - before
        - after
        - side
        - anchor
        
    - ### grid : ``use to grid LineChart``
        Support parameters
        - column
        - columnspan
        - padx
        - pady
        - row
        - rowspan
        - sticky

    - ### place_forget : ``use to place forget the chart``
    - ### pack_forget : ``use to pack forget the chart``
    - ### grid_forget : ``use to grid forget the chart``
    - ### place_back : ``use to place chart in the old location after place forget``
    - ### pack_back : ``use to pack chart in the old location after pack forget``
    - ### grid_back : ``use to grid chart in the old location after grid forget``
    - ### hide_all : ``use to hide all the lines``
        Support parameters
        - state : ``bool``
        
    - ### hide : ``use to hide a specific line``
        Support parameters
        - line : ``tkchart.Line``
        - state : ``bool``
    - ### reset : ``use to reset chart``

    
```
linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5
                        )
```

<div align="center"><img src="https://drive.google.com/thumbnail?id=1UnGHJ-tLrki3HegDs7WM1TVUIkMAbWVS&sz=w900"></div> 
<br>
<br>

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5,
                            
                            y_axis_section_count=5,
                            x_axis_section_count=5,
                            y_axis_label_count=5,
                        )
```
<div align="center"><img src="https://drive.google.com/thumbnail?id=1FPzXc0NVyY50TOKIbBC_bXellnVUTY6l&sz=w900"></div> 
<br>
<br>

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5,
                            
                            y_axis_section_count=5,
                            x_axis_section_count=5,
                            y_axis_label_count=5,
                            x_axis_label_count=10,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                            y_axis__max_value=(0, 1000),
                            y_axis_precision=5
                        )
```
<div align="center"><img src="https://drive.google.com/thumbnail?id=1F8fZdWwA4q-f3cL3Oejvey0rU0yEBF6j&sz=w900"></div> 
<br>
<br>

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5,
                            
                            y_axis_section_count=5,
                            x_axis_section_count=5,
                            y_axis_label_count=5,
                            x_axis_label_count=10,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                            y_axis__max_value=(0, 1000),
                            y_axis_precision=5
                            
                            x_axis_section_color="#404040",
                            y_axis_section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070"
                        )
```
<div align="center"><img src="https://drive.google.com/thumbnail?id=1A1FAprrNkbWjZAyaoL3NvdPu5RASIq5Q&sz=w900"></div> 
<br>
<br>

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5,
                            
                            y_axis_section_count=5,
                            x_axis_section_count=5,
                            y_axis_label_count=5,
                            x_axis_label_count=10,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                            y_axis__max_value=(0, 1000),
                            y_axis_precision=5
                            
                            x_axis_section_color="#404040",
                            y_axis_section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070"
                            
                            data_font_style=("Arial", 15, "bold"),
                            axis_font_style=("Arial", 10, "bold")
                        )
```
<div align="center"><img src="https://drive.google.com/thumbnail?id=1qIk805dmi9wpBUSv2UmnD7gQFSQB5RPF&sz=w900"></div> 
<br>
<br>

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5,
                            
                            y_axis_section_count=5,
                            x_axis_section_count=5,
                            y_axis_label_count=5,
                            x_axis_label_count=10,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                            y_axis__max_value=(0, 1000),
                            y_axis_precision=5
                            
                            x_axis_section_color="#404040",
                            y_axis_section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070"
                            
                            data_font_style=("Arial", 15, "bold"),
                            axis_font_style=("Arial", 10, "bold"),
                            
                            x_space=20,
                            y_space=20
                        )
```
<div align="center"><img src="https://drive.google.com/thumbnail?id=1W8P7wXlNLymaE0sexSSfltv0fX5t7XXD&sz=w900"></div> 
<br>
<br>

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5,
                            
                            y_axis_section_count=5,
                            x_axis_section_count=5,
                            y_axis_label_count=5,
                            x_axis_label_count=10,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                            y_axis__max_value=(0, 1000),
                            y_axis_precision=5
                            
                            x_axis_section_color="#404040",
                            y_axis_section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070"
                            
                            data_font_style=("Arial", 15, "bold"),
                            axis_font_style=("Arial", 10, "bold"),
                            
                            x_space=20,
                            y_space=20,
                            
                            x_axis_data_position="side",
                            y_axis_data_position="side"
                        )

linechart.pack()
```
<div align="center"><img src="https://drive.google.com/thumbnail?id=1kNoJalW6aLx79wxcmrUaAS_D8XsldL3h&sz=w900"></div> 


<br>
<hr>
<br>

# 2 . Creating a Line

```
line = tkchart.Line()
```

- ##  Attributes & Types & Values
    - master : ``tkchart.LineChart``
    - color : ``str``
        - "white"
        - "#10f0f0"
    - size : ``int``
    - style : ``str``
        - "normal"
        - "dashed"
        - "dotted"
    - style_type : ``tuple(int, int)``
        - (5,10)
        - (10,5)


- ##  Methods
    - #### configure : ``use to change Line attributes``
        Support parameters
        - size 
        - color 
        - style
        - style_type

```
line = tkchart.Line(master=linechart,
                color="lightblue",
                size=2,
                style="dashed",
                style_type=(4,10))

```
<div align="center"><img src="https://drive.google.com/thumbnail?id=1PDKdRPfjhzUkAlY-ktFhE70MsYCKeFn5&sz=w900"></div> 

<br>
<hr>
<br>

# 3 . Display of Data
```
import customtkinter 
import tkchart
import random

root = customtkinter.CTk()

linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5,
                            
                            y_axis_section_count=5,
                            x_axis_section_count=5,
                            y_axis_label_count=5,
                            x_axis_label_count=10,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                            y_axis_values=(0, 1000),
                            y_axis_precision=5,
                            
                            x_axis_section_color="#404040",
                            y_axis_section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070",
                            
                            data_font_style=("Arial", 15, "bold"),
                            axis_font_style=("Arial", 10, "bold"),
                            
                            x_space=20,
                            y_space=20,
                            
                            x_axis_data_position="side",
                            y_axis_data_position="side"
                        )
linechart.pack()


line = tkchart.Line(master=linechart,
                    color="lightblue",
                    size=2,
                    style="dashed",
                    style_type=(4, 10))

data = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
def loop():
    linechart.show_data(data=tuple([random.choice(data)]), line=line)
    root.after(250, loop)
loop()

root.mainloop()
```

<div align="center">

https://github.com/Thisal-D/tkchart/assets/93121062/ec29a3f4-7eba-40c5-9f5c-cc7071ff40ff

</div>

<br>
<hr>
<br>

### Examples
- <div align="center"><img src="https://drive.google.com/thumbnail?id=1_fLJaHHxNYf8Hviu_I7HKIst_l2m5_A0&sz=w900"></div> 

- <div align="center"><img src="https://drive.google.com/thumbnail?id=1HoYA0oDPnEW6l7ALNTO8GwPzewXIutU-&sz=w900"></div> 

- <div align="center"><img src="https://drive.google.com/thumbnail?id=1Q5Y8vw4Inh6Ne6WckfBDt_PRYpbgWpiI&sz=w900"></div> 

- <div align="center"><img src="https://drive.google.com/thumbnail?id=10lmTzrQ29Tynx3zjZOHCyW3f5qXdjPMr&sz=w900"></div> 

- <div align="center"><img src="https://drive.google.com/thumbnail?id=1tdo37nq3Hcv2roTOA80qsME9P185F7r1&sz=w900"></div> 

- <div align="center"><img src="https://drive.google.com/thumbnail?id=1_vTP7DIsEdd4gU5hQOYeWF5FVYfilCvG&sz=w900"></div> 

<br>
<hr>
<br>

### go to PyPi
- # PyPi.org   :   <a href="https://pypi.org/project/tkchart" target="_blank" ><i>tkchart</i></a>

### go to GitHub
- # GitHub.com   :  <a href="https://github.com/Thisal-D/tkchart" target="_blank" ><i>tkchart</i></a>