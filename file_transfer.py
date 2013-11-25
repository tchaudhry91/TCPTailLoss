from mininet.node import Host

def transferFileUsingNc6(hostA,hostC):
    print(hostA.cmd("nc6 -X -l -p 7676 < /dev/zero &"))
    print(hostC.cmd("nc6 -X 192.168.1.2 7676 > target"))
