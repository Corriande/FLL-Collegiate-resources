from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

hub = PrimeHub()
leftWheel   = Motor(Port.F, Direction.COUNTERCLOCKWISE)
rightWheel  = Motor(Port.B, Direction.CLOCKWISE)
wheelsize   = 62.4
axletrackwidth = 110
#robot and robot initial settings
robot = DriveBase(leftWheel,rightWheel,wheelsize,axletrackwidth)
robot.settings(straight_speed=400,straight_acceleration=700,turn_rate=400,turn_acceleration=700 )

#left attachment motor
LAM = Motor(Port.E, Direction.COUNTERCLOCKWISE)
#right attachment motor
RAM = Motor(Port.A,Direction.COUNTERCLOCKWISE)

#Turn on Gyro Sensor if the hub is good, turn off if it is bad
robot.use_gyro(True)
hub.imu.reset_heading(0)

async def main():
   if hub.imu.ready():
        
        

      await robot.straight(600)
      await robot.straight(-600)
      await robot.turn(60)
      await robot.straight(400)
      await robot.straight(-800)   
  


# Runs the main program from start to finish.
run_task(main())