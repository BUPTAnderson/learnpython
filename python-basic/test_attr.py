# -*- coding: utf-8 -*-
class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
        self._no = "10010"

    def say(self):
        print("我正在学Python")


clangs = CLanguage()
print(hasattr(clangs, "name"))
print(hasattr(clangs, "add"))
print(hasattr(clangs, "_no"))
print(hasattr(clangs, "say"))
