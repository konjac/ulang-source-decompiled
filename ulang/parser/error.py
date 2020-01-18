# uncompyle6 version 3.6.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ulang\parser\error.py


class SyntaxError(ValueError):

    def __init__(self, message, filename, lineno, colno, source=None):
        self.message_ = message
        self.filename_ = filename
        self.lineno_ = lineno if lineno > 0 else 1
        self.colno_ = colno if colno > 0 else 1
        self.source_ = source

    def __str__(self):
        msg = 'File "%s", line %d:%d, %s' % (
         self.filename_, self.lineno_, self.colno_, self.message_)
        if self.source_:
            line = self.source_[(self.lineno_ - 1)]
            col = ' ' * (self.colno_ - 1) + '^'
            msg = '%s\n%s\n%s' % (msg, line, col)
        return msg
# okay decompiling ulang-0.2.2.exe_extracted\PYZ-00.pyz_extracted\ulang.parser.error.pyc
