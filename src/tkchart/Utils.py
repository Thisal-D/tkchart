import tkinter as tk
from typing import Union, Tuple, Any, List


class Utils:

    @staticmethod
    def _RequiredWidth(text: Any, font: Tuple[str, int, str]) -> int:
        """Get the required width of a label for the given text and font."""
        label = tk.Label(font=font)
        label.config(text=str(text))
        return label.winfo_reqwidth()

    @staticmethod
    def _RequiredHeight(text: Any, font: Tuple[str, int, str]) -> int:
        """Get the required height of a label for the given text and font."""
        label = tk.Label(font=font)
        label.config(text=str(text))
        return label.winfo_reqheight()

    @staticmethod
    def _format_float_with_precision(float_val: Union[int, float], decimals: int) -> str:
        """
        Format a float value with the specified number of decimal places.

        Args:
            float_val (int | float): The number to format.
            decimals (int): Number of decimal places to show.

        Returns:
            str: Formatted number as a string.
        """
        if decimals > 0:
            rounded = round(float(float_val), decimals)
            integer_part, dot, fraction_part = str(rounded).partition(".")
            fraction_part = fraction_part.ljust(decimals, "0")
            return f"{integer_part}.{fraction_part}"
        return str(int(float_val))

    @staticmethod
    def _get_max_required_label_width(data: List[Any], font: Tuple[str, int, str]) -> int:
        """Return the maximum required label width from a list of data."""
        return max(Utils._RequiredWidth(text=d, font=font) for d in data)

    @staticmethod
    def _get_max_required_label_height(data: List[Any], font: Tuple[str, int, str]) -> int:
        """Return the maximum required label height from a list of data."""
        return max(Utils._RequiredHeight(text=d, font=font) for d in data)

    @staticmethod
    def _sort_tuple(values: Tuple[int, ...]) -> Tuple[int, ...]:
        """Return a sorted tuple of unique integers."""
        return tuple(sorted(set(values)))

    @staticmethod
    def _toInt(value: Union[int, str]) -> int:
        """Convert a string or int to int."""
        return int(value)
