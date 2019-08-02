import machine, onewire, ds18x20, time
import tornado.ioloop
from property import Property
from thing import Thing
from value import Value

metadata = {
    '@type': 'TemperatureProperty',
    'label': 'Temperature Led',
    'type': 'number',
}

class Temperature(Thing):

    def __init__(self, pin):
        Thing.__init__(self, 'Temperature', ['TemperatureSensor'], 'Temperature Thing')

        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(pin))
        self.roms = self.ds_sensor.scan()

        self.value = Value(0, 0)
        pty = Property(self, 'temperature', self.value, metadata=metadata)
        self.add_property(pty)

        self.timer = tornado.ioloop.PeriodicCallback(
            self.read,
            3000
        )
        self.timer.start()

    def read(self):
        self.ds_sensor.convert_temp()
        time.sleep_ms(750)
        for rom in self.roms:
            value = self.ds_sensor.read_temp(rom)
            self.value.notify_of_external_update(value)

    def stop(self):
        self.timer.stop()
