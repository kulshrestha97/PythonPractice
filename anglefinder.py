from math import *
# ABC is a right triangle
# M is mid point
# you have to find ang(MBC)
# which in turn is equal to ang(ACB)
AB = float(raw_input())
BC = float(raw_input())
AC = float(hypot(AB,BC))
MC = AC/2
ratio = float(AB/BC)
ACB = int(round(degrees(atan(ratio)),0))
print "%d%s" %(ACB,unichr(176))


