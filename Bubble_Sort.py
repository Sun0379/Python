...python
#!/usr/bin/env python
# -*- coding:<encoding name> -*-

#冒泡排序

#data_all = [10,9,8,7,6,5,4,3,2,1]
data_len = int(input("请输入数组长度："))
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
            print("输入错误太多，再见！")
            exit()
count = 0
count_flag = 0
for j in range(len(data_all)):
    print("第",j,"次排序：",data_all)
    for i in range(len(data_all)-j-1):
        if data_all[i] > data_all[i+1]:
            data_all[i],data_all[i+1] = data_all[i+1],data_all[i]
            count_flag = 1
    if count_flag == 1:
            count += 1
            count_flag = 0
print("最终排序：",data_all)
print("排序次数：",count)
