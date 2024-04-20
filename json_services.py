import json
import os


def create_json():
    if not os.path.isdir('result'):
        os.mkdir('result')
    with open('result/result.json', 'w', encoding='utf-8') as json_file:
        json.dump({'items': []}, json_file, ensure_ascii=False)


def print_product_data_from_json(name, price, phone):
    with open('result/result.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        data['items'].append({
            'name': name,
            'price': price,
            'phone': phone
        })
    with open('result/result.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
