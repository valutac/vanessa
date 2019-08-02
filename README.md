# Vanessa - Web of Things Boilerplate

## Quick Start

### Flashing Loboris Micropython

Clone the fork of Loboris Micropython repository, this repository has been
updated to allow PUT command to work with microWebSrv and fix for microWebSocket
based on [this](https://github.com/dhylands/MicroPython_ESP32_psRAM_LoBo) branch and latest update from [Loboris](https://github.com/dhylands/MicroPython_ESP32_psRAM_LoBo) master branch

```
$ git clone https://github.com/ariestiyansyah/MicroPython_ESP32_psRAM_LoBo.git
```

Config the micropython and build the Firmware
```
$ cd MicroPython_ESP32_psRAM_LoBo/MicroPython_BUILD/
$ ./BUILD.sh menuconfig
$ ./BUILD.sh
```

Flash it
This example using SparkFun ESP32 Thing on Mac

```
$ ./BUILD.sh --port /dev/tty.usbserial-DN03F9EP flash
```

SparkFun connected to my mac using `/dev/tty.usbserial-DN03F9EP` port, this will be
different on each device, check it using following command

```
$ ls /dev/tty.usbserial*
```

### Install Gateway

Follow instruction from
[https://github.com/mozilla-iot/gateway/blob/master/README.md](https://github.com/mozilla-iot/gateway/blob/master/README.md)
to install Mozilla Gateway in your Raspberry Pi or PC/Mac.

### Web of Things Micropython

Clone  project
```
$ git clone https://github.com/valutac/vanessa.git
```


change variable SSID and PASSWORD value in `config.py` with wifi credentials, for example
```
SSID = 'vanessa'
PASSWORD = 'wot'
```

Sync local files to ESP32 by using [rshell](https://github.com/dhylands/rshell),
you can also use ampy :) mine is rhsell.

```
$ rshell -a --buffer-size=30 -p /dev/tty.usbserial-DN03F9EP
fitra> rsync -v . /flash
fitra> repl
>>> Control-D # Soft reset
```

## HOW TO ADD THINGS

TO DO

