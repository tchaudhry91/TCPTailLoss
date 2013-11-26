from mininet.node import Host

def transferFileUsingNc6(hostA,hostC,transferSize):
    if transferSize == "short":
        bytesT = (1500*64)
    elif transferSize == "medium":
        bytesT = (1500*128)
    elif transferSize == "long":
        bytesT = (1500*256)
    hostA.cmd("dd if=/dev/zero of=temp count="+str(bytesT)+" bs=1")
    hostA.cmd("nc6 -X -l -p 7676 < temp &")
    hostC.cmd("nc6 -X 192.168.1.2 7676 > /dev/null")
    hostA.cmd("rm temp")
