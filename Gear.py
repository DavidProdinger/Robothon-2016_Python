import serbus, time

class Gear:
    def drive(self):
        bus = serbus.I2CDev(1)
        bus.open()
        bus.write(5, [11, 0x90, 5, 100])
        bus.write(5, [11, 0x11, 5, 100])
        bus.close()
    def stopMotors(self):
        bus = serbus.I2CDev(1)
        bus.open()
        bus.write(5, [11, 0x90, 5, 0])
        bus.write(5, [11, 0x11, 5, 0])
        bus.close()
    def turnAround(self, dir):
        bus = serbus.I2CDev(1)
        bus.open()
        self.stopMotors()
        if dir == 1:#turnright
            bus.write(5, [11, 0x90,6,200])
            bus.write(5, [11, 0x11,5,200])
        else:#turnleft
            bus.write(5, [11,0x90,5,200])
            bus.write(5, [11,0x11,6,200])
        bus.close()
    def correctLeft(self):
        bus = serbus.I2CDev(1)
        bus.open()
        bus.write(5, [11, 0x90, 5, 50])
        bus.write(5, [11, 0x11, 5, 150])
        bus.close()
    def correctRight(self):
        bus = serbus.I2CDev(1)
        bus.open()
        bus.write(5, [11, 0x90, 5, 150])
        bus.write(5, [11, 0x11, 5, 50])
        bus.close()


