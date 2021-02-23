# coding:utf-8
# @Create time: 2021/2/23 6:42 下午
# @Author: KongJingchun
# @remark: 九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{} * {} = {}'.format(j, i, i * j), end=' ')
    print()
