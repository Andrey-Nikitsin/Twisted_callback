from twisted.internet import protocol, reactor, threads
from twisted.internet.defer import Deferred
from twisted.protocols.basic import LineReceiver



class TwistServer(LineReceiver):
    def connectionMade(self):
        self.transport.write(b'SERVER CONNECT\n')
        

    def funk(self):

        def SlowFunk():
            a = 1
            while a < 10000000:
                a+=1
            return a

        def CreateDeffered():
            deffered = threads.deferToThread(SlowFunk)
            return deffered.addCallback(print)

        val = CreateDeffered()


    def lineReceived(self, line):
        if line == b'a':
            TwistServer.funk(self)
        print(line)
class FactoryTwistedServer(protocol.ServerFactory):
    def buildProtocol(self, addr):
        return TwistServer()

reactor.listenTCP(8051, FactoryTwistedServer())
reactor.run()


