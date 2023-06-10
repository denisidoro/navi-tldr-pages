#! /usr/bin/env nix-shell
#! nix-shell -i python

import re
import sys

def process_text(text):
    def repl(matchobj):
        s = matchobj.group(1)
        if s.startswith("/") and not s.startswith("~/"):
            s = s[1:]
        if not s.startswith("~/"):
            s = s.replace("/", "_")
        return "<" + s + ">"
    return re.sub(r"{{([^}]*)}}", repl, text)

text = sys.stdin.read()
print(process_text(text), end='')
