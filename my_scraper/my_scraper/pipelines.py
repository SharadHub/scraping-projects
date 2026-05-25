from pymongo import MongoClient
from itemadapter import ItemAdapter


class MyScraperPipeline:

    def open_spider(self, spider):
        self.client = MongoClient(
            host = "mongodb+srv://bishalbista737_db_user:T18ympGeCDxegb2j@ebook.du6qfei.mongodb.net/?appName=Ebook",
            connect=False
        )
        self.collection = self.client.get_database("Ebooks").get_collection("Travel")

    def process_item(self, item, spider):
        self.collection.insert_one(
            ItemAdapter(item).asdict()
        )
        return item
    
    def close_spider(self, spider):
        self.client.close()