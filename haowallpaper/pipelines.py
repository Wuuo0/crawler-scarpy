# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import logging


class HaowallpaperPipeline:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def open_spider(self, spider):
        self.count = 0  # number of dropped item
        self.file = open('papers.jsonl', 'w')

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        threshold = 5
        stars = int(adapter.get('stars', 0))
        if stars < threshold:
            self.count += 1
            raise DropItem(f'Stars number({stars}) < 10')
        else:
            line = json.dumps(adapter.asdict()) + '\n'
            self.file.write(line)
        return item

    def close_spider(self, spider):
        self.logger.info(f'dropped items : {self.count}')
        self.file.close()
