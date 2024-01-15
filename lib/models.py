# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

engine= create_engine('sqlite:///contactbook.db')
Session= sessionmaker(bind=engine)
session =Session()

contact_group= Table(
    'contact_group',
    Base.metadata,
    Column('contact_id', ForeignKey('contacts.id'), primary_key=True),
    Column ('group_id', ForeignKey('groups.id'), primary_key = True),
    extend_existing=True,
)

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    address = Column(String)

    groups = relationship('Group', secondary=contact_group, back_populates= 'contacts')

    def __repr__(self):
        return f"Name: {self.name} Address: {self.address} Phone: {self.phone} E-mail: {self.email}"

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    contacts= relationship('Contact', secondary= contact_group, back_populates='groups')
    # contacts = relationship('Contact', back_populates='group')



 