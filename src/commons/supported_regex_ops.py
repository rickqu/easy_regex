
from enum import Enum

class RegexOp(Enum):
    MATCH = 0
    COMPOUND = 1
    START_WITH = 2
    END_WITH = 3
    CHAR_CLASS = 4