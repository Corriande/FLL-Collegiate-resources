# Simple settings program to ensure all robots are on the same shared settings
# DO NOT ALTER AFTER AGREEING ON SHARED SETTINGS
# At start of later scripts, use "from robot_settings import robot, ready" and 
# run ready() at start of program and then robot.straight, robot.turn, etc. as normal 

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Define left and right wheels
left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right = Motor(Port.D)

# Define DriveBase using left + right motors
# Note: Wheel diameter of 56 is for standard blue spike wheel
# Axle track can be calculated used a bea m of length N
# If the center of the wheels are on the end holes of an N length beam -> (N-1) x 8, ex. 15 beam -> (15-1) x 8 = 112
# If the center of the wheels are flush (perfectly lined up) with the ends of an N length beam -> N x 8, ex. 15 beam -> 15 x 8 = 120
robot = DriveBase(left, right, wheel_diameter=56, axle_track=120)

# Use gyro for turns and straights for higher accuracy turns and straights
robot.use_gyro(True)

# Define robot speed and acceleration settings by standardizing speed and acceleration
# This will assist in reducing wheel slip and slight changes to angles or distances caused by fast and jerky movement
# NOTE: There is a balance of speed and accuracy. Trying to maximize speed will cause stalling down the line. Maximum speed on motors is 
# ~480mm/s anyway, better to stay at 400 or below to ensure proper steering. Trying to go too fast will reduce tolerance accuracy
# and cause robot to stop. 

robot.settings(
    straight_speed=500,
    turn_rate=180,
    # Acceleration settings can take a tuple (two numbers), meaning it can take
    # input of (launch speed, landing speed) so (300, 150) is a faster launch with a softer landing
    # which allows for speed while still allowing better accuracy at slow down time
    straight_acceleration=(300, 150), 
    turn_acceleration=(300, 150)  
)

# Distance moves are "done" when BOTH are true:
#   - the robot is moving slower than 20 mm/s (basically stopped)
#   - it's within 2 mm of the target (ex. robot.straight(500) -> between 498 and 502 mm)
# If it's slowed down but not within 2 mm yet, it nudges forward or back
# until it is, then holds position.
robot.distance_control.target_tolerances(speed=20, position=2)

# Turns are "done" when BOTH are true:
#   - the robot is turning slower than 50 deg/s (basically stopped)
#   - it's within 1 degree of the target (ex. robot.turn(180) -> between 179 and 181 degrees)
# If it's slowed down but not within 1 degree yet, it nudges left or right
# until it is, then holds position.
robot.heading_control.target_tolerances(speed=50, position=1)

# Function to call at beginning of run
# This allows for the gyroscope to settle before initiating the run
def ready():
    wait(1000)
    robot.reset()
