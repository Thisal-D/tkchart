import tkinter
from typing import Union, List, Tuple, Literal, Any, Callable
from .Utils import Utils
from .Line import Line
from .Validate import Validate


class LineChart:
    def __init__(
            self,
            master: Any = None,
            width: int = 700,
            height: int = 400,
            axis_size: int = 1,

            axis_color: str = "#2C2C2C",
            bg_color: str = "#191919",
            fg_color: str = "#191919",
            data_font_style: Tuple[str, int, str] = ("arial", 9, "bold"),
            axis_font_style: Tuple[str, int, str] = ("arial", 8, "normal"),

            y_axis_precision: int = 0,
            y_axis_data: Any = "Y",
            y_axis_label_count: int = 1,
            y_axis_values: Tuple[Union[int, float], Union[int, float]] = (None, None),
            y_axis_font_color: str = "#606060",
            y_axis_data_font_color: str = "#707070",
            y_axis_data_position: Literal["top", "side"] = "top",
            y_axis_section_count: int = 0,
            y_axis_section_style: Literal["normal", "dashed"] = "normal",
            y_axis_section_style_type: Tuple[int, int] = (100, 50),
            y_axis_section_color: str = "#2C2C2C",

            x_axis_data: str = "X",
            x_axis_label_count: int = None,
            x_axis_values: Tuple[Any, ...] = (None, "None", None, "None"),
            x_axis_display_values_indices: Tuple[int, ...] = None,
            x_axis_font_color: str = "#606060",
            x_axis_data_font_color: str = "#707070",
            x_axis_data_position: Literal["top", "side"] = "top",
            x_axis_section_count: int = 0,
            x_axis_section_style: Literal["normal", "dashed"] = "normal",
            x_axis_section_style_type: Tuple[int, int] = (100, 50),
            x_axis_section_color: str = "#2C2C2C",

            x_axis_point_spacing: Union[int, Literal["auto"]] = "auto",
            y_space: int = 0,
            x_space: int = 0,

            pointer_state: Literal["enabled", "disabled"] = "disabled",
            pointing_callback_function: Callable = None,
            pointer_color: str = "#606060",
            pointing_values_precision: int = 1,
            pointer_lock: Literal["enabled", "disabled"] = "disabled",
            pointer_size: int = 1,

            *args: Any) -> None:
        """
        Initialize a LineChart object.

        Args:
            master (Any): The master object.
            width (int): Width of the LineChart widget.
            height (int): Height of the LineChart widget.
            axis_size (int): Size/thickness of the axis lines.

            axis_color (str): Color of the axis lines.
            bg_color (str): Background color of the LineChart widget.
            fg_color (str): Foreground color of the LineChart widget.
            data_font_style (Tuple[str, int, str]): Font style for data labels.
            axis_font_style (Tuple[str, int, str]): Font style for axis labels.

            y_axis_precision (int): Precision for y-axis values.
            y_axis_data (Any): Data label for the y-axis.
            y_axis_label_count (int): Number of y-axis labels.
            y_axis_values (Tuple[Union[int, float], Union[int, float]]): Range of y-axis values.
            y_axis_font_color (str): Font color for y-axis labels.
            y_axis_data_font_color (str): Font color for y-axis data label.
            y_axis_data_position (str): Position of y-axis data label.
            y_axis_section_count (int): Number of sections in the y-axis.
            y_axis_section_style (str): Style of the y-axis sections.
            y_axis_section_style_type (Tuple[int, int]): Style type for y-axis sections.
            y_axis_section_color (str): Color of the y-axis sections.

            x_axis_data (str): Data label for the x-axis.
            x_axis_label_count (int): Number of x-axis labels.
            x_axis_values (Tuple[Any, ...]): Values for x-axis labels.
            x_axis_display_values_indices (Tuple[int, ...]): Indices of x-axis values to display.
            x_axis_font_color (str): Font color for x-axis labels.
            x_axis_data_font_color (str): Font color for x-axis data label.
            x_axis_data_position (str): Position of x-axis data label.
            x_axis_section_count (int): Number of sections in the x-axis.
            x_axis_section_style (str): Style of the x-axis sections.
            x_axis_section_style_type (Tuple[int, int]): Style type for x-axis sections.
            x_axis_section_color (str): Color of the x-axis sections.

            x_axis_point_spacing (Union[int, str]): Spacing between x-axis points.
            y_space (int): Space between y-axis and LineChart.
            x_space (int): Space between x-axis and LineChart.

            pointer_state (str): State of pointer (enabled/disabled).
            pointing_callback_function (callable): Callback function for pointing.
            pointer_color (str): Color of the pointer.
            pointing_values_precision (int): Precision for pointer values.
            pointer_lock (str): Lock state of the pointer (enabled/disabled).
            pointer_size (int): Size of the pointer.
        """

        Validate._isInt(height, "height")
        Validate._isInt(width, "width")
        Validate._isInt(axis_size, "axis_size")
        Validate._isInt(y_space, "y_space")
        Validate._isInt(x_space, "x_space")
        Validate._isInt(y_axis_precision, "y_axis_precision")
        Validate._isInt(y_axis_label_count, "y_axis_label_count")
        Validate._isInt(y_axis_section_count, "y_axis_section_count")
        Validate._isInt(x_axis_section_count, "x_axis_section_count")
        Validate._isInt(pointing_values_precision, "pointing_values_precision")
        Validate._isInt(pointer_size, "pointer_size")
        Validate._isValidXAxisValues(x_axis_values, "x_axis_values")
        Validate._isValidYAxisValues(y_axis_values, "y_axis_values")
        Validate._isValidColor(y_axis_section_color, "y_axis_section_color")
        Validate._isValidColor(x_axis_section_color, "x_axis_section_color")
        Validate._isValidColor(axis_color, "axis_color")
        Validate._isValidColor(bg_color, "bg_color")
        Validate._isValidColor(fg_color, "fg_color")
        Validate._isValidColor(y_axis_font_color, "y_axis_font_color")
        Validate._isValidColor(x_axis_font_color, "x_axis_font_color")
        Validate._isValidColor(y_axis_data_font_color, "y_axis_data_font_color")
        Validate._isValidColor(x_axis_data_font_color, "x_axis_data_font_color")
        Validate._isValidColor(pointer_color, "pointer_color")
        Validate._isValidFont(data_font_style, "data_font_style")
        Validate._isValidFont(axis_font_style, "axis_font_style")
        Validate._isValidDataPostion(y_axis_data_position, "y_axis_data_position")
        Validate._isValidDataPostion(x_axis_data_position, "x_axis_data_position")
        Validate._isValidStyleType(y_axis_section_style_type, "y_axis_section_style_type")
        Validate._isValidStyleType(x_axis_section_style_type, "x_axis_section_style_type")
        Validate._isValidSectionStyle(y_axis_section_style, "y_axis_section_style")
        Validate._isValidSectionStyle(x_axis_section_style, "x_axis_section_style")
        Validate._isValidXAxisPointSpacing(x_axis_point_spacing, "x_axis_point_spacing")
        Validate._isValidPointerState_Lock(pointer_state, "pointer_state")
        Validate._isValidPointerState_Lock(pointer_lock, "pointer_lock")
        Validate._isValidFunction(pointing_callback_function, "pointing_callback_function")
        Validate._isValidXAxisIndices(x_axis_values, x_axis_display_values_indices, "x_axis_display_values_indices")
        Validate._isValidXAxisLabelCount(x_axis_label_count, "x_axis_label_count")

        if master is not None:
            self.__master = master
        elif len(args) != 0:
            self.__master = args[0]
        else:
            self.__master = master

        self.__height: int = height
        self.__width: int = width
        self.__axis_size: int = axis_size
        self.__axis_color: str = axis_color
        self.__x_axis_point_spacing: Union[int, float, Literal["auto"]] = x_axis_point_spacing
        self.__x_axis_point_spacing_handle_by: str = "auto"
        self.__data_font_style: Tuple[str, int, str] = data_font_style
        self.__axis_font_style: Tuple[str, int, str] = axis_font_style
        self.__lines: List[Line] = []
        self.__bg_color: str = bg_color
        self.__fg_color: str = fg_color
        self.__y_axis_font_color: str = y_axis_font_color
        self.__y_axis_data_font_color: str = y_axis_data_font_color
        self.__y_axis_section_color: str = y_axis_section_color
        self.__y_axis_section_style: Literal["normal", "dashed"] = y_axis_section_style
        self.__y_axis_section_style_type: Tuple[int, int] = y_axis_section_style_type
        self.__y_axis_section_count: int = y_axis_section_count
        self.__y_axis_label_count: int = y_axis_label_count
        self.__y_axis_data = str(y_axis_data)
        self.__y_axis_data_position: Literal["top", "side"] = y_axis_data_position
        self.__y_axis_values: Tuple[Union[int, float], Union[int, float]] = y_axis_values
        self.__y_axis_min_value: Union[int, float] = y_axis_values[0]
        self.__y_axis_max_value: Union[int, float] = y_axis_values[1]
        self.__y_axis_precision: int = y_axis_precision
        self.__y_space: int = y_space
        self.__x_axis_font_color: str = x_axis_font_color
        self.__x_axis_data_font_color: str = x_axis_data_font_color
        self.__x_axis_section_color: str = x_axis_section_color
        self.__x_axis_section_style: Literal["normal", "dashed"] = x_axis_section_style
        self.__x_axis_section_style_type: Tuple[int, int] = x_axis_section_style_type
        self.__x_axis_section_count: int = x_axis_section_count
        self.__x_axis_label_count: int = x_axis_label_count
        self.__x_axis_display_values_indices: Tuple[int, ...] = x_axis_display_values_indices
        self.__x_labels_values_index_change: int = 1
        self.__x_axis_data: str = str(x_axis_data)
        self.__x_axis_data_position: Literal["top", "side"] = x_axis_data_position
        self.__x_axis_values: Tuple[Any, ...] = x_axis_values
        self.__x_axis_values_handle_by: str = "label_count"
        self.__x_space: int = x_space
        self.__pointer_state: Literal["enabled", 'disabled'] = pointer_state
        self.__pointing_callback_function: Callable = pointing_callback_function
        self.__pointing_values_precision: int = pointing_values_precision
        self.__pointer_lock: Literal["enabled", 'disabled'] = pointer_lock
        self.__pointer_size: int = pointer_size
        self.__pointer_color: str = pointer_color
        self.__x_values_frame_place_req: bool = True
        self.__y_values_frame_place_req: bool = True

        self.__place_x: int = 0
        self.__real_height: int = 0
        self.__real_width: int = 0
        self.__const_real_height: int = 0
        self.__const_real_width: int = 0
        self.__visibility: bool = True

        self.__place_info_x: Union[int, None] = None
        self.__place_info_y: Union[int, None] = None
        self.__place_info_rely: Union[int, float, None] = None
        self.__place_info_relx: Union[int, float, None] = None
        self.__place_info_anchor: Literal["n", "e", "s", "w", "ne", "nw", "se", "sw", "center", None] = None

        self.__pack_info_pady: Union[int, None] = None
        self.__pack_info_padx: Union[int, None] = None
        self.__pack_info_before: Any = None
        self.__pack_info_after: Any = None
        self.__pack_info_side: Literal["top", "bottom", "left", "right", None] = None
        self.__pack_info_anchor: Literal["n", "e", "s", "w", "ne", "nw", "se", "sw", "center", None] = None

        self.__grid_info_column: Union[int, None] = None
        self.__grid_info_columnspan: Union[int, None] = None
        self.__grid_info_padx: Union[int, None] = None
        self.__grid_info_pady: Union[int, None] = None
        self.__grid_info_row: Union[int, None] = None
        self.__grid_info_rowspan: Union[int, None] = None
        self.__grid_info_sticky: Literal["n", "e", "s", "w", "ne", "nw", "se", "sw", None] = None

        if self.__x_axis_point_spacing == "auto":
            self.__x_axis_point_spacing_handle_by = "auto"
        else:
            self.__x_axis_point_spacing_handle_by = "manual"

        if self.__x_axis_display_values_indices is not None:
            self.__x_axis_display_values_indices = Utils._sort_tuple(self.__x_axis_display_values_indices)
            self.__x_axis_values_handle_by = "label_indices"
        else:
            self.__x_axis_values_handle_by = "label_count"

        self.__create_widgets()
        self.__configure_required_widget_size()
        self.__configure_x_axis_labels_info()
        self.__configure_x_axis_point_spacing()
        self.__create_x_axis_labels()
        self.__set_x_axis_values()
        self.__create_y_axis_labels()
        self.__set_y_axis_values()
        self.__create_y_axis_sections()
        self.__create_x_axis_sections()
        self.__set_x_y_axis_data_texts()
        self.__set_pointer_state()
        self.__set_pointer_size()
        self.__set_widgets_fonts()
        self.__set_widgets_colors()
        self.__place_widgets()
        self.__reset_chart_info()

    def __create_widgets(self) -> None:
        """
        Create widgets for the LineChart.

        This method initializes the main frame along with frames for the y-axis, x-axis,
        y-axis values, x-axis values, y-axis data label, x-axis data label, output frame,
        output canvas, and pointer.
        """

        self.__main_frame = tkinter.Frame(master=self.__master)
        self.__x_axis_values_frame = tkinter.Frame(master=self.__main_frame)
        self.__y_axis_values_frame = tkinter.Frame(master=self.__main_frame)
        self.__y_axis_data_label = tkinter.Label(master=self.__main_frame)
        self.__x_axis_data_label = tkinter.Label(master=self.__main_frame)
        self.__output_frame = tkinter.Frame(master=self.__main_frame)
        self.__output_canvas = tkinter.Canvas(master=self.__output_frame, highlightthickness=0)
        self.__y_axis_frame = tkinter.Frame(master=self.__main_frame)
        self.__x_axis_frame = tkinter.Frame(master=self.__main_frame)
        self.__pointer = tkinter.Frame(master=self.__output_canvas)

    def __set_pointer_state(self) -> None:
        """
        Set the state of the pointer.

        This method configures the behavior of the pointer based on its state (enabled or disabled).
        If the pointer is enabled, it binds events for mouse movement to display pointed values.
        If the pointer is disabled, it unbinds those events.
        """

        if self.__pointer_state == "enabled":
            self.__output_canvas.bind("<Leave>", self.__hide_pointer)
            self.__output_canvas.bind("<Motion>", self.__return_pointed_values)
        elif self.__pointer_state == "disabled":
            self.__output_canvas.unbind("<Leave>")
            self.__output_canvas.unbind("<Motion>")

    def __set_widgets_colors(self) -> None:
        """
        Set the colors for LineChart widgets.

        This method configures the background and foreground colors for various widgets in the LineChart,
        including the frames for y-axis, x-axis, y-axis values, x-axis values, main frame, output frame,
        output canvas, y-axis data label, x-axis data label, and pointer.
        """

        self.__y_axis_frame.configure(bg=self.__axis_color)
        self.__x_axis_frame.configure(bg=self.__axis_color)
        self.__y_axis_values_frame.configure(bg=self.__bg_color)
        self.__x_axis_values_frame.configure(bg=self.__bg_color)

        self.__main_frame.configure(bg=self.__bg_color)
        self.__output_frame.configure(bg=self.__fg_color)
        self.__output_canvas.configure(bg=self.__fg_color)

        self.__y_axis_data_label.configure(bg=self.__bg_color, fg=self.__y_axis_data_font_color)
        for label in self.__x_axis_values_frame.winfo_children():
            if type(label) == tkinter.Label:
                label.configure(bg=self.__bg_color, fg=self.__x_axis_font_color)

        self.__x_axis_data_label.configure(bg=self.__bg_color, fg=self.__x_axis_data_font_color)
        for label in self.__y_axis_values_frame.winfo_children():
            if type(label) == tkinter.Label:
                label.configure(bg=self.__bg_color, fg=self.__y_axis_font_color)

        self.__pointer.configure(bg=self.__pointer_color)

    def __set_widgets_fonts(self) -> None:
        """
        Set the fonts for LineChart widgets.

        This method configures the font styles for various widgets in the LineChart,
        including the y-axis data label, x-axis data label, y-axis values labels,
        and x-axis values labels, using the specified data font style and axis font style.
        """

        self.__y_axis_data_label.configure(font=self.__data_font_style)
        self.__x_axis_data_label.configure(font=self.__data_font_style)

        for label in self.__y_axis_values_frame.winfo_children():
            if type(label) == tkinter.Label:
                label.configure(font=self.__axis_font_style)

        for label in self.__x_axis_values_frame.winfo_children():
            if type(label) == tkinter.Label:
                label.configure(font=self.__axis_font_style)

    def __set_pointer_size(self) -> None:
        """
        Set the size of the pointer.

        This method adjusts the width and height of the pointer widget based on the specified pointer size.
        """

        self.__pointer.configure(width=self.__pointer_size)
        self.__pointer.config(height=self.__const_real_height)

    def __place_widgets(self) -> None:
        """
        Place widgets within the LineChart.

        This method handles the placement of various widgets within the LineChart, including the main frame,
        y-axis frame, x-axis frame, output frame, output canvas, y-axis values frame, and x-axis values frame,
        based on the specified dimensions and positions.
        """

        self.__main_frame.configure(width=self.__width, height=self.__height)

        self.__y_axis_data_label.place_forget()
        self.__x_axis_data_label.place_forget()

        if self.__y_axis_data != "":
            if self.__y_axis_data_position == "top":
                self.__y_axis_data_label.place(x=0, y=0)
            else:
                self.__y_axis_data_label.place(
                    x=0,
                    y=self.__y_space + self.__y_special_height_space + self.__real_height / 2,
                    anchor="w"
                )

        if self.__x_axis_data != "":
            if self.__x_axis_data_position == "top":
                self.__x_axis_data_label.place(
                    rely=1,
                    relx=1,
                    x=-self.__x_axis_data_req_width,
                    y=-self.__x_axis_data_req_height
                )
            else:
                self.__x_axis_data_label.place(
                    rely=1,
                    y=-self.__x_axis_data_req_height, relx=0, anchor="n",
                    x=(
                        self.__const_real_width / 2 + self.__y_axis_data_req_width_space_side +
                        self.__y_value_req_width_space + self.__axis_size + self.__x_axis_data_req_width_space_top +
                        self.__x_special_width_space
                    )
                )

        self.__y_axis_frame.configure(width=self.__axis_size)
        self.__x_axis_frame.configure(height=self.__axis_size)

        self.__y_axis_frame.place(
            x=self.__y_value_req_width_space + self.__y_axis_data_req_width_space_side,
            y=float(
                self.__y_axis_data_req_height_space_top +
                (self.__y_value_req_height_space / 2) +
                self.__y_special_height_space
            ),
            height=self.__const_real_height + self.__y_space + self.__axis_size
        )
        self.__x_axis_frame.place(
            x=self.__y_value_req_width_space + self.__y_axis_data_req_width_space_side,
            rely=1,
            y=-self.__axis_size + -self.__x_value_req_height_space + -self.__x_axis_data_req_height_space_side,
            width=self.__const_real_width + self.__axis_size + self.__x_space
        )

        self.__output_frame.place(
            x=self.__y_value_req_width_space + self.__axis_size + self.__y_axis_data_req_width_space_side,
            width=self.__const_real_width,
            height=self.__const_real_height,
            y=float(
                self.__y_axis_data_req_height_space_top + (self.__y_value_req_height_space / 2) +
                self.__y_special_height_space + self.__y_space
            )
        )

        self.__output_canvas.place(y=0, x=0, height=self.__const_real_height, width=self.__const_real_width)

        if self.__y_values_frame_place_req:
            self.__y_axis_values_frame.place(
                x=self.__y_axis_data_req_width_space_side,
                width=self.__y_value_req_width_space,
                height=self.__height
            )
        else:
            self.__y_axis_values_frame.place_forget()

        if self.__x_values_frame_place_req:
            self.__x_axis_values_frame.place(
                x=0,
                rely=1,
                y=-self.__x_value_req_height_space + -self.__x_axis_data_req_height_space_side,
                height=self.__x_value_req_height_space,
                width=self.__width
            )
        else:
            self.__x_axis_values_frame.place_forget()

    def __configure_x_axis_point_spacing(self) -> None:
        """
        Configure the spacing between points on the x-axis.

        This method calculates and sets the spacing between points on the x-axis based on the
        specified handle method. If the spacing is handled automatically, it calculates the spacing
        based on the real width of the LineChart and the number of x-axis values. If handled manually,
        it uses the specified x-axis point spacing value.
        """

        if self.__x_axis_point_spacing_handle_by == "auto":
            self.__x_axis_point_spacing = (self.__const_real_width / len(self.__x_axis_values))
        elif self.__x_axis_point_spacing_handle_by == "manual":
            self.__x_axis_point_spacing = self.__x_axis_point_spacing

    def __configure_required_widget_size(self) -> None:
        """
        Configure the required sizes of the LineChart's widgets.

        This method calculates and sets the required sizes for various widgets in the LineChart,
        such as axis labels, based on the provided data and styling options. It determines the
        necessary space for displaying the data labels, axis values, and adjusts the real width
        and height of the LineChart accordingly.
        """

        self.__x_axis_data_req_width_space_top = 0
        self.__x_axis_data_req_height_space_side = 0
        self.__x_special_width_space = 0
        self.__x_axis_data_req_height = 0
        self.__x_axis_data_req_width = 0
        if self.__x_axis_data != "":
            self.__x_axis_data_req_height = Utils._RequiredHeight(text=self.__x_axis_data, font=self.__data_font_style)
            self.__x_axis_data_req_width = Utils._RequiredWidth(text=self.__x_axis_data, font=self.__data_font_style)
            if self.__x_axis_data_position == "top":
                self.__x_special_width_space = 15
                self.__x_axis_data_req_width_space_top = Utils._RequiredWidth(
                    text=self.__x_axis_data, font=self.__data_font_style
                )
            else:
                self.__x_axis_data_req_height_space_side = Utils._RequiredHeight(
                    text=self.__x_axis_data, font=self.__data_font_style
                )

        self.__y_axis_data_req_height_space_top = 0
        self.__y_axis_data_req_width_space_side = 0
        self.__y_special_height_space = 0

        self.__y_values_frame_place_req = True
        self.__x_values_frame_place_req = True
        # self.__y_axis_data_req_height = Utils._RequiredHeight(text=self.__y_axis_data, font=self.__data_font_style)
        # self.__y_axis_data_req_width = Utils._RequiredWidth(text=self.__y_axis_data, font=self.__data_font_style)
        if self.__y_axis_data != "":
            if self.__y_axis_data_position == "top":
                self.__y_special_height_space = 15
                self.__y_axis_data_req_height_space_top = Utils._RequiredHeight(
                    text=self.__y_axis_data, font=self.__data_font_style
                )
            else:
                self.__y_axis_data_req_width_space_side = Utils._RequiredWidth(
                    text=self.__y_axis_data[0], font=self.__data_font_style
                )

        if self.__y_axis_label_count == 0:
            self.__y_value_req_height_space = 0
            self.__y_value_req_width_space = 0
            self.__y_values_frame_place_req = False
        else:
            if (len(Utils._format_float_with_precision(self.__y_axis_max_value, self.__y_axis_precision)) >
                    len(Utils._format_float_with_precision(self.__y_axis_min_value, self.__y_axis_precision))):
                y_value_temp = self.__y_axis_max_value
            else:
                y_value_temp = self.__y_axis_min_value
            self.__y_value_req_height_space = Utils._RequiredHeight(
                text=Utils._format_float_with_precision(y_value_temp, self.__y_axis_precision),
                font=self.__axis_font_style
            )
            self.__y_value_req_width_space = Utils._RequiredWidth(
                text=Utils._format_float_with_precision(y_value_temp, self.__y_axis_precision),
                font=self.__axis_font_style
            )

        self.__x_value_req_width_space = 0
        self.__x_value_req_height_space = 0
        if self.__x_axis_label_count == 0 and self.__x_axis_values_handle_by == "label_count":
            self.__x_values_frame_place_req = False
        elif self.__x_axis_values_handle_by == "label_indices" and (len(self.__x_axis_display_values_indices) == 0):
            self.__x_values_frame_place_req = False
        else:
            self.__x_value_req_height_space = Utils._RequiredHeight(
                text=self.__x_axis_values[0], font=self.__axis_font_style
            )
            # self.__x_value_req_width_space = RequiredWidth(text=format_float_with_precision(self.__x_axis_data_max,
            # self.__x_values_decimals), font=self.__axis_font_style)
            self.__x_value_req_width_space = Utils._get_max_required_label_width(
                data=self.__x_axis_values, font=self.__axis_font_style
            )

        if self.__y_value_req_height_space / 2 > self.__x_value_req_height_space:
            self.__x_value_req_height_space = self.__y_value_req_height_space / 2

        self.__real_width = self.__width - (
                self.__y_value_req_width_space + self.__axis_size + self.__x_axis_data_req_width_space_top +
                self.__y_axis_data_req_width_space_side + (self.__x_value_req_width_space / 2) +
                self.__x_special_width_space + self.__x_space
        )

        self.__const_real_width = self.__real_width
        self.__real_height = self.__height - (
                self.__y_axis_data_req_height_space_top + self.__axis_size + self.__x_value_req_height_space +
                self.__x_axis_data_req_height_space_side + (self.__y_value_req_height_space / 2) +
                self.__y_special_height_space + self.__y_space
        )
        self.__real_height = self.__real_height

        self.__const_real_height = int(self.__real_height)

        self.__y_axis_values_gap = abs(self.__y_axis_max_value - self.__y_axis_min_value)

    def __set_x_y_axis_data_texts(self) -> None:
        """
        Set the text for the x and y axis data labels.

        This method sets the text for the y-axis data label based on its position. If the position
        is 'top', the label text is set to the provided y-axis data. Otherwise, if the position is
        'side', the label text is set as a newline-separated string of the y-axis data elements.

        The text for the x-axis data label is set directly to the provided x-axis data.
        """

        if self.__y_axis_data_position == "top":
            self.__y_axis_data_label.configure(text=self.__y_axis_data)
        else:
            self.__y_axis_data_label.configure(text="\n".join(self.__y_axis_data))
        self.__x_axis_data_label.configure(text=self.__x_axis_data)

    def __set_y_axis_values(self) -> None:
        """
        Set the values for the y-axis labels.

        This method sets the values for the y-axis labels based on the specified label count and the
        range of values between the maximum and minimum y-axis values. If the y-axis label count is greater
        than 0, it iterates over the y-axis labels and calculates the value for each label using the
        formula: maximum y-axis value - ((y-axis value range) / y-axis label count) * index. If the minimum
        y-axis value is 0 and the index is equal to the y-axis label count, the value is set to 0. The values
        are formatted with the specified precision before being assigned to the labels.
        """

        if self.__y_axis_label_count > 0:
            for i, label in enumerate(self.__y_axis_values_frame.winfo_children()):
                value = (self.__y_axis_max_value - (self.__y_axis_values_gap / self.__y_axis_label_count) * i)
                if self.__y_axis_min_value == 0 and i == self.__y_axis_label_count:
                    value = 0
                value = Utils._format_float_with_precision(value, self.__y_axis_precision)
                label.configure(text=value)

    def __create_y_axis_labels(self) -> None:
        """
        Create the y-axis labels.

        This method creates the y-axis labels based on the specified label count. If the y-axis label count is
        greater than 0, it iterates over the range of label count and creates a tkinter Label for each label.
        The labels are placed vertically with equal spacing between them. The y-coordinate for each label is
        calculated based on the initial y-position, the height of each label, additional spacing, and the total
        height of the plot area divided by the number of labels.
        """

        if self.__y_axis_label_count > 0:
            y = self.__y_axis_data_req_height_space_top + (
                    self.__y_value_req_height_space / 2) + self.__y_special_height_space + self.__y_space
            for i in range(self.__y_axis_label_count + 1):
                tkinter.Label(
                    master=self.__y_axis_values_frame,
                    justify="right"
                ).place(
                    y=y,
                    x=0,
                    anchor="w",
                    width=self.__y_value_req_width_space
                )
                y += self.__real_height / self.__y_axis_label_count

    def __destroy_y_axis_labels(self) -> None:
        """
        Destroy the y-axis labels.

        This method removes and destroys all existing y-axis labels. It iterates over the children of the
        y-axis values frame, which contain the y-axis labels, and calls the place_forget() and destroy() methods
        for each label to remove them from the GUI and release system resources.
        """

        for y_value in self.__y_axis_values_frame.winfo_children():
            y_value.place_forget()
            y_value.destroy()

    def __set_x_axis_values_using_label_count(self) -> None:
        """
        Set the x-axis values using the label count.

        This method sets the x-axis values using the label count. It iterates over the children of the
        x-axis values frame, which contain the x-axis labels, and assigns values to each label from the
        provided x-axis values list in reverse order. The index is decremented by the value of
        x_labels_values_index_change for each iteration.
        """

        index = -1
        for label in (self.__x_axis_values_frame.winfo_children()):
            value = self.__x_axis_values[index]
            index -= self.__x_labels_values_index_change
            label.configure(text=value)

    def __set_x_axis_values_using_indices(self) -> None:
        """
        Set the x-axis values using the specified display indices.

        This method sets the x-axis values using the specified display indices. It iterates over the children of the
        x-axis values frame, which contain the x-axis labels, and assigns values to each label from the
        provided x-axis values list based on the display indices provided.
        """

        index = -1
        for label in (self.__x_axis_values_frame.winfo_children()):
            value = self.__x_axis_values[self.__x_axis_display_values_indices[index]]
            index -= 1
            label.configure(text=value)

    def __create_x_axis_labels_using_label_count(self) -> None:
        """
        Create x-axis labels using the specified label count.

        This method creates x-axis labels using the specified label count. It iterates over the range of the label count
        and places labels inside the x-axis values frame. The labels are evenly spaced across the x-axis based on the
        provided label count.
        """

        x = self.__width - self.__x_axis_data_req_width_space_top - (
                self.__x_value_req_width_space / 2) - self.__x_special_width_space - self.__x_space
        for i in range(self.__x_axis_label_count):
            tkinter.Label(master=self.__x_axis_values_frame).place(
                rely=1,
                y=-self.__x_value_req_height_space,
                x=x,
                anchor="n"
            )
            x -= self.__const_real_width / self.__x_axis_label_count

    def __create_x_axis_labels_using_indices(self) -> None:
        """
        Create x-axis labels using the specified display indices.

        This method creates x-axis labels using the specified display indices. It iterates over the range of
        the label count and places labels inside the x-axis values frame. The labels are placed at positions
        corresponding to the indices specified for display.
        """

        x = self.__width - self.__x_axis_data_req_width_space_top - (
                self.__x_value_req_width_space / 2) - self.__x_special_width_space - self.__x_space
        for i in range(self.__x_axis_label_count):
            if (self.__x_axis_label_count - (i + 1)) in self.__x_axis_display_values_indices:
                tkinter.Label(master=self.__x_axis_values_frame).place(
                    rely=1,
                    y=-self.__x_value_req_height_space,
                    x=x,
                    anchor="n"
                )
            x -= self.__const_real_width / self.__x_axis_label_count

    def __create_x_axis_labels(self) -> None:
        """
        Create x-axis labels based on the method specified for handling x-axis values.

        This method creates x-axis labels based on the method specified for handling x-axis values. If the values are
        to be displayed using label indices, it calls the __create_x_axis_labels_using_indices method.
        Otherwise, it calls the __create_x_axis_labels_using_label_count method.
        """

        if self.__x_axis_values_handle_by == "label_indices":
            self.__create_x_axis_labels_using_indices()
        else:
            self.__create_x_axis_labels_using_label_count()

    def __set_x_axis_values(self) -> None:
        """
        Set x-axis values based on the method specified for handling x-axis values.

        This method sets x-axis values based on the method specified for handling x-axis values. If the values are to be
        set using label indices, it calls the __set_x_axis_values_using_indices method. Otherwise, it calls the
        __set_x_axis_values_using_label_count method.
        """

        if self.__x_axis_values_handle_by == "label_indices":
            self.__set_x_axis_values_using_indices()
        else:
            self.__set_x_axis_values_using_label_count()

    def __destroy_x_axis_labels(self) -> None:
        """
        Destroy x-axis labels.

        This method destroys all the x-axis labels by iterating through the children of the x-axis values frame,
        forgetting their placement, and then destroying them.
        """

        for x_value in self.__x_axis_values_frame.winfo_children():
            x_value.place_forget()
            x_value.destroy()

    def __configure_x_axis_labels_info(self) -> None:
        """
        Configure information for x-axis labels.

        This method determines the count and index change for x-axis labels based on the method used to provide
        x-axis values. If x-axis values are provided using label indices, it sets the label count to the length
        of the x-axis values. If x-axis values are handled automatically or by label count, it adjusts the label
        count and index change accordingly to ensure proper spacing and distribution of labels.
        """

        if self.__x_axis_values_handle_by == "label_indices":
            self.__x_axis_label_count = len(self.__x_axis_values)

        elif self.__x_axis_values_handle_by == "label_count":
            if self.__x_axis_label_count == 0:
                return
            if self.__x_axis_label_count is None:
                self.__x_axis_label_count = len(self.__x_axis_values)
            x_axis_real_label_count = len(self.__x_axis_values)
            if self.__x_axis_label_count > x_axis_real_label_count:
                self.__x_axis_label_count = x_axis_real_label_count
            else:
                while x_axis_real_label_count % self.__x_axis_label_count != 0:
                    self.__x_axis_label_count += 1
            self.__x_labels_values_index_change = int(x_axis_real_label_count / self.__x_axis_label_count)

    def __create_y_axis_sections(self) -> None:
        """
        Create sections on the y-axis.

        This method creates sections on the y-axis based on the specified section style.
        If the section style is 'normal', it creates evenly spaced sections. If the section style is 'dashed',
        it creates sections with custom width and spacing as specified in the style type tuple.
        """

        y = 0
        if self.__y_axis_section_style == "normal":
            for i in range(self.__y_axis_section_count):
                tkinter.Frame(
                    master=self.__output_frame,
                    height=1,
                    width=self.__const_real_width,
                    bg=self.__y_axis_section_color
                ).place(y=y, anchor="w")
                y += self.__real_height / self.__y_axis_section_count
        else:
            width_ = self.__y_axis_section_style_type[0]
            space_ = self.__y_axis_section_style_type[1]
            for i in range(self.__y_axis_section_count):
                x_ = self.__const_real_width - width_
                while x_ > -(width_ + space_):
                    tkinter.Frame(
                        master=self.__output_frame,
                        height=1,
                        width=width_,
                        bg=self.__y_axis_section_color
                    ).place(y=y, anchor="w", x=x_)
                    x_ -= width_ + space_
                y += self.__real_height / self.__y_axis_section_count

    def __create_x_axis_sections(self) -> None:
        """
        Create sections on the x-axis.

        This method creates sections on the x-axis based on the specified section style.
        If the section style is 'normal',it creates evenly spaced sections. If the section style is 'dashed',
        it creates sections with custom height and spacing is specified in the style type tuple.
        """

        x = self.__const_real_width - 1
        if self.__x_axis_section_style == "normal":
            for i in range(self.__x_axis_section_count):
                tkinter.Frame(
                    master=self.__output_frame,
                    height=self.__const_real_height,
                    width=1,
                    bg=self.__x_axis_section_color
                ).place(x=x, anchor="n")
                x -= (self.__const_real_width / self.__x_axis_section_count)
        else:
            height_ = self.__x_axis_section_style_type[0]
            space_ = self.__x_axis_section_style_type[1]
            for i in range(self.__x_axis_section_count):
                y_ = 0
                while y_ < self.__const_real_height:
                    tkinter.Frame(
                        master=self.__output_frame,
                        height=height_,
                        width=1,
                        bg=self.__x_axis_section_color
                    ).place(x=x, anchor="n", y=y_)
                    y_ += height_ + space_
                x -= (self.__const_real_width / self.__x_axis_section_count)

    def __destroy_x_y_sections(self) -> None:
        """
        Destroy all x-axis and y-axis sections.

        This method destroys all sections created on both the x-axis and y-axis by removing them from the output frame.
        """

        for widget in self.__output_frame.winfo_children():
            if type(widget) == tkinter.Frame:
                widget.place_forget()
                widget.destroy()

    def configure(
            self,
            width: int = None,
            height: int = None,
            axis_size: int = None,
            x_axis_point_spacing: Union[int, Literal["auto"]] = None,

            bg_color: str = None,
            axis_color: str = None,
            fg_color: str = None,
            data_font_style: Tuple[str, int, str] = None,
            axis_font_style: Tuple[str, int, str] = None,

            y_axis_values: Union[int, float] = None,
            y_axis_precision: int = None,
            y_axis_font_color: str = None,
            y_axis_data_font_color: str = None,
            y_axis_section_count: int = None,
            y_axis_section_color: str = None,
            y_axis_section_style: Literal["normal", "dashed"] = None,
            y_axis_section_style_type: Tuple[int, int] = None,
            y_axis_label_count: int = None,
            y_axis_data: Any = None,
            y_axis_data_position: Literal["top", "side"] = None,
            y_space: int = None,

            x_axis_values: Tuple[Any, ...] = None,
            x_axis_data: Any = None,
            x_axis_font_color: str = None,
            x_axis_data_font_color: str = None,
            x_axis_label_count: int = None,
            x_axis_section_count: int = None,
            x_axis_section_style: Literal["normal", "dashed"] = None,
            x_axis_section_style_type: Tuple[int, int] = None,
            x_axis_section_color: str = None,
            x_axis_display_values_indices: Tuple[int, ...] = None,
            x_axis_data_position: Literal["top", "side"] = None,
            x_space: int = None,

            pointer_state: Literal["enabled", "disabled"] = None,
            pointing_values_precision: int = None,
            pointer_color: str = None,
            pointer_lock: Literal["enabled", "disabled"] = None,
            pointing_callback_function: callable = None,
            pointer_size: int = None) -> None:

        """
        Configures the properties of the chart widget based on the provided arguments.

        Args:
            width (int): The width of the chart widget.
            height (int): The height of the chart widget.
            axis_size (int): The size of the axis lines.
            x_axis_point_spacing (Union[int, str]): The spacing between x-axis points.

            bg_color (str): The background color of the chart.
            axis_color (str): The color of the axis lines.
            fg_color (str): The foreground color of the chart.
            data_font_style (Tuple[str, int, str]): The font style for data labels.
            axis_font_style (Tuple[str, int, str]): The font style for axis labels.

            y_axis_values (Union[int, float]): The range of values for the y-axis.
            y_axis_precision (int): The precision of values on the y-axis.
            y_axis_font_color (str): The font color of y-axis labels.
            y_axis_data_font_color (str): The font color of y-axis data labels.
            y_axis_section_count (int): The number of sections on the y-axis.
            y_axis_section_color (str): The color of sections on the y-axis.
            y_axis_section_style (str): The style of sections on the y-axis.
            y_axis_section_style_type (Tuple[int, int]): The type of style for sections on the y-axis.
            y_axis_label_count (int): The count of labels on the y-axis.
            y_axis_data (Any): The data for y-axis labels.
            y_axis_data_position (str): The position of y-axis data labels.
            y_space (int): The space between y-axis and the chart.

            x_axis_values (Tuple[Any, ...]): The values for the x-axis.
            x_axis_data (Any): The data for x-axis labels.
            x_axis_font_color (str): The font color of x-axis labels.
            x_axis_data_font_color (str): The font color of x-axis data labels.
            x_axis_label_count (int): The count of labels on the x-axis.
            x_axis_section_count (int): The number of sections on the x-axis.
            x_axis_section_style (str): The style of sections on the x-axis.
            x_axis_section_style_type (Tuple[int, int]): The type of style for sections on the x-axis.
            x_axis_section_color (str): The color of sections on the x-axis.
            x_axis_display_values_indices (Tuple[int, ...]): The indices of displayed x-axis values.
            x_axis_data_position (str): The position of x-axis data labels.
            x_space (int): The space between the x-axis and the chart.

            pointer_state (str): The state of the pointer. Possible values are "enabled" or "disabled".
            pointing_values_precision (int): The precision of values displayed by the pointer.
            pointer_color (str): The color of the pointer.
            pointer_lock (str): The state of the pointer lock. Possible values are "enable" or "disable".
            pointing_callback_function (callable): A callback function triggered when the pointer is clicked or moved.
            pointer_size (int): The size of the pointer.
        """

        chart_reset_req: bool = False
        widget_color_change_req: bool = False
        widget_size_change_req: bool = False
        widget_font_change_req: bool = False
        chart_x_values_change_req: bool = False
        chart_sections_change_req: bool = False
        chart_sections_color_change_req: bool = False
        chart_x_labels_change_req: bool = False
        chart_y_labels_change_req: bool = False
        pointer_state_change_req: bool = False
        pointer_size_change_req: bool = False
        reshow_data_req: bool = False

        if width is not None:
            Validate._isInt(width, "width")
            if width != self.__width:
                self.__width = width
                chart_reset_req = True

        if height is not None:
            Validate._isInt(height, "height")
            if height != self.__height:
                self.__height = height
                chart_reset_req = True

        if y_space is not None:
            Validate._isInt(y_space, "y_space")
            if y_space != self.__y_space:
                self.__y_space = y_space
                chart_reset_req = True

        if x_space is not None:
            Validate._isInt(x_space, "x_space")
            if x_space != self.__x_space:
                self.__x_space = x_space
                chart_reset_req = True

        if y_axis_values is not None:
            Validate._isValidYAxisValues(y_axis_values, "y_axis_values")
            if y_axis_values != self.__y_axis_values:
                self.__y_axis_values = y_axis_values
                self.__y_axis_min_value = y_axis_values[0]
                self.__y_axis_max_value = y_axis_values[1]
                chart_reset_req = True

        if axis_size is not None:
            Validate._isInt(axis_size, "axis_size")
            if axis_size != self.__axis_size:
                self.__axis_size = axis_size
                chart_reset_req = True

        if y_axis_precision is not None:
            Validate._isInt(y_axis_precision, "y_axis_precision")
            if y_axis_precision != self.__y_axis_precision:
                self.__y_axis_precision = y_axis_precision
                chart_reset_req = True

        if x_axis_data is not None:
            if x_axis_data != self.__x_axis_data:
                self.__x_axis_data = x_axis_data
                chart_reset_req = True

        if data_font_style is not None:
            Validate._isValidFont(data_font_style, "data_font_style")
            if data_font_style != self.__data_font_style:
                self.__data_font_style = data_font_style
                chart_reset_req = True

        if axis_font_style is not None:
            Validate._isValidFont(axis_font_style, "axis_font_style")
            if axis_font_style != self.__axis_font_style:
                self.__axis_font_style = axis_font_style
                chart_reset_req = True

        if bg_color is not None:
            Validate._isValidColor(bg_color, "bg_color")
            if bg_color != self.__bg_color:
                self.__bg_color = bg_color
                widget_color_change_req = True

        if axis_color is not None:
            Validate._isValidColor(axis_color, "axis_color")
            if axis_color != self.__axis_color:
                self.__axis_color = axis_color
                widget_color_change_req = True

        if fg_color is not None:
            Validate._isValidColor(fg_color, "fg_color")
            if fg_color != self.__fg_color:
                self.__fg_color = fg_color
                widget_color_change_req = True

        if y_axis_font_color is not None:
            Validate._isValidColor(y_axis_font_color, "y_axis_font_color")
            if y_axis_font_color != self.__y_axis_font_color:
                self.__y_axis_font_color = y_axis_font_color
                widget_color_change_req = True

        if x_axis_font_color is not None:
            Validate._isValidColor(x_axis_font_color, "x_axis_font_color")
            if x_axis_font_color != self.__x_axis_font_color:
                self.__x_axis_font_color = x_axis_font_color
                widget_color_change_req = True

        if y_axis_data_font_color is not None:
            Validate._isValidColor(y_axis_data_font_color, "y_axis_data_font_color")
            if y_axis_data_font_color != self.__y_axis_data_font_color:
                self.__y_axis_data_font_color = y_axis_data_font_color
                widget_color_change_req = True

        if x_axis_data_font_color is not None:
            Validate._isValidColor(x_axis_data_font_color, "x_axis_data_font_color")
            if x_axis_data_font_color != self.__x_axis_data_font_color:
                self.__x_axis_data_font_color = x_axis_data_font_color
                widget_color_change_req = True

        if x_axis_section_color is not None:
            Validate._isValidColor(x_axis_section_color, "x_axis_section_color")
            if x_axis_section_color != self.__x_axis_section_color:
                self.__x_axis_section_color = x_axis_section_color
                chart_sections_color_change_req = True

        if y_axis_section_color is not None:
            Validate._isValidColor(y_axis_section_color, "y_axis_section_color")
            if y_axis_section_color != self.__y_axis_section_color:
                self.__y_axis_section_color = y_axis_section_color
                chart_sections_color_change_req = True

        if y_axis_section_style is not None:
            Validate._isValidSectionStyle(y_axis_section_style, "y_axis_section_style")
            if y_axis_section_style != self.__y_axis_section_style:
                self.__y_axis_section_style = y_axis_section_style
                chart_sections_change_req = True

        if x_axis_section_style is not None:
            Validate._isValidSectionStyle(x_axis_section_style, "x_axis_section_style")
            if x_axis_section_style != self.__x_axis_section_style:
                self.__x_axis_section_style = x_axis_section_style
                chart_sections_change_req = True

        if y_axis_section_style_type is not None:
            Validate._isValidStyleType(y_axis_section_style_type, "y_axis_section_style_type")
            if y_axis_section_style_type != self.__y_axis_section_style_type:
                self.__y_axis_section_style_type = y_axis_section_style_type
                chart_sections_change_req = True

        if x_axis_section_style_type is not None:
            Validate._isValidStyleType(x_axis_section_style_type, "x_axis_section_style_type")
            if x_axis_section_style_type != self.__x_axis_section_style_type:
                self.__x_axis_section_style_type = x_axis_section_style_type
                chart_sections_change_req = True

        if y_axis_label_count is not None:
            Validate._isInt(y_axis_label_count, "y_axis_label_count")
            if y_axis_label_count != self.__y_axis_label_count:
                if y_axis_label_count == 0 or self.__y_axis_label_count == 0:
                    chart_reset_req = True
                self.__y_axis_label_count = y_axis_label_count
                chart_y_labels_change_req = True
                widget_color_change_req = True

        if x_axis_section_count is not None:
            Validate._isInt(x_axis_section_count, "x_axis_section_count")
            if x_axis_section_count != self.__x_axis_section_count:
                self.__x_axis_section_count = x_axis_section_count
                chart_sections_change_req = True

        if y_axis_section_count is not None:
            Validate._isInt(y_axis_section_count, "y_axis_section_count")
            if y_axis_section_count != self.__y_axis_section_count:
                self.__y_axis_section_count = y_axis_section_count
                chart_sections_change_req = True

        if x_axis_data_position is not None:
            Validate._isValidDataPostion(x_axis_data_position, "x_axis_data_position")
            if x_axis_data_position != self.__x_axis_data_position:
                self.__x_axis_data_position = x_axis_data_position
                chart_reset_req = True

        if y_axis_data_position is not None:
            Validate._isValidDataPostion(y_axis_data_position, "y_axis_data_position")
            if y_axis_data_position != self.__y_axis_data_position:
                self.__y_axis_data_position = y_axis_data_position
                chart_reset_req = True

        if y_axis_data is not None:
            if y_axis_data != self.__y_axis_data:
                self.__y_axis_data = y_axis_data
                chart_reset_req = True

        if x_axis_values is not None:
            if x_axis_values != self.__x_axis_values:
                Validate._isValidXAxisValues(x_axis_values, "x_axis_values")
                if self.__x_axis_values_handle_by == "label_indices":
                    if x_axis_display_values_indices is not None:
                        Validate._isValidXAxisIndices(
                            x_axis_values,
                            x_axis_display_values_indices,
                            "x_axis_display_values_indices"
                        )
                    else:
                        Validate._isValidXAxisIndices(
                            x_axis_values,
                            self.__x_axis_display_values_indices,
                            "x_axis_display_values_indices"
                        )
                if len(x_axis_values) != len(self.__x_axis_values):
                    chart_reset_req = True
                elif Utils._get_max_required_label_width(
                        x_axis_values, self.__axis_font_style
                ) != self.__x_value_req_width_space:
                    chart_reset_req = True
                else:
                    chart_x_values_change_req = True
                self.__x_axis_values = x_axis_values

        if x_axis_display_values_indices is not None:
            if x_axis_values is None:
                Validate._isValidXAxisIndices(
                    self.__x_axis_values,
                    x_axis_display_values_indices,
                    "x_axis_display_values_indices"
                )
            self.__x_axis_values_handle_by = "label_indices"
            x_axis_display_values_indices = Utils._sort_tuple(x_axis_display_values_indices)
            if x_axis_display_values_indices != self.__x_axis_display_values_indices:
                self.__x_axis_display_values_indices = x_axis_display_values_indices
                chart_x_labels_change_req = True
                widget_color_change_req = True
                widget_font_change_req = True

        elif x_axis_label_count is not None:
            Validate._isValidXAxisLabelCount(x_axis_label_count, "x_axis_label_count")
            self.__x_axis_values_handle_by = "label_count"
            if x_axis_label_count != self.__x_axis_label_count:
                if x_axis_label_count == 0 or self.__x_axis_label_count == 0:
                    chart_reset_req = True
                self.__x_axis_label_count = x_axis_label_count
                chart_x_labels_change_req = True
                widget_color_change_req = True
                widget_font_change_req = True

        if pointer_color is not None:
            Validate._isValidColor(pointer_color, "pointer_color")
            self.__pointer_color = pointer_color
            widget_color_change_req = True

        if pointing_callback_function is not None:
            Validate._isValidFunction(pointing_callback_function, "pointing_callback_function")
            self.__pointing_callback_function = pointing_callback_function

        if pointing_values_precision is not None:
            Validate._isInt(pointing_values_precision, "pointing_values_precision")
            self.__pointing_values_precision = pointing_values_precision

        if pointer_lock is not None:
            Validate._isValidPointerState_Lock(pointer_lock, "pointer_lock")
            self.__pointer_lock = pointer_lock

        if pointer_state is not None:
            Validate._isValidPointerState_Lock(pointer_state, "pointer_state")
            self.__pointer_state = pointer_state
            pointer_state_change_req = True

        if pointer_size is not None:
            Validate._isInt(pointer_size, "pointer_size")
            self.__pointer_size = pointer_size
            pointer_size_change_req = True

        if x_axis_point_spacing is not None:
            Validate._isValidXAxisPointSpacing(x_axis_point_spacing, "x_axis_point_spacing")
            if x_axis_point_spacing == "auto":
                if self.__x_axis_point_spacing_handle_by != "auto":
                    self.__x_axis_point_spacing_handle_by = "auto"
                    reshow_data_req = True
            elif self.__x_axis_point_spacing != x_axis_point_spacing:
                self.__x_axis_point_spacing_handle_by = "manual"
                self.__x_axis_point_spacing = x_axis_point_spacing
                reshow_data_req = True

        if chart_reset_req:
            self.__destroy_x_axis_labels()
            self.__destroy_y_axis_labels()
            self.__destroy_x_y_sections()
            self.__configure_required_widget_size()
            self.__configure_x_axis_point_spacing()
            self.__configure_x_axis_labels_info()
            self.__create_x_axis_labels()
            self.__set_x_axis_values()
            self.__create_y_axis_labels()
            self.__set_y_axis_values()
            self.__create_y_axis_sections()
            self.__create_x_axis_sections()
            self.__set_x_y_axis_data_texts()
            self.__set_pointer_state()
            self.__set_pointer_size()
            self.__set_widgets_fonts()
            self.__set_widgets_colors()
            self.__place_widgets()
            self.__reset_chart_info()
            self.__reshow_data()

        if chart_x_labels_change_req:
            self.__configure_x_axis_labels_info()
            self.__destroy_x_axis_labels()
            self.__create_x_axis_labels()
            self.__set_x_axis_values()

        elif chart_y_labels_change_req:
            self.__destroy_y_axis_labels()
            self.__create_y_axis_labels()
            self.__set_y_axis_values()

        if chart_x_values_change_req:
            self.__set_x_axis_values()

        if chart_sections_change_req or chart_sections_color_change_req:
            self.__destroy_x_y_sections()
            self.__create_y_axis_sections()
            self.__create_x_axis_sections()

        if widget_color_change_req:
            self.__set_widgets_colors()

        if widget_size_change_req:
            self.__set_pointer_size()

        if reshow_data_req:
            self.__configure_x_axis_point_spacing()
            self.__reshow_data()

        if pointer_size_change_req:
            self.__set_pointer_size()

        if pointer_state_change_req:
            self.__set_pointer_state()

        if widget_font_change_req:
            self.__set_widgets_fonts()

    def __reset_chart_info(self) -> None:
        """
        Reset the chart information and clear the canvas.

        This method deletes all items on the canvas and recalculates the real width and real height of the chart.
        """

        self.__output_canvas.delete("all")
        self.__real_width = self.__width - (
                self.__y_value_req_width_space + self.__axis_size + self.__x_axis_data_req_width_space_top +
                self.__y_axis_data_req_width_space_side + (self.__x_value_req_width_space / 2) +
                self.__x_special_width_space + self.__x_space
        )

        self.__const_real_width = self.__real_width
        self.__real_height = self.__height - (
                self.__y_axis_data_req_height_space_top + self.__axis_size + self.__x_value_req_height_space +
                self.__x_axis_data_req_height_space_side + (self.__y_value_req_height_space / 2) +
                self.__y_special_height_space + self.__y_space
        )
        self.__real_height = self.__real_height

        self.__const_real_height = self.__real_height

        self.__output_canvas.place(y=0, x=0, height=self.__const_real_height, width=self.__const_real_width)
        self.__place_x = 0

    def __reset_lines_info(self) -> None:
        """
        Reset the information for all lines in the chart.

        This method calls the __reset() method for each line object stored in the __lines list.
        """

        for line in self.__lines:
            line._Line__reset()

    def __reshow_data(self) -> None:
        """
        Re-shows data on the chart.

        This method recalculates the chart info, ensures that the chart can support the maximum amount of data to be
        shown, resets each line with the latest data, and then displays the data for each line.
        """

        lines_values = [len(line._Line__data) for line in self.__lines]
        self.__reset_chart_info()

        if len(lines_values) > 0:
            maximum_data = max(lines_values)
            max_support = int(self.__const_real_width / self.__x_axis_point_spacing) + 1

            for line in self.__lines:
                if maximum_data > max_support:
                    line._Line__temp_data = line._Line__data[maximum_data - max_support::]
                else:
                    line._Line__temp_data = line._Line__data
                line._Line__reset()

            lines = self.__lines
            self.lines = []

            for line in lines:
                self.show_data(line=line, data=line._Line__temp_data)

    def show_data(self, line: Line, data: List[Union[int, float]]) -> None:
        """
        Show data on the chart for the given line.

        Args:
            line (Line): The line object to which the data belongs.
            data (List[Union[int, float]]): The list of data points to be displayed.

        Raises:
            ValueError: If the provided line object is not valid or not found in the chart.

        This method adds the provided data to the line's existing data, adjusts the display of the chart accordingly,
        and shows the data points on the chart. It also handles various styles for displaying the data points,
        such as dashed or dotted lines, and highlights for individual data points.
        """

        Validate._isValidLine(line, "line")
        Validate._isValidData(data, "data")

        re_show_data = False
        if line not in self.__lines:
            Validate._invalidLine(line)

        line._Line__data += data

        if line._Line__visibility:

            for d in data:

                x_start = line._Line__x_end
                y_start = line._Line__y_end

                line._Line__x_end += self.__x_axis_point_spacing

                if d >= 0:
                    d = d - self.__y_axis_min_value
                    line._Line__y_end = self.__const_real_height - (
                            d / self.__y_axis_values_gap * self.__const_real_height)
                else:
                    d = abs(d) + self.__y_axis_max_value
                    line._Line__y_end = (d / self.__y_axis_values_gap * self.__const_real_height)
                line._Line__y_end += (line._Line__size / 2)

                if round(line._Line__x_end) > round(self.__real_width) and self.__real_width < self.__width * 5:
                    self.__place_x -= self.__x_axis_point_spacing

                    self.__output_canvas.place(
                        x=self.__place_x,
                        width=self.__real_width + self.__x_axis_point_spacing
                    )

                    self.__real_width += self.__x_axis_point_spacing

                elif self.__real_width > self.__width * 5:
                    re_show_data = True
                    break

                if line._Line__fill == "enabled":
                    points_of_polygon = [
                        x_start, y_start,
                        line._Line__x_end, line._Line__y_end,
                        line._Line__x_end, self.__const_real_height,
                        x_start, self.__const_real_height
                    ]
                    self.__output_canvas.create_polygon(
                        points_of_polygon, fill=line._Line__fill_color
                    )

                if line._Line__style == "dashed":
                    dash_width = line._Line__style_type[0]
                    space_width = line._Line__style_type[1]
                    total_width = dash_width + space_width
                    real_x_axis_point_spacing = ((abs(y_start - line._Line__y_end) ** 2) + (
                            self.__x_axis_point_spacing ** 2)) ** (1 / 2)
                    dash_count = real_x_axis_point_spacing / (dash_width + space_width)
                    total_change_x = (line._Line__x_end - x_start)
                    total_change_y = (line._Line__y_end - y_start)
                    dash_change_percentage = dash_width / total_width
                    space_change_percentage = space_width / total_width
                    change_x = (total_change_x / dash_count)
                    change_y = (total_change_y / dash_count)
                    dash_change_x = change_x * dash_change_percentage
                    dash_change_y = change_y * dash_change_percentage
                    space_change_x = change_x * space_change_percentage
                    space_change_y = change_y * space_change_percentage
                    dashed_x_start = x_start
                    dashed_y_start = y_start
                    if y_start > line._Line__y_end:
                        line_going = "to_up"
                    else:
                        line_going = "to_down"
                    while line._Line__x_end > dashed_x_start:
                        dashed_x_end = dashed_x_start + dash_change_x
                        dashed_y_end = dashed_y_start + dash_change_y
                        if dashed_x_end > line._Line__x_end:
                            dashed_x_end = dashed_x_end - (dashed_x_end - line._Line__x_end)
                        if dashed_y_end <= line._Line__y_end and line_going == "to_up":
                            dashed_y_end = dashed_y_end - (dashed_y_end - line._Line__y_end)
                        if dashed_y_end > line._Line__y_end and line_going == "to_down":
                            dashed_y_end = dashed_y_end - (dashed_y_end - line._Line__y_end)
                        self.__output_canvas.create_line(
                            dashed_x_start, dashed_y_start,
                            dashed_x_end, dashed_y_end,
                            fill=line._Line__color, width=line._Line__size
                        )
                        dashed_x_start += dash_change_x + space_change_x
                        dashed_y_start += dash_change_y + space_change_y

                elif line._Line__style == "dotted":
                    circle_size = line._Line__style_type[0]
                    space_width = line._Line__style_type[1]
                    total_width = circle_size + space_width
                    real_x_axis_point_spacing = ((abs(y_start - line._Line__y_end) ** 2) + (
                            self.__x_axis_point_spacing ** 2)) ** (1 / 2)
                    circle_count = real_x_axis_point_spacing / (circle_size + space_width)
                    total_change_x = (line._Line__x_end - x_start)
                    total_change_y = (line._Line__y_end - y_start)
                    circle_change_percentage = circle_size / total_width * 100
                    space_change_percentage = space_width / total_width * 100
                    circle_change_x = (total_change_x / circle_count) / 100 * circle_change_percentage
                    circle_change_y = (total_change_y / circle_count) / 100 * circle_change_percentage
                    space_change_x = (total_change_x / circle_count) / 100 * space_change_percentage
                    space_change_y = (total_change_y / circle_count) / 100 * space_change_percentage
                    dotted_x_start = x_start
                    dotted_y_start = y_start

                    while line._Line__x_end > dotted_x_start:
                        self.__output_canvas.create_oval(
                            dotted_x_start - circle_size / 2,
                            dotted_y_start - circle_size / 2,
                            dotted_x_start + circle_size - circle_size / 2,
                            dotted_y_start + circle_size - circle_size / 2,
                            fill=line._Line__color, outline=line._Line__color
                        )
                        dotted_x_start += circle_change_x + space_change_x
                        dotted_y_start += circle_change_y + space_change_y

                elif line._Line__style == "normal":
                    self.__output_canvas.create_line(
                        x_start, y_start,
                        line._Line__x_end, line._Line__y_end,
                        fill=line._Line__color, width=line._Line__size
                    )

                if line._Line__point_highlight == "enabled" and line._Line__point_highlight_size > 0:
                    highlight_size = line._Line__point_highlight_size / 2
                    self.__output_canvas.create_oval(
                        line._Line__x_end - highlight_size,
                        line._Line__y_end - highlight_size,
                        line._Line__x_end + highlight_size,
                        line._Line__y_end + highlight_size,
                        fill=line._Line__point_highlight_color,
                        outline=line._Line__point_highlight_color
                    )

                    self.__output_canvas.create_oval(
                        x_start - highlight_size,
                        y_start - highlight_size,
                        x_start + highlight_size,
                        y_start + highlight_size,
                        fill=line._Line__point_highlight_color,
                        outline=line._Line__point_highlight_color
                    )

            if re_show_data:
                self.__reshow_data()

    def __hide_pointer(self, event_: tkinter.Event) -> None:
        """
        Hides the pointer widget from the GUI canvas.

        Args:
            event_ (tkinter.Event): The event_ triggering the pointer hiding.
        """

        self.__pointer.place_forget()

    def __return_pointed_values(self, event_: tkinter.Event) -> None:
        """
        Returns the values pointed by the user's mouse cursor.

        Args:
            event_ (tkinter.Event): The mouse event_ containing cursor position.
        """

        def round_x(x) -> Union[int, float]:
            """
            Rounds the x-coordinate to the nearest x-axis point spacing.

            Args:
                x (float): The x-coordinate to be rounded.

            Returns:
                float: The rounded x-coordinate.
            """

            x_: Union[int, float] = (x // self.__x_axis_point_spacing) * self.__x_axis_point_spacing
            if x % self.__x_axis_point_spacing >= self.__x_axis_point_spacing / 2:
                x_ += self.__x_axis_point_spacing
            return x_

        max_sup = int(self.__const_real_width / self.__x_axis_point_spacing)
        max_view = max_sup + 1
        values = []
        try:
            max_data = max([len(line._Line__data) for line in self.__lines])
            if self.__pointer_lock == "enabled":
                event_x = round_x(event_.x)
            else:
                event_x = event_.x
            if self.__const_real_width >= self.__real_width:
                event_x_converted = event_x
            else:
                event_x_converted = event_x - (self.__x_axis_point_spacing * (max_data - max_view))
            width_x = self.__const_real_width - (self.__const_real_width - (self.__x_axis_point_spacing * max_sup))
            index_float = ((event_x_converted / width_x) * max_sup)
            index_round_float = round(index_float)
            if event_x == self.__real_width:
                self.__pointer.place(x=((event_x - self.__pointer_size / 2) - 2), y=0)
            else:
                self.__pointer.place(x=((event_x - self.__pointer_size / 2) + 1), y=0)
            index_int = int(index_float)
            x_index = index_int
            if index_float != 0 and index_float == index_int:
                x_index -= 1
            for line in self.__lines:
                line._Line__ret_data = line._Line__data + (max_data - len(line._Line__data)) * [None]
                line._Line__ret_data = line._Line__ret_data[-int(max_view)::]
                line._Line__ret_data = line._Line__ret_data + (int(max_view) - len(line._Line__ret_data)) * [None]
            for line in self.__lines:
                try:
                    if self.__pointer_lock == "enabled":
                        value = line._Line__ret_data[int(index_round_float)]
                    else:
                        if index_float == index_int:
                            value = line._Line__ret_data[index_int]
                        else:
                            value = line._Line__ret_data[index_int]
                            value = value + (
                                ((line._Line__ret_data[index_int + 1] - value) * (index_float - index_int)))
                    values.append(Utils._format_float_with_precision(float(value), self.__pointing_values_precision))
                except:
                    values.append("null")
            if self.__pointing_callback_function is not None:
                try:
                    self.__pointing_callback_function(self.__x_axis_values[x_index], values)
                except:
                    self.__pointing_callback_function("null", values)
        except:
            pass

    def place(
            self,
            x: int = None,
            y: int = None,
            rely: Union[int, float] = None,
            relx: Union[int, float] = None,
            anchor: Literal[
                "n", "e", "s", "w", "ne", "nw", "se", "sw", "center"
            ] = None) -> None:
        """
        Place the widget at a specific position within its parent widget.

        Args:
            x (int): The x-coordinate of the upper-left corner of the widget.
            y (int): The y-coordinate of the upper-left corner of the widget.
            rely (Union[int, float]): The vertical relative position of the widget, ranging from 0 to 1.
            relx (Union[int, float]): The horizontal relative position of the widget, ranging from 0 to 1.
            anchor (str): Specifies which part of the widget is to be placed at the given coordinates.
        """

        self.__main_frame.place(x=x, y=y, rely=rely, relx=relx, anchor=anchor)
        self.__place_info_x = x
        self.__place_info_y = y
        self.__place_info_rely = rely
        self.__place_info_relx = relx
        self.__place_info_anchor = anchor

    def pack(
            self,
            pady: int = None,
            padx: int = None,
            before: Any = None,
            after: Any = None,
            side: Literal["top", "bottom", "left", "right"] = None,
            anchor: Literal[
                "n", "e", "s", "w", "ne", "nw", "se", "sw", "center"
            ] = None) -> None:
        """
        Pack the widget into its parent widget.

        Args:
            pady (int): Vertical padding.
            padx (int): Horizontal padding.
            before (Any): Widget before which this widget will be packed.
            after (Any): Widget after which this widget will be packed.
            side (str): Specifies which side of the parent widget to pack against.
            anchor (str): Specifies where the widget will be placed if the available area is larger than the widget's 
                        requested size.
        """

        self.__main_frame.pack(
            pady=pady, padx=padx, before=before,
            after=after, side=side, anchor=anchor
        )
        self.__pack_info_pady = pady
        self.__pack_info_padx = padx
        self.__pack_info_before = before
        self.__pack_info_after = after
        self.__pack_info_side = side
        self.__pack_info_anchor = anchor

    def grid(
            self,
            column: int = None,
            columnspan: int = None,
            padx: int = None,
            pady: int = None,
            row: int = None,
            rowspan: int = None,
            sticky: Literal[
                "n", "e", "s", "w", "ne", "nw", "se", "sw"
            ] = None) -> None:
        """
        Grid the widget into its parent widget.

        Args:
            column (int): The column in which to place the widget.
            columnspan (int): The number of columns the widget occupies.
            padx (int): Horizontal padding.
            pady (int): Vertical padding.
            row (int): The row in which to place the widget.
            rowspan (int): The number of rows the widget occupies.
            sticky (str): Specifies how the widget should be expanded to fill the cell.
        """

        self.__main_frame.grid(
            column=column, columnspan=columnspan,
            padx=padx, pady=pady, row=row,
            rowspan=rowspan, sticky=sticky
        )
        self.__grid_info_column = column
        self.__grid_info_columnspan = columnspan
        self.__grid_info_padx = padx
        self.__grid_info_pady = pady
        self.__grid_info_row = row
        self.__grid_info_rowspan = rowspan
        self.__grid_info_sticky = sticky

    def place_forget(self) -> None:
        """
        Remove the widget from the grid.
        """

        self.__main_frame.place_forget()
        self.__place_info_x = None
        self.__place_info_y = None
        self.__place_info_rely = None
        self.__place_info_relx = None
        self.__place_info_anchor = None

    def pack_forget(self) -> None:
        """
        Remove the widget from the pack.
        """

        self.__main_frame.pack_forget()
        self.__pack_info_pady = None
        self.__pack_info_padx = None
        self.__pack_info_before = None
        self.__pack_info_after = None
        self.__pack_info_side = None
        self.__pack_info_anchor = None

    def grid_forget(self) -> None:
        """
        Remove the widget from the grid.
        """

        self.__main_frame.grid_forget()
        self.__grid_info_column = None
        self.__grid_info_columnspan = None
        self.__grid_info_padx = None
        self.__grid_info_pady = None
        self.__grid_info_row = None
        self.__grid_info_rowspan = None
        self.__grid_info_sticky = None

    def set_line_visibility(self, line: Line, state: bool) -> None:
        """
        Hide or show a specific line.

        Args:
            line (Line): The line object to hide or show.
            state (bool): The hide/show state of the line.
        """

        Validate._isValidLine(line, "line")
        Validate._isBool(state, "state")
        if line._Line__visibility != state or self.__visibility != state:
            line._Line__visibility = state
            self.__reshow_data()

    def set_lines_visibility(self, state: bool) -> None:
        """
        Hide or show all lines.

        Args:
            state (bool): The hide/show state of all lines.
        """

        Validate._isBool(state, "state")
        self.__visibility = state
        if state is False:
            self.__output_canvas.place_forget()
        for line in self.__lines:
            line._Line__visibility = state
        self.__reshow_data()

    def reset(self) -> None:
        """
        Reset the chart and lines to their initial state.
        """

        self.__reset_chart_info()
        self.__reset_lines_info()

    def __apply_line_configuration(self) -> None:
        """
        Apply changes to the lines and redraw the chart.
        """

        self.__reshow_data()

    def cget(
            self,
            attribute_name: Literal[
                "width", "height", "axis_color", "bg_color", "fg_color",
                "data_font_style", "axis_font_style", "y_axis_precision",
                "y_axis_data", "y_axis_label_count", "y_axis_values",
                "y_axis_font_color", "y_axis_data_font_color",
                "y_axis_data_position", "y_axis_section_count",
                "y_axis_section_style", "y_axis_section_style_type",
                "y_axis_section_color", "x_axis_data", "x_axis_label_count",
                "x_axis_values", "x_axis_display_values_indices",
                "x_axis_font_color", "x_axis_data_font_color",
                "x_axis_data_position", "x_axis_section_count",
                "x_axis_section_style", "x_axis_section_style_type",
                "x_axis_section_color", "x_axis_point_spacing",
                "y_space", "x_space", "pointer_state",
                "pointing_callback_function", "pointer_color",
                "pointing_values_precision", "pointer_lock",
                "pointer_size", "__all__"
            ] = "__all__") -> Any:
        """
        Get the value of the specified attribute.

        Args:
            attribute_name (str): The name of the attribute to get. __all__ (str): all the attributes as a dict

        Returns:
            Any: The value of the specified attribute.
        """

        if attribute_name == "width":
            return self.__width
        if attribute_name == "height":
            return self.__height
        if attribute_name == "axis_color":
            return self.__axis_color
        if attribute_name == "bg_color":
            return self.__bg_color
        if attribute_name == "fg_color":
            return self.__fg_color
        if attribute_name == "data_font_style":
            return self.__data_font_style
        if attribute_name == "axis_font_style":
            return self.__axis_font_style
        if attribute_name == "y_axis_precision":
            return self.__y_axis_precision
        if attribute_name == "y_axis_data":
            return self.__y_axis_data
        if attribute_name == "y_axis_label_count":
            return self.__y_axis_label_count
        if attribute_name == "y_axis_values":
            return self.__y_axis_values
        if attribute_name == "y_axis_font_color":
            return self.__y_axis_font_color
        if attribute_name == "y_axis_data_font_color":
            return self.__y_axis_data_font_color
        if attribute_name == "y_axis_data_position":
            return self.__y_axis_data_position
        if attribute_name == "y_axis_section_count":
            return self.__y_axis_section_count
        if attribute_name == "y_axis_section_style":
            return self.__y_axis_section_style
        if attribute_name == "y_axis_section_style_type":
            return self.__y_axis_section_style_type
        if attribute_name == "y_axis_section_color":
            return self.__y_axis_section_color
        if attribute_name == "x_axis_data":
            return self.__x_axis_data
        if attribute_name == "x_axis_label_count":
            return self.__x_axis_label_count
        if attribute_name == "x_axis_values":
            return self.__x_axis_values
        if attribute_name == "x_axis_display_values_indices":
            return self.__x_axis_display_values_indices
        if attribute_name == "x_axis_font_color":
            return self.__x_axis_font_color
        if attribute_name == "x_axis_data_font_color":
            return self.__x_axis_data_font_color
        if attribute_name == "x_axis_data_position":
            return self.__x_axis_data_position
        if attribute_name == "x_axis_section_count":
            return self.__x_axis_section_count
        if attribute_name == "x_axis_section_style":
            return self.__x_axis_section_style
        if attribute_name == "x_axis_section_style_type":
            return self.__x_axis_section_style_type
        if attribute_name == "x_axis_section_color":
            return self.__x_axis_section_color
        if attribute_name == "x_axis_point_spacing":
            return self.__x_axis_point_spacing
        if attribute_name == "y_space":
            return self.__y_space
        if attribute_name == "x_space":
            return self.__x_space
        if attribute_name == "pointer_state":
            return self.__pointer_state
        if attribute_name == "pointing_callback_function":
            return self.__pointing_callback_function
        if attribute_name == "pointer_color":
            return self.__pointer_color
        if attribute_name == "pointing_values_precision":
            return self.__pointing_values_precision
        if attribute_name == "pointer_lock":
            return self.__pointer_lock
        if attribute_name == "pointer_size":
            return self.__pointer_size

        if attribute_name == "__all__":
            return {
                "width": self.__width,
                "height": self.__height,
                "axis_color": self.__axis_color,
                "bg_color": self.__bg_color,
                "fg_color": self.__fg_color,
                "data_font_style": self.__data_font_style,
                "axis_font_style": self.__axis_font_style,
                "y_axis_precision": self.__y_axis_precision,
                "y_axis_data": self.__y_axis_data,
                "y_axis_label_count": self.__y_axis_label_count,
                "y_axis_values": self.__y_axis_values,
                "y_axis_font_color": self.__y_axis_font_color,
                "y_axis_data_font_color": self.__y_axis_data_font_color,
                "y_axis_data_position": self.__y_axis_data_position,
                "y_axis_section_count": self.__y_axis_section_count,
                "y_axis_section_style": self.__y_axis_section_style,
                "y_axis_section_style_type": self.__y_axis_section_style_type,
                "y_axis_section_color": self.__y_axis_section_color,
                "x_axis_data": self.__x_axis_data,
                "x_axis_label_count": self.__x_axis_label_count,
                "x_axis_values": self.__x_axis_values,
                "x_axis_display_values_indices": self.__x_axis_display_values_indices,
                "x_axis_font_color": self.__x_axis_font_color,
                "x_axis_data_font_color": self.__x_axis_data_font_color,
                "x_axis_data_position": self.__x_axis_data_position,
                "x_axis_section_count": self.__x_axis_section_count,
                "x_axis_section_style": self.__x_axis_section_style,
                "x_axis_section_style_type": self.__x_axis_section_style_type,
                "x_axis_section_color": self.__x_axis_section_color,
                "x_axis_point_spacing": self.__x_axis_point_spacing,
                "y_space": self.__y_space,
                "x_space": self.__x_space,
                "pointer_state": self.__pointer_state,
                "pointing_callback_function": self.__pointing_callback_function,
                "pointer_color": self.__pointer_color,
                "pointing_values_precision": self.__pointing_values_precision,
                "pointer_lock": self.__pointer_lock,
                "pointer_size": self.__pointer_size
            }

        Validate._invalidCget(attribute_name)

    def get_line_visibility(self, line: Line):
        """
        Get the visibility state of a specific line.

        Args:
            line (Line): The Line object for which visibility is queried.

        Returns:
            bool: True if the line is visible, False otherwise.

        Raises:
            ValueError: If the provided line object is not valid or not found in the chart.
        """

        Validate._isValidLine(line, "line")
        if line in self.__lines:
            return line._Line__visibility
        else:
            Validate._invalidLine(line)

    def place_info(
            self,
            attribute_name: Literal[
                "x", "y", "relx", "rely", "anchor", "__all__"
            ] = "__all__") -> Any:
        """
        Get the value of the specified place info.

        Args:
            attribute_name (str): The name of the attribute to get.

        Returns:
            Any: The value of the specified attribute.
        """

        if attribute_name == "x":
            return self.__place_info_x
        if attribute_name == "y":
            return self.__place_info_y
        if attribute_name == "relx":
            return self.__place_info_relx
        if attribute_name == "rely":
            return self.__place_info_rely
        if attribute_name == "anchor":
            return self.__place_info_anchor

        if attribute_name == "__all__":
            return {
                "x": self.__place_info_x,
                "y": self.__place_info_y,
                "relx": self.__place_info_relx,
                "rely": self.__place_info_rely,
                "anchor": self.__place_info_anchor
            }

        Validate._invalidCget(attribute_name)

    def pack_info(
            self,
            attribute_name: Literal[
                "padx", "pady", "before", "after",
                "side", "anchor", "__all__"
            ] = "__all__") -> Any:
        """
        Get the value of the specified pack info.

        Args:
            attribute_name (str): The name of the attribute to get.

        Returns:
            Any: The value of the specified attribute.
        """

        if attribute_name == "padx":
            return self.__pack_info_padx
        if attribute_name == "pady":
            return self.__pack_info_pady
        if attribute_name == "before":
            return self.__pack_info_before
        if attribute_name == "after":
            return self.__pack_info_after
        if attribute_name == "side":
            return self.__pack_info_side
        if attribute_name == "anchor":
            return self.__pack_info_anchor

        if attribute_name == "__all__":
            return {
                "padx": self.__pack_info_padx,
                "pady": self.__pack_info_pady,
                "before": self.__pack_info_before,
                "after": self.__pack_info_after,
                "side": self.__pack_info_side,
                "anchor": self.__pack_info_anchor
            }

        Validate._invalidCget(attribute_name)

    def grid_info(
            self,
            attribute_name: Literal[
                "row", "column", "rowspan", "columnspan",
                "padx", "pady", "sticky", "__all__"
            ] = "__all__") -> Any:
        """
        Get the value of the specified grid info.

        Args:
            attribute_name (str): The name of the attribute to get.

        Returns:
            Any: The value of the specified attribute.
        """

        if attribute_name == "row":
            return self.__grid_info_row
        if attribute_name == "column":
            return self.__grid_info_column
        if attribute_name == "rowspan":
            return self.__grid_info_rowspan
        if attribute_name == "columnspan":
            return self.__grid_info_columnspan
        if attribute_name == "padx":
            return self.__grid_info_padx
        if attribute_name == "pady":
            return self.__grid_info_pady
        if attribute_name == "sticky":
            return self.__grid_info_sticky

        if attribute_name == "__all__":
            return {
                "row": self.__grid_info_row,
                "column": self.__grid_info_column,
                "rowspan": self.__grid_info_rowspan,
                "columnspan": self.__grid_info_columnspan,
                "padx": self.__grid_info_padx,
                "pady": self.__grid_info_pady,
                "sticky": self.__grid_info_sticky
            }

        Validate._invalidCget(attribute_name)
