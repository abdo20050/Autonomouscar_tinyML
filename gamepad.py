from inputs import get_gamepad
import math
import threading
import serial

ser = serial.Serial('/dev/ttyUSB0',115200)  # open serial port

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):
        self.eventOn = 0
        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()
        self.funcTrigger = None

    def customfunc(self):
        func = self.funcTrigger
        if func is None:
            return
        func()

    def read(self): # return the buttons/triggers that you care about in this methode
        # events = get_gamepad()
        if self.eventOn:
            x = self.LeftDPad
            y = self.RightDPad
            z = self.UpDPad
            e = self.DownDPad
            a = self.A
            rt = self.RightTrigger
            rb = self.RightBumper
            return [x, y, z, e, a, rt, rb]


    def _monitor_controller(self):
        while True:    
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    # self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                    self.RightBumper = event.state
                    _type = ord('r')
                    val = event.state
                    msg = bytearray([_type,val])
                    ser.write(msg)
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightTrigger = event.state
                    _type = ord('e')
                    val = event.state
                    msg = bytearray([_type,val])
                    ser.write(msg)
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                    _type = ord('a')
                    val = event.state
                    msg = bytearray([_type,val])
                    ser.write(msg)
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state #previously switched with X
                elif event.code == 'BTN_WEST':
                    self.X = event.state #previously switched with Y
                    self.customfunc()
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'ABS_HAT0Y':
                    _type = ord('d') 
                    if event.state == -1:
                        val = 2
                        self.UpDPad = 1
                    elif event.state == 1:
                        val = 4
                        self.DownDPad = 1
                    else:
                        val = 0
                        self.UpDPad = 0
                        self.DownDPad = 0
                    msg = bytearray([_type, val])
                    ser.write(msg)
                elif event.code == 'ABS_HAT0X':
                    _type = ord('d') 
                    if event.state == -1:
                        val = 1
                        self.LeftDPad = 1
                    elif event.state == 1:
                        val = 3
                        self.RightDPad = 1
                    else:
                        val = 0
                        self.LeftDPad = 0
                        self.RightDPad = 0
                    msg = bytearray([_type,val])
                    ser.write(msg)





if __name__ == '__main__':
    joy = XboxController()
    while True:
       pass
        # print(joy.read())