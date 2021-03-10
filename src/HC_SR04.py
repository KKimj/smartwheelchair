from serial import Serial

class HC_SR04_quad:
    leftPort = '/dev/ttyUSB0'
    rightPort = '/dev/ttyUSB1'
    
    left_sensors = None
    right_sensors = None
    

    @staticmethod
    def setSerialPort(_leftPort = '/dev/ttyUSB0', _rightPort = '/dev/ttyUSB1'):
        HC_SR04_quad.closeSerial()

        HC_SR04_quad.leftPort = _leftPort
        HC_SR04_quad.rightPort = _rightPort

        HC_SR04_quad.openSerial()
                    
    @staticmethod
    def openSerial():
        HC_SR04_quad.left_sensors = Serial(HC_SR04_quad.leftPort, 115200, timeout = 3)
        HC_SR04_quad.right_sensors = Serial(HC_SR04_quad.rightPort, 115200, timeout = 3)
    
    @staticmethod
    def closeSerial():
        HC_SR04_quad.left_sensors.close()
        HC_SR04_quad.right_sensors.close()

        
    @staticmethod
    def getLeftSensors():
        return list(map(int, HC_SR04_quad.left_sensors.readline().decode('utf-8').strip().split()))

    @staticmethod
    def getRightSensors():
        return list(map(int, HC_SR04_quad.right_sensors.readline().decode('utf-8').strip().split()))
        
    @staticmethod
    def getFront():
        return HC_SR04_quad.getLeftSensors()[:2] + HC_SR04_quad.getRightSensors()[:2]
    
    @staticmethod
    def getLeftside():
        return HC_SR04_quad.getLeftSensors()[2:]
    
    @staticmethod
    def getRightside():
        return HC_SR04_quad.getRightSensors()[2:]
    
    @staticmethod
    def getTotalData():
        return HC_SR04_quad.getLeftSensors + HC_SR04_quad.getRightSensors
