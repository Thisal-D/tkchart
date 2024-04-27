from typing import Tuple, Literal, Any
from .Validate import Validate


class Line:
    def __init__(
            self,
            master: Any = None,
            color: str = "#768df1",
            size: int = 1,
            style: Literal["normal", "dashed", "dotted"] = "normal",
            style_type: Tuple[int, int] = (4, 4),
            point_highlight: Literal["enabled", "disabled"] = "disabled",
            point_highlight_size: int = 4,
            point_highlight_color: str = "#768df1",
            fill: Literal["enabled", "disabled"] = "disabled",
            fill_color: str = "#5d6db6",
            *args: Any) -> None:
        """
        Initialize a Line object.

        Args:
            master (LineChart): The master object.
            color (str): The color of the line.
            size (int): The size/thickness of the line.
            style (str): The style of the line (e.g., 'normal', 'dashed', 'dotted').
            style_type (Tuple[int, int]): The style type for dashed or dotted lines.
            point_highlight (str): Whether point highlighting is enabled or disabled.
            point_highlight_size (int): The size of points used for highlighting.
            point_highlight_color (str): The color of points used for highlighting.
            fill (str): Whether fill for the line is enabled or disabled.
            fill_color (str): The color of the fill for the line.
        """

        if master is None:
            if len(args) != 0:
                master = args[0]
            else:
                Validate._MasterAttNotProvideForLine("master")

        Validate._isValidLineChart(master, "master")
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
        self.__x_end = self.__master._LineChart__x_axis_point_spacing * -1
        self.__data = []
        self.__temp_data = []
        self.__ret_data = []
        self.__visibility = self.__master._LineChart__visibility
        self.__style = style
        self.__style_type = style_type
        self.__point_highlight = point_highlight
        self.__point_highlight_size = point_highlight_size
        self.__point_highlight_color = point_highlight_color
        self.__fill = fill
        self.__fill_color = fill_color

        self.__master._LineChart__lines.append(self)

    def configure(
            self,
            color: str = None,
            size: int = None,
            style: Literal["normal", "dashed", "dotted"] = None,
            style_type: Tuple[int, int] = None,
            point_highlight: Literal["enabled", "disabled"] = None,
            point_highlight_size: int = None,
            point_highlight_color: str = None,
            fill: Literal["enabled", "disabled"] = None,
            fill_color: str = None) -> None:
        """
        Configure attributes of the Line object.

        Args:
            color (str): The color of the line.
            size (int): The size/thickness of the line.
            style (str): The style of the line (e.g., 'normal', 'dashed', 'dotted').
            style_type (Tuple[int, int]): The style type for dashed or dotted lines.
            point_highlight (str): Whether point highlighting is enabled or disabled.
            point_highlight_size (int): The size of points used for highlighting.
            point_highlight_color (str): The color of points used for highlighting.
            fill (str): Whether fill for the line is enabled or disabled.
            fill_color (str): The color of the fill for the line.
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
            self.__master._LineChart__apply_line_configuration()

    def __reset(self) -> None:
        """
        Reset the Line object.
        """
        self.__y_end = 0
        self.__x_end = self.__master._LineChart__x_axis_point_spacing * -1
        self.__data = []

    def reset(self) -> None:
        """
        Reset the line.
        """
        self.__reset()
        self.__master._LineChart__call_reshow_data()

    def set_visible(self, state: bool) -> None:
        """
        Set the visibility of the line.

        Args:
            state (bool): True if the line should be visible, False otherwise.
        """
        Validate._isBool(state, "state")
        if self.__visibility != state:
            self.__visibility = state
            self.__master._LineChart__call_reshow_data()

    def cget(
            self,
            attribute_name: Literal[
                "master", "color", "size", "style", "style_type", "point_highlight",
                "point_highlight_size", "point_highlight_color", "fill", "fill_color",
                "__all__"]) -> Any:
        """
        Get the value of a Line attribute.

        Args:
            attribute_name (str): Name of the attribute.

        Returns:
            Any: Value of the attribute.
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
