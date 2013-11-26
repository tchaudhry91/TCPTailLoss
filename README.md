Milestone 1
Mininet TCP Tail Loss Measurement

Tanmay Chaudhry ga35luj 
Jay Shah        ga35zub

USAGE DOCUMENTATION:
For all usage queries use --help or -h option
sudo python mininet_tlp_measurement.py -h
    the help command specifies all the available options

sample usage:
sudo python mininet_tlp_measurement.py link1Config link2config transferSize
                                                        fileToDump


The project here does the following :
    Create a simple topology using mininet (described below):
        HostA <-----LinkA-----> HostB <----LinkB----> HostC
        Here HostA and HostC act as normal nodes and HostB acts as a router.

        Most of the above topology is defined in the file 'basic_topology.py'
            This File contains a Class BasicTopology to create the actual topo.
            Another function (configureHosts) is used to set IP Addresses and
            the routing information for hostB.
            The links betweens the hosts are configured using a supplied param.

    The second task to use nc6 for a file transfer is defined in the file
    'file_transfer.py'. 
    The number of bytes to transfer is calculated as follows (MTU*Segments).
    This is then sent over the network.

    The third task involving creating a tcp dump is also created in a separate
    file TCPDump.py. The method here takes the argument of the filename to which 
    the data has to be dumped.

Finally mininet_tlp_measurement.py brings together the above 3 tasks.

        
