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
    part_id = Column("part_id", Integer, ForeignKey("parts.id"))
    part = relationship("Parts", back_populates="teams")

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


class Parts(Base):
    __tablename__ = "parts"
    id = Column(Integer, primary_key=True)
    part_name = Column("Part", String)
    teams = relationship("Team", back_populates="part")
    suppliers = relationship("Supplier", back_populates="parts")

    def __repr__(self):
        return f"{self.id}: {self.part_name}"


class Supplier(Base):
    __tablename__ = "supplier"
    id = Column(Integer, primary_key=True)
    supplier_name = Column("Supplier", String)
    parts = relationship("Parts", back_populates="suppliers")

    def __repr__(self):
        return f"{self.id}: {self.supplier_name}"




if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)