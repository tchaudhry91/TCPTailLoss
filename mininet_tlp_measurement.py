from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel 

class BasicTopology(Topo):
    def __init__(self, **opts):
        #Initialise
        Topo.__init__(self, **opts)
        hostA = self.addHost('hostA')
        hostA.seIP('10.0.0.1')
        hostB = self.addHost('hostB')
        hostC = self.addHost('hostC')
        self.addLink(hostA,hostB)
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
