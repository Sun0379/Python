#!/usr/bin/env python
# -*- coding:<encoding name> -*-

data_all = [10,9,8,7,6,5,4,3,2,1]

count = 0
count_flag = 0
for j in range(len(data_all)):
    print("第",j,"次排序：",data_all)
    for i in range(len(data_all)-j-1):
        if data_all[i] > data_all[i+1]:
            temp = data_all[i]
            data_all[i] = data_all[i+1]
            data_all[i+1] = temp
            count_flag = 1
    if count_flag == 1:
             count += 1
             count_flag = 0
print("最终排序：",data_all)
print("排序次数：",count)
