from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user1 = User(name="dummy", email="dummy@dummy.com",picture="https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png")
session.add(user1)
session.commit()
# Create dummy categories
category1 = Category(name = "Football")
session.add(category1)
session.commit()

category2 = Category(name = "Tennis")
session.add(category2)
session.commit()

category3 = Category(name = "Handball")
session.add(category3)
session.commit()

# Create dummy items
item1 = Item(name = "Zamalek",description="1911",category=category1,user=user1)
session.add(item1)
session.commit()

item2 = Item(name = "Rafael Nadal", description = "the king of clay", category= category2,user=user1)
session.add(item2)
session.commit()

item3 = Item(name = "Ahmed El-ahmar", description="the king of handball",category = category3,user=user1)
session.add(item3)
session.commit()

item4 = Item(name = "Ahly",description="1907",category=category1,user=user1)
session.add(item4)
session.commit()