from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Set up the database connection
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Example usage of the defined models and methods
# Fetch the first customer and their restaurants
first_customer = session.query(Customer).first()
print(f"Customer: {first_customer.full_name()}")
print(f"Restaurants reviewed: {[r.name for r in first_customer.restaurants()]}")

# Fetch the fanciest restaurant
fanciest_restaurant = Restaurant.fanciest()
print(f"Fanciest restaurant: {fanciest_restaurant.name}")

# Fetch all reviews for a restaurant
restaurant_reviews = first_customer.restaurants()[0].all_reviews()
print(f"Reviews for {first_customer.restaurants()[0].name}:")
for review in restaurant_reviews:
    print(review)
