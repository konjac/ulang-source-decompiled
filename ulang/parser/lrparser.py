# uncompyle6 version 3.6.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ulang\parser\lrparser.py
from rply.errors import ParsingError

class LRParser:

    def __init__(self, lrparser):
        self.lr_table = lrparser.lr_table
        self.error_handler = lrparser.error_handler

    def parse(self, tokenizer, state=None):
        from rply.token import Token
        lookahead = None
        lookaheadstack = []
        statestack = [
         0]
        symstack = [Token('$end', '$end')]
        current_state = 0
        while True:
            if self.lr_table.default_reductions[current_state]:
                t = self.lr_table.default_reductions[current_state]
                current_state = self._reduce_production(t, symstack, statestack, state)
                continue
            elif lookahead is None:
                if lookaheadstack:
                    lookahead = lookaheadstack.pop()
                else:
                    try:
                        lookahead = next(tokenizer)
                    except StopIteration:
                        lookahead = None

            if lookahead is None:
                lookahead = Token('$end', '$end')
            ltype = lookahead.gettokentype()
            if ltype in self.lr_table.lr_action[current_state]:
                t = self.lr_table.lr_action[current_state][ltype]
                if t > 0:
                    statestack.append(t)
                    current_state = t
                    symstack.append(lookahead)
                    lookahead = None
                    continue
                else:
                    if t < 0:
                        current_state = self._reduce_production(t, symstack, statestack, state)
                        continue
                    else:
                        n = symstack[(-1)]
                    return n
            elif self.error_handler is not None:
                if state is None:
                    self.error_handler(lookahead)
                else:
                    self.error_handler(state, lookahead)
                lookahead = None
                continue
            else:
                raise ParsingError(None, lookahead.getsourcepos())

    def _reduce_production(self, t, symstack, statestack, state):
        p = self.lr_table.grammar.productions[(-t)]
        pname = p.name
        plen = p.getlength()
        start = len(symstack) + (-plen - 1)
        assert start >= 0
        targ = symstack[start + 1:]
        start = len(symstack) + -plen
        if not start >= 0:
            raise AssertionError
        else:
            del symstack[start:]
            del statestack[start:]
            if state is None:
                value = p.func(targ)
            value = p.func(state, targ)
        symstack.append(value)
        current_state = self.lr_table.lr_goto[statestack[(-1)]][pname]
        statestack.append(current_state)
        return current_state
# okay decompiling ulang-0.2.2.exe_extracted\PYZ-00.pyz_extracted\ulang.parser.lrparser.pyc
