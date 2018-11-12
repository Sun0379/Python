#/use/sbin/env python
#-*- coding:utf-8 -*-
def trim(s):
    #考虑s前后都有可能存在空格，使用j/k分别定位空格位置
    n = len(s);
    j = 0;
    k = 0;
    #考虑s可能为空
    if n != 0:
        for i in range(n):
            if s[i].isspace():
                j = i+1;
                L = s[j:];
                continue;
            else:
                break;
        n = len(s);
        for i in range(n):
            if s[-i-1].isspace():
                k = -i -1;
                L = s[j:k];
                continue;
            else:
                break;
        s = L;
    else :
        pass;
    return s;


if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')
