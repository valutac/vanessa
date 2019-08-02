import config
import connect
import sys

sys.path.append('/flash/lib/onewire')
sys.path.append('/flash/lib/upy')
sys.path.append('/flash/lib/webthing')
sys.path.append('/flash/lib/things')

from webserver import run_server

connect.connect_to_ap(config.SSID, config.PASSWORD)

def start_server():
	run_server()
