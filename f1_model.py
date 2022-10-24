from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/f1.db')
Base = declarative_base()


class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    team_name = Column("Team name", String)
    origin = Column("Country", String)
    drivers = relationship("Driver", back_populates="team")
    parts = relationship("Part", back_populates="team")

    def __repr__(self):
        return f"{self.id}: {self.team_name}, {self.origin}"


class Driver(Base):
    __tablename__ = "driver"
    id = Column(Integer, primary_key=True)
    driver_name = Column("Name", String)
    driver_surname = Column("Surname", String)
    team_id = Column("team_id", Integer, ForeignKey("team.id"))
    team = relationship("Team", back_populates="drivers")

    def __repr__(self):
        return f"{self.id}: {self.driver_name} {self.driver_surname} - {self.team}"


class Part(Base):
    __tablename__ = "part"
    id = Column(Integer, primary_key=True)
    part_name = Column("Part", String)
    manufacturer = Column("Manufacturer", String)
    team_id = Column("team_id", Integer, ForeignKey("team.id"))
    team = relationship("Team", back_populates="parts")

    def __repr__(self):
        return f"{self.id}: {self.part_name}, {self.manufacturer} - {self.team}"




if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)