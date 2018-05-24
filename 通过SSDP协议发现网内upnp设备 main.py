#!/usr/bin/env python2
import socket  
import sys

dst = "239.255.255.250"  
if len(sys.argv) > 1:  
    dst = sys.argv[1]
st = "upnp:rootdevice"  
st = "ssdp:all"
if len(sys.argv) > 2:  
    st = sys.argv[2]

msg = [  
    'M-SEARCH * HTTP/1.1',
    'Host:172.16.2.35:1900', #µ¥²¥
    #'Host:239.255.255.250:1900', #×é²¥
    'ST:%s' % (st,),
    'Man:"ssdp:discover"',
    'MX:3',
    '']

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  


s.settimeout(10)  
s.sendto('\r\n'.join(msg), (dst, 1900) )



# s.bind(address)

while True:  
    try:
        data, addr = s.recvfrom(32*1024)
    except socket.timeout:
        continue
        break
    print "[+] %s\n%s" % (addr, data)
    
print "finish"