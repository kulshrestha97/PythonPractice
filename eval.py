n = int(raw_input())
input_list = []


for i in range(0,n):
    command = raw_input()
    commandL = command.split()

    if(commandL[0]=='insert'):
        eval('input_list.' + commandL[0] + '(%s,%s)' % (commandL[1],commandL[2]))

    if(commandL[0]=='append'):
        eval('input_list.' + commandL[0] + '(%s)' % (commandL[1]))

    if(commandL[0]=='sort'):
        eval('input_list.' + commandL[0] + '()')

    if(commandL[0]=='print'):
        print input_list

    if(commandL[0]=='pop'):
        eval('input_list.' + commandL[0] + '()')
    if(commandL[0]=='reverse'):
        eval('input_list.' + commandL[0] + '()')
    if(commandL[0]=='remove'):
        eval('input_list.' + commandL[0] + '(%s)' % (commandL[1]))