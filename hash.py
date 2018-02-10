def print_formatted(number):
    m = number
    b = []
    o = []
    h = []
    for i in range(1, m + 1):
        bi = (str(bin(i)))

        bi = list(bi)
        del bi[0]
        del bi[0]

        bi = ''.join(str(e) for e in bi)

        oc = (str(oct(i)))

        oc = list(oc)
        del oc[0]
        oc = ''.join(str(e) for e in oc)

        he = str(hex(i))

        he = list(he)
        del he[0]
        del he[0]
        he = ''.join(str(e).capitalize() for e in he)


        b.append(bi)
        o.append(oc)
        h.append(he)
    for i in range(1, m + 1):
        print i, o[i - 1], h[i - 1], b[i - 1]
    print o

n = int(raw_input())
print_formatted(n)