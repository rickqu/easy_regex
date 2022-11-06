from typing import List
from commons.groups.group import Group
from commons.match import Match
from commons import RegexTerm
from commons.supported_regex_ops import RegexOp

class CompoundExpression(RegexTerm):
    def __init__(self, beginning: RegexTerm = None):
        if (beginning != None):
            self._children: List[RegexTerm] = [beginning]
        else:
            self._children: List[RegexTerm] = []
        self._mode: RegexOp = RegexOp.COMPOUND
    
    def __radd__(self, other) -> 'CompoundExpression':
        return self.__add(other, False)

    def __add__(self, other) -> 'CompoundExpression':
        return self.__add(other, True)
    
    def __add(self, other, is_left: bool) -> 'CompoundExpression':
        if isinstance(other, RegexTerm):
            if is_left:
                self._children.append(other)
            else:
                self._children.insert(0, other)
            return self
        elif isinstance(other, str):
            if is_left:
                self._children.append(Match(other))
            else:
                self._children.insert(0, Match(other))
            return self
        else:
            raise TypeError(f'Unsupported concatenation of type {type(other)}')
    
    def __call__(self, first, second = None, third = None) -> 'CompoundExpression':
        return CompoundExpression(Group(self, first, second, third))

    def get_children(self) -> List[RegexTerm]:
        return self._children

    def render(self)-> str:
        return ''.join([term.render() for term in self._children])