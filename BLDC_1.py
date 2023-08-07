import RPi.GPIO as GPIO
import time

GPIO.cleanup()

# 设置GPIO模式为BCM编码方式
GPIO.setmode(GPIO.BCM)

# 配置GPIO引脚
GPIO.setup(27, GPIO.OUT) # 输出PWM信号
GPIO.setup(22, GPIO.OUT) 
GPIO.output(22, GPIO.LOW)
#GPIO.output(4, GPIO.LOW)
#GPIO.setup(23, GPIO.OUT) # 输出电机方向控制信号

# 设置PWM频率为1000Hz
pwm = GPIO.PWM(4, 1000)

# 定义一个函数来控制电机旋转
def rotate_motor(duration):
    '''
    # 设置电机方向
    if direction == "CW":
        GPIO.output(23, GPIO.LOW)
    elif direction == "CCW":
        GPIO.output(23, GPIO.HIGH)
    else:
        print("Invalid direction")
        return
        '''

    # 开始PWM输出
    pwm.start(35) # 占空比为50%

    # 等待一段时间
    time.sleep(duration)

    # 停止PWM输出
    pwm.stop()

# 控制电机多次转动
while True:
    file1 = open('/home/bio/bio_ins_rob_code/BLDC_1_state.txt','r')
    state = file1.read()
    file1.close()

    if(state == '1'):
        file1 = open('/home/bio/bio_ins_rob_code/BLDC_1_state.txt','w')
        file1.write('0')
        file1.close()
        time.sleep(0)
        rotate_motor(1) # 顺时针旋转2秒

    time.sleep(0.1)

# 清理GPIO引脚 gg
# GPIO.cleanup()