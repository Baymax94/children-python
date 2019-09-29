#!/usr/bin/python
"""
  This class is a port from the https://github.com/sparkfun/RedBot Arduino library into Pymata-aio
  It is NOT a complete port. It just shows some of the main basic features.  Feel free to port more.
"""
from pymata_aio.constants import Constants
from .mma8452q3 import MMA8452Q3 # Some IDEs mark this type of import style as an error, but it should work fine.

# RedBot motor pins from RedBot.h
L_CTRL_1 = 2
L_CTRL_2 = 4
PWM_L = 5

R_CTRL_1 = 7
R_CTRL_2 = 8
PWM_R = 6

ENCODER_PIN_LEFT = 16
ENCODER_PIN_RIGHT = 10

DIRECTION_FORWARD = 1
DIRECTION_REVERSE = -1
encoder_object = None

class RedBotEncoder:
    def __init__(self, board):
        global encoder_object
        encoder_object = self # Save a global reference to the one and only encoder_object so that the motors can set the direciton.
        self.board = board
        self.left_encoder_count = 0
        self.right_encoder_count = 0
        self.left_direction = DIRECTION_FORWARD # default to forward if not set
        self.right_direction = DIRECTION_FORWARD # default to forward if not set
        board.encoder_config(ENCODER_PIN_LEFT, ENCODER_PIN_RIGHT, self.encoder_callback,
                             Constants.CB_TYPE_DIRECT, True)

    def encoder_callback(self, data):
        if self.left_direction == DIRECTION_FORWARD:
            self.left_encoder_count += data[0]
        else:
            self.left_encoder_count -= data[0]
        if self.right_direction == DIRECTION_FORWARD:
            self.right_encoder_count += data[1]
        else:
            self.right_encoder_count -= data[1]

    def clear_enc(self, flag=None):
        if flag == None:
            self.left_encoder_count = 0
            self.right_encoder_count = 0
        elif flag == ENCODER_PIN_RIGHT:
            self.right_encoder_count = 0
        elif flag == ENCODER_PIN_LEFT:
            self.left_encoder_count = 0

    def get_ticks(self, encoder):
        if encoder == ENCODER_PIN_LEFT:
            return self.left_encoder_count
        elif encoder == ENCODER_PIN_RIGHT:
            return self.right_encoder_count


