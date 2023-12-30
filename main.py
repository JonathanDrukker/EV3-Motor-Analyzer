#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from time import time, sleep


m = Motor(Port.A)

times = []
speeds = []
dutys = []

filename = 'analysis.log'

st = time()
for duty in range(0, 101):

    m.dc(duty)

    loopT = time()
    while time() - loopT < 0.5:

        times.append(time() - st)
        speeds.append(m.speed())
        dutys.append(duty)

m.dc(0)

acc = []
_speed = []
_dutys = []

dutys.append(101)

for duty in range(0, 101):

    index = dutys.index(duty)
    slice = speeds[index:dutys.index(duty+1)]

    maxV = max(slice)
    maxVIndex = slice.index(maxV) + index

    deltaT = times[maxVIndex] - times[index]

    if deltaT == 0:
        acc.append(0)
    else:
        acc.append(maxV / deltaT)

    _speed.append(maxV)
    _dutys.append(duty)


with open(filename, 'w') as f:
    f.write(
        str({'duty': _dutys, 'time': times, 'velocity': _speed,
             'acceleration': acc}))

sleep(1)

times = []
speeds = []
dutys = []

filename = 'analysis.log'

st = time()
for duty in range(0, -101, -1):

    m.dc(duty)

    loopT = time()
    while time() - loopT < 0.5:

        times.append(time() - st)
        speeds.append(m.speed())
        dutys.append(duty)

m.dc(0)

acc = []
_speed = []
_dutys = []

dutys.append(-101)

for duty in range(0, -101, -1):

    index = dutys.index(duty)
    slice = speeds[index:dutys.index(duty-1)]

    maxV = max(slice)
    maxVIndex = slice.index(maxV) + index

    deltaT = times[maxVIndex] - times[index]

    if deltaT == 0:
        acc.append(0)
    else:
        acc.append(maxV / deltaT)

    _speed.append(maxV)
    _dutys.append(duty)


with open("negative_"+filename, 'w') as f:
    f.write(
        str({'duty': _dutys, 'time': times, 'velocity': _speed,
             'acceleration': acc}))
