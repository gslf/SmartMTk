from MotorDriver import MotorDriver

class SmartMTk:
    """This class manage an RC monstrer truck powered by a RaspberryPI
    """

    def __init__(self):
        """SmartMTk class constructor
        """

        # Init motors
        self.motors = MotorDriver(22,27,17,24,23,18,25)

    def forward(self):
        """Move forward the monster truck
        """
        self.motors.a_forward(100)

    def backward(self):
        """Move backward the monster truck
        """
        self.motors.a_backward(100)

    def shortBrake(self):
        """Short brake
        """
        self.motors.a_shortBrake()

    def turnRight(self):
        """Turn the wheels to the right
        """
        self.motors.b_forward(100)


    def turnLeft(self):
        """Move forward the monster truck
        """
        self.motors.b_backward(100)

    def straight(self):
        """Go straight
        """
        self.motors.b_stop()

