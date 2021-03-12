# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
print('欢迎来到\'不选3\'小游戏,现在请你设置游戏难度')
NewArray=[]
num_1=0
end_1=int(input('从:'))
end_2=int(input('到:'))
for num in list(range(end_1,end_2+1)):
    if num%3!=0 and num//10!=3 and num%10!=3:
        NewArray.append(num)
        num_1+=1
SuiJi=random.randint(0,1)
if SuiJi ==0:
    adc_1=int(input('请输入第一个数字'))
    adc_2=0
    while adc_1 ==NewArray[adc_2]:
        print(NewArray[adc_2+1])
        if NewArray[adc_2+1]==NewArray[-1]:
            break
        adc_1=int(input('请输入'))
        if adc_1==NewArray[-1]:
            break
        adc_2+=2
        
    if adc_1==NewArray[-1] or NewArray[adc_2+1]==NewArray[-1]:
        print('你赢了')
    else:
        print('你输了')
else:
    adc_3=0
    print(NewArray[adc_3])
    cda_1=int(input('请输入第二个数字'))
    while cda_1==NewArray[adc_3+1]:
        adc_3+=2
        print(NewArray[adc_3])
        if NewArray[adc_3]==NewArray[-1]:
            break
        cda_1=int(input('请输入'))
        if cda_1==NewArray[-1]:
            break
    if NewArray[adc_3]==NewArray[-1] or cda_1==NewArray[-1]:
        print('你赢了')
    else:
        print('你输了')

    
    
    

