from serial import Serial

class USBSerial:
    def __init__(self, port, baudrate, timeout = 0.1, write_timeout = 0.11, open = False):
        '''
        init method
        if open is set True then call open_serial()
        '''
        self._port = port
        self._baudrate = baudrate
        self._timeout = timeout
        self._write_timeout = write_timeout
        self.serial = None
        if open:
            self.open_serial()

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        '''
        port setter method
        if serial was opened
        - Close serial
        - Open serial
        '''
        self._port = port
        if not self.serial:
            self.close_serial()
            self.open_serial()
    
    @property
    def baudrate(self):
        return self._baudrate
    
    @property
    def timeout(self):
        return self._timeout

    def open_serial(self):
        if not self.serial:
            self.close_serial()
        try:
            self.serial = Serial(port = self._port, baudrate = self._baudrate, timeout = self._timeout)

        except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args
            print(inst)   
            print('Error : Can not open Serial, Retry!')
            return False
        return True

    def close_serial(self):
        if self.serial:
            self.serial.close()
        self.serial = None

    def write(self, message):
        if self.serial:
            if type(message) is not str:
                message = str(message)
            message += '\n'
            self.serial.write(bytes(message.encode()))
    
    def readline(self):
        if not self.serial:
            if not self.open_serial():
                return

        return self.serial.readline().decode('utf-8').strip()
        
    def read(self, size = 1):
        if not self.serial:
            if not self.open_serial():
                return

        return self.serial.read(size)

    def flush(self):
        self.serial.flush()

    def test(self):
        '''
        Print out status
        '''
        if self:
            if self.serial:
                print('> Serial is opened')
            else:
                print('> Serial is not opened')
            if self.port:
                print('Port : %s'%(self.port))
            if self._baudrate:
                print('Baudrate : %s'%(self._baudrate))
            if self._timeout:
                print('Timeout : %s'%(self._timeout))