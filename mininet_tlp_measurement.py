from basic_topology import BasicTopology
from basic_topology import configureHosts
from mininet.net import Mininet
from mininet.link import TCLink
from file_transfer import transferFileUsingNc6

import argparse

def start():
    """
        Initiate a MininetTLPMeasurementSession.
    """
    #ParseArguments
    parser = argparse.ArgumentParser()
    addArguments(parser)
    args = parser.parse_args()

    #Build Topology
    topo = BasicTopology(args.ConfigLink1,
                         args.ConfigLink2)
    net = Mininet(topo=topo, link=TCLink)
    configureHosts(net)
    
    #Start Network and Measurement
    net.start()
    net.pingAll()
    transferFileUsingNc6(net.get('hostA'),net.get('hostC'),args.TransferSize)
    net.stop()


def addArguments(parser):
    parser.add_argument("ConfigLink1", 
                        help=("The Configuration Of Link 1 -"+
                              " Fast/Moderate/Slow"))
    parser.add_argument("ConfigLink2",
                        help=("The Configuration of Link 2 -"+
                              " Fast/Moderate/Slow"))
    parser.add_argument("TransferSize",
                        help=("Short/Medium/Long"))

if __name__=="__main__":
    start()
