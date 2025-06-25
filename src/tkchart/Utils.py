import tkinter as tk
from typing import Union, Tuple, Any, List


class Utils:

    @staticmethod
    def _required_width(text: Any, font: Tuple[str, int, str]) -> int:
        """
        Get the required width of a label to display the given text with the specified font.

        Args:
            text (Any): Text to measure.
            font (Tuple[str, int, str]): Font specification (family, size, style).

        Returns:
            int: Required label width in pixels.
        """
        label = tk.Label(font=font)
        label.config(text=str(text))
        return label.winfo_reqwidth()

    @staticmethod
    def _required_height(text: Any, font: Tuple[str, int, str]) -> int:
        """
        Get the required height of a label to display the given text with the specified font.

        Args:
            text (Any): Text to measure.
            font (Tuple[str, int, str]): Font specification (family, size, style).

        Returns:
            int: Required label height in pixels.
        """
        label = tk.Label(font=font)
        label.config(text=str(text))
        return label.winfo_reqheight()

    @staticmethod
    def _format_float_with_precision(float_val: Union[int, float], decimals: int) -> str:
        """
        Format a float or int value as a string with a specified number of decimal places.

        Args:
            float_val (int | float): Number to format.
            decimals (int): Number of decimal places.

        Returns:
            str: Number formatted as a string with exact decimals.
        """
        if decimals > 0:
            rounded = round(float(float_val), decimals)
            integer_part, dot, fraction_part = str(rounded).partition(".")
            fraction_part = fraction_part.ljust(decimals, "0")
            return f"{integer_part}.{fraction_part}"
        return str(int(float_val))

    @staticmethod
    def _get_max_required_label_width(data: List[Any], font: Tuple[str, int, str]) -> int:
        """
        Calculate the maximum label width needed to display all data items with given font.

        Args:
            data (List[Any]): List of data items to measure.
            font (Tuple[str, int, str]): Font specification.

        Returns:
            int: Maximum required label width in pixels.
        """
        return max(Utils._required_width(text=d, font=font) for d in data)

    @staticmethod
    def _get_max_required_label_height(data: List[Any], font: Tuple[str, int, str]) -> int:
        """
        Calculate the maximum label height needed to display all data items with given font.

        Args:
            data (List[Any]): List of data items to measure.
            font (Tuple[str, int, str]): Font specification.

        Returns:
            int: Maximum required label height in pixels.
        """
        return max(Utils._required_height(text=d, font=font) for d in data)

    @staticmethod
    def _sort_tuple(values: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Sort a tuple of integers and remove duplicates.

        Args:
            values (Tuple[int, ...]): Tuple of integers.

        Returns:
            Tuple[int, ...]: Sorted tuple with unique integers.
        """
        return tuple(sorted(set(values)))

    @staticmethod
    def _to_int(value: Union[int, str]) -> int:
        """
        Convert a string or integer to an integer.

        Args:
            value (Union[int, str]): Value to convert.

        Returns:
            int: Converted integer.
        """
        return int(value)
