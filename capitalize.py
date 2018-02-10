import string
def capitalize(string):
    c = string.split()
    for i in range(0, len(c)):
        c[i] = c[i].capitalize()
        string = ' '.join(c)
    return string

strin = raw_input()
strin = strin.center(5,'-')
print string.capwords(strin,' ')
