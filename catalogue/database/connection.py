from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# db settings
dbuser = 'root'
dbpass = '1234'
dbhost = 'localhost'
dbname = 'mobile_db'

engine = create_engine("mysql://%s:%s@%s/%s?charset=utf8&use_unicode=0"
                       %(dbuser, dbpass, dbhost, dbname),
                       echo=False,
                       pool_recycle=1800)

db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))
print(db)

