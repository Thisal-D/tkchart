class FontStyle:
    _colors = {
        "black": ("30", "40"),
        "gray": ("90", "100"),
        "red": ("31", "41"),
        "green": ("32", "42"),
        "yellow": ("33", "43"),
        "blue": ("34", "44"),
        "magenta": ("35", "45"),
        "cyan": ("36", "46"),
        "white": ("37", "47"),
        "bright red": ("91", "101"),
        "bright green": ("92", "102"),
        "bright yellow": ("93", "103"),
        "bright blue": ("94", "104"),
        "bright magenta": ("95", "105"),
        "bright cyan": ("96", "106"),
        "bright white": ("97", "107"),
    }

    _styles = {
        "normal": "0",
        "italic": "3",
        "underline": "4"
    }

    @staticmethod
    def _get_font_style_code(fg_color: str, bg_color: str, style: str) -> str:
        """
        Returns the ANSI escape code for the given foreground color,
        background color, and style.

        Raises:
            ValueError: If any of the colors or style are invalid.
        """
        fg_color = fg_color.lower()
        bg_color = bg_color.lower()
        style = style.lower()

        if fg_color not in FontStyle._colors:
            raise ValueError(f"Invalid foreground color: {fg_color}")
        if bg_color not in FontStyle._colors:
            raise ValueError(f"Invalid background color: {bg_color}")
        if style not in FontStyle._styles:
            raise ValueError(f"Invalid style: {style}")

        fg_code = FontStyle._colors[fg_color][0]
        bg_code = FontStyle._colors[bg_color][1]
        style_code = FontStyle._styles[style]

        return f"\x1b[{style_code};{fg_code};{bg_code}m"

    @staticmethod
    def apply(value: str, fg_color: str, bg_color: str, style: str = "normal") -> str:
        """
        Apply the font style to the given string.

        Args:
            value (str): The text to style.
            fg_color (str): Foreground color name.
            bg_color (str): Background color name.
            style (str, optional): Style name. Defaults to "normal".

        Returns:
            str: The styled text with ANSI escape codes.
        """
        code = FontStyle._get_font_style_code(fg_color, bg_color, style)
        reset = "\x1b[0m"
        return f"{code}{value}{reset}"
