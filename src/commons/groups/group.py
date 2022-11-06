from commons import RegexTerm, NO_LIMIT
from enum import Enum

class Group(RegexTerm):
    class GroupType(Enum):
        UNKNOWN = 0
        JUST_NAME = 1
        EXACT_REPEAT = 2
        EXACT_REPEAT_AND_NAME = 3
        BETWEEN_REPEAT = 4
        BETWEEN_REPEAT_AND_NAME = 5

    def __init__(self, term, first, second, third):
        if not isinstance(term, RegexTerm):
            raise TypeError(f'Must supply a Regex term, supplied {type(term)}')
        self.__term = term
        self.__first = first
        self.__second = second
        self.__third = third
    
    def render(self) -> str:
        call_type: Group.GroupType = Group.__determine_call_type(self.__first, self.__second, self.__third)
        if call_type == Group.GroupType.JUST_NAME:
            return f'(?<{self.__first}>{self.__term.render()})'
        elif call_type == Group.GroupType.EXACT_REPEAT:
            return f'{self.__term.render()}{{{self.__first}}}'
        elif call_type == Group.GroupType.EXACT_REPEAT_AND_NAME:
            return f'(?<{self.__second}>{self.__term.render()}{{{self.__first}}})'
        elif call_type == Group.GroupType.BETWEEN_REPEAT:
            # This means we should just use optional
            if self.__first == 0 and self.__second == 1:
                return f'(?:{self.__term.render()})?'
            # Means we can use "at least 1"
            if self.__first == 1 and self.__second == NO_LIMIT:
                return f'(?:{self.__term.render()})+'
            # Zero or more
            if self.__first == 0 and self.__second == NO_LIMIT:
                return f'(?:{self.__term.render()})*'
            if self.__second == NO_LIMIT:
                upper_limit = ""
            else:
                upper_limit = str(self.__second)
            return f'{self.__term.render()}{{{self.__first},{upper_limit}}}'
        elif call_type == Group.GroupType.BETWEEN_REPEAT_AND_NAME:
            if self.__second == NO_LIMIT:
                upper_limit = ""
            else:
                upper_limit = str(self.__second)
            return f'(?<{self.__third}>{self.__term.render()}{{{self.__first},{upper_limit})'
        else:
            raise TypeError('Not supported way of using brackets')

    def __determine_call_type(first, second, third) -> GroupType:
        # TERM('some name')
        if isinstance(first, str) and second == None and third == None:
            return Group.GroupType.JUST_NAME
        # TERM(2)
        elif isinstance(first, int) and second == None and third == None:
            return Group.GroupType.EXACT_REPEAT
        # TERM(2, 'some name')
        elif isinstance(first, int) and isinstance(second, str) and third == None:
            return Group.GroupType.EXACT_REPEAT_AND_NAME
        # TERM(2, 3)
        elif isinstance(first, int) and isinstance(second, int) and third == None:
            return Group.GroupType.BETWEEN_REPEAT
        # TERM(2, 3, 'some name')
        elif isinstance(first, int) and isinstance(second, int) and isinstance(third, str):
            return Group.GroupType.BETWEEN_REPEAT_AND_NAME
        else:
            return Group.GroupType.UNKNOWN
