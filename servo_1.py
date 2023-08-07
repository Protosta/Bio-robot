import serial
import time

# GPIO 14 也就是txd
ser = serial.Serial('/dev/ttyAMA0',115200)
ser.isOpen()#返回Ture则代表串口已打开

while True:
    file1 = open('/home/bio/bio_ins_rob_code/servo_1_state.txt','r')
    state = file1.read()
    file1.close()
    # print(state)
    # print(config.get_servo())
    if(state == '1'):
        file1 = open('/home/bio/bio_ins_rob_code/servo_1_state.txt','w')
        file1.write('0')
        file1.close()
        # config.set_servo(0)
        ser.write('#000P0800T0100!'.encode('utf-8'))#向串口发送字符串并指定编码为utf-8
        time.sleep(2)
        ser.write('#000P1600T0100!'.encode('utf-8'))#向串口发送字符串并指定编码为utf-8
        time.sleep(2)
        ser.close()
    time.sleep(0.1)