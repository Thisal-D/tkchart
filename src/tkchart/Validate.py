from .FontStyle import *
from .Exceptions import *
import tkinter

class Validate:

    def _error_font(value):
        return FontStyle._fontStyle(value, "red", "black", "underline")

    def _var_font(value):
        return FontStyle._fontStyle(value, "green", "black", "italic")

    def _isTuple(value: any, var: str) -> None:
        if type(value) != tuple:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be tuple.')}"
            )

    def _isInt(value: any, var: str) -> None:
        if type(value) != int:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be int.')}"
            )

    def _isFloat(value: any, var: str) -> None:
        if type(value) != float:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be float.')}"
            )

    def _isStr(value: any, var: str) -> None:
        if type(value) != str:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be str.')}"
            )

    def _isNumeric(value: int, var: str) -> None:
        if type(value) == int or type(value) == float:
            ...
        else:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be int or float.')}"
            )

    def _isValidColor(value: any, var: str) -> None:
        Validate._isStr(value, var)
        try:
            tkinter.Label(fg=value)
        except:
            raise ColorError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be valid color. eg:- '#ff0000'/ 'red'")}'''
            )

    def _isValidFont(value: any, var: str) -> None:
        Validate._isTuple(value, var)
        try:
            tkinter.Label(font=value)
        except:
            raise FontError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be valid font. eg:- ('arial',10,'bold')")}'''
            )

    def _isValidFunction(value: any, var: str) -> None:
        if not callable(value) and value != None:
            raise FunctionError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be function with two parameters or *args.")}'''
            )

    def _isValidXAxisIndices(values: tuple, indices: tuple, var: str) -> None:
        if indices != None:
            Validate._isTuple(indices, var)
            for index in indices:
                if index >= len(values):
                    raise IndexError(
                        f'''{Validate._var_font(var)} {Validate._error_font("values must be lower than length of x_axis_values.")}'''
                    )

    def _isValidXAxisLabelCount(values: any, var: str) -> None:
        if values != None:
            Validate._isInt(values, var)

    def _isValidStyleType(value: any, var: str) -> None:
        Validate._isTuple(value, var)
        if len(value) == 2:
            if type(value[0]) == int and type(value[1]) == int:
                ...
            else:
                raise TypeError(
                    f'''{Validate._var_font(var)} {Validate._error_font("values must be integers.")}'''
                )
        else:
            raise LengthError(
                f'''{Validate._var_font(var)} {Validate._error_font("length must be two.")}'''
            )

    def _isValidDataPostion(value: any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "top" or value == "side":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'top' or 'side'.")}'''
            )

    def _isValidLineStyle(value: any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "dotted" or value == "dashed" or value == "normal":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'normal' or 'dotted' or 'dashed'.")}'''
            )

    def _isValidSectionStyle(value: any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "dashed" or value == "normal":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'normal' or 'dashed'.")}'''
            )

    def _isValidLineWidth(value: any, var: str) -> None:
        if type(value) == int:
            ...
        elif type(value) == str and value == "auto":
            ...
        else:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be integer or 'auto'.")}'''
            )

    def _isValidPointerState_Lock(value: any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "disabled" or value == "enabled":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'disabled' or 'enabled'.")}'''
            )

    def _isValidYAxisValues(value: any, var: str) -> None:
        Validate._isTuple(value, var)
        if len(value) == 2:
            if type(value[0]) == int or type(value[0]) == float and type(
                    value[1]) == int or type(value[1]) == float:
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
            raise LengthError(
                f'''{Validate._var_font(var)} {Validate._error_font("length must be two.")}'''
            )

    def _isValidYAxisMaxValue(value: any, var: str) -> None:
        Validate._isNumeric(value, var)
        if value == 0:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be less than 0 or bigger than 0")}'''
            )
