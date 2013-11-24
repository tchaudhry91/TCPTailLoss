from basic_topology import BasicTopology
from basic_topology import configureHosts
from mininet.net import Mininet

def start():
    """
    """
    topo = BasicTopology()
    net = Mininet(topo)
    configureHosts(net)
    net.start()
    net.pingAll()
    net.stop()

if __name__=="__main__":
    start()
