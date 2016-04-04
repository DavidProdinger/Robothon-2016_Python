import serbus, time

class Arm:
    def turnLeft(self):
        bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [22, 0x20, 0,0,0x23,0x28])
	bus.close()
    def turnStop(self):
	bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [22, 0x20, 0,0,0,0])
	bus.close()
    def turnRight(self):
	bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [22, 0x20, 0xff,0xff,0xdc,0xd8])
	bus.close()
    def grap(self):
	bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [11, 0xa0, 5, 100])
	bus.close()
    def release(self):
	bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [11, 0xa0, 6, 100])
	bus.close()
    def holdItem(self):
	bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [11, 0xa0, 6, 0])
	bus.close()
    def up(self):
	bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [11, 0x90, 6, 100])
	bus.close()
    def upDownStop(self):
	bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [11, 0x90,5,0])
        bus.close()    
    def down(self):
        bus = serbus.I2CDev(1)
        bus.open()
        bus.write(10, [11, 0x90, 5, 50])
        bus.close()     
    def fwd(self):
	bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [22, 0x10, 0,0,0x23,0x28])
	bus.close()
    def backwd(self):
	bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [22, 0x10, 0xff,0xff,0xdc,0xd8])
	bus.close()
    def inOutStop(self):
	bus = serbus.I2CDev(1)
	bus.open()
	bus.write(10, [22, 0x10, 0,0,0,0])
	bus.close()
