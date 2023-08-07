import multiprocessing as mp
import os


def bldc_1():
    os.system('python3 BLDC_1.py')

def servo_1():
    os.system('python3 servo_1.py')

def control():
    os.system('python3 main_control.py')

def bldc_2():
    os.system('python3 BLDC_2.py')

def servo_2():
    os.system('python3 servo_2.py')

def multicore():
    p1 = mp.Process(target=bldc_1)
    p2 = mp.Process(target=servo_1)
    p3 = mp.Process(target=control)
    p4 = mp.Process(target=bldc_2)
    p5 = mp.Process(target=servo_2)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()


if __name__ == '__main__':

    multicore()