# -*- coding:utf-8 -*-

from bottle import route, run
import subprocess
import time

USB_ENERGY_ON = ["sudo", "hub-ctrl", "-h", "0", "-P", "2", "-p", "1"]
USB_ENERGY_OFF = ["sudo", "hub-ctrl", "-h", "0", "-P", "2", "-p", "0"]

@route('/flash')
def flashUsb():
    for i in range(4):
        subprocess.call(USB_ENERGY_ON)
        time.sleep(0.7)
        subprocess.call(USB_ENERGY_OFF)
        time.sleep(0.3)

subprocess.call(USB_ENERGY_OFF)
run(host='localhost', port=8080, debug=True)
