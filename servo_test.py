import serial
import time


ser = serial.Serial('/dev/ttyAMA0',115200)
ser.isOpen()#返回Ture则代表串口已打开

ser.write('#000P1200T1000!'.encode('utf-8'))#向串口发送字符串并指定编码为utf-8
time.sleep(1)
ser.write('#000P1500T1000!'.encode('utf-8'))#向串口发送字符串并指定编码为utf-8
