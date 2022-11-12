from easy_regex.brackets import Brackets
from easy_regex.commons import CompoundExpression

def CHARS(chars: str):
    return CompoundExpression(Brackets(chars, True))

def NOT_CHARS(chars: str):
    return CompoundExpression(Brackets(chars, False))