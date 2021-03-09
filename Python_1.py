# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 23:01:37 2021

@author: 19520
"""

import time
localtime = time.asctime( time.localtime(time.time()) )
localtime1=str(localtime)

if localtime1[-13]==0:
    licaltimeshi=int(localtime1[-12])
else:
    localtimeshi=int(localtime1[-13:-11:1])
    
if localtime1[-10]==0:
    licaltimefen=int(localtime1[-9])
else:
    localtimefen=int(localtime1[-10:-8:1])
    
alarm=input('请输入闹铃时间（时）')
alarm1=input('请输入闹铃时间（分）')
alarmshi=int(alarm)
alarmfen=int(alarm1)

if alarmfen-localtimefen>=0:
    adc_1=alarmfen-localtimefen
    if alarmshi>=localtimeshi:
        adc_2=alarmshi-localtimeshi
    else:
        adc_2=alarmshi+24-localtimeshi   
        
else:
    adc_1=alarmfen+(60-localtimefen) 
    if alarmshi>=localtimeshi:
        adc_2=alarmshi-localtimeshi-1
    else:
        adc_2=alarmshi+24-localtimeshi-1
        
        
print('闹铃距现在还有%d小时，%d分钟'%(adc_2,adc_1))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
