from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Set up the database connection
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Seed data for Restaurants
restaurant1 = Restaurant(name="Restaurant A", price=3)
restaurant2 = Restaurant(name="Restaurant B", price=4)
session.add_all([restaurant1, restaurant2])

# Seed data for Customers
customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Jane", last_name="Smith")
session.add_all([customer1, customer2])

# Seed data for Reviews
review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer2)
session.add_all([review1, review2])

# Commit the changes to the database
session.commit()
