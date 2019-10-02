name = "Test"
f"My app name is {name}."
'My app name is Test.'

import dis

def f1():
    a = "test"
    return f"{a}"

def f2():
    return "{a}".format(a='test')

print(dis.dis(f1))
print(dis.dis(f2))

pip install fstring

from fstring import fstring

x = 1

y = 2.0

plus_result = "3.0"

print fstring("{x}+{y}={plus_result}")
