from typing import List
from easy_regex.back_match.back_match import BackMatch
from easy_regex.commons.groups.group import Group
from easy_regex.commons.match import Match
from easy_regex.commons import RegexTerm
from easy_regex.commons.supported_regex_ops import RegexOp
from easy_regex.look_ahead_behind.look_ahead import LookAheadBehind

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
    
    def before(self, term):
        other_term = self.__parse_term(term)
        return CompoundExpression(LookAheadBehind(self, other_term, LookAheadBehind.LookAheadBehindType.AHEAD_MATCH))
    
    def after(self, term):
        other_term = self.__parse_term(term)
        return CompoundExpression(LookAheadBehind(self, other_term, LookAheadBehind.LookAheadBehindType.BEHIND_MATCH))
    
    def not_before(self, term):
        other_term = self.__parse_term(term)
        return CompoundExpression(LookAheadBehind(self, other_term, LookAheadBehind.LookAheadBehindType.AHEAD_NOT_MATCH))
    
    def not_after(self, term):
        other_term = self.__parse_term(term)
        return CompoundExpression(LookAheadBehind(self, other_term, LookAheadBehind.LookAheadBehindType.BEHIND_NOT_MATCH))
    
    def back_match(self, num: int):
        return CompoundExpression(BackMatch(self, num))

    def __parse_term(self, term) -> RegexTerm:
        if isinstance(term, str):
            return CompoundExpression(Match(term))
        elif isinstance(term, RegexTerm):
            return term
        else:
            raise ValueError(f'Term {term} is not a RegexTerm or a string')

    def render(self)-> str:
        return ''.join([term.render() for term in self._children])