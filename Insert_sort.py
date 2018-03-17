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
        
i = 0

for i in list(range(1,data_len)):
    j = 0
    while j < i:
        if data_all[j] > data_all[i]:
            data_all.insert(j,data_all[i])
            del data_all[i+1]
            j += 1
        #这里出过一个bug，else缩进错误，和while放一起了，程序无法进行下去
        else:
            j += 1
    print("第",i,"次调整：",data_all)
print("最终排序：",data_all)
