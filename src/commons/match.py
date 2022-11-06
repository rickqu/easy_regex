from typing import Final
from commons.regex_term import RegexTerm
from commons.supported_regex_ops import RegexOp

class Match(RegexTerm):
    __reserved_chars: Final = '.^$*+?()[{\|}]/'

    def __init__(self, const_str: str):
        self.__value: str = const_str
        self.__type: RegexOp = RegexOp.MATCH

    def get_type(self) -> RegexOp:
        return self.__type

    def render(self)-> str:
        return Match.__escape_reserved_chars(self.__value)

    def __escape_reserved_chars(const_str: str) -> str:
        input_str = list(const_str)
        return ''.join([char if char not in Match.__reserved_chars else f'\\{char}' for char in input_str])