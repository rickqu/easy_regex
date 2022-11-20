from enum import Enum
from easy_regex.commons import RegexTerm

class LookAheadBehind(RegexTerm):
    class LookAheadBehindType(Enum):
        AHEAD_MATCH = 0,
        AHEAD_NOT_MATCH = 1,
        BEHIND_MATCH = 2,
        BEHIND_NOT_MATCH = 3

    def __init__(self, core_term: RegexTerm, other_term: RegexTerm, look_ahead_behind_type: LookAheadBehindType):
        self.__core_term = core_term
        self.__other_term = other_term
        self.__look_ahead_behind_type = look_ahead_behind_type

    def render(self) -> str:
        look_ahead_behind_str = self.__get_look_ahead_behind_str()
        if self.__look_ahead_behind_type == LookAheadBehind.LookAheadBehindType.AHEAD_MATCH \
            or self.__look_ahead_behind_type == LookAheadBehind.LookAheadBehindType.AHEAD_NOT_MATCH:
            return f'{self.__core_term.render()}(?{look_ahead_behind_str}{self.__other_term.render()})'
        else:
            return f'(?{look_ahead_behind_str}{self.__other_term.render()}){self.__core_term.render()}'
    
    def __get_look_ahead_behind_str(self) -> str:
        if self.__look_ahead_behind_type == LookAheadBehind.LookAheadBehindType.AHEAD_MATCH:
            return '='
        elif self.__look_ahead_behind_type == LookAheadBehind.LookAheadBehindType.AHEAD_NOT_MATCH:
            return '!'
        elif self.__look_ahead_behind_type == LookAheadBehind.LookAheadBehindType.BEHIND_MATCH:
            return '<='
        elif self.__look_ahead_behind_type == LookAheadBehind.LookAheadBehindType.BEHIND_NOT_MATCH:
            return '<!'