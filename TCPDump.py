from mininet.node import Host


def startDump(hostB, fileName):
    hostB.cmd("tcpdump -w "+fileName+" -i hostB-eth0 -s 68 -p &")
    


def stopDump(hostB):
    hostB.cmd("killall tcpdump 2> error.txt")
