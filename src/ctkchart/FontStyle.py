class FontStyle:
    @staticmethod
    def _get_font_style_code(
            fg_color: str,
            bg_color: str,
            style: str) -> str:
        
        colors_data = {
            "black": ("30", "40"),
            "gray": ("90", "100"),
            "red": ("31", "41"),
            "green": ("32", "42"),
            "yellow": ("33", "43"),
            "blue": ("34", "44"),
            "Magenta": ("35", "45"),
            "cyan": ("36", "46"),
            "white": ("37", "47"),
            "bright red": ("91", "101"),
            "bright green": ("92", "102"),
            "bright yellow": ("92", "102"),
            "bright blue": ("92", "102"),
            "bright magenta": ("92", "102"),
            "bright cyan": ("92", "102"),
            "bright white": ("92", "102")
        }
        
        fg_color_code = colors_data[fg_color][0]
        bg_color_code = colors_data[bg_color][1]
            
        styles_data = {
            "normal": "0",
            "italic": "3",
            "underline": "4"
        }
        style_code = styles_data[style]
        
        styled_font_code = "\x1b[" + style_code + ";" + fg_color_code + ";" + bg_color_code + "m"

        return styled_font_code

    @staticmethod
    def _fontStyle(
            value: str,
            fg_color: str,
            bg_color: str,
            style: str = "normal") -> str:
        output_text = FontStyle._get_font_style_code(fg_color, bg_color, style) + value + "\x1b[0m"
        return output_text
