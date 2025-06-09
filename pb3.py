#!/usr/bin/python3

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI  # Use CLI, not CLI_wifi

def topology():
    net = Mininet_wifi(controller=Controller)

    info("*** Creating nodes\n")
    ap1 = net.addAccessPoint('ap1', ssid='testwifi', mode='g', channel='1', position='10,10,0', range=120)
    sta1 = net.addStation('sta1', position='20,10,0')
    sta2 = net.addStation('sta2', position='100,10,0')
    c1 = net.addController('c1', controller=Controller)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])

    info("*** Setting IP addresses\n")
    sta1.setIP('10.0.0.1/8')
    sta2.setIP('10.0.0.2/8')

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()

