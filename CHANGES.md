# Changes

## New Method Added to Line Object

| Method Name      | Description                                    | Parameters                              | Return Type |
|------------------|------------------------------------------------|------------------------------------------|-------------|
| `cget`           | Get the value of the specified parameter      | `attribute_name: str \| "__all__"`       | `any`       |
| `set_visible`    | Change the visibility of the line             | `state: bool`                            | `None`      |
| `get_visibility` | Get the visibility of the line                | -                                        | `bool`      |

<br>
<br>

## New Methods Added to LineChart Object

| Method Name            | Description                                    | Parameters                                       | Return Type |
|------------------------|------------------------------------------------|--------------------------------------------------|-------------|
| `set_lines_visibility` | Change the visibility of all the lines        | `state: bool`                                   | `None`      |
| `set_line_visibility`  | Change the visibility of a specific line      | `line: tkchart.Line`<br>`state: bool`       | `None`      |
| `get_line_visibility`  | Get the visibility of a specific line         | `line: tkchart.Line`                        | `bool`      |
| `cget`        | Get the value of the specified parameter| `attribute_name: str \| "__all__"`       | `any`       |
| `place_info`  | Get info about place                    | `attribute_name: str \| "__all__"`       | `any`       |
| `pack_info`   | Get info about pack                     | `attribute_name: str \| "__all__"`       | `any`       |
| `grid_info`   | Get info about grid                     | `attribute_name: str \| "__all__"`       | `any`       |


<br>
<br>

## Removed Methods

| Method Name | Description          | Parameters                                   | Return Type |
|-------------|----------------------|----------------------------------------------|-------------|
| hide_all    | Hide all the lines   | state:  ``bool``                             | None        |
| hide        | hide a specific line | line:  ``tkchart.Line``<br> state:  ``bool`` | None        |
