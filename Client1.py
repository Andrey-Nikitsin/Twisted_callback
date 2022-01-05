from twisted.internet.protocol import ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver


class Client1(LineReceiver):
    def __init__(self):
        self.number = 0
        self.connect = 0
        self.nameFile = ''
        self.chet = 0

    def connectionMade(self):
        self.sendLine(b'CLIENT CONNECT\n')

    def saveFile(self, name):
        with open(name, 'wb') as file:
            return file

    def saveData(self, file, data):
        file.write(data)

    def lineReceived(self, line):
        def ConnectServer(line):
            line = line.decode("UTF-8")
            print(line)
            data = input('введите количество картинок: ')
            data = data.encode("UTF-8")
            self.sendLine(data)
            self.sendLine(b'ready')
            self.connect+=1

        def saveFile(name, data):
            with open(name, 'wb') as file:
                file.write(data)

        if self.connect == 0:
            ConnectServer(line)
        else:
            try:
                line = line.decode("UTF-8")
                self.nameFile = line
                self.sendLine(b'')
                self.sendLine(b'')
            except UnicodeError:
                print('error')
                saveFile(self.nameFile, line)
                self.sendLine(b'')
                self.sendLine(b'')


class ClientFactory1(ClientFactory):

    def buildProtocol(self, addr):
        return Client1()


if __name__=='__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8051)
    endpoint.connect(ClientFactory1())
    reactor.run()




