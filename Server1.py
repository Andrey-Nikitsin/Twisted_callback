from twisted.internet import protocol, reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.protocols.basic import LineReceiver
import requests



class Server1(LineReceiver):
    def __init__(self):
        self.schet = 0
        self.number = 0
        self.generator = Server1.gen(self, self.number)
        self.response = None

    URL = "https://loremflickr.com/320/240"

    def connectionMade(self):
        self.sendLine(b'server connect\nenter number of pictures:\n')

    def getFile(url):
        r = requests.get(url, allow_redirects=True)
        return r

    def SendFile(self):
        print('send name')
        self.response = Server1.getFile(Server1.URL)
        file_name = self.response.url.split('/')[-1]
        file_name = file_name.encode("UTF-8")
        self.sendLine(file_name)

    def SendData(self):
        print('send data')
        self.sendLine(self.response.content)

    def gen(self, data):
        print(data)
        a = 0
        while a < data*2:
            a+=1
            if a%2 !=0:
                yield Server1.SendFile(self)
            else:
                yield Server1.SendData(self)

    def lineReceived(self, line):
        if self.number !=0:
            try:
                next(self.generator)
            except StopIteration:
                self.connectionLost()
        else:
            def funk(data):
                self.number = data
                self.generator = Server1.gen(self, self.number)
            def hendlerFunk(line):
                if self.schet == 0:
                    line = line.decode("UTF-8")
                    print(line)
                    self.schet+=1
                else:
                    line = line.decode("UTF-8")
                    if line.isdigit() ==True:
                        self.number +=int(line)
                        funk(self.number)
                    else:
                        self.sendLine(b'enter only a number\n')

            hendlerFunk(line)

class FactoryServer(protocol.ServerFactory):

    def buildProtocol(self, addr):
        return Server1()

if __name__=='__main__':
    endpoint = TCP4ServerEndpoint(reactor, 8051)
    endpoint.listen(FactoryServer())
    reactor.run()