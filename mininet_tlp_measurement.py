from basic_topology import BasicTopology
from basic_topology import configureHosts
from mininet.net import Mininet

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
    net = Mininet(topo)
    configureHosts(net)
    
    #Start Network and Measurement
    net.start()
    net.pingAll()
    net.stop()


def addArguments(parser):
    parser.add_argument("ConfigLink1", 
                        help=("The Configuration Of Link 1 -"+
                              " Fast/Moderate/Slow"))
    parser.add_argument("ConfigLink2",
                        help=("The Configuration of Link 2 -"+
                              " Fast/Moderate/Slow"))


if __name__=="__main__":
    start()
