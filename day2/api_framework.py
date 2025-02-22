import requests




# 1. 读取excel
# 2. 把excel的数据变成列表
# 3. 循环调用 函数




def send_request(url,method,parms,data):
    res = requests.request(url=url,
                        method=method,
                           params=parms,
                           data=data) # 这种方式，将你的请求方式全部变为变量，可以访问所有的接口
