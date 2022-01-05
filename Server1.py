from twisted.internet import protocol, reactor, threads, endpoints
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.defer import Deferred
from twisted.protocols.basic import LineReceiver
import socket
import requests


# URL = "https://loremflickr.com/320/240"
#
# def getFile(url):
#     r = requests.get(url, allow_redirects=True)
#     return r
#
# def WriteFile(response):
#     with open('image.jpeg','wb') as file:
#         file.write(response.content)
#
# WriteFile(getFile(URL))


class Server1(protocol.Protocol):

    def connectionMade(self):
        self.transport.write(b'server connect\n')
        self.transport.write(b'enter number of pictures:\n')

    def dataReceived(self, data):
        data = data.decode("UTF-8")

        URL = "https://loremflickr.com/320/240"

        def getFile(url):
            r = requests.get(url, allow_redirects=True)
            return r

        def FileName(response):
            print('send')
            file_name = response.url.split('/')[-1]
            file_name = file_name.encode("UTF-8")
            self.transport.write(file_name)

        def sendFile(data):
            a=0
            while a < int(data):
                FileName(getFile(URL))
                a+=1

        print(data)
        if data == 'CLIENT CONNECT':
            pass
        else:
            if data.isdigit() == True:
                self.transport.write(b'ok')
                sendFile(data)
            else:
                self.transport.write(b'enter only numbers\n')

class FactoryServer(protocol.ServerFactory):

    def buildProtocol(self, addr):
        return Server1()

if __name__=='__main__':
    endpoint = TCP4ServerEndpoint(reactor, 8051)
    endpoint.listen(FactoryServer())
    reactor.run()