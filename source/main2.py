import sys
from pathlib import Path
import importlib.machinery as imm

Path('a/').mkdir(exist_ok=True)
with open('a/core.py', 'w') as fp:
    fp.write('x = "Hello"')

Path('b/').mkdir(exist_ok=True)
with open('b/core.py', 'w') as fp:
    fp.write('x = "World"')

sys.path.insert(0, 'a/')
core_a = imm.SourceFileLoader('core_a', 'a/core.py').load_module()

# Hello
print(core_a.x)

sys.path.insert(0, 'b/')
core_b = imm.SourceFileLoader('core_b', 'b/core.py').load_module()

# World
print(core_b.x)

# Hello
print(core_a.x)

