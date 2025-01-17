[![Chinese](https://img.shields.io/badge/Language-中文-red)](CHANGES_zh.md)


## v2.1.6 

- ### New Methods Added to `LineChart` Object  
    | Method Name                  | Description                                                | Parameters                               | Return Type      |  
    |------------------------------|------------------------------------------------------------|------------------------------------------|-----------------|  
    | `get_lines_data`              | Retrieves data points for all lines within a specified range with an optional step value. | start: `int` <br> end: `int` <br> step: `int` | `Dict[tkchart.Line, Tuple[int]]` |  
     `get_line_data`               | Retrieves data points for a specific line within a specified range and step. | line: `tkchart.Line` <br> start: `int` <br> end: `int`<br> step: `int` | `Tuple[int \| float]` |  
    | `get_x_axis_visible_point_count` | Retrieves the maximum number of data points that can be visible along the X-axis. | -                                       | `int` |  
    | `get_lines_visible_data`      | Retrieves currently visible data points for all lines based on the maximum data length and visible points. | -                                       | `Dict[tkchart.Line, Tuple[int \| float]]` |  
    | `get_line_visible_data`       | Retrieves currently visible data points for a specific line. | line: `tkchart.Line`                          | `Tuple[int \| float]` |  



- ### New Methods Added to `Line` Object  
    | Method Name                  | Description                                                | Parameters          | Return Type      |  
    |------------------------------|------------------------------------------------------------|---------------------|-----------------|  
    | `get_data`                   | Retrieves data points from a specified range with an optional step value. If no parameters are given, it returns all available data. | start: `int` <br> end: `int` <br> step: `int` | `Tuple[int \| float]` |  
    | `get_current_visible_data`    | Returns the currently visible data points based on the maximum data length across all lines and the maximum number of visible points. | -                   | `Tuple[int \| float]` |  
    | `get_x_axis_visible_point_count` | Retrieves the maximum number of data points that can be visible along the X-axis. | -                   | `int` |  


## v2.1.5

- ### New Method Added to `LineChart` Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `clear_data`  | Clears the data for all lines within the chart, ensuring that only the most recent visible data points are retained. If the total data points exceed the maximum visible points, the older data is removed from each line's data. This method ensures that the chart displays only the relevant portion of data based on the maximum visible range.                                                           | -              | ``None``    |  

- ### New Method Added to `Line` Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `clear_data`     | Clears the data for a specific line, ensuring that only the most recent visible data points are retained. If the line's data exceeds the maximum visible points, the older data is trimmed. This method allows each line to independently clean its data, ensuring it remains within the visible range.                                                           | -              | ``None``    | 

---

## v2.1.4

- ### New Methods Added to `LineChart` Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `get_line_area`  | Get the are of specific line                               | line: `tkchart.Line` | ``float`` | 
    | `get_lines_area` | Get the are of all lines                                   | -                    | ``float`` | 

---

## v2.1.3

- ### New Method Added to `LineChart` Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `destroy`        | Destroy the line chart, along with its lines               | -              | `None`      |

- ### New Method Added to `Line` Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `destroy`        | Destroy the line object                                    | -              | `None`      |

---

## v2.1.2

- ### New Method Added to `Line` Object

    | Method Name      | Description                                    | Parameters                               | Return Type |
    |------------------|------------------------------------------------|------------------------------------------|-------------|
    | `cget`           | Get the value of the specified parameter       | attribute_name: `str \| "__all__"`       | `any`       |
    | `set_visible`    | Change the visibility of the line              | state: `bool`                            | `None`      |
    | `get_visibility` | Get the visibility of the line                 | -                                        | `bool`      |

- ### New Methods Added to `LineChart` Object

    | Method Name            | Description                                    | Parameters                                       | Return Type |
    |------------------------|------------------------------------------------|--------------------------------------------------|-------------|
    | `set_lines_visibility` | Change the visibility of all the lines         | state: `bool`                                    | `None`      |
    | `set_line_visibility`  | Change the visibility of a specific line       | line: `tkchart.Line`<br>state: `bool`            | `None`      |
    | `get_line_visibility`  | Get the visibility of a specific line          | line: `tkchart.Line`                             | `bool`      |
    | `cget`                 | Get the value of the specified parameter       | attribute_name: `str \| "__all__"`               | `any`       |
    | `place_info`           | Get info about place                           | attribute_name: `str \| "__all__"`               | `any`       |
    | `pack_info`            | Get info about pack                            | attribute_name: `str \| "__all__"`               | `any`       |
    | `grid_info`            | Get info about grid                            | attribute_name: `str \| "__all__"`               | `any`       |

- ### Removed Methods in `LineChart` Object

    | Method Name | Description          | Parameters                                   | Return Type |
    |-------------|----------------------|----------------------------------------------|-------------|
    | hide_all    | Hide all the lines   | state:  ``bool``                             | None        |
    | hide        | hide a specific line | line:  ``tkchart.Line``<br> state:  ``bool`` | None        |