import RPi.GPIO as GPIO

class MotorDriver:
    """This class manages 2 motors through the TB6612FNC motor driver

    Attribs:
        a_in1 (int)   . Pin # for motor A input 1
        a_in2 (int)   . Pin # for motor A input 2
        a_pwm         . Pin # for motor A pwm
        b_in1 (int)   . Pin # for motor B input 1
        b_in2 (int)   . Pin # for motor B input 2
        b_pwm         . Pin # for motor B pwm
        stby        . Pin # for motor stby
        freq        . Motor frequency
    """

    def __init__(self, a_in1, a_in2, a_pwm, b_in1, b_in2, b_pwm, stby):
        """Motor class constructor

        Params:
            a_in1 (int)   . Pin # for motor input 1
            a_in2 (int)   . Pin # for motor input 2
            a_pwm         . Pin # for motor pwm
            b_in1 (int)   . Pin # for motor input 1
            b_in2 (int)   . Pin # for motor input 2
            b_pwm         . Pin # for motor pwm
            stby        . Pin # for motor stby
        """

        # Load attrbutes from params
        self.a_in1 = a_in1
        self.a_in2 = a_in2
        self.a_pwm = a_pwm
        self.b_in1 = b_in1
        self.b_in2 = b_in2
        self.b_pwm = b_pwm
        self.stby = stby

        # Load default attributes
        self.freq = 1000 #hertz
        
        # Setup GPIO mode
        GPIO.setmode(GPIO.BCM)

        # Setup pins
        GPIO.setup(a_in1,GPIO.OUT)
        GPIO.setup(a_in2,GPIO.OUT)
        GPIO.setup(a_pwm,GPIO.OUT)
        GPIO.setup(b_in1,GPIO.OUT)
        GPIO.setup(b_in2,GPIO.OUT)
        GPIO.setup(b_pwm,GPIO.OUT)
        GPIO.setup(stby,GPIO.OUT)
        GPIO.output(stby,GPIO.HIGH)

        # Setup PWM
        self.rpi_a_pwm = GPIO.PWM(a_pwm, self.freq)
        self.rpi_a_pwm.start(0)
        self.rpi_b_pwm = GPIO.PWM(b_pwm, self.freq)
        self.rpi_b_pwm.start(0)




    def a_forward(self, speed):
        """Motor A: move forward at certain speed

        Params:
            speed (int) - Movement speed 0-100
        """
        GPIO.output(self.a_in1,GPIO.HIGH)
        GPIO.output(self.a_in2,GPIO.LOW)
        self.rpi_a_pwm.ChangeDutyCycle(speed)


    def a_backward(self, speed):
        """Motor A: move backward at certain speed

        Params:
            speed (int) - Movement speed 0-100
        """
        GPIO.output(self.a_in1,GPIO.LOW)
        GPIO.output(self.a_in2,GPIO.HIGH)
        self.rpi_a_pwm.ChangeDutyCycle(speed)


    def a_shortBrake(self):
        """Motor A: sort brake 
        """
        GPIO.output(self.a_in1,GPIO.HIGH)
        GPIO.output(self.a_in2,GPIO.HIGH)
        self.rpi_a_pwm.ChangeDutyCycle(0)

    def a_stop(self):
        """Motor A: stop 
        """
        GPIO.output(self.a_in1,GPIO.LOW)
        GPIO.output(self.a_in2,GPIO.LOW)
        self.rpi_a_pwm.ChangeDutyCycle(0)


    def b_forward(self, speed):
        """Motor B: move forward at certain speed

        Params:
            speed (int) - Movement speed 0-100
        """
        GPIO.output(self.b_in1,GPIO.HIGH)
        GPIO.output(self.b_in2,GPIO.LOW)
        self.rpi_b_pwm.ChangeDutyCycle(speed)

    def b_backward(self, speed):
        """Motor B: move backward at certain speed

        Params:
            speed (int) - Movement speed 0-100
        """
        GPIO.output(self.b_in1,GPIO.LOW)
        GPIO.output(self.b_in2,GPIO.HIGH)
        self.rpi_b_pwm.ChangeDutyCycle(speed)


    def b_shortBrake(self):
        """Motor B: sort brake 
        """
        GPIO.output(self.b_in1,GPIO.HIGH)
        GPIO.output(self.b_in2,GPIO.HIGH)
        self.rpi_b_pwm.ChangeDutyCycle(0)

    def b_stop(self):
        """Motor B: stop 
        """
        GPIO.output(self.b_in1,GPIO.LOW)
        GPIO.output(self.b_in2,GPIO.LOW)
        self.rpi_b_pwm.ChangeDutyCycle(0)

    def standby(self):
        """Motor driver standby
        """
        self.rpi_a_pwm.ChangeDutyCycle(0)
        self.rpi_b_pwm.ChangeDutyCycle(0)
        GPIO.output(self.stby,value)

    def __del__(self):
        """GPIO cleanup when object will be destroyed
        """
        GPIO.cleanup()
