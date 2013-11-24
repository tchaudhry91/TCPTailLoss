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
            h.cmdPrint("ifconfig hostA-eth0 192.168.1.2 netmask 255.255.255.0")
	    h.cmdPrint("route add default gw 192.168.1.1")
        elif h.name == "hostB":
	    h.cmdPrint("ifconfig hostB-eth0 192.168.1.1 netmask 255.255.255.0")
            h.cmdPrint("ifconfig hostB-eth1 192.168.2.1 netmask 255.255.255.0")
	    h.cmdPrint("echo 1 > /proc/sys/net/ipv4/ip_forward") 
        elif h.name == "hostC":
            h.cmdPrint("ifconfig hostC-eth0 192.168.2.2 netmask 255.255.255.0")
	    h.cmdPrint("route add default gw 192.168.2.1")

def tests(net):
    for h in net.hosts:
        if h.name == "hostA":
	    print(h.cmd("tracepath 192.168.2.2"))
	if h.name == "hostC":
            print(h.cmd("tracepath 192.168.1.2"))

def simpleTest():
    "Create and test a simple network"
    topo = BasicTopology()
    net = Mininet(topo)
    configureHosts(net)    
    net.start()
    print "Dumping host Connections"
    dumpNodeConnections(net.hosts)
    print(net.hosts)
    #tests(net)
    net.pingAll()
    net.stop()

if __name__=="__main__":
    setLogLevel('info')
    simpleTest()
