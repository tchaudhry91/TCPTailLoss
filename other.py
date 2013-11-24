from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

class Router_Topo(Topo):
    def __init__(self):
        Topo.__init__(self)
            # Add hosts
            h1 = self.addHost( 'h1' )
            h2 = self.addHost( 'h2' )
            r = self.addHost( 'r' )

            # Add links
            self.addLink( h1, r )
            self.addLink( r, h2 )

def simpleTest():
    topo = Router_Topo()
    net = Mininet(topo)
    #Start Network
    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    r = net.get('r')
    h1.cmd('ifconfig h1-eth0 192.168.12.1 netmask 255.255.255.0')
    h2.cmd('ifconfig h2-eth0 192.168.23.3 netmask 255.255.255.0')
    r.cmd('ifconfig r-eth0 192.168.12.2 netmask 255.255.255.0')
    r.cmd('ifconfig r-eth1 192.168.23.2 netmask 255.255.255.0')

    h1.cmd('route add default gw 192.168.12.2')
    h2.cmd('route add default gw 192.168.23.2')
    r.cmd('sysctl net.ipv4.ip_forward=1')

    #dumpNodeConnections(net.hosts)
    #net.pingAll()
        
    #Run CLI
    CLI(net)
    #Stop Network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    simpleTest()
