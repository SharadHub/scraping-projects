from scrapy import Field, Item
from itemloaders.processors import MapCompose, TakeFirst

def get_price(txt):
    return float(txt.replace("£", " "))

def get_quantity(txt):
    return int(
        txt.replace('(', '').split()[0]
    )
def convert_to_dollar(pound):
    return pound * 1.30

class EbookItem(Item):
    title = Field(
        output_processor = TakeFirst()
    )
    price = Field(
        input_processor = MapCompose(get_price, convert_to_dollar),
        output_processor = TakeFirst()
    )
    quantity = Field(
        input_processor = MapCompose(get_quantity),
        output_processor = TakeFirst()
    )