import json
import csv
from xml.etree import ElementTree as ET


class BookDataAdapter:
    @staticmethod
    def adapt_from_json(data):
        books = json.loads(data)
        return [book['title'] for book in books]

    @staticmethod
    def adapt_from_csv(data):
        reader = csv.DictReader(data.splitlines())
        return [row['title'] for row in reader]

    @staticmethod
    def adapt_from_xml(data):
        root = ET.fromstring(data)
        return [book.find('title').text for book in root.findall('book')]
