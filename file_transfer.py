from mininet.node import Host


def transferFileUsingNc6(hostA, hostC, transferSize):
    if transferSize == "short":
        count = 64
    elif transferSize == "medium":
        count = 128
    elif transferSize == "long":
        count = 256
    read_cmd = "dd if=/dev/zero count="+str(count)+" bs=1448"
    hostA.cmd(read_cmd+" | nc6 -X -l -p 7676 &")
    hostC.cmd("nc6 -X 192.168.1.2 7676 > /dev/null ")
