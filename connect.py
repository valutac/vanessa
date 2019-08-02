import network
import time


def connect_to_ap(ssid, password):
    station = network.WLAN(network.STA_IF)
    if not station.active():
        station.active(True)
        if not station.isconnected():
            print('Connecting to', ssid)
            station.connect(ssid, password)
            while not station.isconnected():
                time.sleep(1)
                print('.', end='')
            print('')
    print('ifconfig =', station.ifconfig())