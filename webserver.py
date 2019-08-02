import logging
from server import MultipleThings, WebThingServer
from temperature import Temperature

log = logging.getLogger(__name__)

def run_server():
    log.info('preparing to run server')
    tempThing = Temperature(15)

    server = WebThingServer(MultipleThings([tempThing], 'SparkFun-ESP32-Thing'), port=80)

    try:
        log.info('starting the server')
        server.start()
    except KeyBoardInterrupt:
        log.info('stopping the server')
        server.stop()
        tempThing.stop()
        log.info('done')
