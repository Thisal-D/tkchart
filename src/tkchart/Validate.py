from typing import Tuple, Any
from .FontStyle import FontStyle
import tkinter


class Validate:
    @staticmethod
    def _error_font(value: str) -> str:
        return FontStyle._fontStyle(value, "red", "black", "underline")

    @staticmethod
    def _var_font(value: str) -> str:
        return FontStyle._fontStyle(value, "green", "black", "italic")

    @staticmethod
    def _isTuple(value: Any, var: str) -> None:
        if type(value) is not tuple:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be tuple.')}"
            )

    @staticmethod
    def _isList(value: Any, var: str) -> None:
        if type(value) is not list:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be list.')}"
            )

    @staticmethod
    def _isInt(value: Any, var: str) -> None:
        if type(value) is not int:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be int.')}"
            )

    @staticmethod
    def _isBool(value: Any, var: str) -> None:
        if type(value) is not bool:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be bool.')}"
            )

    @staticmethod
    def _isFloat(value: Any, var: str) -> None:
        if type(value) is not float:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be float.')}"
            )

    @staticmethod
    def _isStr(value: Any, var: str) -> None:
        if type(value) is not str:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be str.')}"
            )

    @staticmethod
    def _isValidColor(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        try:
            tkinter.Label(fg=value)
        except:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be valid color. eg:- '#ff0000'/ 'red'")}'''
            )

    @staticmethod
    def _isValidFont(value: Any, var: str) -> None:
        Validate._isTuple(value, var)
        try:
            tkinter.Label(font=value)
        except:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be valid font. eg:- ('arial',10,'bold')")}'''
            )

    @staticmethod
    def _isValidFunction(value: Any, var: str) -> None:
        if not callable(value) and value is not None:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be function with two parameters or *args.")}'''
            )

    @staticmethod
    def _isValidXAxisIndices(values: Tuple[int, ...], indices: Any, var: str) -> None:
        if indices is not None:
            Validate._isTuple(indices, var)
            Validate._isValidIndices(indices, var)
            for index in indices:
                if index >= len(values):
                    raise ValueError(
                        f'''{Validate._var_font(var)} {Validate._error_font("values must be lower than length of x_axis_values.")}'''
                    )

    @staticmethod
    def _isValidXAxisLabelCount(values: Any, var: str) -> None:
        if values is not None:
            Validate._isInt(values, var)

    @staticmethod
    def _isValidStyleType(value: Any, var: str) -> None:
        Validate._isTuple(value, var)
        if len(value) == 2:
            if type(value[0]) is int and type(value[1]) is int:
                ...
            else:
                raise TypeError(
                    f'''{Validate._var_font(var)} {Validate._error_font("values must be integers.")}'''
                )
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("length must be two.")}'''
            )

    @staticmethod
    def _isValidDataPostion(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "top" or value == "side":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'top' or 'side'.")}'''
            )

    @staticmethod
    def _isValidLineStyle(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "dotted" or value == "dashed" or value == "normal":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'normal' or 'dotted' or 'dashed'.")}'''
            )

    @staticmethod
    def _isValidSectionStyle(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "dashed" or value == "normal":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'normal' or 'dashed'.")}'''
            )

    @staticmethod
    def _isValidXAxisPointSpacing(value: Any, var: str) -> None:
        if type(value) is int:
            ...
        elif type(value) is str and value == "auto":
            ...
        else:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be integer or 'auto'.")}'''
            )

    @staticmethod
    def _isValidPointerState_Lock(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "disabled" or value == "enabled":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'disabled' or 'enabled'.")}'''
            )

    @staticmethod
    def _isValidLineHighlight(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "disabled" or value == "enabled":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'disabled' or 'enabled'.")}'''
            )

    @staticmethod
    def _isValidLineFill(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "disabled" or value == "enabled":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'disabled' or 'enabled'.")}'''
            )

    @staticmethod
    def _isValidYAxisValues(value: Any, var: str) -> None:
        Validate._isTuple(value, var)
        if value == (None, None):
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be provide.")}'''
            )
        if len(value) == 2:
            if type(value[0]) is int or type(value[0]) is float and type(value[1]) is int or type(value[1]) is float:
                if value[0] < value[1]:
                    ...
                else:
                    raise ValueError(
                        f'''{Validate._var_font(var)} {Validate._error_font("first value must be less than second value.")}'''
                    )
            else:
                raise TypeError(
                    f'''{Validate._var_font(var)} {Validate._error_font("values must be integer or float.")}'''
                )
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("length must be two.")}'''
            )

    @staticmethod
    def _isValidXAxisValues(value: Any, var: str) -> None:
        if value == (None, "None", None, "None"):
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be provide.")}'''
            )
        Validate._isTuple(value, "x_axis_values")

    @staticmethod
    def _isValidLine(value: Any, var: str) -> None:
        from .Line import Line
        if type(value) is not Line:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("type must be tkchart.Line")}'''
            )

    @staticmethod
    def _isValidLineChart(value: Any, var: str) -> None:
        from .LineChart import LineChart
        if type(value) is not LineChart:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("type must be tkchart.LineChart")}'''
            )

    @staticmethod
    def _isValidData(value: Any, var: str) -> None:
        Validate._isList(value, var)
        if all(isinstance(value, (int, float)) for value in value):
            ...
        else:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("all values in the list should be either int or float.")}'''
            )

    @staticmethod
    def _isValidIndices(value: Any, var: str) -> None:
        if all(isinstance(value, int) for value in value):
            ...
        else:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("all values should be int.")}'''
            )

    @staticmethod
    def _invalidCget(var: str) -> None:
        raise ValueError(
            f'''{Validate._var_font(var)} {Validate._error_font("Invalid attribute.")}'''
        )

    @staticmethod
    def _invalidLine(line: Any) -> None:
        raise ValueError(
            f'''{Validate._var_font(str(line))} {Validate._error_font("The line is not part of this line chart.")}'''
        )

    @staticmethod
    def _MasterAttNotProvideForLine(value):
        raise ValueError(
            f'''{Validate._var_font(str(value))} {Validate._error_font("master must be provide for Line.")}'''
        )
