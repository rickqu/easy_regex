from enum import Enum
from easy_regex.commons import RegexTerm

class SupportedAnchors(Enum):
    START_WITH = 0
    END_WITH = 1

class Anchors(RegexTerm):
    def __init__(self, char_class: SupportedAnchors, anchor: str):
        self._char_class: SupportedAnchors = char_class
        self._anchor: str = anchor

    def render(self)-> str:
        if self._char_class == SupportedAnchors.START_WITH:
            return f'^{self._anchor}'
        elif self._char_class == SupportedAnchors.END_WITH:
            return f'{self._anchor}$'
        else:
            raise TypeError('Unsupported anchor')