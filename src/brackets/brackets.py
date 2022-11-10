from commons import RegexTerm

class Brackets(RegexTerm):
    def __init__(self, chars: str, match: bool):
        self.__chars = chars
        self.__match = match
    
    def render(self):
        return f'[{"^" if not self.__match else ""}{self.__chars}]'