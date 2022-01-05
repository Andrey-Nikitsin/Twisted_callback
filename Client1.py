from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint


def gen(number):
    print('run gen')
    numbers = int(number)
    a = 0
    while a < numbers:
        if a == 0:
            a+=1
            yield 0
        else:
            a += 1
            yield 1


class Client1(Protocol):
    def __init__(self):
        self.number = 0
        self.connect = 0

    # def connectionMade(self):
    #     pass
    #     # self.transport.write(b'CLIENT CONNECT')


    def dataReceived(self, data):
        data = data.decode("UTF-8")
        def FirstConnect(data):
            print(data)
            answer = input()
            self.number = answer
            answer = answer.encode("UTF-8")
            self.transport.write(answer)
            self.connect+=1
        if self.connect == 0:
            FirstConnect(data)
        def CreateFile(data):
            with open(data, 'wb') as file:
                return file
        print(data)
        if data == "ok":
            print(data)
            gen(self.number)

        # if gen(self.number) == 1:
        #     CreateFile(data)



class ClientFactory1(ClientFactory):

    def buildProtocol(self, addr):
        return Client1()


if __name__=='__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8051)
    endpoint.connect(ClientFactory1())
    reactor.run()




