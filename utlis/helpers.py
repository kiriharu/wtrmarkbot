from typing import Optional, Any


def get_key_by_value(d: dict, v: Any) -> Optional[Any]:
    for key, value in d.items():
        if value == v:
            return key


def check_in(text: str, _list: list) -> Optional[str]:
    if text in _list:
        return text


def validate_number(num: str, max_num: int = 255) -> Optional[int]:
    if not num.isdigit():
        return
    int_num = int(num)
    if not int_num > max_num:
        return int_num
