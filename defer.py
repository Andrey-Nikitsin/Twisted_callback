from twisted.internet import reactor , threads
from twisted.internet.defer import Deferred


def SlowFunk():
    print('slow')
    a = 1
    while a < 100000000000:
        a += 1
    return a


def CreateDeffered():
    defferad = threads.deferToThread(SlowFunk)
    defferad.addCallback(print)
    print('rabotaet')


val = CreateDeffered()
reactor.run()