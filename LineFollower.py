import serbus, time

class LineFollower:
    def checkIfOnLine(self):
        bus = serbus.I2CDev(1)
        bus.open()
        bus.write(5, [51, 0x30])
        time.sleep(0.02)
        sensorState1 = bus.read(5, 2)
        bus.write(5, [51, 0x60])
        time.sleep(0.02)
        sensorState2 = bus.read(5, 2)
        bus.close()
        
        # print sensorState1[1]
        # print sensorState2[1]

        if (sensorState1[1] == 1) & (sensorState2[1] == 2):
            return 1 #straigth
        elif (sensorState1[1] == 1) & (sensorState2[1] == 0):
            return 2 #turnright
        elif (sensorState1[1] == 0) & (sensorState2[1] == 2):
            return 3 #turnleft
        elif (sensorState1[1] == 3) & (sensorState2[1] == 3):
            return 4 #stop
        elif sensorState2[1] == 3:
            return 5 #correction left
        elif sensorState1[1] == 3:
            return 6 #correction right
        else:
            return -1

                
