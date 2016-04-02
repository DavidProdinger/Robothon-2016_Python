import serbus, time
from LineFollower import LineFollower
from Gear import Gear

bus = serbus.I2CDev(1)
bus.open()

department = 3
position = 2
currentDepartment = 0
lastOnline = 1
onLine = 1
changed = False

lineFollower = LineFollower()
gear = Gear()
ifTurnAround = False

while True:
   #print lastOnline , " last Online"
   #print lineFollower.checkIfOnLine() , " onLine"
   if(onLine  == lineFollower.checkIfOnLine()):
       changed = False
   else: 
       changed = True 
   if (ifTurnAround == False):
       onLine = lineFollower.checkIfOnLine()
       lastOnLine = onLine       
       print currentDepartment
       if onLine == 1:     
          gear.drive()
          time.sleep(0.1)
       elif onLine == 3:
          if department == currentDepartment:
              ifTurnAround = True
              gear.drive()
              time.sleep(2.2)
              gear.turnAround(1)       
              time.sleep(3)
              ifTurnAround = False
          else: 
             if changed:
                 currentDepartment += 1  
       elif onLine == 2:
          if department == currentDepartment:
              ifTurnAround = True
              gear.drive()
              time.sleep(2.2)
              gear.turnAround(2)
              time.sleep(3)
              ifTurnAround = False
          else:
              if changed:
                  currentDepartment += 1 
       elif onLine == 4:
          gear.drive()
	  print "Stop"
          time.sleep(1.5)
          gear.stopMotors()
       elif onLine == 5:
          gear.correctLeft()
          time.sleep(0.1)
       elif onLine == 6:
          gear.correctRight()
	  time.sleep(0.1)
       else: 
          gear.stopMotors()
   time.sleep(0.2)
#bus.write(5, [11, 0x10, 5, 0])

#data = bus.write(5, 1)
#print "Byte received: {:x}".format(data[0])

bus.close()



