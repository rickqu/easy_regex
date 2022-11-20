from easy_regex.commons.regex_term import RegexTerm

class BackMatch(RegexTerm):
    def __init__(self, term: RegexTerm, match):
        self.__term = term
        self.__match = match

    def render(self) -> str:
        if isinstance(self.__match, int): 
            return f'({self.__term.render()})\{self.__match}'
        elif isinstance(self.__match, str):
            return f'({self.__term.render()})\k<{self.__match}>'
        else:
            raise ValueError(f'{self.__match} cannot be used in a back reference')