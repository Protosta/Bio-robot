import time

time.sleep(2)
print('start')

print('one side')
file1 = open('/home/bio/bio_ins_rob_code/servo_1_state.txt','w')
file2 = open('/home/bio/bio_ins_rob_code/BLDC_1_state.txt','w')
file1.write('1')
file2.write('1')
file1.close()
file2.close()

time.sleep(2)
print('another side')
file1 = open('/home/bio/bio_ins_rob_code/servo_2_state.txt','w')
file2 = open('/home/bio/bio_ins_rob_code/BLDC_2_state.txt','w')
file1.write('1')
file2.write('1')
file1.close()
file2.close()

print('finish')
