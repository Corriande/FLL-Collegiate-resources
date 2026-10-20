from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Initialize the SPIKE Prime hub
hub = PrimeHub()

# Initialize the motors on ports B and D
# Note: If they are on opposite sides of a robot, you might need to set 
# one to Direction.COUNTERCLOCKWISE so they drive the same way.

# F and B are wheels
motor_b = Motor(Port.B)
motor_F = Motor(Port.F)

# E is left gear/attachment
motor_e = Motor(Port.E)


# Spin both wheels at 500 degrees per second
motor_b.run(500)
motor_F.run(-500)


# Keep them spinning for 3 seconds (3000 milliseconds)
wait(1000)

# Stop the motors
motor_b.stop()
motor_F.stop()
# motor_e.stop()