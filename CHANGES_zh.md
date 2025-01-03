## v2.1.5

- ### 新增方法到 `LineChart` 对象
    | 方法名称      | 描述                                                | 参数     | 返回类型 |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `clear_data`  | 清除图表中所有线的数据，确保只保留最新的可见数据点。如果数据点总数超过最大可见点，则会从每条线的数据中移除旧数据。此方法确保图表仅显示基于最大可见范围的相关数据部分。                                                           | -              | `None`    |  

- ### 新增方法到 `Line` 对象
    | 方法名称      | 描述                                                | 参数     | 返回类型 |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `clear_data`     | 清除特定线的数据，确保只保留最新的可见数据点。如果线的数据超过最大可见点，则会修剪旧数据。此方法允许每条线独立清除其数据，确保它始终保持在可见范围内。                                                           | -              | `None`    | 

---

## v2.1.4

- ### 新增方法到 `LineChart` 对象
    | 方法名称      | 描述                                                | 参数     | 返回类型 |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `get_line_area`  | 获取特定线的区域大小                               | line: `tkchart.Line` | `float` | 
    | `get_lines_area` | 获取所有线的区域大小                                   | -                    | `float` | 

---

## v2.1.3

- ### 新增方法到 `LineChart` 对象
    | 方法名称      | 描述                                                | 参数     | 返回类型 |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `destroy`        | 销毁线图及其所有线               | -              | `None`      |

- ### 新增方法到 `Line` 对象
    | 方法名称      | 描述                                                | 参数     | 返回类型 |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `destroy`        | 销毁线对象                                    | -              | `None`      |

---

## v2.1.2

- ### 新增方法到 `Line` 对象

    | 方法名称      | 描述                                    | 参数                               | 返回类型 |
    |------------------|------------------------------------------------|------------------------------------------|-------------|
    | `cget`           | 获取指定参数的值       | attribute_name: `str \| "__all__"`       | `any`       |
    | `set_visible`    | 更改线的可见性              | state: `bool`                            | `None`      |
    | `get_visibility` | 获取线的可见性                 | -                                        | `bool`      |

- ### 新增方法到 `LineChart` 对象

    | 方法名称            | 描述                                    | 参数                                       | 返回类型 |
    |------------------------|------------------------------------------------|--------------------------------------------------|-------------|
    | `set_lines_visibility` | 更改所有线的可见性         | state: `bool`                                    | `None`      |
    | `set_line_visibility`  | 更改特定线的可见性       | line: `tkchart.Line`<br>state: `bool`            | `None`      |
    | `get_line_visibility`  | 获取特定线的可见性          | line: `tkchart.Line`                             | `bool`      |
    | `cget`                 | 获取指定参数的值       | attribute_name: `str \| "__all__"`               | `any`       |
    | `place_info`           | 获取位置相关信息                           | attribute_name: `str \| "__all__"`               | `any`       |
    | `pack_info`            | 获取打包相关信息                            | attribute_name: `str \| "__all__"`               | `any`       |
    | `grid_info`            | 获取网格相关信息                            | attribute_name: `str \| "__all__"`               | `any`       |

- ### 移除 `LineChart` 对象的方法

    | 方法名称 | 描述          | 参数                                   | 返回类型 |
    |-------------|----------------------|----------------------------------------------|-------------|
    | hide_all    | 隐藏所有的线   | state:  `bool`                             | None        |
    | hide        | 隐藏特定的线 | line:  `tkchart.Line`<br> state:  `bool` | None        |
