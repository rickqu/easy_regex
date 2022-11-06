from commons import RegexTerm, Match

class Or(RegexTerm):
    def __init__(self, *args):
        self.__args = [x if isinstance(x, RegexTerm) else Match(x) for x in args]
    
    def render(self) -> str:
        terms = ''.join([f'{"|" + x.render()}' for x in self.__args])
        return f'(?:{terms[1:]})'