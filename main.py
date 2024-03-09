#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from time import time, sleep


print("[", end='')

m = Motor(Port.A)

m.dc(-100)
sleep(3)

st = time()
for duty in range(-100, 101):

    m.dc(duty)

    loopT = time()
    while time() - loopT < 0.5:
        print([time() - st, duty, m.speed()], ',')

m.dc(0)

print("]")
