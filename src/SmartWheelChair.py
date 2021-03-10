from HC_SR04 import HC_SR04_quad
from motor import Motor

class SmartWheelChair:
    def isObstacle_Front(self):
        if min(HC_SR04_quad.getFront()) <= 20 :
            return True
        else :
            return False

    def isObstacle_Left(self):
        if min(HC_SR04_quad.getLeftside()) <= 20 :
            return True
        else :
            return False

    def isObstacle_Right(self):
        if min(HC_SR04_quad.getRightside()) <= 20 :
            return True
        else :
            return False
    
    @staticmethod
    def Run():
        pass