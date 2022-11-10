from .brackets import Brackets
from commons import CompoundExpression

def CHARS(chars: str):
    return CompoundExpression(Brackets(chars, True))

def NOT_CHARS(chars: str):
    return CompoundExpression(Brackets(chars, False))