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
        
        

      await robot.straight(720)
      await robot.turn(100)
      await LAM.run_angle(600,300)
      await robot.turn(2)
      await robot.straight(85)
      await robot.turn(17)
      await LAM.run_angle(-100 ,150)
      await robot.straight(-100)
      await robot.turn(-50)
      await robot.turn(-33)
      await robot.straight(-100)
      await robot.turn(30)
      await LAM.run_angle(-2000 ,75)
      await robot.turn(90)
      await robot.straight(50)


      
     
  


# Runs the main program from start to finish.
run_task(main())