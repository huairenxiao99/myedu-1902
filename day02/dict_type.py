import json

#声明一个全量 dict 变量（字典）

adict = {"name":"ysl","pwd":"123456"}
#这是一个字符串 不过他是json 格式， 也是字典的格式
adictStr = '{"name":"ysl","pwd":"123456","1":"数字"}'

if __name__ == '__main__':
    # adictStr = '{"name":"ysl","pwd":"123456","1"："数字"}'
    # adict.pop('name')
    # print(adict['name'])
    # print(adict)
    json_loads = json.loads(adictStr)
    print(json_loads)
    print(type(json_loads))
    dumps = json.dumps(json_loads)
    print(dumps)
    # dumps = json.dumps(adict)
    # print(type(dumps))

    # print(type(adictStr))
    # json.loads(adictStr)



    pass
