from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel 
from mininet.node import Node

class BasicTopology(Topo):
    def __init__(self, **opts):
        #Initialise
        Topo.__init__(self, **opts)
        hostA = self.addHost('hostA')
        hostB = self.addHost('hostB')
        hostC = self.addHost('hostC')
        self.addLink(hostB,hostA)
        self.addLink(hostB,hostC)

def configureHosts(net):
    for h in net.hosts:
        if h.name == "hostA":
            h.setIP("10.0.0.3")
            h.setDefaultRoute('hostA-eth0')
        elif h.name == "hostB":
            h.setIP(ip="10.0.0.1", intf="hostB-eth0")
            h.setIP(ip="10.0.0.2", intf="hostB-eth1")
            h.setHostRoute(ip="10.0.0.3", intf="hostB-eth0")
            h.setHostRoute(ip="10.0.0.4", intf="hostB-eth1")
        elif h.name == "hostC":
            h.setIP("10.0.0.4")
            h.setDefaultRoute('hostC-eth0')

def simpleTest():
    "Create and test a simple network"
    topo = BasicTopology()
    net = Mininet(topo)
    configureHosts(net)    
    net.start()
    print "Dumping host Connections"
    dumpNodeConnections(net.hosts)
    print(net.hosts)
    net.pingAll()
    net.stop

if __name__=="__main__":
    setLogLevel('info')
    simpleTest()
