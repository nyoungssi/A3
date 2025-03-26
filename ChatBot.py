#Comp 1020 Assginment 3 Chat Bot
#By Nayoung Lim

import random
import string


#Defines a function that takes one argument called phrase_list.
def random_choice_from_list(phrase_list):

#Randomly selects and returns
   return random.choice(phrase_list)

def make_list_from_file(filename):

   with open(filename, 'r') as file: #Opens the file in read mode
       return [line.strip() for line in file.readlines()]

def make_response_dictionary(response_list):
#Initializes an empty dictionary to store keyword-response pairs.
   response_dict = {}

   for line in response_list:
       key, response = line.split(',', 1)
       response_dict[key.strip()] = response.strip() #Removes extra spaces from the keyword and response.

   return response_dict


class ChatBot:

#Initializes the chatbot with greetings, responses, and a default response.
   def __init__(self, greetings_file, responses_file, default_response):

       self.greetings = make_list_from_file(greetings_file)
       responses = make_list_from_file(responses_file)
       self.keyword_and_response = make_response_dictionary(responses)
       self.default_response = default_response

#Provides a random greeting when the chatbot starts a chat.
   def greet(self):
       return random_choice_from_list(self.greetings)


   def respond(self, user_text):
       user_text = user_text.lower() #Converts user input to lowercase
       user_text = user_text.translate(str.maketrans('', '', string.punctuation)) #Creates a translation table to remove all punctuation.
       words = user_text.split()
       potential_responses = []

       for word in words:
           if word in self.keyword_and_response:
               potential_responses.append(self.keyword_and_response[word])
       if not potential_responses:
           return self.default_response
       return random_choice_from_list(potential_responses)