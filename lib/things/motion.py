import machine, onewire, ds18x20, time
import tornado.ioloop
from property import Property
from thing import Thing
from value import Value

metadata = {
    '@type': 'MotionProperty',
    'label': 'Motion Thing',
    'type': 'boolean',
}

class Motion(Thing):

    def __init__(self, pin):
        Thing.__init__(self, 'Motion', ['MotionSensor'], 'Motion Thing')

        self.pir = machine.Pin(pin, machine.PIN.IN)

        self.value = Value(False)
        pty = Property(self, 'motion', self.value, metadata=metadata)
        self.add_property(pty)

        self.timer = tornado.ioloop.PeriodicCallback(
            self.read,
            1000
        )
        self.timer.start()

    def read(self):
        self.value.notify_of_external_update(self.pin.value() == 1)

    def stop(self):
        self.timer.stop()
