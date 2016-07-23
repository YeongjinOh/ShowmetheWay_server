from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Rank

engine = create_engine('sqlite:///rank.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

score1 = Rank(name="Yeongjin Oh", email="oyj9109@snu.ac.kr", score=150)
score2 = Rank(name="Sungmin Oh", email="osm9009@snu.ac.kr", score=120)
score3 = Rank(name="Somebody", email="somebody@gmail.com", score=130)
session.add(score1)
session.add(score2)
session.add(score3)
session.commit()



