#the date and time module contains datetime
from datetime import datetime

#class Spy defines all the details of the Spy
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#class ChatMessage defines the details of the chat messages of the user.
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Bond', 'Mr.', 24, 4.7)

#the content below contains the details (name, salutation, spy rating and the age of the friends added)
friend_one = Spy('Garry', 'Mr.', 4.9, 27)
friend_two = Spy('Amber', 'Ms.', 4.39, 21)
friend_three = Spy('Rose', 'Ms.', 4.95, 37)

#the details of the friends are stored in a dictionary
friends = [friend_one, friend_two, friend_three]
