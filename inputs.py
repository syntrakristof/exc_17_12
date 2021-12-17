from typing import Any, Optional

def get_input_item(text:str, result_type:int = 0, retry_count:int = 5) -> Any: # pragma: no cover
    """get the input

    Args:
        text (str) : text to display
        result_type (int, optional): used for converting the result to a type
                                     0 -> default -> string
                                     1 -> converts result to an int
                                     2 -> convert result to float

    Returns:
        any (int, str, float): result of the input 
    """
    result: Optional[Any] = None

    try:
        inp = input(text).strip()
        if result_type == 1:
            result =  int(inp)
        elif result_type == 2:
            result = float(inp.replace(',', '.'))
        else:
            result = inp
    except Exception as e:
        if retry_count < 5:
            result = get_input_item(text, result_type, retry_count+1)

    return result

