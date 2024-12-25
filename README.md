
<div align="center"><h1> tkchart </h1> </div>

<div align="center">
<img src="https://drive.google.com/uc?export=view&id=16Y00GIKEpmC4t3gAlUv7IJutE4yzFszo">
<img src="https://drive.google.com/uc?export=view&id=1kMVifs_1oLZPyQkX4mHGyPWThbqj8nNU">
</div>


### <li>tkchart Library is a Python library that simplifies the process of creating line charts in tkinter and customtkinter GUI applications.</li>

## Examples
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1F_elYaMgKzVMNLgDjBN6B7P4EX9X43YV"></div>

<br>
<br>

## tkchart - 1.2.0

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

# 1 . Creating a LineChart
 
```
linechart = tkchart.LineChart()
```
- ##  Attributes & Types & Values
    - master : ``tkinter | customtkinter (Frame | Canvas | Tk)``
    - width : ``int``
    - height : ``int``
    - axis_size : ``int``
    - y_axis_section_count : ``int``
    - x_axis_section_count : ``int``
    - y_axis_label_count : ``int``
    - y_axis_data : ``str | int | float``
    - x_axis_data : ``str | int | float``
    - y_axis_max_value : ``int | float``
    - x_axis_values : ``List(str | float| str)`` 
        - ["2020 Year", "2021 Year", "2022 Year", "2023 Year", "2024 Year"]
    - y_axis_precision : ``int``
    - section_color : ``str``
        - "#ffffff"
        - "white"
    - y_axis_font_color : ``str``
    - x_axis_font_color : ``str``
    - y_axis_data_font_color : ``str``
    - x_axis_data_font_color : ``str``
    - bg_color : ``str``
    - fg_color : ``str``
    - axis_color : ``str``
    - data_font_style : ``tuple``
        - ("arial",10,"bold")
        - ("arial",20,"normal")
    - axis_font_style : ``tuple``
    - line_width : ``int | str``
    - y_space : ``int``
    - x_space : ``int``
    - x_axis_data_position : ``str``
        - "top"
        - "side"
    - y_axis_data_position : ``str``
        - "top"
        - "side"

- ##  Methods
    
    - ### configure : ``use to change LineChart attributes``
        Support parameters
        - height
        - axis_size
        - y_axis_section_count
        - x_axis_section_count
        - y_axis_label_count
        - y_axis_data
        - x_axis_data
        - y_axis_max_value
        - x_axis_values
        - y_axis_precision
        - section_color
        - y_axis_font_color
        - x_axis_font_color
        - y_axis_data_font_color
        - x_axis_data_font_color
        - bg_color
        - fg_color
        - axis_color
        - data_font_style
        - axis_font_style
        - line_width
        - y_space
        - x_space
        - x_axis_data_position
        - y_axis_data_position
    
    - ### show_data : ``use to display data``
        Support parameters
        - data : ``int``
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
        - ancho
        
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
        
    - ### hide : ``use hide a specific line``
        Support parameters
        - line : ``tkchart.Line``
        - state : ``bool``

    

```
linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5
                        )
```

<div align="center"><img src="https://drive.google.com/uc?export=view&id=1UnGHJ-tLrki3HegDs7WM1TVUIkMAbWVS"></div>
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
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1FPzXc0NVyY50TOKIbBC_bXellnVUTY6l"></div>
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
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=[1,2,3,4,5,6,7,8,9,10],
                            y_axis_max_value=1000,
                            y_axis_precision=5
                        )
```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1F8fZdWwA4q-f3cL3Oejvey0rU0yEBF6j"></div>
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
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=[1,2,3,4,5,6,7,8,9,10],
                            y_axis_max_value=1000,
                            y_axis_precision=5,
                            
                            section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070"
                        )
```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1A1FAprrNkbWjZAyaoL3NvdPu5RASIq5Q"></div>
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
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=[1,2,3,4,5,6,7,8,9,10],
                            y_axis_max_value=1000,
                            y_axis_precision=5,
                            
                            section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070",
                            
                            data_font_style=("Arial", 15,"bold"),
                            axis_font_style=("Arial", 10,"bold")
                        )
```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1qIk805dmi9wpBUSv2UmnD7gQFSQB5RPF"></div>
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
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=[1,2,3,4,5,6,7,8,9,10],
                            y_axis_max_value=1000,
                            y_axis_precision=5,
                            
                            section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070",
                            
                            data_font_style=("Arial", 15,"bold"),
                            axis_font_style=("Arial", 10,"bold"),
                            
                            x_space=20,
                            y_space=20
                        )
```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1W8P7wXlNLymaE0sexSSfltv0fX5t7XXD"></div>
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
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=[1,2,3,4,5,6,7,8,9,10],
                            y_axis_max_value=1000,
                            y_axis_precision=5,
                            
                            section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070",
                            
                            data_font_style=("Arial", 15,"bold"),
                            axis_font_style=("Arial", 10,"bold"),
                            
                            x_space=20,
                            y_space=20,
                            
                            x_axis_data_position="side",
                            y_axis_data_position="size"
                        )

linechart.pack()
```
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1kNoJalW6aLx79wxcmrUaAS_D8XsldL3h"></div>


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
        - "line"
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
<div align="center"><img src="https://drive.google.com/uc?export=view&id=1PDKdRPfjhzUkAlY-ktFhE70MsYCKeFn5"></div>

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
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=[1,2,3,4,5,6,7,8,9,10],
                            y_axis_max_value=1000,
                            y_axis_precision=5,
                            
                            section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070",
                            
                            data_font_style=("Arial", 15,"bold"),
                            axis_font_style=("Arial", 10,"bold"),
                            
                            x_space=20,
                            y_space=20,
                            
                            x_axis_data_position="side",
                            y_axis_data_position="size"
                        )
linechart.pack()


line = tkchart.Line(master=linechart,
                color="lightblue",
                size=2,
                style="dashed",
                style_type=(4,10))

data = [0,100,200,300,400,500,600,700,800,900,1000]
def loop():
    linechart.show_data(data=[random.choice(data)], line=line)
    root.after(250,loop)
loop()

root.mainloop()
```

<div align="center">

#### Click to play

[![Watch the video](https://drive.google.com/uc?export=view&id=1PDKdRPfjhzUkAlY-ktFhE70MsYCKeFn5)](https://drive.google.com/file/d/1MYVyu8rRSJ9febuF5vikNpCs_WZxVxKi/view?usp=drive_link)

</div>

<br>
<hr>
<br>

### Examples
- <div align="center"><img src="https://drive.google.com/uc?export=view&id=1_fLJaHHxNYf8Hviu_I7HKIst_l2m5_A0"></div>

- <div align="center"><img src="https://drive.google.com/uc?export=view&id=1HoYA0oDPnEW6l7ALNTO8GwPzewXIutU-"></div>

- <div align="center"><img src="https://drive.google.com/uc?export=view&id=1Q5Y8vw4Inh6Ne6WckfBDt_PRYpbgWpiI"></div>

- <div align="center"><img src="https://drive.google.com/uc?export=view&id=10lmTzrQ29Tynx3zjZOHCyW3f5qXdjPMr"></div>

- <div align="center"><img src="https://drive.google.com/uc?export=view&id=1tdo37nq3Hcv2roTOA80qsME9P185F7r1"></div>

- <div align="center"><img src="https://drive.google.com/uc?export=view&id=1_vTP7DIsEdd4gU5hQOYeWF5FVYfilCvG"></div>

<br>
<hr>
<br>

### go to GitHub
- #  GitHub.com   :   <a href="https://github.com/Thisal-D/tkchart"><i>tkchart<i></a>