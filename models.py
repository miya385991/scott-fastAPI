from sqlalchemy import Column, Integer, String, DATE
from sqlalchemy.schema import ForeignKey
from database import Base


class Depts(Base):
    __tablename__ = "depts"
    id = Column(Integer, autoincrement=True, primary_key=True)
    dp_no = Column(Integer, nullable=False)
    dp_name = Column(String, nullable=False)
    dp_loc = Column(String)


class Emps(Base):
    __tablename__ = "emps"

    id = Column(Integer, autoincrement=True, primary_key=True)
    em_no = Column(Integer, nullable=False)
    em_name = Column(String, nullable=False)
    em_job = Column(String, nullable=False)
    em_mgr = Column(Integer, nullable=False)
    em_hiredate = Column(DATE, nullable=False)
    em_sal = Column(Integer, nullable=False)
    dept_id = Column(Integer, ForeignKey("depts.id",
                                         onupdate='CASCADE',
                                         ondelete='CASCADE'))
