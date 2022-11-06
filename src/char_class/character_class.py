from enum import Enum

from commons import RegexOp
from commons import RegexTerm

class SupportedCharacterClass(Enum):
    CHAR = 0
    DIGIT = 1
    NOT_DIGIT = 2
    WORD_CHAR = 3
    NOT_WORD_CHAR = 4
    WHITESPACE = 5
    NOT_WHITESPACE = 6
    WORD = 7

class CharacterClass(RegexTerm):
    def __init__(self, char_class: SupportedCharacterClass):
        self._char_class: SupportedCharacterClass = char_class
        self._mode: RegexOp = RegexOp.CHAR_CLASS

    def render(self)-> str:
        if self._char_class == SupportedCharacterClass.CHAR:
            return '\.'
        elif self._char_class == SupportedCharacterClass.DIGIT:
            return '\d'
        elif self._char_class == SupportedCharacterClass.WORD:
            return '\w'
        else:
            raise TypeError('Unsupported character class')