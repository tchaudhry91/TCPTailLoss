from mininet.node import Host

def startDump(hostB,fileName):
    hostB.cmd("tcpdump -w "+fileName+" -i hostB-eth0 -s 68 -p &")
