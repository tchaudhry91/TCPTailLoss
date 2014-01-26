Milestone 1
Mininet TCP Tail Loss Measurement

Tanmay Chaudhry ga35luj 
Jay Shah        ga35zub

mininet_tlp_measurement.py
USAGE DOCUMENTATION:
For all usage queries use --help or -h option
sudo python mininet_tlp_measurement.py -h
    the help command specifies all the available options

sample usages:
sudo python mininet_tlp_measurement.py link1Config link2config transferSize
                                                        fileToDump toDrop

tcp_analysis.py dump_file

automatic_measurements.py TLPStatus link_speeds payloads
    TLPStatus = enabled/disabled
    link_speed = all/fast/moderate/slow
    payloads = all/long/medium/short
    *NOTE - TLP status must be set manually, the script does not change the 
            kernel variable.


The project here does the following :
    Create a simple topology using mininet (described below):
        HostA <-----LinkA-----> HostB <----LinkB----> HostC
        Here HostA and HostC act as normal nodes and HostB acts as a router.

        Most of the above topology is defined in the file 'basic_topology.py'
            This File contains a Class BasicTopology to create the actual topo.
            Another function (configureHosts) is used to set IP Addresses and
            the routing information for hostB.
            The links betweens the hosts are configured using a supplied param.

    The network is also configured so as to DROP a predefined number of packets
    at the end of the queue.
    This is done using a netfilter queue and directing all traffic to it.
    An implicit call to drop_tail ensures proper drop according to the supplied
    argument.
    
    The second task to use nc6 for a file transfer is defined in the file
    'file_transfer.py'. 
    The number of bytes to transfer is calculated as follows (MTU*Segments).
    This is then sent over the network.

    The third task involving creating a tcp dump is also created in a separate
    file TCPDump.py. The method here takes the argument of the filename to which 
    the data has to be dumped.

Since we have a number of configurations to work with, an automatic measurement script,
automatic_measurements.py, generates measurements for the total time taken for complet
ing the transmission and the time between the first packed dropped and first packed 
retransmitted (using a call to tcp_analysis, which calculates this using the generated
dump).

With all the measurements available, to put them in a more readable and easily analyse
them, we use a script to plot box and whisker plots for each of the configurations.
Highlighting differences between TLP enabled and disabled

