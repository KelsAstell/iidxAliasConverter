import json
import numpy as np

# 定义文件路径
path = './data/'

# 打开文件,r是读取,encoding是指定编码格式
with open(path + 'alias.json', 'r', encoding='utf-8') as fp1:
    data_old = json.load(fp1)  # load()函数将fp(一个支持.read()的文件类对象，包含一个JSON文档)反序列化为一个Python对象
with open(path + 'all_alias.json', 'r', encoding='utf-8') as fp2:
    data_new = json.load(fp2)
# for keys in data_old:
#     print(data_old[keys])
# print(data_new[1]['Alias'])
for keys in data_old:
    if len(data_old[keys]) != 0:
        for song_id in data_old[keys]:
            a = int(song_id)
        # print(data_old[keys])
            for data in data_new:
                if data['ID'] == a:
                    if keys in data['Alias']:
                        print(keys+" 已存在,因此跳过")
                    else:
                        data['Alias'].append(keys)
    else:
        print("跳过空的别名键值对, thanks xray")
print(data_new)
json_str = json.dumps(data_new, indent=4, ensure_ascii=False)
with open(path+'target.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)
fp1.close()
fp2.close()
