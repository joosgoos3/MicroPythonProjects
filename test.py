from machine import Pin
import time

p0 = Pin(2, Pin.OUT)    # create output pin on GPIO0
p0.on()                 # set pin to "on" (high) level
time.sleep(0.5)
p0.off()                # set pin to "off" (low) level
time.sleep(0.5)
p0.on()                 # set pin to "on" (high) level
time.sleep(0.1)
p0.off()                # set pin to "off" (low) level
time.sleep(0.1)
p0.on()                 # set pin to "on" (high) level
time.sleep(0.1)
p0.off()                # set pin to "off" (low) level
time.sleep(0.1)
p0.on()                 # set pin to "on" (high) level
time.sleep(0.1)
p0.off()                # set pin to "off" (low) level
time.sleep(0.1)
p0.on()                 # set pin to "on" (high) level
time.sleep(0.1)
p0.off()                # set pin to "off" (low) level
time.sleep(0.1)
p0.on()                 # set pin to "on" (high) level
time.sleep(0.1)
p0.off()                # set pin to "off" (low) level
time.sleep(0.1)
p0.on()                 # set pin to "on" (high) level
time.sleep(0.1)
p0.off()                # set pin to "off" (low) level
time.sleep(0.1)
print('done')
