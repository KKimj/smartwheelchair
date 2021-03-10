from serial import Serial


class SONIC2CAN:
    def __init__(self):
        self.serial_left = Serial('/dev/serial0', 115200, timeout = 3)
        self.serial_right = Serial('/dev/serial1', 115200, timeout = 3)

    def getData(self):
        command = ';06\r'
        
        self.serial_left.write(bytes(command.encode()))
        self.data_left = self.serial_left.readline()

        self.serial_right.write(bytes(command.encode()))
        self.data_right = self.serial_right.readline()




    def test(self):
        command = ';06\r'
        self.serial_left.write(bytes(command.encode()))
        line = self.serial_left.readline()
        print('left : '+line)

        self.serial_right.write(bytes(command.encode()))
        line = self.serial_right.readline()
        print('right : '+line)
        pass
    

