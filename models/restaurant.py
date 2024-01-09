from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base  # Assuming Base is imported from your main file

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship("Review", back_populates="restaurant")

    def reviews(self):
        return self.reviews

    def customers(self):
        return [review.customer for review in self.reviews]
