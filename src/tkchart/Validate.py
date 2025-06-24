import tkinter as tk
from typing import Any, Tuple
from .FontStyle import FontStyle


class Validate:

    @staticmethod
    def _error_font(value: str) -> str:
        return FontStyle.apply(value, "red", "black", "underline")

    @staticmethod
    def _var_font(value: str) -> str:
        return FontStyle.apply(value, "green", "black", "italic")

    # --- Basic Type Checkers ---

    @staticmethod
    def _isTuple(value: Any, var: str) -> None:
        if not isinstance(value, tuple):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be a tuple.')}")

    @staticmethod
    def _isList(value: Any, var: str) -> None:
        if not isinstance(value, list):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be a list.')}")

    @staticmethod
    def _isInt(value: Any, var: str) -> None:
        if not isinstance(value, int):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be an int.')}")

    @staticmethod
    def _isBool(value: Any, var: str) -> None:
        if not isinstance(value, bool):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be a bool.')}")

    @staticmethod
    def _isFloat(value: Any, var: str) -> None:
        if not isinstance(value, float):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be a float.')}")

    @staticmethod
    def _isStr(value: Any, var: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be a str.')}")

    # --- Complex Validators ---

    @staticmethod
    def _isValidColor(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        try:
            tk.Label(fg=value)
        except tk.TclError:
            raise ValueError(
                f"""{Validate._var_font(var)} {Validate._error_font("must be a valid color, e.g. 'red' or '#ff0000'.")}"""
            )

    @staticmethod
    def _isValidFont(value: Any, var: str) -> None:
        Validate._isTuple(value, var)
        try:
            tk.Label(font=value)
        except tk.TclError:
            raise ValueError(
                f"""{Validate._var_font(var)} {Validate._error_font("must be a valid font, e.g. ('Arial', 10, 'bold').")}"""
            )

    @staticmethod
    def _isValidFunction(value: Any, var: str) -> None:
        if value is not None and not callable(value):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a callable function or None.')}"
            )

    @staticmethod
    def _isValidIndices(value: Any, var: str) -> None:
        if not all(isinstance(v, int) for v in value):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('all values must be int.')}")

    @staticmethod
    def _isValidXAxisIndices(values: Tuple[int, ...], indices: Any, var: str) -> None:
        if indices is not None:
            Validate._isTuple(indices, var)
            Validate._isValidIndices(indices, var)
            for index in indices:
                if index >= len(values):
                    raise ValueError(
                        f"{Validate._var_font(var)} {Validate._error_font('index must be less than length of x_axis_values.')}"
                    )

    @staticmethod
    def _isValidXAxisLabelCount(value: Any, var: str) -> None:
        if value is not None:
            Validate._isInt(value, var)

    @staticmethod
    def _isValidStyleType(value: Any, var: str) -> None:
        Validate._isTuple(value, var)
        if len(value) != 2 or not all(isinstance(v, int) for v in value):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a tuple of two integers.')}"
            )

    @staticmethod
    def _isValidDataPostion(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        if value not in {"top", "side"}:
            raise ValueError(
                f"""{Validate._var_font(var)} {Validate._error_font("must be 'top' or 'side'.")}"""
            )

    @staticmethod
    def _isValidLineStyle(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        if value not in {"normal", "dashed", "dotted"}:
            raise ValueError(
                f"""{Validate._var_font(var)} {Validate._error_font("must be 'normal', 'dashed', or 'dotted'.")}"""
            )

    @staticmethod
    def _isValidSectionStyle(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        if value not in {"normal", "dashed"}:
            raise ValueError(
                f"""{Validate._var_font(var)} {Validate._error_font("must be 'normal' or 'dashed'.")}"""
            )

    @staticmethod
    def _isValidXAxisPointSpacing(value: Any, var: str) -> None:
        if not (isinstance(value, int) or (isinstance(value, str) and value == "auto")):
            raise TypeError(
                f"""{Validate._var_font(var)} {Validate._error_font("must be int or 'auto'.")}"""
            )

    @staticmethod
    def _isValidPointerState_Lock(value: Any, var: str) -> None:
        Validate._isStr(value, var)
        if value not in {"enabled", "disabled"}:
            raise ValueError(
                f"""{Validate._var_font(var)} {Validate._error_font("must be 'enabled' or 'disabled'.")}"""
            )

    @staticmethod
    def _isValidLineHighlight(value: Any, var: str) -> None:
        Validate._isValidPointerState_Lock(value, var)

    @staticmethod
    def _isValidLineFill(value: Any, var: str) -> None:
        Validate._isValidPointerState_Lock(value, var)

    @staticmethod
    def _isValidYAxisValues(value: Any, var: str) -> None:
        Validate._isTuple(value, var)
        if value == (None, None):
            raise ValueError(f"{Validate._var_font(var)} {Validate._error_font('must be provided.')}")
        if len(value) != 2 or not all(isinstance(v, (int, float)) for v in value):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a tuple of two numbers.')}"
            )
        if value[0] >= value[1]:
            raise ValueError(
                f"{Validate._var_font(var)} {Validate._error_font('first value must be less than second.')}"
            )

    @staticmethod
    def _isValidXAxisValues(value: Any, var: str) -> None:
        if value in [(None, None), ("None", "None")]:
            raise ValueError(f"{Validate._var_font(var)} {Validate._error_font('must be provided.')}")
        Validate._isTuple(value, var)

    @staticmethod
    def _isValidLine(value: Any, var: str) -> None:
        from .Line import Line
        if not isinstance(value, Line):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a tkchart.Line instance.')}"
            )

    @staticmethod
    def _isValidLineChart(value: Any, var: str) -> None:
        from .LineChart import LineChart
        if not isinstance(value, LineChart):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a tkchart.LineChart instance.')}"
            )

    @staticmethod
    def _isValidData(value: Any, var: str) -> None:
        Validate._isList(value, var)
        if not all(isinstance(v, (int, float)) for v in value):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('all values must be int or float.')}"
            )

    # --- Error Helpers ---

    @staticmethod
    def _invalidCget(var: str) -> None:
        raise ValueError(
            f"{Validate._var_font(var)} {Validate._error_font('Invalid attribute.')}"
        )

    @staticmethod
    def _invalidLine(line: Any) -> None:
        raise ValueError(
            f"{Validate._var_font(str(line))} {Validate._error_font('The line is not part of this chart.')}"
        )

    @staticmethod
    def _MasterAttNotProvideForLine(value: Any) -> None:
        raise ValueError(
            f"{Validate._var_font(str(value))} {Validate._error_font('master must be provided for Line.')}"
        )