class RedBotMotors:
    """Controls the motors on the RedBot"""

    def __init__(self, board):
        """Constructor for pin setup"""

        self.board = board
        self.total_left_ticks = 0
        self.total_right_ticks = 0
        # The interface to the motor driver is kind of ugly. It's three pins per
        # channel: two that define role (forward, reverse, stop, brake) and one
        # PWM input for speed.
        board.set_pin_mode(L_CTRL_1, Constants.OUTPUT)
        board.set_pin_mode(L_CTRL_2, Constants.OUTPUT)
        board.set_pin_mode(PWM_L, Constants.PWM)  # Not done in RedBot motors but I just went ahead and added it.
        board.set_pin_mode(R_CTRL_1, Constants.OUTPUT)
        board.set_pin_mode(R_CTRL_2, Constants.OUTPUT)
        board.set_pin_mode(PWM_R, Constants.PWM)  # Not done in RedBot motors but I just went ahead and added it.

    def brake(self):
        """effectively shorts the two leads of the motor together, which causes the motor to resist being turned. It stops quite quickly."""
        self.left_brake()
        self.right_brake()

    def drive(self, speed, durationS=-1.0):
        """
            Starts both motors. It figures out whether the motors should go
            forward or revers, then calls the appropriate individual functions. Note
            the use of a 16-bit integer for the speed input an 8-bit integer doesn't
            have the range to reach full speed. The calls to the actual drive functions
            are only 8-bit, since we only have 8-bit PWM.
        """
        if speed > 0:
            self.left_fwd(min(abs(speed), 255))
            self.right_fwd(min(abs(speed), 255))
        else:
            self.left_rev(min(abs(speed), 255))
            self.right_rev(min(abs(speed), 255))
        if durationS > 0:
            self.board.sleep(durationS)
            self.left_stop()
            self.right_stop()

    def left_motor(self, speed, durationS=-1.0):
        """Basically the same as drive(), but omitting the right motor."""
        if speed > 0:
            self.left_rev(min(abs(speed), 255))
        else:
            self.left_fwd(min(abs(speed), 255))
        if durationS > 0:
            self.board.sleep(durationS)
            self.left_stop()

    def right_motor(self, speed, durationS=-1.0):
        """Basically the same as drive(), but omitting the left motor."""
        if speed > 0:
            self.right_fwd(min(abs(speed), 255))
        else:
            self.right_rev(min(abs(speed), 255))
        if durationS > 0:
            self.board.sleep(durationS)
            self.left_stop()

    def stop(self):
        """
            stop() allows the motors to coast to a stop, rather than trying to stop them
            quickly. As will be the case with functions affecting both motors, the
            global stop just calls the individual stop functions for each wheel.
        """
        self.left_stop()
        self.right_stop()

    def left_brake(self):
        """allows left motor to coast to a stop"""
        self.board.digital_write(L_CTRL_1, 1)
        self.board.digital_write(L_CTRL_2, 1)
        self.board.analog_write(PWM_L, 0)

    def right_brake(self):
        """allows left motor to coast to a stop"""
        self.board.digital_write(R_CTRL_1, 1)
        self.board.digital_write(R_CTRL_2, 1)
        self.board.analog_write(PWM_R, 0)

    def left_stop(self):
        """allows left motor to coast to a stop"""
        self.board.digital_write(L_CTRL_1, 0)
        self.board.digital_write(L_CTRL_2, 0)
        self.board.analog_write(PWM_L, 0)

    def right_stop(self):
        """allows left motor to coast to a stop"""
        self.board.digital_write(R_CTRL_1, 0)
        self.board.digital_write(R_CTRL_2, 0)
        self.board.analog_write(PWM_R, 0)

    def pivot(self, speed, durationS=-1.0):
        """
            pivot() controls the pivot speed of the RedBot. The values of the pivot function inputs
            range from -255:255, with -255 indicating a full speed counter-clockwise rotation.
            255 indicates a full speed clockwise rotation
        """
        if speed < 0:
            self.left_fwd(min(abs(speed), 255))
            self.right_rev(min(abs(speed), 255))
        else:
            self.left_rev(min(abs(speed), 255))
            self.right_fwd(min(abs(speed), 255))
        if durationS > 0:
            self.board.sleep(durationS)
            self.left_stop()
            self.right_stop()

    # ******************************************************************************
    #  Private functions for RedBotMotor
    # ******************************************************************************/
    # These are the motor-driver level abstractions for turning a given motor the
    #  right direction. Users never see them, and *should* never see them, so we
    #  make them private.

    def left_fwd(self, spd):
        self.board.digital_write(L_CTRL_1, 1)
        self.board.digital_write(L_CTRL_2, 0)
        self.board.analog_write(PWM_L, spd)
        # If we have an encoder in the system, we want to make sure that it counts
        # in the right direction when ticks occur.
        if encoder_object:
            encoder_object.left_direction = DIRECTION_FORWARD

    def left_rev(self, spd):
        self.board.digital_write(L_CTRL_1, 0)
        self.board.digital_write(L_CTRL_2, 1)
        self.board.analog_write(PWM_L, spd)
        # If we have an encoder in the system, we want to make sure that it counts
        # in the right direction when ticks occur.
        if encoder_object:
            encoder_object.left_direction = DIRECTION_REVERSE

    def right_fwd(self, spd):
        self.board.digital_write(R_CTRL_1, 1)
        self.board.digital_write(R_CTRL_2, 0)
        self.board.analog_write(PWM_R, spd)
        # If we have an encoder in the system, we want to make sure that it counts
        # in the right direction when ticks occur.
        if encoder_object:
            encoder_object.right_direction = DIRECTION_FORWARD

    def right_rev(self, spd):
        self.board.digital_write(R_CTRL_1, 0)
        self.board.digital_write(R_CTRL_2, 1)
        self.board.analog_write(PWM_R, spd)
        # If we have an encoder in the system, we want to make sure that it counts
        # in the right direction when ticks occur.
        if encoder_object:
            print("Right is in reverse")
            encoder_object.right_direction = DIRECTION_REVERSE


class RedBotSensor:
    pin_number = 0

    def __init__(self, board, pin_number):
        self.board = board
        self.pin_number = pin_number
        board.set_pin_mode(pin_number, Constants.ANALOG)

    def read(self):
        return self.board.analog_read(self.pin_number)


class RedBotBumper:
    pin_number = 0

    def __init__(self, board, pin_number):
        self.pin_number = pin_number
        self.board = board
        self.board.set_pin_mode(pin_number, Constants.INPUT)
        self.board.digital_write(pin_number, 1)  # sets pin pull-up resistor. INPUT_PULLUP is not an option with Pymata
        pass

    def read(self):
        return self.board.digital_read(self.pin_number)


class RedBotAccelerometer(MMA8452Q3):
    """An import of the mma8452q3 library"""
    
    # Positions in the returned array for the accel.read() function
    VAL_RAW_X = 0
    VAL_RAW_Y = 1
    VAL_RAW_Z = 2
    VAL_X = 3  # Corrected X Value. The CX,CY,CZ Values take the 0-2048 raw value and convert them to a 'G-value' 
    VAL_Y = 4
    VAL_Z = 5
    VAL_ANGLE_XZ = 6
    VAL_ANGLE_YZ = 7
    VAL_ANGLE_XY = 8
    
    def __init__(self, board):
        DEVICE_ADDRESS = 0x1d  # Physical board address of the accelerometer 
        SCALE = 2  # sets a scaling factor for the outputted results
        OUTPUT_DATA_RATE = 0
    
        super().__init__(board, DEVICE_ADDRESS, SCALE, OUTPUT_DATA_RATE)
        self.board = board
