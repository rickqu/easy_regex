from commons import CompoundExpression
from .or_op import Or

def OR(*args):
    return CompoundExpression(Or(*args))