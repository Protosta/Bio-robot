import serial
import time

# GPIO0 也就是从左下角往上数第七个口
ser = serial.Serial('/dev/ttyAMA1',115200)
ser.isOpen()#返回Ture则代表串口已打开

while True:
    file1 = open('/home/bio/bio_ins_rob_code/servo_2_state.txt','r')
    state = file1.read()
    file1.close()
    # print(state)
    # print(config.get_servo())
    if(state == '1'):
        file1 = open('/home/bio/bio_ins_rob_code/servo_2_state.txt','w')
        file1.write('0')
        file1.close()
        # config.set_servo(0)
        ser.write('#000P0800T0100!'.encode('utf-8'))#向串口发送字符串并指定编码为utf-8
        time.sleep(0.8)
        ser.write('#000P1500T0100!'.encode('utf-8'))#向串口发送字符串并指定编码为utf-8
        time.sleep(0.8)
        ser.close()
    time.sleep(0.1)