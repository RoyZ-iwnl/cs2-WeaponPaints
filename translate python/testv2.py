import json
import re

# 读取已翻译的文本
translated_file_path = "translated_file.cfg"
with open(translated_file_path, "r", encoding="utf8") as translated_file:
    translated_text = translated_file.read()

# 提取翻译文本和对应的index
translations = re.findall(r'"([^"]+)"\s*{\s*"index"\s*"(\d+)"', translated_text)

# 读取未翻译的JSON文件
json_file_path = "untranslated_file.json"
with open(json_file_path, "r", encoding="utf8") as json_file:
    json_data = json.load(json_file)

# 替换翻译文本
for item in json_data:
    index = item['paint']
    for translation in translations:
        if index == translation[1]:
            item['paint_name'] = re.sub(r'\|[^|]+', '| ' + translation[0], item['paint_name'])
            break

# 写入结果到新的JSON文件
output_file_path = "outputv2.json"
with open(output_file_path, "w", encoding="utf8") as output_file:
    json.dump(json_data, output_file, ensure_ascii=False, indent=4)
