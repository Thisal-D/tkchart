import tkinter
from typing import Union, Tuple

class Utils:
    def _RequiredWidth(text: any, font: Tuple[str, int, str]) -> int:
        label = tkinter.Label(font=font)
        label.config(text=str(text) +"")
        return label.winfo_reqwidth()


    def _RequiredHeight(text: any, font: Tuple[str, int, str]) -> int:
        label = tkinter.Label(font=font)
        label.config(text=str(text) +"")
        return label.winfo_reqheight()


    def _format_float_with_precision(float_val: Union[int, float], decimals: int) -> str:
        if decimals:
            float_val = round(float(float_val),decimals)
            float_val = str(float_val) + ((decimals-len(str(float_val).split(".")[-1]))*"0")
            return float_val
        else:
            return str(int(float_val))


    def _get_max_required_label_width(data: any, font: Tuple[str, int, str]) -> int:
        max_required_width = 0
        for d in data:
            required_width = Utils._RequiredWidth(text=d, font=font)
            if max_required_width<required_width:
                max_required_width=required_width
        return max_required_width


    def _get_max_required_label_height(data :any, font: Tuple[str, int, str]) -> int:
        max_required_height = 0
        for d in data:
            required_height = Utils._RequiredHeight(text=d, font=font)
            if max_required_height<required_height:
                max_required_height=required_height
        return max_required_height


    def _sort_tuple(values: Tuple[int, ...]) -> Tuple[int, ...]:
        values_list = list(set(values))
        values_list.sort()
        return tuple(values_list)
    
    
    def _toInt(value: Union[int, str]) -> int:
        #return math.ceil(value)
        return value