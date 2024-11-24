from typing import Union, Tuple, Literal
from .Validate import Validate


class CTkLine:
    def __init__(
            self,
            master: any = None,
            color: Union[Tuple[str, str], str] = ("#768df1", "#768df1"),
            size: int = 1,
            style: Literal["normal", "dashed", "dotted"] = "normal",
            style_type: Tuple[int, int] = (4, 4),
            point_highlight: Literal["enabled", "disabled"] = "disabled",
            point_highlight_size: int = 8,
            point_highlight_color: Union[Tuple[str, str], str] = ("#768df1", "#768df1"),
            fill: Literal["enabled", "disabled"] = "disabled",
            fill_color: Union[Tuple[str, str], str] = ("#bdc6ed", "#5d6db6"),
            *args: any) -> None:
        """
        Initialize a CTkLine object.

        Args:
            master (any): The master object.
            color (Union[Tuple[str, str], str]): The color of the line.
            size (int): The size/thickness of the line.
            style (str): The style of the line (e.g., 'normal', 'dashed', 'dotted').
            style_type (Tuple[int, int]): The style type for dashed or dotted lines.
            point_highlight (str): Whether point highlighting is enabled or disabled.
            point_highlight_size (int): The size of points used for highlighting.
            point_highlight_color (Union[Tuple[str, str], str]): The color of points used for highlighting.
            fill (str): Whether fill for the line is enabled or disabled.
            fill_color (Union[Tuple[str, str], str]): The color of the fill for the line.
        """

        if master is None:
            if len(args) != 0:
                master = args[0]
            else:
                Validate._MasterAttNotProvideForLine("master")

        Validate._isValidCTkLineChart(master, "master")
        Validate._isValidColor(color, "color")
        Validate._isInt(size, "size")
        Validate._isValidLineStyle(style, "style")
        Validate._isValidStyleType(style_type, "style_type")
        Validate._isValidLineHighlight(point_highlight, "point_highlight")
        Validate._isInt(point_highlight_size, "point_highlight_size")
        Validate._isValidColor(point_highlight_color, "point_highlight_color")
        Validate._isValidLineFill(fill, "fill")
        Validate._isValidColor(fill_color, "fill_color")

        self.__master = master
        self.__color = color
        self.__size = size
        self.__y_end = 0
        self.__x_end = self.__master._CTkLineChart__x_axis_point_spacing * -1
        self.__data = []
        self.__temp_data = []
        self.__ret_data = []
        self.__visibility = self.__master._CTkLineChart__visibility
        self.__style = style
        self.__style_type = style_type
        self.__point_highlight = point_highlight
        self.__point_highlight_size = point_highlight_size
        self.__point_highlight_color = point_highlight_color
        self.__fill = fill
        self.__fill_color = fill_color

        self.__master._CTkLineChart__lines.append(self)

    def configure(
            self,
            color: Union[Tuple[str, str], str] = None,
            size: int = None,
            style: Literal["normal", "dashed", "dotted"] = None,
            style_type: Tuple[int, int] = None,
            point_highlight: Literal["enabled", "disabled"] = None,
            point_highlight_size: int = None,
            point_highlight_color: Union[Tuple[str, str], str] = None,
            fill: Literal["enabled", "disabled"] = None,
            fill_color: Union[Tuple[str, str], str] = None) -> None:
        """
        Configure attributes of the CTkLine object.

        Args:
            color (Union[Tuple[str, str], str]): The color of the line.
            size (int): The size/thickness of the line.
            style (str): The style of the line (e.g., 'normal', 'dashed', 'dotted').
            style_type (Tuple[int, int]): The style type for dashed or dotted lines.
            point_highlight (str): Whether point highlighting is enabled or disabled.
            point_highlight_size (int): The size of points used for highlighting.
            point_highlight_color (Union[Tuple[str, str], str]): The color of points used for highlighting.
            fill (str): Whether fill for the line is enabled or disabled.
            fill_color (Union[Tuple[str, str], str]): The color of the fill for the line.
        """

        changes_req = False

        if color is not None:
            Validate._isValidColor(color, "color")
            self.__color = color
            changes_req = True

        if size is not None:
            Validate._isInt(size, "size")
            self.__size = size
            changes_req = True

        if style is not None:
            Validate._isValidLineStyle(style, "style")
            self.__style = style
            changes_req = True

        if style_type is not None:
            Validate._isValidStyleType(style_type, "style_type")
            self.__style_type = style_type
            changes_req = True

        if point_highlight is not None:
            Validate._isValidLineHighlight(point_highlight, "point_highlight")
            self.__point_highlight = point_highlight
            changes_req = True

        if point_highlight_size is not None:
            Validate._isInt(point_highlight_size, "point_highlight_size")
            self.__point_highlight_size = point_highlight_size
            changes_req = True

        if point_highlight_color is not None:
            Validate._isValidColor(point_highlight_color, "point_highlight_color")
            self.__point_highlight_color = point_highlight_color
            changes_req = True

        if fill is not None:
            Validate._isValidLineFill(fill, "fill")
            self.__fill = fill
            changes_req = True

        if fill_color is not None:
            Validate._isValidColor(fill_color, "fill_color")
            self.__fill_color = fill_color
            changes_req = True

        if changes_req:
            self.__master._CTkLineChart__apply_line_configuration()

    def __reset_positions(self) -> None:
        """
        Reset the Line object.
        """
       
        self.__y_end = 0
        self.__x_end = self.__master._CTkLineChart__x_axis_point_spacing * -1
        
    def __reset_data(self) -> None:
        self.__data = []
        
    def clear_data(self) -> None:
        """
        Clears the chart data, ensuring that only the relevant visible data is retained.

        This method works by checking the maximum number of data points across all lines in the chart 
        and the maximum number of visible data points. If the chart contains more data points than 
        the visible limit, the data is cropped so that only the most recent data points (up to the 
        visible limit) are kept. If the chart is already within the visible limit, the data is not altered.

        The data is trimmed from the beginning of the dataset, and the most recent points are kept.
        
        This ensures that the chart does not display more data than the allowed visible limit, 
        optimizing performance and display consistency.

        Attributes:
            self.__data: The internal list that holds all the data for the lines on the chart.

        Returns:
            None: This method modifies the internal state of the data but does not return any value.

        Example:
            line.clear_data()
        
        In this example, the data is cleaned up to ensure that only the most recent visible data 
        points are kept, improving the rendering performance and reducing memory usage.
        """
        
        maximum_data = self.__master._CTkLineChart__get_max_data_length_across_lines()
        max_visible_points = self.__master._CTkLineChart__get_max_visible_data_points()
        
        if maximum_data > max_visible_points:
            self.__data = self.__data[maximum_data - max_visible_points::]

    def reset(self) -> None:
        """
        Reset the line.
        """
        self.__reset_positions()
        self.__reset_data()
        self.__master._CTkLineChart__apply_line_configuration()

    def set_visible(self, state: bool) -> None:
        """
        Set the visibility of the line.

        Args:
            state (bool): True if the line should be visible, False otherwise.
        """
        
        Validate._isBool(state, "state")
        if self.__visibility != state:
            self.__visibility = state
            self.__master._CTkLineChart__apply_line_configuration()

    def cget(
            self,
            attribute_name: Literal[
                "master", "color", "size", "style", "style_type", "point_highlight",
                "point_highlight_size", "point_highlight_color", "fill", "fill_color",
                "__all__"]) -> any:
        """
        Get the value of a CTkLine attribute.

        Args:
            attribute_name (str): Name of the attribute.

        Returns:
            any: Value of the attribute.
        """

        if attribute_name == "master":
            return self.__master
        if attribute_name == "color":
            return self.__color
        if attribute_name == "size":
            return self.__size
        if attribute_name == "style":
            return self.__style
        if attribute_name == "style_type":
            return self.__style_type
        if attribute_name == "point_highlight":
            return self.__point_highlight
        if attribute_name == "point_highlight_size":
            return self.__point_highlight_size
        if attribute_name == "point_highlight_color":
            return self.__point_highlight_color
        if attribute_name == "fill":
            return self.__fill
        if attribute_name == "fill_color":
            return self.__fill_color

        if attribute_name == "__all__":
            return {
                "master": self.__master,
                "color": self.__color,
                "size": self.__size,
                "style": self.__style,
                "style_type": self.__style_type,
                "point_highlight": self.__point_highlight,
                "point_highlight_size": self.__point_highlight_size,
                "point_highlight_color": self.__point_highlight_color,
                "fill": self.__fill,
                "fill_color": self.__fill_color
            }
        Validate._invalidCget(attribute_name)

    def get_visibility(self) -> bool:
        """
        Get the visibility of the line.

        Returns:
            bool: True if the line is visible, False otherwise.
        """

        return self.__visibility

    def __del__(self) -> None:
        """Destructor method to delete instance attributes."""
        del self.__master
        del self.__color
        del self.__size
        del self.__y_end
        del self.__x_end
        del self.__data
        del self.__temp_data
        del self.__ret_data
        del self.__visibility
        del self.__style
        del self.__style_type
        del self.__point_highlight
        del self.__point_highlight_size
        del self.__point_highlight_color
        del self.__fill
        del self.__fill_color

    def destroy(self) -> None:
        """
        Removes the instance from its master's line chart and 
        applies the updated line configuration. Calls the destructor 
        to clean up resources.
        """
        try:
            self.__master._CTkLineChart__lines.remove(self)
            self.__master._CTkLineChart__apply_line_configuration()
        except ValueError:
            pass  # In case the line is not in the list
        finally:
            self.__del__()
