import tkinter as tk
from typing import Any, Tuple
from .FontStyle import FontStyle


class Validate:

    @staticmethod
    def _error_font(value: str) -> str:
        """Return a styled error message."""
        return FontStyle._apply(value, "red", "black", "underline")

    @staticmethod
    def _var_font(value: str) -> str:
        """Return a styled variable name."""
        return FontStyle._apply(value, "green", "black", "italic")

    # --- Basic Type Checkers ---

    @staticmethod
    def _is_tuple(value: Any, var: str) -> None:
        """Check if value is a tuple."""
        if not isinstance(value, tuple):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be a tuple.')}")

    @staticmethod
    def _is_list(value: Any, var: str) -> None:
        """Check if value is a list."""
        if not isinstance(value, list):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be a list.')}")

    @staticmethod
    def _is_int(value: Any, var: str) -> None:
        """Check if value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be an int.')}")

    @staticmethod
    def _is_bool(value: Any, var: str) -> None:
        """Check if value is a boolean."""
        if not isinstance(value, bool):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be a bool.')}")

    @staticmethod
    def _is_float(value: Any, var: str) -> None:
        """Check if value is a float."""
        if not isinstance(value, float):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be a float.')}")

    @staticmethod
    def _is_str(value: Any, var: str) -> None:
        """Check if value is a string."""
        if not isinstance(value, str):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('must be a str.')}")

    # --- Complex Validators ---

    @staticmethod
    def _is_valid_color(value: Any, var: str) -> None:
        """Check if value is a valid color string."""
        Validate._is_str(value, var)
        try:
            tk.Label(fg=value)
        except tk.TclError:
            raise ValueError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a valid color, e.g. \'red\' or \'#ff0000\'.')}"
            )

    @staticmethod
    def _is_valid_font(value: Any, var: str) -> None:
        """Check if value is a valid font tuple."""
        Validate._is_tuple(value, var)
        try:
            tk.Label(font=value)
        except tk.TclError:
            raise ValueError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a valid font, e.g. (\'Arial\', 10, \'bold\').')}"
            )

    @staticmethod
    def _is_valid_function(value: Any, var: str) -> None:
        """Check if value is callable or None."""
        if value is not None and not callable(value):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a callable function or None.')}"
            )

    @staticmethod
    def _is_valid_indices(value: Any, var: str) -> None:
        """Check if all values in iterable are integers."""
        if not all(isinstance(v, int) for v in value):
            raise TypeError(f"{Validate._var_font(var)} {Validate._error_font('all values must be int.')}")

    @staticmethod
    def _is_valid_x_axis_indices(values: Tuple[int, ...], indices: Any, var: str) -> None:
        """Validate that indices are within bounds of values."""
        if indices is not None:
            Validate._is_tuple(indices, var)
            Validate._is_valid_indices(indices, var)
            for index in indices:
                if index >= len(values):
                    raise ValueError(
                        f"{Validate._var_font(var)} {Validate._error_font('index must be less than length of x_axis_values.')}"
                    )

    @staticmethod
    def _is_valid_x_axis_label_count(value: Any, var: str) -> None:
        """Check if x-axis label count is an int if provided."""
        if value is not None:
            Validate._is_int(value, var)

    @staticmethod
    def _is_valid_style_type(value: Any, var: str) -> None:
        """Check if style type is a tuple of two integers."""
        Validate._is_tuple(value, var)
        if len(value) != 2 or not all(isinstance(v, int) for v in value):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a tuple of two integers.')}"
            )

    @staticmethod
    def _is_valid_data_position(value: Any, var: str) -> None:
        """Check if data position is 'top' or 'side'."""
        Validate._is_str(value, var)
        if value not in {"top", "side"}:
            raise ValueError(
                f"{Validate._var_font(var)} {Validate._error_font('must be \'top\' or \'side\'.')}"
            )

    @staticmethod
    def _is_valid_line_style(value: Any, var: str) -> None:
        """Check if line style is one of the accepted strings."""
        Validate._is_str(value, var)
        if value not in {"normal", "dashed", "dotted"}:
            raise ValueError(
                f"{Validate._var_font(var)} {Validate._error_font('must be \'normal\', \'dashed\', or \'dotted\'.')}"
            )

    @staticmethod
    def _is_valid_section_style(value: Any, var: str) -> None:
        """Check if section style is either 'normal' or 'dashed'."""
        Validate._is_str(value, var)
        if value not in {"normal", "dashed"}:
            raise ValueError(
                f"{Validate._var_font(var)} {Validate._error_font('must be \'normal\' or \'dashed\'.')}"
            )

    @staticmethod
    def _is_valid_x_axis_point_spacing(value: Any, var: str) -> None:
        """Check if x-axis point spacing is int or 'auto'."""
        if not (isinstance(value, int) or (isinstance(value, str) and value == "auto")):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be int or \'auto\'.')}"
            )

    @staticmethod
    def _is_valid_pointer_state_lock(value: Any, var: str) -> None:
        """Check if pointer lock state is 'enabled' or 'disabled'."""
        Validate._is_str(value, var)
        if value not in {"enabled", "disabled"}:
            raise ValueError(
                f"{Validate._var_font(var)} {Validate._error_font('must be \'enabled\' or \'disabled\'.')}"
            )

    @staticmethod
    def _is_valid_line_highlight(value: Any, var: str) -> None:
        """Validate line highlight state."""
        Validate._is_valid_pointer_state_lock(value, var)

    @staticmethod
    def _is_valid_line_fill(value: Any, var: str) -> None:
        """Validate line fill state."""
        Validate._is_valid_pointer_state_lock(value, var)

    @staticmethod
    def _is_valid_y_axis_values(value: Any, var: str) -> None:
        """Validate y-axis values as a tuple of two numbers, first less than second."""
        Validate._is_tuple(value, var)
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
    def _is_valid_x_axis_values(value: Any, var: str) -> None:
        """Validate x-axis values tuple is provided and not placeholders."""
        if value in [(None, None), ("None", "None")]:
            raise ValueError(f"{Validate._var_font(var)} {Validate._error_font('must be provided.')}")
        Validate._is_tuple(value, var)

    @staticmethod
    def _is_valid_line(value: Any, var: str) -> None:
        """Check if value is an instance of Line."""
        from .Line import Line
        if not isinstance(value, Line):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a tkchart.Line instance.')}"
            )

    @staticmethod
    def _is_valid_line_chart(value: Any, var: str) -> None:
        """Check if value is an instance of LineChart."""
        from .LineChart import LineChart
        if not isinstance(value, LineChart):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be a tkchart.LineChart instance.')}"
            )

    @staticmethod
    def _is_valid_data(value: Any, var: str) -> None:
        """Validate that value is a list of ints or floats."""
        Validate._is_list(value, var)
        if not all(isinstance(v, (int, float)) for v in value):
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('all values must be int or float.')}"
            )

    # --- Error Helpers ---

    @staticmethod
    def _invalid_cget(var: str) -> None:
        """Raise error for invalid attribute."""
        raise ValueError(
            f"{Validate._var_font(var)} {Validate._error_font('Invalid attribute.')}"
        )

    @staticmethod
    def _invalid_line(line: Any) -> None:
        """Raise error if line is not part of chart."""
        raise ValueError(
            f"{Validate._var_font(str(line))} {Validate._error_font('The line is not part of this chart.')}"
        )

    @staticmethod
    def _master_att_not_provided_for_line(value: Any) -> None:
        """Raise error if master is not provided for Line."""
        raise ValueError(
            f"{Validate._var_font(str(value))} {Validate._error_font('master must be provided for Line.')}"
        )
