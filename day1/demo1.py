import requests
import jsonpath
from day1.demo2 import EncryptDate

headers = {
    "application":"app",
     "application_client_type": "weixin",
}

params = {
    "application":"app",
     "application_client_type": "weixin",
}
data = {
    "accounts": "huace_xm",
    "pwd": 123456,
    "type": "username"
}

rs = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login",
              headers=headers,
              params=params,
              data=data)

print(rs.text)
token = rs.json()["data"]["token"]
token_list = jsonpath.jsonpath(rs.json(),'$..token')
print(token_list[0])



data2 = {
    "goods_id": "2",
    "spec":[
{
        "type":"保温杯",
        "value":"套餐二"
    },
    {
        "type":"颜色",
        "value":"银色"
    },
    {
        "type":"容量",
        "value":"64G"
    }
    ],
    "stock":2
}

rs2 = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/save&token={}".format(token_list[0]),
              params=params,
              data=data2)
print(rs2.text)


eg = EncryptDate("1234567812345678")
eg.encrypt()
eg.decrypt()

