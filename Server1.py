from twisted.internet import protocol, reactor, threads, endpoints
from twisted.internet.defer import Deferred
from twisted.protocols.basic import LineReceiver
import socket
import requests


URL = "https://loremflickr.com/320/240"

def getFile(url):
    r = requests.get(url, allow_redirects=True)
    return r

def WriteFile(response):
    with open('image.jpeg','wb') as file:
        file.write(response.content)

WriteFile(getFile(URL))


class Server1(LineReceiver):

    def connectionMade(self):
        self.transport.write(b'server connect\n')


class FactoryServer(protocol.ServerFactory):

    def buildProtocol(self, addr):
        return Server1()

endpoints.serverFromString(reactor, 'tcp:8051').listen(FactoryServer())
reactor.run()