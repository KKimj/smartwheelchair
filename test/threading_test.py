import threading
import curses
import time
import random

command = None
command_lock = threading._allocate_lock()

stdscr = curses.initscr()
stdscr.nodelay(1)

def input_handler():
    print('input_handler')
    # do not wait for input when calling getch
    global command, command_lock
    tmp_command = None

    

    while True:
        # stdscr.clear()
        # stdscr.move(0, 0)
        # stdscr.refresh()
        c = stdscr.getch()
        if c == -1:
            continue
        c = chr(c)

        if c == 'w':
            tmp_command = 'forward'
        elif c == 'a':
            tmp_command = 'turn_left'
        elif c == 's':
            tmp_command = 'stop'
        elif c == 'd':
            tmp_command = 'turn_right'
        elif c == 'x':
            tmp_command = 'backward'
        elif c == 'q':
            tmp_command = 'quit'
        else:
            continue

        with command_lock:
            command = tmp_command
            time.sleep(1)
        
        
        if command == 'quit':
            # curses.endwin()
            break
        
        # time.sleep(1)

def motor_handler():
    global command, command_lock
    prev_command = None
    while True:
        while not command:
            time.sleep(0.01)

        if prev_command == command:
            continue

        # with command_lock:
        #   pass
        stdscr.clear()
        stdscr.move(0, 0)
        stdscr.refresh()
        print(command, end="motor_handler\n")
        
        prev_command = command
        
        if command == 'quit':
                # curses.endwin()
                break
            # command = None
        # time.sleep(1)

def obstacle_handler():
    global command, command_lock
    time_offset = 0.85
    tmp_command = None
    while True:
        direction = random.choice(['front', 'right', 'left', 'near'])
        obstacle_status = {
            'front' : False,
            'left' : False,
            'right' : False,
            'near' : False,
        }
        obstacle_status[direction] = True
        if True:
            # print('obstacle_status', obstacle_status)
            pass

        if obstacle_status['front']:
            # break
            if obstacle_status['left'] and obstacle_status['right']:
                tmp_command = 'backward'

            elif obstacle_status['left']:
                tmp_command = 'turn_right'

            
            elif obstacle_status['right']:
                tmp_command = 'turn_left'

            else:
                tmp_command = 'turn_left'

        elif obstacle_status['left']:
            tmp_command = 'turn_right'

            
        elif obstacle_status['right']:
            tmp_command = 'turn_left'


        elif obstacle_status['near']:
            tmp_command = 'forward'

        # Safe from obstacle
        else:
            tmp_command = 'forward'

        with command_lock:
            command = tmp_command
            tmp_command = None
        time.sleep(0.1)
        if command == 'quit':
                break
        
    

if __name__ == '__main__':
    # 데몬 쓰레드
    input_thread = threading.Thread(target=input_handler, args=())
    input_thread.daemon = True 
    input_thread.start()

    motor_thread = threading.Thread(target=motor_handler, args=())
    motor_thread.daemon = True
    motor_thread.start()
    
    obstacle_thread = threading.Thread(target=obstacle_handler, args=())
    obstacle_thread.daemon = True
    obstacle_thread.start()

    # global command
    while True:
        try:
            if command == 'quit':
                break
        except KeyboardInterrupt:
            curses.endwin()
            print("### End ###")
            break

