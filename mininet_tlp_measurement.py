from basic_topology import BasicTopology
from basic_topology import configureHosts
from mininet.net import Mininet
from mininet.link import TCLink
from file_transfer import transferFileUsingNc6
from file_transfer import getPayloadSize
from mininet.cli import CLI
from TCPDump import startDump
from TCPDump import stopDump
import time
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
    time.sleep(1)
    startDump(net.get('hostB'), args.DumpFileName)

    #Start DropTail
    hostB = net.get('hostB')
    hostB.cmd("python drop_tail.py " + args.DropCount +
              " " + str(getPayloadSize(args.TransferSize)) +
              " 2>error.txt &")

    #Start Transfer
    transferFileUsingNc6(net.get('hostA'), net.get('hostC'),
                         args.TransferSize)
    stopDump(net.get('hostB'))
    time.sleep(1)
    net.stop()


def addArguments(parser):
    parser.add_argument("ConfigLink1",
                        help=("The Configuration Of Link 1 -" +
                              " Fast/Moderate/Slow"))
    parser.add_argument("ConfigLink2",
                        help=("The Configuration of Link 2 -" +
                              " Fast/Moderate/Slow"))
    parser.add_argument("TransferSize",
                        help=("Short/Medium/Long"))
    parser.add_argument("DumpFileName",
                        help=("The Name you want of the generated TCPDump"))
    parser.add_argument("DropCount",
                        help=("Number of Segments to drop at the end"))

if __name__ == "__main__":
    start()
