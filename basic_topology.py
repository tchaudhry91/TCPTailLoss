from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node

class BasicTopology(Topo):
	def __init__(self, configLink1, configLink2,  **opts):
        #Initialise	
		if configLink1 == "fast":
			self.bw = 1
			self.delay = '5ms'
		elif configLink1 == "moderate":
			self.bw = 0.5
			self.delay = '10ms'
		elif configLink1 == "slow":
			self.bw = 0.1
			self.delay = '20ms'
		
		linkOpts1 = dict(bw=self.bw, delay=self.delay,
						use_tbf=True)
        
		if configLink2 == "fast":
			self.bw2 = 1 
			self.delay2 = '5ms'
		elif configLink2 == "moderate":
			self.bw2 = 0.5
			self.delay2 = '10ms'
		elif configLink2 == "slow":
			self.bw2 = 0.1
			self.delay2 = '20ms'

		linkOpts2 = dict(bw=self.bw2, delay=self.bw2,
						use_tbf=True)
		Topo.__init__(self, **opts)
		hostA = self.addHost('hostA')
		hostB = self.addHost('hostB')
		hostC = self.addHost('hostC')
		self.addLink(hostB,hostA, **linkOpts1)
		self.addLink(hostB,hostC, **linkOpts2)

def configureHosts(net):
    for h in net.hosts:
        if h.name == "hostA":
            h.setIP(intf="hostA-eth0",ip="192.168.1.2/24")
            h.cmdPrint("route add default gw 192.168.1.1")
        elif h.name == "hostB":
            h.setIP(intf="hostB-eth0", ip="192.168.1.1/24")
            h.setIP(intf="hostB-eth1", ip="192.168.2.1/24")
            h.cmdPrint("echo 1 > /proc/sys/net/ipv4/ip_forward") 
            h.setHostRoute(ip="192.168.1.2/24",intf="hostB-eth0")
            h.setHostRoute(ip="192.168.2.2/24",intf="hostB-eth1")
            h.cmd("iptables -A FORWARD -i hostB-eth0 -o hostB-eth1 "+
                        "-p tcp -j NFQUEUE --queue-num 0")
        elif h.name == "hostC":
            h.setIP(intf="hostC-eth0", ip="192.168.2.2/24")
            h.cmdPrint("route add default gw 192.168.2.1")

