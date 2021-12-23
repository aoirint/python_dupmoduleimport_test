import sys
from pathlib import Path

Path('a/').mkdir(exist_ok=True)
with open('a/core.py', 'w') as fp:
    fp.write('x = "Hello"')

Path('b/').mkdir(exist_ok=True)
with open('b/core.py', 'w') as fp:
    fp.write('x = "World"')

sys.path.insert(0, 'a/')
import core

# Hello
print(core.x)

sys.path.insert(0, 'b/')
import core

# Hello
print(core.x)

