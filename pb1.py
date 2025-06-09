from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference

def topology():
    net = Mininet_wifi(controller=Controller, link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', position='10,20,0', wlan='wlan0', ieee80211_mode='a')
    sta2 = net.addStation('sta2', position='20,20,0', wlan='wlan0', ieee80211_mode='g')
    sta3 = net.addStation('sta3', position='30,20,0', wlan='wlan0', ieee80211_mode='n')
    ap1 = net.addAccessPoint('ap1', ssid='wifi-ssid', mode='g', channel='1', position='20,40,0')
    c1 = net.addController('c1')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap1)

    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if _name_ == '_main_':
    setLogLevel('info')
    topology()
