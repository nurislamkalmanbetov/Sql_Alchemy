## documentation https://pythonru.com/biblioteki/shemy-v-sqlalchemy-orm 

#### я declarative_base() была перемещена в SQLAlchemy версии 2.0 и теперь доступна как sqlalchemy.orm.declarative_base(). Поэтому вы можете использовать sqlalchemy.orm.declarative_base() вместо    declarative_base(), чтобы избежать будущих предупреждений.


#### from sqlalchemy.orm import declarative_base
#### Base = declarative_base() 