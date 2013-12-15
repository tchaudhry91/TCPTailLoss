from basic_topology import BasicTopology
from basic_topology import configureHosts
from mininet.net import Mininet
from mininet.link import TCLink
from file_transfer import transferFileUsingNc6
from mininet.cli import CLI
from TCPDump import startDump
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
    startDump(net.get('hostB'), args.DumpFileName)
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
    parser.add_argument("DumpFileName",
                        help=("The Name you want of the generated TCPDump file"))
    parser.add_argument("PayloadSize",
                        help=("Argument for drop_tail, the size of Payload"))
    parser.add_argument("DropCount",
                        help=("Number of Segments to drop at the end"))

if __name__=="__main__":
    start()
