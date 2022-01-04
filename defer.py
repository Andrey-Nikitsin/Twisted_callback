from twisted.internet import reactor, defer


def callback_func_2(result):
    a = 1
    while a < 10000000:
        a += 1
    return print(a)

def do():
    print('do')
    d = defer.Deferred()
    reactor.callLater(1, d.callback, 'result')
    d.addCallback(callback_func_2)
    return d

do()
print('asdfas')
reactor.run()