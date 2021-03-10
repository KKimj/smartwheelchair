from HC_SR04 import HC_SR04_quad
from motor import Motor

class SmartWheelChair:
    @staticmethod
    def isObstacle_Front():
        if min(HC_SR04_quad.getFront()) <= 20 :
            return True
        else :
            return False

    @staticmethod
    def isObstacle_Left():
        if min(HC_SR04_quad.getLeftside()) <= 20 :
            return True
        else :
            return False

    @staticmethod
    def isObstacle_Right():
        if min(HC_SR04_quad.getRightside()) <= 20 :
            return True
        else :
            return False
    
    @staticmethod
    def Run():
        while True:
            if SmartWheelChair.isObstacle_Front():
                Motor.Stop()
            
            elif SmartWheelChair.isObstacle_Left():
                Motor.TurnRight()
            
            elif SmartWheelChair.isObstacle_Right():
                Motor.TurnRight()
            
            else:
                Motor.Forward()
            
