# Problem 5
# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint


class Train:
    def __init__(self, train_no):
        self.train_no = train_no

    def book(self, starting, destination):
        print(f"Your ticket is booked in train number: {
              self.train_no}, from {starting} to {destination}. ")

    def get_status(self):
        print(f"Train number: {self.train_no} is running on time.")

    def get_fare(self, starting, destination):
        print(f"Your fare in train number: {
              self.train_no}, from {starting} to {destination} is {randint(222, 5555)}. ")


train = Train(12399)
train.book("Rampur", "Delhi")
train.get_status()
train.get_fare("Rampur", "Delhi")
