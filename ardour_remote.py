#!/usr/bin/env python

# example from http://das.nasophon.de/pyliblo/examples.html

import liblo, sys

# send all messages to port 1234 on the local machine
try:
    target = liblo.Address(3819)
except liblo.AddressError, err:
    print str(err)
    sys.exit()

# Listen loop  
def listen():
    c = raw_input('--> ')
    return c
while True:
    c = listen() 
    if c == "p":
        liblo.send(target, "/ardour/transport_play")
        print("Play")
    elif c == "s":
        liblo.send(target, "/ardour/transport_stop")
        print("Stop")
    elif c == "tr":
        t = raw_input('track ? ')
        l = raw_input('level ? ')
        liblo.send(target, "/ardour/routes/gaindB", ('d', t), ('f',l))

        print( l + " level applied to track" + t )
    elif c == "ls":
        ls = liblo.send(target, "/ardour/routes/list")
        print(ls)
    elif c == "test":
        # Hard coded works fine?
#        liblo.send(target, "/ardour/routes/gaindB if 1 -5")
        liblo.send(target, "/ardour/routes/gaindB", ('d', 1), ('f', 
                 -5.0))

    elif c == "br":
        break
        



