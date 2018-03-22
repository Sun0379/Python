#!/usr/bin/env python
# -*- coding:<encoding name> -*-

#data_all = [10,9,8,7,6,5,4,3,2,1]

data_flag = False
data_info = 0
#while false退出
while not data_flag:
    try:
        data_len = int(input("请输入数组长度："))
        data_flag = True
        data_info = 0
    except ValueError:
        print("输入有误，请重试！")
        data_info += 1
    if data_info <= 5:
        continue
    else:
        print("输入错误太多！")
        exit()

#初始化数组
data_all = list(range(data_len))
for k in list(range(0,data_len)):
    h = str(k+1)
    data_flag = False
    data_info = 0
    #while false退出
    while not data_flag:
        try:
            data_all[k] = int(input("请输入第"+h+"个数："))
            data_flag = True
            data_info = 0
        except ValueError:
            print("输入有误，请重试！")
            data_info += 1
        if data_info <= 5:
            continue
        else:
            print("输入错误太多！")
            exit()

#输入间隔
step = int(input("请输入步长："))
group_num = data_len/step
for i in(0,data_len-step-1):
    for j in(0,group_num):
        if data_all[i] > data_all[i+step-1]:
            data_all[i] , data_all[i+step-1] = data_all[i+step-1] , data_all[i]
            print(data_all)
    print("第",i+1,"次排序：",data_all)

print("最终排序：",data_all)
