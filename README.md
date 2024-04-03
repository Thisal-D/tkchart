🌟**If you find this project helpful, your support by starring it would mean a lot! Your feedback motivates me to keep refining and enhancing it further.** 🚀

Your support means a lot and inspires me to do better with each update. Thank you for taking the time to check out this project!🥰

<div align="center">

[![tkchart](https://snyk.io/advisor/python/tkchart/badge.svg)](https://snyk.io/advisor/python/tkchart)

<img src="https://drive.google.com/thumbnail?id=16Y00GIKEpmC4t3gAlUv7IJutE4yzFszo&sz=w2500" style="width: 100%">

[![Downloads](https://static.pepy.tech/badge/tkchart)](https://pepy.tech/project/tkchart) [![Downloads](https://static.pepy.tech/badge/tkchart/month)](https://pepy.tech/project/tkchart) [![Downloads](https://static.pepy.tech/badge/tkchart/week)](https://pepy.tech/project/tkchart)

<img src="https://drive.google.com/thumbnail?id=1cHrsFILHJ7a2bgMXvk-PWlnLZx1vCnVR&sz=w180">


</div>

**<li>tkchart is a Python library for creating live updating line charts in tkinter.</li>**

</div>

<hr>

### Features

- **Live Update**: Display live data with line charts.
- **Multiple Lines**: Support for plotting multiple lines on the same chart for easy comparison.
- **Color Customization**: Customize colors to match your application's design or data representation.
- **Font Customization**: Adjust fonts for text elements to enhance readability.
- **Dimension Customization**: Customize chart dimensions to fit various display sizes and layouts.

<hr>

### Importing & Installation
* **Installation**
    ```
    pip install tkchart
    ```

* **Importing**
    ```
    import tkchart
    ```

<hr>

### Simple Guide
- **import package**
    ```
    import tkchart
    ```

- **Create Line Chart and place the chart**
    ```
    chart = tkchart.LineChart(master=root,
                                x_axis_values=("a", "b", "c", "d", "e", "f"),
                                y_axis_values=(100, 900))
    chart.place(x=10, y=10)
    ```

- **Create Line**
    ```
    line = tkchart.Line(master=chart)
    ```

- **Display Data**
    display data using a loop
    ```

    def loop():
        while True:
            random_data = random.choice(range(100, 900))
            chart.show_data(line=line, data=[random_data])
            time.sleep(1)
    
    #call the loop as thead
    theading.Thread(target=loop).start()
    ```

<hr>

### Links

- **Documentation :** [Documents](documentation)
    - [English doc.](documentation/DOCUMENTATION_EN.md)
    - [Chinese doc.](documentation/DOCUMENTATION_CN.md)
- **Python official :** [tkchart](https://pypi.org/project/tkchart/)

<hr>

### What You Can Accomplish

- **Simple**

    https://github.com/Thisal-D/ctkchart/assets/93121062/6f1e844f-d51c-467a-a3dc-ee03fea78fc9
    
    ```
    import tkinter as tk  # Importing the tkinter library as tk
    import tkchart  # Importing the tkchart module for chart creation
    import random  # Importing the random module for generating random data
    import threading  # Importing the threading module for running tasks concurrently
    import time  # Importing the time module for adding delays

    # Create the root window and configure
    root = tk.Tk()
    root.configure(bg="#0d1117")
    root.geometry("720x430+200+200")  

    # Create a line chart widget
    line_chart = tkchart.LineChart(
        master=root,  # Set the master as the root window
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X-axis values
        y_axis_values=(0, 1000)  # Y-axis values (range)
    )

    line_chart.pack(pady=15)  # Pack the line chart widget into the root

    # Create a line for the line chart
    line = tkchart.Line(master=line_chart)  # Set the master as the line chart

    def display_data():
        """Function to continuously display random data on the line chart."""
        while True:
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line, data=random_data)  # Display the random data on the line chart
            time.sleep(0.5)  # Pause for 0.5 seconds before the next iteration

    # Call the display_data function as a separate thread
    threading.Thread(target=display_data).start()


    # Start the main event loop
    root.mainloop()
    ```
    <hr>

- **Simple style**

    https://github.com/Thisal-D/ctkchart/assets/93121062/afe56452-68c3-44f0-9c67-2ab6f6910f6e
    
    ```
    import tkinter as tk  # Importing the tkinter library as tk
    import tkchart  # Importing the tkchart module for chart creation
    import random  # Importing the random module for generating random data
    import threading  # Importing the threading module for running tasks concurrently
    import time  # Importing the time module for adding delays

    # Create the root window and configure
    root = tk.Tk()
    root.configure(bg="#0d1117")
    root.geometry("720x430+200+200")  

    # Create a line chart widget
    line_chart = tkchart.LineChart(
        master=root,  # Set the master as the root window
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X-axis values
        y_axis_values=(0, 1000),  # Y-axis values (range)
        
        y_axis_label_count=10, # set y axis labels count to 10
    )

    line_chart.pack(pady=15)  # Pack the line chart widget into the root

    # Create a line for the line chart
    line = tkchart.Line(
        master=line_chart,  # Set the master as the line chart
        
        size=2,  # Set the line size to 2
        fill="enabled" # enable line fill
    )  

    def display_data():
        """Function to continuously display random data on the line chart."""
        while True:
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line, data=random_data)  # Display the random data on the line chart
            time.sleep(0.5)  # Pause for 0.5 seconds before the next iteration

    # Call the display_data function as a separate thread
    threading.Thread(target=display_data).start()


    # Start the main event loop
    root.mainloop()
    ```
    <hr>

- **2 lines with different line styles**

    https://github.com/Thisal-D/ctkchart/assets/93121062/9bc35a39-a8ca-4942-9fc7-a1c89d1bd1bc
    
    ```
    import tkinter as tk  # Importing the tkinter library as tk
    import tkchart  # Importing the tkchart module for chart creation
    import random  # Importing the random module for generating random data
    import threading  # Importing the threading module for running tasks concurrently
    import time  # Importing the time module for adding delays

    # Create the root window and configure
    root = tk.Tk()
    root.configure(bg="#0d1117")
    root.geometry("720x430+200+200")  

    # Create a line chart widget
    line_chart = tkchart.LineChart(
        master=root,  # Set the master as the root window
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X-axis values
        y_axis_values=(0, 1000),  # Y-axis values (range)
        
        y_axis_label_count=10, # set y axis labels count to 10
    )

    line_chart.pack(pady=15)  # Pack the line chart widget into the root



    line1 = tkchart.Line(
        master=line_chart,  # Set the master as the line chart
        
        color="#5dffb6", # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        style="dashed", # style change to dashed
        style_type=(10, 5), #index 0 for dash width and 1 for space between dashes
    ) 

    line2 = tkchart.Line(
        master=line_chart,  # Set the master as the line chart

        color="#FFBAD2", # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        point_highlight="enabled", # enable point highlight
        point_highlight_color="#FFBAD2", # enable point highlight
    )  

    def display_data():
        """Function to continuously display random data on the line chart."""
        while True:
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line1, data=random_data)  # Display the random data on the line 1 on chart
            
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line2, data=random_data)  # Display the random data on the line 2 on chart    
        
            time.sleep(0.5)  # Pause for 0.5 seconds before the next iteration

    # Call the display_data function as a separate thread
    threading.Thread(target=display_data).start()

    # Start the main event loop
    root.mainloop()
    ```

    <hr>

- **3 lines with different line styles**

    https://github.com/Thisal-D/ctkchart/assets/93121062/6d568b70-2ceb-42d0-b93c-0096f2745134
    
    ```
    import tkinter as tk  # Importing the tkinter library as tk
    import tkchart  # Importing the tkchart module for chart creation
    import random  # Importing the random module for generating random data
    import threading  # Importing the threading module for running tasks concurrently
    import time  # Importing the time module for adding delays

    # Create the root window and configure
    root = tk.Tk()
    root.configure(bg="#0d1117")
    root.geometry("720x430+200+200")  

    # Create a line chart widget
    line_chart = tkchart.LineChart(
        master=root,  # Set the master as the root window
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X-axis values
        y_axis_values=(0, 1000),  # Y-axis values (range)
        
        y_axis_label_count=10, # set y axis labels count to 10
    )

    line_chart.pack(pady=15)  # Pack the line chart widget into the root

    # Create a line 1 for the line chart
    line1 = tkchart.Line(
        master=line_chart,  # Set the master as the line chart
        
        size=2,  # Set the line size to 2
        fill="enabled" # enable line fill
    )  

    line2 = tkchart.Line(
        master=line_chart,  # Set the master as the line chart
        
        color="#5dffb6", # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        style="dashed", # style change to dashed
        style_type=(10, 5), #index 0 for dash width and 1 for space between dashes
    ) 

    line3 = tkchart.Line(
        master=line_chart,  # Set the master as the line chart

        color="#FFBAD2", # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        point_highlight="enabled", # enable point highlight
        point_highlight_color="#FFBAD2", # enable point highlight
        
    )  

    def display_data():
        """Function to continuously display random data on the line chart."""
        while True:
            random_data = random.choices(range(0, 1000),k=1)  # Generate random data between 0 and 1000
            line_chart.show_data(line=line1, data=random_data)  # Display the random data on the line 1 on chart
            
            random_data = random.choices(range(0, 1000),k=1) # Generate random data between 0 and 1000
            line_chart.show_data(line=line2, data=random_data)  # Display the random data on the line 2 on chart
            
            random_data = random.choices(range(0, 1000),k=1) # Generate random data between 0 and 1000
            line_chart.show_data(line=line3, data=random_data)  # Display the random data on the line 3 on chart
            
        
            time.sleep(0.5)  # Pause for 0.5 seconds before the next iteration

    # Call the display_data function as a separate thread
    threading.Thread(target=display_data).start()


    # Start the main event loop
    root.mainloop()
    ```

    <hr>

- **Advance** (Actually not, Just Two More Attributes Added)
 
    https://github.com/Thisal-D/ctkchart/assets/93121062/c2838fd6-3a0f-45be-bb39-9953d007067d
    
    ```
    import tkinter as tk  # Importing the tkinter library as tk
    import tkchart  # Importing the tkchart module for chart creation
    import random  # Importing the random module for generating random data
    import threading  # Importing the threading module for running tasks concurrently
    import time  # Importing the time module for adding delays

    # Create the root window and configure
    root = tk.Tk()
    root.configure(bg = "#0d1117")
    root.geometry("720x430+200+200")  

    # Create a line chart widget
    line_chart = tkchart.LineChart(
        master=root,  # Set the master as the root window
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X-axis values
        y_axis_values=(0, 1000),  # Y-axis values (range)
        
        y_axis_label_count=10, # set y axis labels count to 1
        y_axis_section_count=10,
        x_axis_section_count=10,
    )

    line_chart.pack(pady=15)  # Pack the line chart widget into the root


    line1 = tkchart.Line(
        master=line_chart,  # Set the master as the line chart
        
        color="#5dffb6", # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        style="dashed", # style change to dashed
        style_type=(10, 5), #index 0 for dash width and 1 for space between dashes
    ) 

    line2 = tkchart.Line(
        master=line_chart,  # Set the master as the line chart

        color="#FFBAD2", # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        point_highlight="enabled", # enable point highlight
        point_highlight_color="#FFBAD2", # enable point highlight
    )  

    def display_data():
        """Function to continuously display random data on the line chart."""
        while True:
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line1, data=random_data)  # Display the random data on the line 1 on chart
            
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line2, data=random_data)  # Display the random data on the line 2 on chart    
        
            time.sleep(0.5)  # Pause for 0.5 seconds before the next iteration

    # Call the display_data function as a separate thread
    threading.Thread(target=display_data).start()


    # Start the main event loop
    root.mainloop()
    ```

<hr>

**Explore customizable features such as colors, fonts, and more in the documentation.**

#### Please refer to the full documentation
- [**English doc.**](documentation/DOCUMENTATION_EN.md)
- [**Chinese doc.**](documentation/DOCUMENTATION_CN.md)
