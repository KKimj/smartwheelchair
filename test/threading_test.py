import threading
import curses
import time

command = None
command_lock = threading._allocate_lock()

def input_handler():
    print('input_handler')
    # do not wait for input when calling getch
    global command, command_lock
    while True:
        c = input().strip()
        with command_lock:
            command = c
        # time.sleep(1)

def motor_handler():
    global command, command_lock
    while True:
        while not command:
            time.sleep(0.01)
        with command_lock:
            print(command, end="motor_handler\n")
            command = None
        # time.sleep(1)

def obstacle_hanler():
    pass

if __name__ == '__main__':
    # 데몬 쓰레드
    input_thread = threading.Thread(target=input_handler, args=())
    input_thread.daemon = True 
    input_thread.start()

    motor_thread = threading.Thread(target=motor_handler, args=())
    motor_thread.daemon = True
    motor_thread.start()
    
    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("### End ###")
            break

