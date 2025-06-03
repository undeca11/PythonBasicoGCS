########################################################################
###  R S S  S C R A P P I N G   P A R A   M O N G O D B   A T L A S  ###
########################################################################
### Prof. Filipo Mor - junho de 2025                                 ###
########################################################################

import requests
import xml.etree.ElementTree as ET
from pymongo import MongoClient

# URL do feed RSS
rss_url = 'https://abcnews.go.com/abcnews/usheadlines'

# Conexão com o MongoDB Atlas
client = MongoClient("sua_string_conexao_aqui", tls=True, tlsAllowInvalidCertificates=True)
db = client['NewsDatabase']
collection = db['ultimas_noticias']

def fetch_rss(rss_url):
    response = requests.get(rss_url)
    response.raise_for_status()
    return response.content

def parse_rss(xml_data):
    root = ET.fromstring(xml_data)
    items = []
    for item in root.findall('.//item'):
        news_item = {
            'title': item.findtext('title'),
            'link': item.findtext('link'),
            'description': item.findtext('description'),
            'pubDate': item.findtext('pubDate')
        }
        items.append(news_item)
    return items

def insert_into_mongodb(items):
    if items:
        collection.insert_many(items)
        print(f'{len(items)} notícias inseridas com sucesso!')

def main():
    xml_data = fetch_rss(rss_url)
    news_items = parse_rss(xml_data)
    insert_into_mongodb(news_items)

if __name__ == '__main__':
    main()

