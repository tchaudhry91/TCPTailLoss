from mininet.node import Host

def transferFileUsingNc6(hostA,hostC):
	hostA.cmd("nc6 -X -l -p 7676 < /dev/zero")
	hostC.cmd("nc6 -X 192.168.1.2 7676 > /dev/zero")
