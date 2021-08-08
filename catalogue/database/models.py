from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class AllData(DeclarativeBase):
    __tablename__ = 'mobile_details'

    id = Column(Integer, primary_key=True,autoincrement=True)
    imageUrl = Column(String(500))
    ProviderLogo = Column(String(500))
    brand = Column(String(200))
    model = Column(String(500))
    phoneDescription = Column(String(200))
    phoneDescription2 = Column(String(200))
    packageDetail = Column(String(2000))
    packageName = Column(String(200))
    price = Column(String(200))
    Url = Column(String(500))

    def __init__(self, imageUrl=None, ProviderLogo=None, brand=None, model=None, phoneDescription=None,
                 phoneDescription2=None, packageDetail=None, packageName=None, price=None, Url=None):
        # self.id = id
        self.imageUrl = imageUrl
        self.ProviderLogo = ProviderLogo
        self.brand = brand
        self.model = model
        self.phoneDescription = phoneDescription
        self.phoneDescription2 = phoneDescription2
        self.packageDetail = packageDetail
        self.packageName = packageName
        self.price = price
        self.Url = Url

    # def __repr__(self):
    #     return "<AllData: id='%d', imageUrl='%s', ProviderLogo='%s', brand='%s', model='%s', phoneDescription='%s',phoneDescription2='%s',packageDetail='%s',packageName='%s',price='%s',Url='%s'>" % (
    #     self.id, self.imageUrl, self.ProviderLogo, self.brand, self.model, self.phoneDescription,
    #     self.phoneDescription2, self.packageDetail, self.packageName, self.price, self.Url)

    def __repr__(self):
        return "<AllData: imageUrl='%s', ProviderLogo='%s', brand='%s', model='%s', phoneDescription='%s',phoneDescription2='%s',packageDetail='%s',packageName='%s',price='%s',Url='%s'>" % (
             self.imageUrl, self.ProviderLogo, self.brand, self.model, self.phoneDescription,
            self.phoneDescription2, self.packageDetail, self.packageName, self.price, self.Url)

