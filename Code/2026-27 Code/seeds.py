from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left = Motor(Port.F)
right = Motor(Port.B, Direction.COUNTERCLOCKWISE)

left_arm = Motor(Port.E)

robot = DriveBase(left, right, wheel_diameter=56, axle_track=110)

left_arm.run_target(500, 0)

robot.straight(200)
robot.turn(-90)
robot.straight(230)
robot.turn(45.5)
robot.straight(140.8)
left_arm.run_angle(500,75)
robot.straight(-200)
