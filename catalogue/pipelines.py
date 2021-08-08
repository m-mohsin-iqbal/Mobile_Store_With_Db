from database.connection import db
from database.models import AllData

class BooksPipeline(object):
    def process_item(self, item, spider):
            print(item)
            # create a new SQL Alchemy object and add to the db session
            record = AllData(imageUrl=item['imageUrl'],
                             ProviderLogo=item['ProviderLogo'],
                             brand=item['brand'],
                             model=item['model'],
                             phoneDescription=item['phoneDescription'],
                             phoneDescription2=item['phoneDescription2'],
                             packageDetail=item['packageDetail'],
                             packageName=item['packageName'],
                             price=item['price'],
                             Url =item['Url'],
                             )
            print(record)
            db.add(record)
            db.commit()
            return item
