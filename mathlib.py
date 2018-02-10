import cmath
import math
s = raw_input()
print abs(complex(s))
print cmath.phase(complex(s))

AB = int(raw_input())
BC = int(raw_input())
AC = ((AB**2)+(BC**2))**(1/2)
MC = AC/2
side = MC/BC
angle = math.asin(side)
print angle
