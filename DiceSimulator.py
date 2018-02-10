from random import *
while(1):
    print "Welcome to dice simulator " \
          "do you want to simulate the dice, [Y/N]"
    s = raw_input()
    if (s == 'Y'):
        print randint(1,6)
        continue
    else:
        exit()