from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User

engine = create_engine('sqlite:///user.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

score1 = User(name="Yeongjin Oh", email="oyj9109@snu.ac.kr", score=150)
score2 = User(name="Sangjin Lee", email="lsj8723@naver.com", score=120)
score3 = User(name="Chi Kim", email="somebody@gmail.com", score=130)
session.add(score1)
session.add(score2)
session.add(score3)
session.commit()



