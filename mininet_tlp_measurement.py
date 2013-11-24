from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel 
from mininet.node import Node

class BasicTopology(Topo):
    def __init__(self, **opts):
        #Initialise
        Topo.__init__(self, **opts)
        self.addHost('hostA',ip="10.0.0.2",defaultRoute="10.0.0.1")
        self.addHost('hostB',ip="10.0.0.1")
        self.addHost('hostC',ip="10.0.0.3",defaultRoute="10.0.0.1")
        self.addLink(hostB,hostA)
        self.addLink(hostB,hostC)

def simpleTest():
    "Create and test a simple network"
    topo = BasicTopology()
    net = Mininet(topo)
    net.start()
    print "Dumping host Connections"
    dumpNodeConnections(net.hosts)
    net.pingAll()
    net.stop

if __name__=="__main__":
    setLogLevel('info')
    simpleTest()
