import blescan
import sys
import bluetooth._bluetooth as bluez

dev_id = 0
try:
    sock = bluez.hci_open_dev(dev_id)
    print "ble thread started"

except:
    print "error accessing bluetooth device..."
    sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

DEVICES = {'7c:2f:80:97:cb:ac': {'name': 'gtag arancio'}}

while True:
    returnedList = blescan.parse_events(sock, 10)
    for found in returnedList:
        address = found.split(',')
        if DEVICES.get(address[0]):
            print "Found %s" % address[0]
            print DEVICES.get(address[0]).get('name')

