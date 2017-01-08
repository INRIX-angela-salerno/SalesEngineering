#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from builtins import str
from pprint import pprint

for path, dirs, files in os.walk(path):
    for x in files:
        if x.endswith(".json") == False:
            with open("x","r") as myfile:
                data = myfile.read()
                result = data.replace('\\', '')
                result2 = result.replace('"{', '{')
                result3=result2.replace('}"', '}')
                for i in result3:
                    if (i['ActionName'] == 'FindRoute'):
                        ActionName = i['ActionName']
                        RequestTime = i['RequestTime']
                        ResponseBody = i['ResponseBody']
                        Url = i['Url']
                        print(ActionName, RequestTime, ResponseBody, Url)
                        parsed_dic = {
                                'ActionName': ActionName,
                                'RequestTime':RequestTime,
                                'ResponseBody': ResponseBody,
                                'Url':Url
                                }
                        data2=json.dumps(parsed_dic)
                        name = x + '.json'
                        f = open ('name', 'a')
                        f.write(data2)
                        f.close()