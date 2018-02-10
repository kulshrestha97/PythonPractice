t = raw_input()
value = t[0:8]
time = t[8:len(t)]
hrs = int(value[0:2])
if (time == 'AM' and hrs<12):
    print '%s%s%s' % (value[0:2], value[2:5], value[5:8])

elif (time =='AM' and hrs ==12):

    print '00%s%s' % (value[2:5], value[5:8])
elif (time =='PM'):
    hrs+=12
    print '%d%s%s' % (hrs, value[2:5], value[5:8])