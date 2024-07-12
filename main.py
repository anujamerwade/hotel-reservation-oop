import pandas as pd

hotels = pd.read_csv("hotels.csv", dtype={"id": str})
print(hotels)

# class User:
#     # no methods associated with this class, so you can remove it


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = hotels.loc[hotels['id'] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to NO"""
        hotels.loc[hotels['id'] == self.hotel_id, "available"] = "no"
        hotels.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if hotel is available"""
        availability = hotels.loc[hotels['id'] == self.hotel_id, "available"].squeeze()
        return availability == "yes"

class Reservation:
    def __init__(self, hotel_obj, customer_name):
        self.hotel = hotel_obj
        self.customer_name = customer_name

    def generate(self):
        content = f"Reservation done for {self.customer_name} at {self.hotel.hotel_name}"
        return content

hotel_ID = input("Enter hotel ID: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation = Reservation(hotel_obj=hotel, customer_name=name)
    print(reservation.generate())
else:
    print("hotel is not available")

