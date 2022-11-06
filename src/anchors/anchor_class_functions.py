from anchors import Anchors
from anchors.anchors import SupportedAnchors
from commons import CompoundExpression

def START_WITH(term: str) -> Anchors:
    return CompoundExpression(Anchors(SupportedAnchors.START_WITH, term))

def END_WITH(term: str) -> Anchors:
    return CompoundExpression(Anchors(SupportedAnchors.END_WITH, term))