from mininet.node import Host


pid = ''


def startDump(hostB, fileName):
    global pid
    pid = hostB.cmd("tcpdump -w "+fileName+" -i hostB-eth0 -s 68 -p &")
    print(pid)
