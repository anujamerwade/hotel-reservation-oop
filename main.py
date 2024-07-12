import pandas as pd

hotels = pd.read_csv("hotels.csv", dtype={"id": str})
print(hotels)

cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")

cards_security = pd.read_csv("card_security.csv", dtype=str)

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

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        return card_data in cards


class Spa(Hotel):
    def book_spa_package(self):
        pass


class SpaReservation:
    def __init__(self, hotel_obj, customer_name):
        self.hotel = hotel_obj
        self.customer_name = customer_name

    def generate(self):
        content = f"Spa Reservation done for {self.customer_name} at {self.hotel.hotel_name}"
        return content

# inheritance
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = cards_security.loc[cards_security['number'] == self.number, "password"].squeeze()
        return password == given_password


hotel_ID = input("Enter hotel ID: ")
hotel = Spa(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number="1234")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation = Reservation(hotel_obj=hotel, customer_name=name)
            print(reservation.generate())
            spa_reservation = input("would you like to make a spa reservation? ")
            if spa_reservation == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaReservation(hotel_obj=hotel, customer_name=name)
                print(spa_ticket.generate())
            else:
                exit()
        else:
            print("credit card auth failed")
    else:
        print("payment did not go through")
else:
    print("hotel is not available")

