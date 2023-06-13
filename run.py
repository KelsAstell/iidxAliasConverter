import json

path = './data/'

with open(path + 'alias.json', 'r', encoding='utf-8') as fp1:
    xray_data = json.load(fp1) 
with open(path + 'all_alias.json', 'r', encoding='utf-8') as fp2:
    iidx_data = json.load(fp2)

for keys in xray_data:
    if len(xray_data[keys]) != 0:
        for song_id in xray_data[keys]:
            if song_id in iidx_data:
                if keys not in iidx_data[song_id]["Alias"]:
                    iidx_data[song_id]["Alias"].append(keys)
    else:
        print("跳过空的别名键值对, thanks xray")
json_str = json.dumps(iidx_data, indent=4, ensure_ascii=False)
with open(path+'target.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)
fp1.close()
fp2.close()
