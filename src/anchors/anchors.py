from enum import Enum
import commons

class SupportedAnchors(Enum):
    START_WITH = 0
    END_WITH = 1

class Anchors(commons.RegexTerm):
    def __init__(self, char_class: SupportedAnchors, anchor: str):
        self._char_class: SupportedAnchors = char_class
        self._anchor: str = anchor
        self._mode: commons.RegexOp = commons.RegexOp.CHAR_CLASS

    def render(self)-> str:
        if self._char_class == SupportedAnchors.START_WITH:
            return f'^{self._anchor}'
        elif self._char_class == SupportedAnchors.END_WITH:
            return f'{self._anchor}$'
        else:
            raise TypeError('Unsupported anchor')