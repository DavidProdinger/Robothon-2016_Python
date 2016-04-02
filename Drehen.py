import time
from Arm import Arm

arm = Arm()

arm.up()
time.sleep(2)
arm.upDownStop()
time.sleep(2)
arm.down()
time.sleep(2)
arm.upDownStop()
