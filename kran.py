import time
from Arm import Arm

arm = Arm()

status = 0

while True:
    if status == 0:
        print "Rauf fahren"
        arm.up()
        time.sleep(8)
        print "Oben"
        arm.upDownStop()
        status = 1
    elif status == 1:
	#arm.release()
	time.sleep(1.2)
	arm.holdItem()
 	arm.fwd()
	time.sleep(5)
	status = 2
    elif status == 2:
	time.sleep(3)
	status = 3
    elif status == 3:
	arm.grap()
	time.sleep(1.3)
	arm.holdItem()
	time.sleep(1)
	arm.up()
	time.sleep(1.2)
	arm.upDownStop()
	status = 4
    elif status == 4:
	arm.backwd()
	arm.turnLeft()
	status = 5
    elif status == 5:
	arm.down()
	time.sleep(8)
	arm.upDownStop()
	status = 6
    elif status == 6:
	arm.fwd()
	time.sleep(3)
	arm.inOutStop()
	arm.release()
	time.sleep(1)
	arm.holdItem()
	status = 7
    elif status == 7:
	#arm.down()
	time.sleep(1)
	arm.upDownStop()
	arm.turnRight()
