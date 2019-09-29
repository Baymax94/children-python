"""
  Exp8_1_AccelerometerRead -- RedBot Experiment 8.1

  Measuring speed, velocity, and acceleration are all key
  components to robotics. This first experiment will introduce
  you to using the Accelerometer sensor on the RedBot.

  Hardware setup:
  You'll need to attach the RedBot Accelerometer board to hader on the upper
  right side of the mainboard. See the manual for details on how to do this.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.

  8 Oct 2013 M. Hord
  Revised, 31 Oct 2014 B. Huang

  8 Oct 2013 M. Hord

  This experiment was inspired by Paul Kassebaum at Mathworks, who made
  one of the very first non-SparkFun demo projects and brought it to the
  2013 Open Hardware Summit in Boston. Thanks Paul!
 """

from pymata_aio.pymata3 import PyMata3
import library.redbot as rb

WIFLY_IP_ADDRESS = None            # Leave set as None if not using WiFly
WIFLY_IP_ADDRESS = "10.0.1.19"  # If using a WiFly on the RedBot, set the ip address here.
#WIFLY_IP_ADDRESS = "r01.wlan.rose-hulman.edu"  # If your WiFi network allows it, you can use the device hostname instead.
if WIFLY_IP_ADDRESS:
    # arduino_wait is a timer parameter to allow for the arduino to reboot when the connection is made which is NA for WiFly.
    board = PyMata3(arduino_wait=0, ip_address=WIFLY_IP_ADDRESS)
else:
    # Use a USB cable to RedBot or an XBee connection instead of WiFly.
    COM_PORT = None # Use None for automatic com port detection, or set if needed i.e. "COM7"
    board = PyMata3(com_port=COM_PORT)

board.keep_alive(2) # Important because it will stop the encoder data stream if you stop the Python program.

motors = rb.RedBotMotors(board)
accelerometer = rb.RedBotAccelerometer(board)


def setup():
    accelerometer.start()

def loop():
        if accelerometer.available():
            values = accelerometer.read()
            #print("values = " + str(values))
            x = values[rb.RedBotAccelerometer.VAL_X]
            y = values[rb.RedBotAccelerometer.VAL_Y]
            z = values[rb.RedBotAccelerometer.VAL_Z]
            angle_xz = values[rb.RedBotAccelerometer.VAL_ANGLE_XZ]
            angle_yz = values[rb.RedBotAccelerometer.VAL_ANGLE_YZ]
            angle_xy = values[rb.RedBotAccelerometer.VAL_ANGLE_XY]
            
            tap = accelerometer.read_tap()
            if tap:
                tap = 'TAPPED'
            else:
                tap = 'NO TAP'
                
            port_land = accelerometer.read_portrait_landscape()
            if port_land == accelerometer.LOCKOUT:
                port_land = 'Flat   '
            elif port_land == 0:
                port_land = 'Tilt Lf'
            elif port_land == 1:
                port_land = 'Tilt Rt'
            elif port_land == 2:
                port_land = 'Tilt Up'
            else:
                port_land = 'Tilt Dn'
            print('x-val: {:.2f}, y-val: {:.2f}, z-val: {:.2f} \t angle x-z:{:.2f}, angle y-z: {:.2f}, angle x-y: {:.2f} \t Tapped: {} \t Orientation: {}'.format( \
                  x, y, z, angle_xz, angle_yz, angle_xy, tap, port_land))
        else:
            print("Accelerometer not available.  Please try again.")
            board.sleep(2.0)
        board.sleep(0.025)
    

if __name__ == "__main__":
    setup()
    while True:
        loop()
        board.sleep(.025)
