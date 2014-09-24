from sqlalchemy import String, Integer, LargeBinary, ForeignKey, Boolean, \
    Column, Table, Float, DateTime, Text
from api.database import Base, engine, session

class SourceDest(Base):
    __tablename__ = 'source_dest'
    source = Column(Integer, primary_key=True)
    dest = Column(Integer, primary_key=True)
    in_vehicle_time = Column(Float)
    walk_transfer_time = Column(Float)
    wait_time = Column(Float)
    total_travel_time = Column(Float)

    def __repr__(self):
        return '<SourceDest %r to %r>' % (self.source, self.dest)
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
