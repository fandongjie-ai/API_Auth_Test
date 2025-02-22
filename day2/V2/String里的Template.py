# 注意：“如果碰到特殊字符${} 它会自动用字典的key去替换${}同名的变量”



from string import Template


ss = {"token":"dhuaihgcushdovi"}
url = "http://www.baidu.com?token=${token}"
print(Template(url).substitute(ss))

