import machine
from property import Property
from thing import Thing
from value import Value

metadata = {
    'on': {
        '@type': 'OnOffProperty',
        'label': 'Turn on Led',
        'type': 'boolean',
    },
}

class Led(Thing):

    def __init__(self, pin):
        Thing.__init__(self, 'Led', ['OnOffSwitch', 'Light'], 'Led Thing')
        self.pin = pin
        self.np = machine.Neopixel(machine.Pin(self.pin, machine.Pin.OUT), 24)

        self.state_on = False

        Property(self, 'on', Value(self.state_on, self.on), metadata=metadata['on'])
        self.add_property()

    def on(self):
        pass
