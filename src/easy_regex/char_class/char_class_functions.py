from easy_regex.commons import CompoundExpression
from .character_class import CharacterClass, SupportedCharacterClass


D = CompoundExpression(CharacterClass(SupportedCharacterClass.DIGIT))
C = CompoundExpression(CharacterClass(SupportedCharacterClass.CHAR))
W = CompoundExpression(CharacterClass(SupportedCharacterClass.WORD))
WHITE = CompoundExpression(CharacterClass(SupportedCharacterClass.WHITESPACE))