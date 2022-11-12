from easy_regex.anchors import Anchors
from easy_regex.anchors import SupportedAnchors
from easy_regex.commons import CompoundExpression

def START_WITH(term: str) -> Anchors:
    return CompoundExpression(Anchors(SupportedAnchors.START_WITH, term))

def END_WITH(term: str) -> Anchors:
    return CompoundExpression(Anchors(SupportedAnchors.END_WITH, term))